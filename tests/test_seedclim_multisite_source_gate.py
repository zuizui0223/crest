"""Offline guards for candidate SeedClim spatial/temporal linkage."""

from __future__ import annotations

import runpy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
MOD = runpy.run_path(str(ROOT / "scripts" / "audit_seedclim_multisite_keys.py"))


def metadata():
    return {
        "site_table.csv": [
            {"siteID": "Ulvehaugen"},
            {"siteID": "Ovstedalen"},
            {"siteID": "Skjelingahaugen"},
        ],
        "blocks_table.csv": [
            {"blockID": "Ulv1", "siteID": "Ulvhaugen"},
            {"blockID": "Ovs1", "siteID": "Ovstedal"},
            {"blockID": "Skj1", "siteID": "Skjellingahaugen"},
        ],
        "plots_table.csv": [
            {"plotID": "10", "blockID": "Ulv1"},
            {"plotID": "20", "blockID": "Ovs1"},
            {"plotID": "30", "blockID": "Skj1"},
        ],
        "turfs_table.csv": [
            {
                "turfID": "10 TTC", "originPlotID": "10",
                "destinationPlotID": "10", "TTtreat": "TTC",
            },
            {
                "turfID": "10 TT2 20", "originPlotID": "10",
                "destinationPlotID": "20", "TTtreat": "TT2",
            },
            {
                "turfID": "30 TT1 30", "originPlotID": "30",
                "destinationPlotID": "30", "TTtreat": "TT1",
            },
        ],
    }


def test_explicit_site_crosswalk_restores_referential_integrity():
    result = MOD["audit_tables"](metadata())
    assert result["status"] == (
        "SOURCE_METADATA_VALID_BUT_EMPIRICAL_LINKAGE_NOT_VERIFIED"
    )
    assert result["n_sites"] == 3
    assert result["n_blocks"] == 3
    assert result["n_plots"] == 3
    assert result["n_turfs"] == 3
    assert result["unmatched_raw_block_site_rows"] == 3
    assert result["unmatched_block_site_rows_after_explicit_crosswalk"] == 0
    assert result["unmatched_turf_origin_rows"] == 0
    assert result["unmatched_turf_destination_rows"] == 0
    assert result["turf_treatment_counts"] == {
        "TT1": 1, "TT2": 1, "TTC": 1
    }
    assert result["origin_site_treatment_counts"]["Ulvehaugen"] == {
        "TT2": 1, "TTC": 1
    }
    assert "2008" in MOD["OSF"]["baseline_seedbank_file"][
        "source_field_collection"
    ]
    assert "replicate" in MOD["OSF"]["baseline_seedbank_file"][
        "sampling_grain_from_cleaning_code"
    ]


def test_unrecognized_site_name_fails_closed():
    inp = metadata()
    inp["blocks_table.csv"][0]["siteID"] = "UnrecordedUnknownSite"
    with pytest.raises(ValueError, match="unmatched sites"):
        MOD["audit_tables"](inp)


def test_missing_turf_origin_fails_closed():
    inp = metadata()
    inp["turfs_table.csv"][0]["originPlotID"] = "nobody"
    with pytest.raises(ValueError, match="unmatched sites"):
        MOD["audit_tables"](inp)


def test_duplicate_keys_are_rejected():
    inp = metadata()
    inp["blocks_table.csv"].append(dict(inp["blocks_table.csv"][0]))
    with pytest.raises(ValueError, match="duplicate blockID"):
        MOD["audit_tables"](inp)


def test_csv_reader_retains_site_ids_and_unmatched_count():
    lines = (
        "siteID,latitude,longitude\n"
        "Ulvehaugen,60.1,7.7\n"
        "Skjelingahaugen,60.8,8.1\n"
    )
    records = MOD["read_csv"](lines)
    assert [r["siteID"] for r in records] == [
        "Ulvehaugen", "Skjelingahaugen"
    ]
