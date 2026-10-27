#!/usr/bin/env python3
"""Read-only OSF binary/source-grain audit for the SeedClim empirical HOLD gate.

This script never asserts an ecological effect or fits a predictive model.
OSF source files are only read into temporary storage; no third-party workbook,
community database, individual observation, or extracted dataset is saved
in the CREST repository.

Live: python scripts/audit_seedclim_osf_raw.py --download --output audit.json
Offline: python scripts/audit_seedclim_osf_raw.py \
  --seedbank-xlsx /path/VCG_clean_seedbank.xlsx \
  --community-zip /path/seedclim.2020.4.15.zip --output audit.json

The reader uses standard-library ZIP, XML and SQLite inspection to enumerate
source schemas and keys. It does not edit or recalculate spreadsheet contents.
Any missing source, unknown grain, or unmatched key remains a HOLD.
"""

from __future__ import annotations

import argparse
import io
import json
import posixpath
import re
import shutil
import sqlite3
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path
from urllib.request import Request, urlopen

OSF_FILE_IDS = {
    "seedbank": "634e3a110ecb4203302ed011",
    "community": "6078961aeb9cc900a214cde0",
}
OSF_NODE = "npfa9"
MAX_BYTES = {"seedbank": 15_000_000, "community": 35_000_000}
XL = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PKG_REL = "{http://schemas.openxmlformats.org/package/2006/relationships}"
SEEDBANK_REQUIRED = (
    "siteID", "replicate", "sampling_scale_cm2", "species", "nr_seeds"
)


def _http_bytes(url: str, max_bytes: int) -> bytes:
    with urlopen(Request(url, headers={"User-Agent": "CREST-source-audit/1.0"}), timeout=35) as r:
        length = r.headers.get("Content-Length")
        if length and int(length) > max_bytes:
            raise ValueError("OSF file exceeds audit size cap")
        data = r.read(max_bytes + 1)
    if len(data) > max_bytes:
        raise ValueError("OSF file exceeds audit size cap")
    return data


def fetch_public_osf_file(file_id: str, max_bytes: int) -> bytes:
    """Prefer the OSF API's advertised file download link; fallback to OSF."""
    meta_url = f"https://api.osf.io/v2/files/{file_id}/"
    errors = []
    candidates = []
    try:
        data = json.loads(_http_bytes(meta_url, 250_000).decode("utf-8"))
        resource = data["data"]
        if resource.get("id") != file_id:
            raise ValueError("unexpected OSF file ID")
        url = resource.get("links", {}).get("download")
        if url and url.startswith("https://"):
            candidates.append(url)
    except Exception as error:
        errors.append(f"metadata: {type(error).__name__}: {str(error)[:180]}")
    candidates.extend((
        f"https://osf.io/download/{file_id}/",
        f"https://files.osf.io/v1/resources/{OSF_NODE}/providers/osfstorage/{file_id}",
    ))
    for url in dict.fromkeys(candidates):
        try:
            content = _http_bytes(url, max_bytes)
            if not zipfile.is_zipfile(io.BytesIO(content)):
                raise ValueError("download is not an XLSX/ZIP archive")
            return content
        except Exception as error:
            errors.append(f"source: {type(error).__name__}: {str(error)[:180]}")
    raise RuntimeError("OSF_BINARY_UNAVAILABLE: " + "; ".join(errors))


def _excel_sheet_paths(zf: zipfile.ZipFile) -> dict[str, str]:
    w = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    targets = {
        link.attrib["Id"]: link.attrib["Target"]
        for link in rels.findall(PKG_REL + "Relationship")
    }
    out = {}
    for sheet in w.findall(f"{XL}sheets/{XL}sheet"):
        target = targets[sheet.attrib[REL + "id"]]
        path = (
            target.removeprefix("/")
            if target.startswith("/")
            else posixpath.normpath(posixpath.join("xl", target))
        )
        if path not in zf.namelist():
            raise ValueError(f"worksheet path absent in source: {path}")
        out[sheet.attrib["name"]] = path
    return out


def _shared_strings(zf: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in zf.namelist():
        return []
    root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    return [
        "".join(text.text or "" for text in si.iter(XL + "t"))
        for si in root.findall(XL + "si")
    ]


def _column_index(ref: str) -> int:
    letters = re.match(r"^[A-Z]+", ref)
    if not letters:
        raise ValueError(f"unknown XLSX cell address: {ref}")
    index = 0
    for char in letters.group():
        index = 26 * index + ord(char) - ord("A") + 1
    return index - 1


def _sheet_rows(zf: zipfile.ZipFile, filename: str, strings: list[str]):
    """Stream worksheet XML without importing or changing workbook formulas."""
    with zf.open(filename) as stream:
        for _event, row in ET.iterparse(stream, events=("end",)):
            if row.tag != XL + "row":
                continue
            cells = {}
            for cell in row.findall(XL + "c"):
                col = _column_index(cell.attrib["r"])
                val = cell.find(XL + "v")
                if cell.attrib.get("t") == "s":
                    if val is None:
                        content = None
                    else:
                        content = strings[int(val.text)]
                elif cell.attrib.get("t") == "inlineStr":
                    content = "".join(
                        txt.text or "" for txt in cell.iter(XL + "t")
                    )
                else:
                    content = val.text if val is not None else None
                cells[col] = content
            yield [cells.get(i) for i in range(max(cells) + 1)] if cells else []
            row.clear()


def _sheet_summary(zf: zipfile.ZipFile, name: str, path: str, strings: list[str]) -> dict:
    it = _sheet_rows(zf, path, strings)
    header = list(next(it))
    if not header or len(set(header)) != len(header):
        raise ValueError(f"{name}: empty/duplicate headers")
    header = [str(h) for h in header]
    idx = {key: j for j, key in enumerate(header)}
    keys = tuple(k for k in SEEDBANK_REQUIRED if k in idx)
    site_counts, site_replicates, scale_counts, years = Counter(), set(), Counter(), Counter()
    absent_site, absent_species, absent_nr_seeds, bad_scale, negative_seeds = 0, 0, 0, 0, 0
    unique_samples, keys_seen = set(), set()
    duplicate_taxon_keys = 0
    n = 0
    for arr in it:
        if not arr or all(c is None for c in arr):
            continue
        n += 1
        def get(key):
            j = idx.get(key)
            return arr[j] if j is not None and j < len(arr) else None

        site = get("siteID")
        species = get("species")
        replicate = get("replicate")
        scale = get("sampling_scale_cm2")
        yr = get("year")
        if site in (None, ""):
            absent_site += 1
        else:
            site_counts[str(site)] += 1
        if species in (None, ""):
            absent_species += 1
        if yr is not None:
            years[str(yr)] += 1
        if site is not None and replicate is not None:
            site_replicates.add((str(site), str(replicate)))
        if scale is not None:
            scale_counts[str(scale)] += 1
            try:
                if not (0 < float(scale) <= 4096):
                    bad_scale += 1
            except ValueError:
                bad_scale += 1
        if "nr_seeds" in idx:
            raw = get("nr_seeds")
            if raw in (None, ""):
                absent_nr_seeds += 1
            else:
                try:
                    if float(raw) < 0:
                        negative_seeds += 1
                except ValueError:
                    negative_seeds += 1
        sample_key = (site, replicate, scale)
        if all(z is not None for z in sample_key):
            unique_samples.add(tuple(str(z) for z in sample_key))
            taxon_key = sample_key + (species,)
            if taxon_key in keys_seen:
                duplicate_taxon_keys += 1
            keys_seen.add(taxon_key)
    return {
        "name": name,
        "columns": header,
        "rows": n,
        "missing_required_columns": [x for x in SEEDBANK_REQUIRED if x not in idx],
        "distinct_site_ids": sorted(site_counts),
        "site_counts": dict(sorted(site_counts.items())),
        "year_labels": dict(sorted(years.items())),
        "unique_site_replicate_pairs": len(site_replicates),
        "unique_site_replicate_scale_samples": len(unique_samples),
        "sampling_scale_values": dict(sorted(scale_counts.items())),
        "missing_site_cells": absent_site,
        "missing_species_cells": absent_species,
        "missing_seed_counts": absent_nr_seeds,
        "invalid_sampling_scales": bad_scale,
        "invalid_seed_counts": negative_seeds,
        "duplicate_site_replicate_scale_species_keys": duplicate_taxon_keys,
        "has_turfID": "turfID" in idx,
        "has_blockID": "blockID" in idx,
    }


def audit_xlsx(data: bytes) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        paths = _excel_sheet_paths(zf)
        strings = _shared_strings(zf)
        sheets = {n: _sheet_summary(zf, n, p, strings) for n, p in paths.items()}
    bank = sheets.get("seedbank")
    baseline_grain = (
        "siteID × replicate × sampling_scale_cm2 × species"
        if bank and not bank["missing_required_columns"] else "UNKNOWN"
    )
    return {
        "archive": "VCG_clean_seedbank.xlsx",
        "source_file_id": OSF_FILE_IDS["seedbank"],
        "zip_size_bytes": len(data),
        "sheet_names": list(paths),
        "sheets": sheets,
        "sample_grain": baseline_grain,
        "independent_original_sampling_date": "late August 2008 (Oikos methods)",
        "cleaned_year_value_is_lab_label": True,
        "emergence_assay": "2009–2010",
        "replicate_to_turf_crosswalk": (
            "not_declared"
            if bank is not None and not bank["has_turfID"] and not bank["has_blockID"]
            else "requires_external_provenance"
        ),
        "nested_spatial_scales_are_not_independent_sites": True,
    }


def audit_community_zip(data: bytes) -> dict:
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        sqlite_files = [
            x for x in archive.infolist()
            if x.filename.lower().endswith((".sqlite", ".sqlite3", ".db"))
            and not x.is_dir()
        ]
        out = {
            "archive": "seedclim.2020.4.15.zip",
            "source_file_id": OSF_FILE_IDS["community"],
            "zip_size_bytes": len(data),
            "archive_filenames": [x.filename for x in archive.infolist()][:25],
            "sqlite_candidates": [
                {"filename": x.filename, "uncompressed_bytes": x.file_size}
                for x in sqlite_files
            ],
            "sqlite_opened": False,
        }
        if len(sqlite_files) != 1:
            out["status"] = "HOLD_UNKNOWN_SQLITE_LAYOUT"
            return out
        info = sqlite_files[0]
        if info.file_size > 350_000_000:
            raise ValueError("community SQLite exceeds safe expansion limit")
        with tempfile.TemporaryDirectory(prefix="crest_seedclim_") as tmp:
            target = Path(tmp) / "seedclim.sqlite"
            with archive.open(info) as source, target.open("wb") as dest:
                shutil.copyfileobj(source, dest, 1024 * 1024)
            con = sqlite3.connect(f"file:{target.as_posix()}?mode=ro", uri=True)
            try:
                tables = [
                    r[0] for r in con.execute(
                        "SELECT name FROM sqlite_master WHERE type='table'"
                    )
                ]
                out["sqlite_opened"] = True
                out["table_names"] = sorted(tables)
                for target_table in ("turf_community", "turfCommunity", "turfs", "sites", "blocks", "plots"):
                    if target_table not in tables:
                        continue
                    safe = '"' + target_table.replace('"', '""') + '"'
                    row_count = con.execute(f"SELECT COUNT(*) FROM {safe}").fetchone()[0]
                    details = {"rows": row_count}
                    colnames = {x[1] for x in con.execute(f"PRAGMA table_info({safe})")}
                    if target_table == "sites" and "siteID" in colnames:
                        details["site_ids"] = sorted(
                            str(r[0]) for r in con.execute(
                                f"SELECT DISTINCT siteID FROM {safe} WHERE siteID IS NOT NULL"
                            )
                        )
                    if "year" in colnames:
                        details["year_rows"] = {
                            str(y): n for y, n in con.execute(
                                f"SELECT year, COUNT(*) FROM {safe} GROUP BY year ORDER BY year"
                            )
                        }
                    if "turfID" in colnames:
                        details["distinct_turfs"] = con.execute(
                            f"SELECT COUNT(DISTINCT turfID) FROM {safe}"
                        ).fetchone()[0]
                    out[target_table] = details
            finally:
                con.close()
    return out


def audit(seedbank: bytes, community: bytes) -> dict:
    a, b = audit_xlsx(seedbank), audit_community_zip(community)
    sheet = a["sheets"].get("seedbank")
    source_sites = set(sheet["distinct_site_ids"]) if sheet else set()
    community_sites = set(b.get("sites", {}).get("site_ids", []))
    mismatched_sites = sorted(source_sites - community_sites)
    valid = (
        sheet is not None
        and not sheet["missing_required_columns"]
        and bool(source_sites)
        and bool(community_sites)
        and not mismatched_sites
        and not sheet["has_turfID"] and not sheet["has_blockID"]
        and not sheet["invalid_sampling_scales"]
        and not sheet["invalid_seed_counts"]
        and b["sqlite_opened"]
    )
    return {
        "status": "RAW_GRAIN_VALID_SITE_LEVEL_HOLD_TURF_LINKAGE" if valid
        else "HOLD_SOURCE_CONTENT_OR_SCHEMA_UNRESOLVED",
        "osf_node": OSF_NODE,
        "seedbank": a,
        "community": b,
        "site_linkage": {
            "baseline_sites": sorted(source_sites),
            "community_sites": sorted(community_sites),
            "baseline_sites_absent_from_community": mismatched_sites,
            "exact_site_name_coverage": bool(source_sites) and not mismatched_sites
            and bool(community_sites),
            "replicate_to_block_linkage": "NOT_VERIFIED",
        },
        "scientific_gate": {
            "can_match_one_seedbank_replicate_to_one_transplant_turf": False,
            "may_compare_origin_site_level_baseline_profiles": valid,
            "may_claim_ecological_memory_closure": False,
            "earliest_conservative_future_analysis_year": 2011,
            "reason": (
                "Seed-bank replicate has no documented plot/block/turf key; "
                "field sampled August 2008, greenhouse assayed 2009–2010; "
                "nested sample scales must not be counted as independent sites."
            ),
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--download", action="store_true")
    ap.add_argument("--seedbank-xlsx", type=Path)
    ap.add_argument("--community-zip", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    result = {}
    try:
        if args.download:
            if args.seedbank_xlsx or args.community_zip:
                raise ValueError("choose --download OR two existing local files")
            bank = fetch_public_osf_file(
                OSF_FILE_IDS["seedbank"], MAX_BYTES["seedbank"]
            )
            community = fetch_public_osf_file(
                OSF_FILE_IDS["community"], MAX_BYTES["community"]
            )
        else:
            if not args.seedbank_xlsx or not args.community_zip:
                raise ValueError("provide both local source files or --download")
            bank = args.seedbank_xlsx.read_bytes()
            community = args.community_zip.read_bytes()
        result = audit(bank, community)
    except Exception as exc:
        result = {
            "status": "RAW_SOURCE_NOT_VERIFIED",
            "osf_node": OSF_NODE,
            "error_type": type(exc).__name__,
            "error_message": str(exc)[:900],
            "scientific_gate": {"may_claim_ecological_memory_closure": False},
        }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    if result["status"] == "RAW_SOURCE_NOT_VERIFIED":
        sys.exit(2)


if __name__ == "__main__":
    main()
