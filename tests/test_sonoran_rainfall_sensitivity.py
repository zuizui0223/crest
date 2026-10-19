"""Offline quality-control and temporal-split tests for lagged rainfall sensitivity."""

from __future__ import annotations

import calendar
import math
import runpy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
WEATHER = runpy.run_path(
    str(ROOT / "scripts" / "explore_sonoran_rainfall_sensitivity.py")
)
DEMOGRAPHY = runpy.run_path(
    str(ROOT / "scripts" / "explore_sonoran_seedbank_memory.py")
)


def _synthetic_demography():
    rows = ["species,year,seedlings_per_m2,seeds_per_m2"]
    for species in range(15):
        for year in range(1983, 2017):
            seedling = (species + 2) * ((year - 1981) % 7 + 1)
            bank = (
                str((species + 1) * ((year - 1984) % 11 + 2))
                if 1990 <= year <= 2015 else "."
            )
            rows.append(
                f"taxon{species:02d},{year},{seedling},{bank}"
            )
    return DEMOGRAPHY["parse_panel"]("\n".join(rows) + "\n")


def _synthetic_weather() -> str:
    rows = ["Site,Station,Date,Precip (total mm),Flag"]
    for year in range(1989, 2016):
        for month in range(1, 13):
            for day in range(1, calendar.monthrange(year, month)[1] + 1):
                missing_2002 = (year, month, day) in (
                    (2002, 3, 8), (2002, 3, 9)
                )
                missing_2015 = (year, month) == (2015, 12)
                flag = "M" if missing_2002 else ("" if missing_2015 else "G")
                value = "" if missing_2002 else (
                    "0" if missing_2015 else str(((day + month + year) % 11) / 10)
                )
                rows.append(
                    f"CAP,1,{year:04d}-{month:02d}-{day:02d},{value},{flag}"
                )
    return "\n".join(rows) + "\n"


def test_quality_flags_are_never_imputed_as_zero_precipitation() -> None:
    rain = WEATHER["load_monthly_rainfall"](_synthetic_weather())
    assert rain[2002][3] is None
    assert rain[2002][2] is not None
    assert rain[2015][12] is None
    assert rain[2014][12] is not None
    assert rain[2015][1] is not None


def test_duplicate_daily_source_records_are_rejected() -> None:
    sample = (
        "Site,Station,Date,Precip (total mm),Flag\n"
        "CAP,1,2001-01-01,2,G\n"
        "CAP,1,2001-01-01,0,G\n"
    )
    with pytest.raises(ValueError, match="duplicate rainfall"):
        WEATHER["load_monthly_rainfall"](sample)


def test_weather_covariates_only_consume_previous_year() -> None:
    panel = _synthetic_demography()
    rain = WEATHER["load_monthly_rainfall"](_synthetic_weather())
    augmented = WEATHER["augment_panel"](panel, rain)
    assert len(augmented) == 390
    t2003 = next(
        r for r in augmented
        if r["species"] == "taxon00" and r["year"] == 2003
    )
    assert t2003["x"][3] is not None
    assert t2003["x"][4] is None  # March 2002 marked M, not zero.
    t2015 = next(
        r for r in augmented
        if r["species"] == "taxon00" and r["year"] == 2015
    )
    assert t2015["x"][3] is not None  # prior autumn 2014 is valid.
    assert t2015["x"][4] is not None  # prior Jan-Mar 2014 is valid.
    # Flagless Dec 2015 is NEVER used to predict seedlings in 2016.


def test_climate_sensitivity_forecasts_are_matched_and_offline() -> None:
    panel = _synthetic_demography()
    rain = WEATHER["load_monthly_rainfall"](_synthetic_weather())
    augmented = WEATHER["augment_panel"](panel, rain)
    report = WEATHER["sensitivity_report"](augmented, (2.0,))
    assert report["status"] == "HOLD_NO_INDEPENDENT_CARRIER_PREDICTIVE_BENEFIT"
    assert len(report["results"]) == 3
    by_name = {r["climate_contract"]: r for r in report["results"]}
    assert by_name["no_climate"]["n_species_years"] == 390
    assert by_name["prior_oct_dec"]["n_species_years"] == 390
    assert by_name["prior_oct_dec_and_jan_mar"]["n_species_years"] == 375
    for item in by_name.values():
        assert item["n_test_years"] == 12
        assert item["n_test_species_years"] == 180
        assert len(item["folds"]) == 3
        assert [f["test_species_years"] for f in item["folds"]] == [
            60, 60, 60
        ]
        assert all(math.isfinite(x) and x >= 0 for x in item["mse"])
    assert [
        f["train_species_years"]
        for f in by_name["prior_oct_dec_and_jan_mar"]["folds"]
    ] == [195, 255, 315]
    assert [
        f["train_species_years"]
        for f in by_name["prior_oct_dec"]["folds"]
    ] == [210, 270, 330]
