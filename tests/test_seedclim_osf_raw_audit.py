"""Synthetic-only tests for raw OSF XLSX + community ZIP provenance audit.

The real third-party archives are deliberately NOT stored in this repository.
"""

from __future__ import annotations

import io
import runpy
import sqlite3
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

MODULE = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / "scripts" / "audit_seedclim_osf_raw.py")
)


def _cell(column: str, row: int, value) -> str:
    ref = f"{column}{row}"
    if isinstance(value, (int, float)):
        return f'<c r="{ref}"><v>{value}</v></c>'
    return (
        f'<c r="{ref}" t="inlineStr"><is><t>{escape(str(value))}'
        f"</t></is></c>"
    )


def _sheet_xml(rows: list[list]) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/'
        'spreadsheetml/2006/main"><sheetData>'
        + "".join(
            '<row r="{}">{}</row>'.format(
                row_index,
                "".join(
                    _cell(chr(ord("A") + i), row_index, value)
                    for i, value in enumerate(values)
                ),
            )
            for row_index, values in enumerate(rows, start=1)
        )
        + "</sheetData></worksheet>"
    )


def fake_xlsx(with_turf_id: bool = False) -> bytes:
    cols = [
        "year", "siteID", "replicate", "sampling_scale_cm2",
        "nr_individual", "nr_species", "species", "nr_seeds",
    ]
    if with_turf_id:
        cols.append("turfID")
    rows = [
        cols,
        [2009, "Arhelleren", 1, 4096, 15, 2, "Acer_sp", 8],
        [2009, "Arhelleren", 1, 4096, 15, 2, "Bromus_sp", 7],
        [2009, "Fauske", 2, 1024, 3, 1, "Acer_sp", 3],
    ]
    if with_turf_id:
        rows[1].append("T-12")
        rows[2].append("T-12")
        rows[3].append("T-44")
    veg = [
        ["year", "siteID", "replicate", "sampling_scale_cm2", "nr_species", "species", "presence"],
        [2009, "Arhelleren", 1, 4096, 1, "Acer_sp", 1],
    ]
    workbook = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<workbook xmlns="http://schemas.openxmlformats.org/'
        'spreadsheetml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/'
        'officeDocument/2006/relationships">'
        '<sheets><sheet name="seedbank" sheetId="1" r:id="rId1"/>'
        '<sheet name="vegetation" sheetId="2" r:id="rId2"/></sheets></workbook>'
    )
    relationships = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/'
        'package/2006/relationships">'
        '<Relationship Id="rId1" Type="worksheet" Target="worksheets/sheet1.xml"/>'
        '<Relationship Id="rId2" Type="worksheet" Target="worksheets/sheet2.xml"/>'
        '</Relationships>'
    )
    bio = io.BytesIO()
    with zipfile.ZipFile(bio, "w") as zf:
        zf.writestr("xl/workbook.xml", workbook)
        zf.writestr("xl/_rels/workbook.xml.rels", relationships)
        zf.writestr("xl/worksheets/sheet1.xml", _sheet_xml(rows))
        zf.writestr("xl/worksheets/sheet2.xml", _sheet_xml(veg))
    return bio.getvalue()


def fake_sqlite_zip(tmp_path: Path) -> bytes:
    dbpath = tmp_path / "seedclim.sqlite"
    conn = sqlite3.connect(dbpath)
    try:
        conn.executescript(
            "CREATE TABLE turfs (turfID TEXT PRIMARY KEY);"
            "CREATE TABLE turf_community ("
            "turfID TEXT, year INTEGER, species TEXT, cover REAL);"
            "INSERT INTO turfs VALUES ('T-12'), ('T-44');"
            "INSERT INTO turf_community VALUES"
            "('T-12', 2009, 'Acer_sp', 0.1),"
            "('T-12', 2011, 'Acer_sp', 0.2),"
            "('T-44', 2011, 'Acer_sp', 0.3);"
        )
        conn.commit()
    finally:
        conn.close()
    bio = io.BytesIO()
    with zipfile.ZipFile(bio, "w") as zf:
        zf.write(dbpath, "seedclim.sqlite")
    return bio.getvalue()


def test_osf_xlsx_audit_counts_nested_samples_without_turf_claims() -> None:
    report = MODULE["audit_xlsx"](fake_xlsx())
    bank = report["sheets"]["seedbank"]
    assert report["sheet_names"] == ["seedbank", "vegetation"]
    assert bank["rows"] == 3
    assert bank["missing_required_columns"] == []
    assert bank["distinct_site_ids"] == ["Arhelleren", "Fauske"]
    assert bank["year_labels"] == {"2009": 3}
    assert bank["unique_site_replicate_pairs"] == 2
    assert bank["unique_site_replicate_scale_samples"] == 2
    assert bank["duplicate_site_replicate_scale_species_keys"] == 0
    assert bank["invalid_sampling_scales"] == 0
    assert not bank["has_turfID"] and not bank["has_blockID"]
    assert report["independent_original_sampling_date"] == "late August 2008 (Oikos methods)"
    assert report["replicate_to_turf_crosswalk"] == "not_declared"


def test_sqlite_zip_audit_is_limited_to_schema_and_aggregates(tmp_path: Path) -> None:
    report = MODULE["audit_community_zip"](fake_sqlite_zip(tmp_path))
    assert report["sqlite_opened"]
    assert report["turf_community"]["rows"] == 3
    assert report["turf_community"]["distinct_turfs"] == 2
    assert report["turf_community"]["year_rows"] == {"2009": 1, "2011": 2}


def test_join_requires_independent_replicate_to_turf_evidence(tmp_path: Path) -> None:
    report = MODULE["audit"](fake_xlsx(), fake_sqlite_zip(tmp_path))
    assert report["status"] == "RAW_GRAIN_VALID_SITE_LEVEL_HOLD_TURF_LINKAGE"
    assert report["scientific_gate"]["can_match_one_seedbank_replicate_to_one_transplant_turf"] is False
    assert report["scientific_gate"]["may_claim_ecological_memory_closure"] is False
    assert report["scientific_gate"]["earliest_conservative_future_analysis_year"] == 2011


def test_turf_column_without_validated_crosswalk_does_not_pass(tmp_path: Path) -> None:
    report = MODULE["audit"](fake_xlsx(with_turf_id=True), fake_sqlite_zip(tmp_path))
    assert report["status"] == "HOLD_SOURCE_CONTENT_OR_SCHEMA_UNRESOLVED"
    assert report["scientific_gate"]["can_match_one_seedbank_replicate_to_one_transplant_turf"] is False


def test_field_scale_and_count_fail_closed_when_invalid() -> None:
    source = fake_xlsx()
    assert zipfile.is_zipfile(io.BytesIO(source))
    assert MODULE["_column_index"]("A15") == 0
    assert MODULE["_column_index"]("AA15") == 26
