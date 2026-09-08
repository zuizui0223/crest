from __future__ import annotations

import json
from math import isclose
from pathlib import Path

from crest.explicit_temporal_grammar import AXES
from crest.semantic_access import canonical_nontrivial_companion_model
from crest.semantic_temporal_quotient import (
    semantic_pair_counts,
    semantic_quotient_bits,
    semantic_quotient_size,
    semantic_three_way_dividend,
)

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts" / "crest_sparse_semantic_access_benchmarks_2026-09-08.json"


def test_sparse_benchmark_artifact_matches_code() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    routes, candidates, model = canonical_nontrivial_companion_model()

    assert semantic_pair_counts(model) == (
        data["semantic_pairs"],
        data["addressable_pairs"],
    )

    for row in data["benchmarks"]:
        m = row["m"]
        assert semantic_quotient_size(routes, candidates, model, m, AXES) == row["grand_classes"]
        assert isclose(
            semantic_quotient_bits(routes, candidates, model, m, AXES),
            row["grand_bits"],
            rel_tol=0.0,
            abs_tol=1e-12,
        )
        assert isclose(
            semantic_three_way_dividend(routes, candidates, model, m),
            row["three_way_bits"],
            rel_tol=0.0,
            abs_tol=1e-12,
        )
