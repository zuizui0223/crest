#!/usr/bin/env python3
"""Exploratory seed-bank carrier prediction; NOT evidence of state closure.

Reproduces the small, post-hoc comparison in CREST Issue #140. Data remain
upstream and are downloaded at a fixed commit unless --csv is supplied.
Only aggregate prediction metrics are emitted. No raw third-party data,
individual identities, or invented ecological mechanisms are saved.

Source: https://github.com/wscuello/ESSDesertAnnuals
Paper: https://doi.org/10.1098/rspb.2018.2613
Run: python scripts/explore_sonoran_seedbank_memory.py
Offline: python scripts/explore_sonoran_seedbank_memory.py --csv /path/SpeciesByYear.csv

Crucial limitations:
- ONE ecological site, 15 correlated taxa, 26 annual carrier measurements.
- Held-out evaluation comprises 12 YEARS, not 180 independent year blocks.
- One-step deterministic quotient closure is NOT tested with these regressions.
- Neither a loss of history predictive power nor a small p-value proves the
  carrier causes or uniquely explains ecological memory.
- This exploratory test was not preregistered; do not promote it to Paper A.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import math
from collections import defaultdict
from pathlib import Path
from urllib.request import urlopen

SOURCE_SHA = "f39210d6adb603e7da7517601317ea9ce50305ae"
SOURCE = (
    "https://raw.githubusercontent.com/wscuello/ESSDesertAnnuals/"
    f"{SOURCE_SHA}/SpeciesByYear.csv"
)
FOLDS = (2003, 2007, 2011)
MODEL_COLS = ((0,), (0, 1), (0, 2), (0, 1, 2))


def parse_panel(text: str) -> list[dict]:
    """One row per species and target year; predict seedlings in year t+1.

    The germination-fraction column is deliberately excluded because it is
    derived arithmetically from current seedlings and the seed bank.
    """
    records = list(csv.DictReader(io.StringIO(text)))
    by_species: dict[str, dict[int, dict]] = defaultdict(dict)
    for row in records:
        species = row["species"]
        year = int(row["year"])
        val = row["seeds_per_m2"]
        bank = None if val in ("", ".", "NA") else float(val)
        seedling = float(row["seedlings_per_m2"])
        if seedling < 0 or (bank is not None and bank < 0):
            raise ValueError("seedling and seed-bank densities must be nonnegative")
        by_species[species][year] = {"seedling": seedling, "bank": bank}

    out: list[dict] = []
    for species in sorted(by_species):
        series = by_species[species]
        for year in range(1990, 2016):
            prior = series.get(year - 1)
            present = series.get(year)
            subsequent = series.get(year + 1)
            if not (prior and present and subsequent):
                continue
            if present["bank"] is None:
                continue
            out.append({
                "species": species, "year": year,
                "y": math.log1p(subsequent["seedling"]),
                "x": (
                    math.log1p(present["seedling"]),
                    math.log1p(prior["seedling"]),
                    math.log1p(present["bank"]),
                ),
            })
    return out


def solve_linear(matrix: list[list[float]], vector: list[float]) -> list[float]:
    """Small dense Gaussian elimination with partial pivoting (no numpy)."""
    n = len(vector)
    a = [list(row) + [rhs] for row, rhs in zip(matrix, vector)]
    for k in range(n):
        pivot = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[pivot][k]) < 1e-12:
            raise ValueError("singular ridge system")
        a[k], a[pivot] = a[pivot], a[k]
        diag = a[k][k]
        for j in range(k, n + 1):
            a[k][j] /= diag
        for i in range(n):
            if i == k:
                continue
            factor = a[i][k]
            for j in range(k, n + 1):
                a[i][j] -= factor * a[k][j]
    return [row[n] for row in a]


def forecast_errors(
    train: list[dict],
    test: list[dict],
    cols: tuple[int, ...],
    lam: float = 2.0,
) -> list[dict]:
    """Shared slopes, unpenalized species intercepts, train-only scaling."""
    if lam <= 0:
        raise ValueError("positive ridge penalty required")
    by_species: dict[str, list[dict]] = defaultdict(list)
    for row in train:
        by_species[row["species"]].append(row)
    averages = {}
    for species, group in by_species.items():
        averages[species] = {
            "y": sum(r["y"] for r in group) / len(group),
            "x": [
                sum(r["x"][j] for r in group) / len(group) for j in cols
            ],
        }
    p = len(cols)
    sd = [
        math.sqrt(sum(
            (r["x"][j] - averages[r["species"]]["x"][k]) ** 2
            for r in train
        ) / len(train)) or 1.0
        for k, j in enumerate(cols)
    ]
    gram = [[0.0] * p for _ in range(p)]
    rhs = [0.0] * p
    for row in train:
        avg = averages[row["species"]]
        x = [
            (row["x"][j] - avg["x"][k]) / sd[k]
            for k, j in enumerate(cols)
        ]
        y = row["y"] - avg["y"]
        for j in range(p):
            rhs[j] += x[j] * y
            for k in range(p):
                gram[j][k] += x[j] * x[k]
    for j in range(p):
        gram[j][j] += lam
    beta = solve_linear(gram, rhs)
    errors = []
    for row in test:
        avg = averages[row["species"]]
        yhat = avg["y"] + sum(
            beta[k] * (row["x"][j] - avg["x"][k]) / sd[k]
            for k, j in enumerate(cols)
        )
        errors.append({
            "species": row["species"],
            "year": row["year"],
            "squared_error": (row["y"] - yhat) ** 2,
        })
    return errors


def _fold_rows(rows: list[dict]) -> list[tuple[list[dict], list[dict]]]:
    return [
        (
            [r for r in rows if r["year"] <= end],
            [r for r in rows if end < r["year"] <= end + 4],
        )
        for end in FOLDS
    ]


def _ratio(a: float, b: float) -> float:
    if a <= 0:
        return float("nan")
    return (a - b) / a


def xorshift(seed: int):
    """Deterministic generator for placebo/bootstrap reproducibility."""
    state = seed & 0xFFFFFFFF
    while True:
        state ^= (state << 13) & 0xFFFFFFFF
        state ^= state >> 17
        state ^= (state << 5) & 0xFFFFFFFF
        state &= 0xFFFFFFFF
        yield state / 4294967296


def _shuffled_panel(part: list[dict], rng) -> list[dict]:
    """Shuffle the carrier independently within species and data split."""
    grouped: dict[str, list[float]] = defaultdict(list)
    for r in part:
        grouped[r["species"]].append(r["x"][2])
    for values in grouped.values():
        for i in range(len(values) - 1, 0, -1):
            j = int(next(rng) * (i + 1))
            values[i], values[j] = values[j], values[i]
    index: dict[str, int] = defaultdict(int)
    out = []
    for r in part:
        species = r["species"]
        shuffled = grouped[species][index[species]]
        index[species] += 1
        out.append({**r, "x": (r["x"][0], r["x"][1], shuffled)})
    return out


def percentile(values: list[float], q: float) -> float:
    ordered = sorted(values)
    return ordered[int((len(ordered) - 1) * q)]


def assess(
    rows: list[dict],
    lam: float = 2.0,
    placebo_repeats: int = 300,
    bootstrap_repeats: int = 2000,
) -> dict:
    """Descriptive evaluation with chronological folds and placebo carrier."""
    folds = _fold_rows(rows)
    all_errors: list[list[dict]] = [[] for _ in MODEL_COLS]
    fold_info = []
    for cutoff, (train, test) in zip(FOLDS, folds):
        predictions = [
            forecast_errors(train, test, col, lam=lam)
            for col in MODEL_COLS
        ]
        for index, prediction in enumerate(predictions):
            all_errors[index].extend(prediction)
        fold_info.append({
            "train_through": cutoff,
            "test_years": list(range(cutoff + 1, cutoff + 5)),
            "training_species_years": len(train),
            "test_species_years": len(test),
            "mse": [
                sum(z["squared_error"] for z in prediction) / len(prediction)
                for prediction in predictions
            ],
        })
    mses = [
        sum(r["squared_error"] for r in errs) / len(errs)
        for errs in all_errors
    ]
    # M0: current, MH: current+history, MS: current+seedbank,
    # MHS: current+history+seedbank, all on exactly matched test rows.
    output = {
        "status": "EXPLORATORY_HOLD_NOT_EMPIRICALLY_CONFIRMED",
        "source": SOURCE,
        "source_commit": SOURCE_SHA,
        "time_scale": "annual",
        "species": len({r["species"] for r in rows}),
        "species_year_rows": len(rows),
        "unique_years": len({r["year"] for r in rows}),
        "heldout_species_years": len(all_errors[0]),
        "heldout_unique_years": len({r["year"] for r in all_errors[0]}),
        "ridge_lambda": lam,
        "folds": fold_info,
        "mse_log1p_next_seedlings": {
            "current": mses[0],
            "current_plus_history": mses[1],
            "current_plus_seedbank": mses[2],
            "current_plus_history_plus_seedbank": mses[3],
        },
        "relative_gain_history": _ratio(mses[0], mses[1]),
        "relative_gain_history_after_seedbank": _ratio(mses[2], mses[3]),
        "relative_gain_seedbank_after_current": _ratio(mses[0], mses[2]),
        "relative_gain_seedbank_after_history": _ratio(mses[1], mses[3]),
        "history_attenuation_index": (
            _ratio(mses[0], mses[1]) - _ratio(mses[2], mses[3])
        ),
    }

    if placebo_repeats:
        placebo_gain = []
        history_sse = sum(r["squared_error"] for r in all_errors[1])
        for iteration in range(1, placebo_repeats + 1):
            rand = xorshift(20261013 + iteration * 13)
            total = 0.0
            for train, test in folds:
                shuffled_train = _shuffled_panel(train, rand)
                shuffled_test = _shuffled_panel(test, rand)
                total += sum(
                    row["squared_error"]
                    for row in forecast_errors(
                        shuffled_train, shuffled_test, (0, 1, 2), lam=lam
                    )
                )
            placebo_gain.append(_ratio(history_sse, total))
        observed = output["relative_gain_seedbank_after_history"]
        output["temporal_alignment_placebo"] = {
            "repetitions": placebo_repeats,
            "mean_gain": sum(placebo_gain) / len(placebo_gain),
            "median_gain": percentile(placebo_gain, 0.5),
            "fraction_at_least_as_good_as_observed": (
                sum(z >= observed for z in placebo_gain) / placebo_repeats
            ),
        }

    if bootstrap_repeats:
        by_year: dict[int, list[float]] = {}
        for model, errs in enumerate(all_errors):
            for r in errs:
                by_year.setdefault(r["year"], [0.0] * 4)
                by_year[r["year"]][model] += r["squared_error"]
        test_years = sorted(by_year)
        rng = xorshift(90210)
        improvements, attenuations = [], []
        for _ in range(bootstrap_repeats):
            sums = [0.0] * 4
            for _ in test_years:
                sampled = test_years[int(next(rng) * len(test_years))]
                for j in range(4):
                    sums[j] += by_year[sampled][j]
            improvements.append(_ratio(sums[1], sums[3]))
            attenuations.append(
                _ratio(sums[0], sums[1]) - _ratio(sums[2], sums[3])
            )
        output["fixed_fit_heldout_year_resampling"] = {
            "repetitions": bootstrap_repeats,
            "carrier_after_history_95pct_descriptive_interval": [
                percentile(improvements, 0.025),
                percentile(improvements, 0.975),
            ],
            "history_attenuation_95pct_descriptive_interval": [
                percentile(attenuations, 0.025),
                percentile(attenuations, 0.975),
            ],
            "limitations": (
                "Resamples only held-out year errors with fixed fitted models; "
                "not a full-model confidence interval, not cross-site replication."
            ),
        }
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv", type=Path, help="Optional offline upstream CSV path"
    )
    parser.add_argument("--ridge", type=float, default=2.0)
    parser.add_argument("--placebo-repeats", type=int, default=300)
    parser.add_argument("--bootstrap-repeats", type=int, default=2000)
    args = parser.parse_args()
    if args.csv:
        contents = args.csv.read_text(encoding="utf-8-sig")
    else:
        with urlopen(SOURCE, timeout=45) as response:
            contents = response.read().decode("utf-8-sig")
    panel = parse_panel(contents)
    print(json.dumps(assess(
        panel, lam=args.ridge,
        placebo_repeats=args.placebo_repeats,
        bootstrap_repeats=args.bootstrap_repeats,
    ), indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
