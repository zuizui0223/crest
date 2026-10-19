#!/usr/bin/env python3
"""Source-pinned rainfall-sensitivity analysis for the Sonoran seed-bank pilot.

This is an exploratory robustness check, NOT evidence that a finite stochastic
ecosystem is Markov, or that soil seed bank absorbs ecological memory.

Inputs remain upstream:
  wscuello/ESSDesertAnnuals @ f39210d6adb603e7da7517601317ea9ce50305ae
  SpeciesByYear.csv and LTERDATA1982_2016.csv.

Only *previous-calendar-year* rainfall is included, so no future climate is
used to forecast seedlings in year t+1. CAP is a station proxy rather than
an exact matched field-plot microclimate; it cannot remove all confounding.

Usage:
  python scripts/explore_sonoran_rainfall_sensitivity.py
  python scripts/explore_sonoran_rainfall_sensitivity.py \
      --seedlings-csv /path/SpeciesByYear.csv \
      --rainfall-csv /path/LTERDATA1982_2016.csv
"""

from __future__ import annotations

import argparse
import calendar
import csv
import io
import json
import math
import runpy
from collections import defaultdict
from datetime import date
from pathlib import Path
from urllib.request import urlopen

SHA = "f39210d6adb603e7da7517601317ea9ce50305ae"
ROOT_URL = (
    "https://raw.githubusercontent.com/wscuello/ESSDesertAnnuals/"
    + SHA
    + "/"
)
BASE_SCRIPT = Path(__file__).with_name("explore_sonoran_seedbank_memory.py")
MODEL = runpy.run_path(str(BASE_SCRIPT))
FOLDS = MODEL["FOLDS"]
CONDITIONS = {
    "no_climate": (),
    "prior_oct_dec": (3,),
    "prior_oct_dec_and_jan_mar": (3, 4),
}


def load_monthly_rainfall(text: str) -> dict[int, dict[int, float | None]]:
    """Validated monthly CAP precipitation totals in mm.

    A month is usable only if EVERY calendar day is present exactly once,
    carries an explicit G quality flag, and contains a finite nonnegative
    precipitation value. Missing M flags, empty flags, or partial-year zero
    placeholders are NOT legitimate zero-rain days.
    """
    month: dict[tuple[int, int], dict] = defaultdict(
        lambda: {"days": set(), "total": 0.0, "complete": True}
    )
    for row in csv.DictReader(io.StringIO(text)):
        if row["Site"] != "CAP" or row["Station"] != "1":
            raise ValueError("unexpected source: expected CAP station 1")
        day = date.fromisoformat(row["Date"])
        key = (day.year, day.month)
        entry = month[key]
        if day.day in entry["days"]:
            raise ValueError(f"duplicate rainfall record for {day}")
        entry["days"].add(day.day)
        if row["Flag"] != "G" or row["Precip (total mm)"] == "":
            entry["complete"] = False
            continue
        value = float(row["Precip (total mm)"])
        if not math.isfinite(value) or value < 0:
            raise ValueError(f"invalid rainfall on {day}")
        entry["total"] += value

    annual: dict[int, dict[int, float | None]] = defaultdict(dict)
    for (year, month_no), entry in month.items():
        expected_days = calendar.monthrange(year, month_no)[1]
        good = entry["complete"] and len(entry["days"]) == expected_days
        annual[year][month_no] = entry["total"] if good else None
    return dict(annual)


def augment_panel(panel: list[dict], rain: dict[int, dict[int, float | None]]) -> list[dict]:
    """Append prior-year October–December and January–March rainfall.

    The two variables are logged in mm + 1. Missing or incomplete months
    become None and are excluded only from models using that covariate.
    """
    out = []
    for row in panel:
        months = rain.get(row["year"] - 1, {})

        def total(group: tuple[int, ...]) -> float | None:
            values = [months.get(m) for m in group]
            if any(v is None for v in values):
                return None
            return math.log1p(sum(values))

        features = tuple(row["x"]) + (
            total((10, 11, 12)),
            total((1, 2, 3)),
        )
        out.append({**row, "x": features})
    return out


def sensitivity_report(
    panel: list[dict],
    lambdas: tuple[float, ...] = (0.25, 2.0, 20.0, 100.0),
) -> dict:
    """Chronological, matched-row ridge comparison at each climate contract."""
    output = []
    for name, climate_cols in CONDITIONS.items():
        eligible = [
            r for r in panel if all(r["x"][j] is not None for j in climate_cols)
        ]
        for lam in lambdas:
            errors = [0.0] * 4
            n_test = 0
            fold_detail = []
            for cutoff in FOLDS:
                train = [r for r in eligible if r["year"] <= cutoff]
                test = [
                    r for r in eligible
                    if cutoff < r["year"] <= cutoff + 4
                ]
                if not train or not test:
                    raise ValueError("insufficient chronological fold")
                model_cols = (
                    (0,) + climate_cols,
                    (0, 1) + climate_cols,
                    (0, 2) + climate_cols,
                    (0, 1, 2) + climate_cols,
                )
                sse = [
                    sum(x["squared_error"] for x in MODEL["forecast_errors"](
                        train, test, cols, lam=lam
                    ))
                    for cols in model_cols
                ]
                for j, value in enumerate(sse):
                    errors[j] += value
                n_test += len(test)
                fold_detail.append({
                    "train_through": cutoff,
                    "test_years": list(range(cutoff + 1, cutoff + 5)),
                    "train_species_years": len(train),
                    "test_species_years": len(test),
                    "mse": [x / len(test) for x in sse],
                })

            m0, mh, mb, mhb = [v / n_test for v in errors]
            output.append({
                "climate_contract": name,
                "ridge_lambda": lam,
                "n_species_years": len(eligible),
                "n_years": len({r["year"] for r in eligible}),
                "n_test_species_years": n_test,
                "n_test_years": 12,
                "mse": [m0, mh, mb, mhb],
                "history_gain_before_bank": (m0 - mh) / m0,
                "history_gain_after_bank": (mb - mhb) / mb,
                "seed_bank_gain_after_history": (mh - mhb) / mh,
                "history_gain_attenuation": (
                    (m0 - mh) / m0 - (mb - mhb) / mb
                ),
                "folds": fold_detail if lam == 2.0 else [],
            })
    return {
        "status": "HOLD_NO_INDEPENDENT_CARRIER_PREDICTIVE_BENEFIT",
        "population_source": ROOT_URL + "SpeciesByYear.csv",
        "rainfall_source": ROOT_URL + "LTERDATA1982_2016.csv",
        "source_commit": SHA,
        "precipitation_station": "CAP station 1; proxy, not exact site microclimate",
        "rainfall_contract": (
            "Only prior calendar-year Oct–Dec / Jan–Mar observations, "
            "each requiring complete G-flagged calendar months"
        ),
        "limitations": (
            "Exploratory one-site annual forecasts; 15 taxa share years and "
            "rainfall, and lagged rainfall is not a complete environmental "
            "causal adjustment. No ecological Markov/closure theorem tested."
        ),
        "results": output,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seedlings-csv", type=Path)
    parser.add_argument("--rainfall-csv", type=Path)
    parser.add_argument(
        "--lambdas", type=float, nargs="+",
        default=[0.25, 2.0, 20.0, 100.0],
    )
    args = parser.parse_args()

    def get_text(path: Path | None, filename: str) -> str:
        if path:
            return path.read_text(encoding="utf-8-sig")
        with urlopen(ROOT_URL + filename, timeout=45) as response:
            return response.read().decode("utf-8-sig")

    demographic = get_text(args.seedlings_csv, "SpeciesByYear.csv")
    rainfall = get_text(args.rainfall_csv, "LTERDATA1982_2016.csv")
    panel = MODEL["parse_panel"](demographic)
    climate = load_monthly_rainfall(rainfall)
    data = augment_panel(panel, climate)
    result = sensitivity_report(data, tuple(args.lambdas))
    print(json.dumps(result, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
