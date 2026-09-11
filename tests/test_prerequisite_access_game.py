from itertools import combinations

import pytest

from crest.prerequisite_access_game import (
    ProspectiveQuery,
    direct_refinement_shannon_gain,
    mobius_transform,
    predicted_dividends,
    prospective_game,
    prospective_shannon_gain,
)


H = "H"
THETA = "THETA"
X = "X"
F = "F"
PLAYERS = (H, THETA, X, F)


def _queries() -> tuple[ProspectiveQuery, ...]:
    return (
        ProspectiveQuery("status", frozenset(), frozenset((0, 1)), 1.0),
        ProspectiveQuery("legacy", frozenset((H,)), frozenset((1, 2)), 2.0),
        ProspectiveQuery("joint", frozenset((H, THETA)), frozenset((0, 2, 3)), 3.0),
        ProspectiveQuery("legacy2", frozenset((H,)), frozenset((0, 3)), 0.5),
    )


def _all_coalitions(players: tuple[str, ...]):
    for size in range(len(players) + 1):
        for subset in combinations(players, size):
            yield frozenset(subset)


def test_querywise_formula_matches_direct_cellwise_refinement_with_overlap() -> None:
    ps = (0.10, 0.20, 0.30, 0.40)
    queries = _queries()
    for coalition in _all_coalitions(PLAYERS):
        assert prospective_shannon_gain(ps, queries, coalition) == pytest.approx(
            direct_refinement_shannon_gain(ps, queries, coalition), abs=1e-12
        )


def test_mobius_support_is_exactly_declared_prerequisite_hyperedges() -> None:
    ps = (0.10, 0.20, 0.30, 0.40)
    queries = _queries()
    game = prospective_game(ps, queries, PLAYERS)
    observed = mobius_transform(game)
    expected = predicted_dividends(ps, queries)

    for coalition in game:
        assert observed[coalition] == pytest.approx(expected.get(coalition, 0.0), abs=1e-12)

    assert set(expected) == {
        frozenset((F,)),
        frozenset((H, F)),
        frozenset((H, THETA, F)),
    }
    # X is an irrelevant retained interface and must never acquire a dividend.
    assert all(X not in coalition for coalition, value in observed.items() if abs(value) > 1e-12)


def test_semantic_coverage_changes_weight_not_support() -> None:
    ps = (0.10, 0.20, 0.30, 0.40)
    sparse = ProspectiveQuery("q", frozenset((H, THETA)), frozenset((0,)), 4.0)
    broad = ProspectiveQuery("q", frozenset((H, THETA)), frozenset((0, 1, 2)), 4.0)

    sparse_dividend = predicted_dividends(ps, (sparse,))
    broad_dividend = predicted_dividends(ps, (broad,))
    support = frozenset((H, THETA, F))

    assert set(sparse_dividend) == {support}
    assert set(broad_dividend) == {support}
    assert sparse_dividend[support] == pytest.approx(0.4)
    assert broad_dividend[support] == pytest.approx(2.4)


def test_queries_with_same_prerequisite_set_aggregate_on_one_dividend() -> None:
    ps = (0.25, 0.25, 0.25, 0.25)
    q1 = ProspectiveQuery("a", frozenset((H,)), frozenset((0, 1)), 2.0)
    q2 = ProspectiveQuery("b", frozenset((H,)), frozenset((2, 3)), 3.0)
    expected = predicted_dividends(ps, (q1, q2))
    assert expected == {frozenset((H, F)): pytest.approx(2.5)}


def test_canonical_single_query_has_pure_three_way_shannon_support() -> None:
    ps = (0.25, 0.25, 0.25, 0.25)
    query = ProspectiveQuery(
        "canonical_future",
        frozenset((H, THETA)),
        frozenset((0,)),
        10.0,
    )
    game = prospective_game(ps, (query,), (H, THETA, F))
    dividend = mobius_transform(game)
    grand = frozenset((H, THETA, F))

    assert dividend[grand] == pytest.approx(2.5)
    for coalition, value in dividend.items():
        if coalition != grand:
            assert value == pytest.approx(0.0, abs=1e-12)
