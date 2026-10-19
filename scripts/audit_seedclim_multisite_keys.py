#!/usr/bin/env python3
"""Audit potential multisite SeedClim carrier/outcome linkage; no raw archive.

Only the *public relational metadata tables* are read. This is a source-grain
screen, NOT a causal seed-bank test or a demonstration of ecological memory
closure. Baseline SeedClim seed-bank observations are site/replicate/taxon
measurements and cannot be assigned to an individual transplant turf without
an independent identifier and sampling-design check.

Run: python scripts/audit_seedclim_multisite_keys.py
Offline: python scripts/audit_seedclim_multisite_keys.py --source-dir DIR

Reference: Between-the-Fjords/seedclim-data, pinned at commit below.
The external OSF seed-bank XLSX and community ZIP remain upstream.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from collections import Counter
from pathlib import Path
from urllib.request import urlopen

SOURCE_REPO = "Between-the-Fjords/seedclim-data"
SOURCE_SHA = "a64358a7b34dcf909ca73ccb8590ebd0eb33839c"
RAW_URL = (
    "https://raw.githubusercontent.com/"
    + SOURCE_REPO
    + "/"
    + SOURCE_SHA
    + "/databaseUtils/setup-data/"
)
TABLES = (
    "site_table.csv",
    "blocks_table.csv",
    "plots_table.csv",
    "turfs_table.csv",
)
# These are verified name variants in the upstream blocks_table.csv.
# An unrecognized site name is never silently normalized or dropped.
SITE_NAME_CROSSWALK = {
    "Ovstedal": "Ovstedalen",
    "Skjellingahaugen": "Skjelingahaugen",
    "Ulvhaugen": "Ulvehaugen",
}
OSF = {
    "node": "npfa9",
    "baseline_seedbank_file": {
        "name": "VCG_clean_seedbank.xlsx",
        "file_id": "634e3a110ecb4203302ed011",
        "size_bytes": 2415260,
        "sampling_grain_from_cleaning_code": [
            "year", "siteID", "replicate", "species"
        ],
        "source_field_collection": "late August 2008",
        "lab_emergence_assay": "2009-2010",
    },
    "repeated_community_file": {
        "name": "seedclim.2020.4.15.zip",
        "file_id": "6078961aeb9cc900a214cde0",
        "size_bytes": 6977116,
        "relational_grain": ["turfID", "species", "year"],
        "nominal_years": "2009-2019",
    },
    "population_demography_file": {
        "name": "VCG_clean_transplant_demography_2009-2012.txt",
        "file_id": "635bc6c31e47c90b102a867b",
        "size_bytes": 2441498,
    },
}


def read_csv(text: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(text)))


def _unique_index(rows: list[dict], key: str) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for row in rows:
        value = row[key]
        if value in out:
            raise ValueError(f"duplicate {key}: {value}")
        out[value] = row
    return out


def audit_tables(tables: dict[str, list[dict[str, str]]]) -> dict:
    sites = _unique_index(tables["site_table.csv"], "siteID")
    blocks = _unique_index(tables["blocks_table.csv"], "blockID")
    plots = _unique_index(tables["plots_table.csv"], "plotID")
    turfs = _unique_index(tables["turfs_table.csv"], "turfID")

    raw_bad = Counter(
        b["siteID"] for b in blocks.values()
        if b["siteID"] not in sites
    )
    missing_normalized_sites = Counter(
        SITE_NAME_CROSSWALK.get(b["siteID"], b["siteID"])
        for b in blocks.values()
        if SITE_NAME_CROSSWALK.get(b["siteID"], b["siteID"]) not in sites
    )
    missing_plot_blocks = [
        p["plotID"] for p in plots.values()
        if p["blockID"] not in blocks
    ]

    def plot_to_site(plot_id: str) -> str | None:
        plot = plots.get(plot_id)
        if plot is None:
            return None
        block = blocks.get(plot["blockID"])
        if block is None:
            return None
        name = block["siteID"]
        normalized = SITE_NAME_CROSSWALK.get(name, name)
        return normalized if normalized in sites else None

    bad_origin = [
        t["turfID"] for t in turfs.values()
        if plot_to_site(t["originPlotID"]) is None
    ]
    bad_destination = [
        t["turfID"] for t in turfs.values()
        if plot_to_site(t["destinationPlotID"]) is None
    ]
    treatments = Counter(t["TTtreat"] for t in turfs.values())
    count_by_origin: dict[str, Counter[str]] = {}
    for t in turfs.values():
        origin = plot_to_site(t["originPlotID"])
        if origin is None:
            continue
        count_by_origin.setdefault(origin, Counter())[t["TTtreat"]] += 1

    if missing_normalized_sites or missing_plot_blocks or bad_origin or bad_destination:
        raise ValueError(
            "invalid relational graph; do not silently drop unmatched sites: "
            + json.dumps(
                {
                    "missing_sites": dict(missing_normalized_sites),
                    "missing_plot_blocks": len(missing_plot_blocks),
                    "unmatched_turf_origins": len(bad_origin),
                    "unmatched_turf_destinations": len(bad_destination),
                },
                sort_keys=True,
            )
        )

    return {
        "status": "SOURCE_METADATA_VALID_BUT_EMPIRICAL_LINKAGE_NOT_VERIFIED",
        "upstream_commit": SOURCE_SHA,
        "n_sites": len(sites),
        "n_blocks": len(blocks),
        "n_plots": len(plots),
        "n_turfs": len(turfs),
        "unmatched_raw_block_site_rows": sum(raw_bad.values()),
        "unmatched_raw_site_names": dict(sorted(raw_bad.items())),
        "unmatched_block_site_rows_after_explicit_crosswalk": 0,
        "unmatched_plot_block_rows": len(missing_plot_blocks),
        "unmatched_turf_origin_rows": len(bad_origin),
        "unmatched_turf_destination_rows": len(bad_destination),
        "turf_treatment_counts": dict(sorted(treatments.items())),
        "origin_site_treatment_counts": {
            site: dict(sorted(counts.items()))
            for site, counts in sorted(count_by_origin.items())
        },
        "osf_source_files": OSF,
        "acceptance_conditions": [
            "Read released baseline seed-bank workbook and vegetation SQLite.",
            "Verify baseline source date and site/replicate-to-block mapping.",
            "Never treat a site-level bank as a directly matched turf-level bank.",
            "Use origin-site-blocked evaluation; 356 turfs are not 356 independent sites.",
            "Separate transplant treatment selection, origin and destination climates.",
            "Do not claim future response prediction or memory closure yet.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir", type=Path,
        help="Directory containing the four source-pinned upstream CSVs",
    )
    args = parser.parse_args()

    def get_text(name: str) -> str:
        if args.source_dir:
            return (args.source_dir / name).read_text(encoding="utf-8-sig")
        with urlopen(RAW_URL + name, timeout=40) as response:
            return response.read().decode("utf-8-sig")

    tables = {name: read_csv(get_text(name)) for name in TABLES}
    print(json.dumps(audit_tables(tables), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
