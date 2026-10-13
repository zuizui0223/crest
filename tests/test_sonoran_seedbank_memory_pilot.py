"""Offline regression tests for the exploratory Sonoran seed-bank pilot."""

from __future__ import annotations

import math
import runpy
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parents[1]
MODEL = runpy.run_path(
    str(HERE / "scripts" / "explore_sonoran_seedbank_memory.py")
)


def synthetic_panel() -> list[dict]:
    """Full annual toy panel, generated in memory without external data."""
    data = ["species,year,seedlings_per_m2,seeds_per_m2"]
    for species_id in range(15):
        sp = f"taxon{species_id:02d}"
        for year in range(1983, 2017):
            present = (
                (species_id + 2) * ((year - 1981) % 7 + 1)
                + ((year * species_id) % 5)
            )
            bank = (
                str((species_id + 1) * ((year - 1984) % 11 + 2))
                if 1990 <= year <= 2015 else "."
            )
            data.append(f"{sp},{year},{present},{bank}")
    return MODEL["parse_panel"]("\n".join(data) + "\n")


def test_seedbank_temporal_indices_and_missing_carrier_filter() -> None:
    csv_data = (
        "species,year,seedlings_per_m2,seeds_per_m2\n"
        "plant,1989,2,.\n"
        "plant,1990,4,5\n"
        "plant,1991,6,8\n"
        "plant,1992,9,.\n"
    )
    rows = MODEL["parse_panel"](csv_data)
    assert len(rows) == 2
    assert rows[0]["year"] == 1990
    assert rows[0]["x"] == (
        math.log1p(4), math.log1p(2), math.log1p(5)
    )
    assert rows[0]["y"] == math.log1p(6)
    assert rows[1]["year"] == 1991
    assert rows[1]["y"] == math.log1p(9)


def test_linear_solver_and_positive_ridge() -> None:
    solution = MODEL["solve_linear"](
        [[4.0, 1.0], [1.0, 3.0]], [1.0, 2.0]
    )
    assert solution[0] == pytest.approx(1 / 11)
    assert solution[1] == pytest.approx(7 / 11)


def test_annual_cv_uses_heldout_years_and_no_online_data() -> None:
    rows = synthetic_panel()
    assert len(rows) == 390
    report = MODEL["assess"](
        rows, lam=2.0, placebo_repeats=5, bootstrap_repeats=20
    )
    assert report["species"] == 15
    assert report["unique_years"] == 26
    assert report["heldout_species_years"] == 180
    assert report["heldout_unique_years"] == 12
    assert [f["training_species_years"] for f in report["folds"]] == [
        210, 270, 330
    ]
    assert all(f["test_species_years"] == 60 for f in report["folds"])
    assert report["status"] == "EXPLORATORY_HOLD_NOT_EMPIRICALLY_CONFIRMED"
    assert report["temporal_alignment_placebo"]["repetitions"] == 5
    assert report["fixed_fit_heldout_year_resampling"]["repetitions"] == 20
    mse = report["mse_log1p_next_seedlings"]
    assert all(math.isfinite(x) and x >= 0 for x in mse.values())
    assert report["relative_gain_history"] == pytest.approx(
        (mse["current"] - mse["current_plus_history"]) / mse["current"]
    )
    assert report["relative_gain_seedbank_after_history"] == pytest.approx(
        (
            mse["current_plus_history"]
            - mse["current_plus_history_plus_seedbank"]
        ) / mse["current_plus_history"]
    )
