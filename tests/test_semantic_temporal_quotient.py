from __future__ import annotations

from math import isclose, log2

from crest.explicit_temporal_grammar import AXES
from crest.semantic_access import SemanticAccessModel, canonical_nontrivial_companion_model
from crest.semantic_temporal_quotient import (
    predicted_grand_quotient_size,
    predicted_three_way_dividend,
    semantic_pair_counts,
    semantic_quotient_size,
    semantic_three_way_dividend,
)


def _model_with_first_k_pairs(k: int) -> tuple[tuple, tuple, SemanticAccessModel]:
    routes, candidates, base = canonical_nontrivial_companion_model()
    pairs = sorted(
        (h.carried_map, theta.response_table)
        for h in base.history_modes
        for theta in base.response_types
    )
    model = SemanticAccessModel(
        base.history_modes,
        base.response_types,
        frozenset(pairs[:k]),
    )
    return routes, candidates, model


def test_canonical_sparse_model_has_four_semantic_pairs_but_one_addressable() -> None:
    _, _, model = canonical_nontrivial_companion_model()
    assert semantic_pair_counts(model) == (4, 1)


def test_sparse_grand_classes_match_recomputed_review_values() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    expected = {4: 19, 8: 259, 10: 1027}
    for m, classes in expected.items():
        assert semantic_quotient_size(routes, candidates, model, m, AXES) == classes
        assert predicted_grand_quotient_size(model, m) == classes


def test_sparse_three_way_dividend_is_log_grand_over_semantic_baseline() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    for m in (4, 8, 10):
        observed = semantic_three_way_dividend(routes, candidates, model, m)
        expected = log2((3 + 2**m) / 4)
        assert isclose(observed, expected, rel_tol=0.0, abs_tol=1e-12)
        assert isclose(predicted_three_way_dividend(model, m), expected, abs_tol=1e-12)


def test_sparse_access_attenuates_but_does_not_change_three_way_order() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    for m in (4, 8, 10):
        dividend = semantic_three_way_dividend(routes, candidates, model, m)
        assert 0 < dividend < m
        # Asymptotically k/N=1/4 gives a two-bit sparsity penalty.
        assert abs((m - dividend) - 2.0) < 0.4


def test_general_access_coverage_formula_for_all_k_on_four_pair_model() -> None:
    for k in range(5):
        routes, candidates, model = _model_with_first_k_pairs(k)
        assert semantic_pair_counts(model) == (4, k)
        for m in (1, 3, 6):
            observed = semantic_quotient_size(routes, candidates, model, m, AXES)
            expected = (4 - k) + k * (2**m)
            assert observed == expected
            assert predicted_grand_quotient_size(model, m) == expected


def test_full_access_recovers_v06_complete_addressability_limit() -> None:
    routes, candidates, model = _model_with_first_k_pairs(4)
    for m in (1, 4, 10):
        assert semantic_quotient_size(routes, candidates, model, m, AXES) == 4 * 2**m
        assert isclose(semantic_three_way_dividend(routes, candidates, model, m), m, abs_tol=1e-12)


def test_zero_access_removes_future_interaction_entirely() -> None:
    routes, candidates, model = _model_with_first_k_pairs(0)
    for m in (1, 4, 10):
        assert semantic_quotient_size(routes, candidates, model, m, AXES) == 4
        assert isclose(semantic_three_way_dividend(routes, candidates, model, m), 0.0, abs_tol=1e-12)
