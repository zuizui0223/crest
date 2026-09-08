from __future__ import annotations

import pytest

from crest.conditioned_temporal_bridges import (
    binary_signatures,
    future_conditioned_history_frontier,
    future_conditioned_history_point,
    grammar_conditioned_mechanism_frontier,
    grammar_conditioned_mechanism_point,
    paired_bridge_summary,
)


def test_binary_signature_family_has_exact_size() -> None:
    assert len(binary_signatures(1)) == 2
    assert len(binary_signatures(5)) == 32


def test_future_conditioned_history_frontier_is_exact_one_bit_per_probe() -> None:
    frontier = future_conditioned_history_frontier(6)
    assert tuple(point.query_count for point in frontier) == tuple(range(7))
    assert tuple(point.equivalence_classes for point in frontier) == tuple(2**k for k in range(7))
    assert tuple(point.information_bits for point in frontier) == pytest.approx(tuple(float(k) for k in range(7)))


def test_grammar_conditioned_mechanism_frontier_matches_history_count_law() -> None:
    history = future_conditioned_history_frontier(7)
    mechanism = grammar_conditioned_mechanism_frontier(7)
    assert tuple(point.equivalence_classes for point in history) == tuple(
        point.equivalence_classes for point in mechanism
    )
    assert tuple(point.information_bits for point in history) == pytest.approx(
        tuple(point.information_bits for point in mechanism)
    )


def test_closed_and_open_endpoints_are_zero_and_m_bits() -> None:
    for m in (1, 2, 4, 8, 10):
        h0 = future_conditioned_history_point(m, 0)
        hm = future_conditioned_history_point(m, m)
        t0 = grammar_conditioned_mechanism_point(m, 0)
        tm = grammar_conditioned_mechanism_point(m, m)
        assert h0.equivalence_classes == 1
        assert h0.information_bits == pytest.approx(0.0)
        assert hm.equivalence_classes == 2**m
        assert hm.information_bits == pytest.approx(float(m))
        assert t0.equivalence_classes == 1
        assert t0.information_bits == pytest.approx(0.0)
        assert tm.equivalence_classes == 2**m
        assert tm.information_bits == pytest.approx(float(m))


def test_m10_summary_closes_at_1024_classes_and_10_bits() -> None:
    summary = paired_bridge_summary(10)
    assert summary["history_closed_classes"] == 1
    assert summary["history_open_classes"] == 1024
    assert summary["history_inflation_bits"] == pytest.approx(10.0)
    assert summary["mechanism_closed_response_types"] == 1
    assert summary["mechanism_open_response_types"] == 1024
    assert summary["mechanism_inflation_bits"] == pytest.approx(10.0)


def test_query_count_validation() -> None:
    with pytest.raises(ValueError):
        future_conditioned_history_point(4, 5)
    with pytest.raises(ValueError):
        grammar_conditioned_mechanism_point(0, 0)
