from math import inf

import pytest

from crest.prerequisite_access_game import ProspectiveQuery, mobius_transform
from crest.prerequisite_renyi_leakage import (
    prospective_renyi_game,
    symmetric_two_query_leakage,
    symmetric_two_query_leakage_sign,
)


H = "H"
THETA = "THETA"
F = "F"


def _witness_queries() -> tuple[ProspectiveQuery, ...]:
    return (
        ProspectiveQuery("left", frozenset((H,)), frozenset((0,)), 1.0),
        ProspectiveQuery("right", frozenset((THETA,)), frozenset((1,)), 1.0),
    )


def test_closed_form_matches_direct_mobius_dividend() -> None:
    ps = (0.5, 0.5)
    grand = frozenset((H, THETA, F))
    for q in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 5.0, inf):
        game = prospective_renyi_game(ps, _witness_queries(), (H, THETA, F), q)
        dividend = mobius_transform(game)
        assert dividend[grand] == pytest.approx(symmetric_two_query_leakage(q), abs=1e-12)


def test_shannon_is_the_unique_zero_leakage_order_in_the_witness() -> None:
    assert symmetric_two_query_leakage(1.0) == 0.0
    for q in (0.0, 0.1, 0.5, 0.9, 1.1, 1.5, 2.0, 10.0, inf):
        assert abs(symmetric_two_query_leakage(q)) > 1e-6


def test_leakage_changes_sign_at_shannon_order() -> None:
    for q in (0.0, 0.2, 0.5, 0.9):
        assert symmetric_two_query_leakage_sign(q) == -1
    assert symmetric_two_query_leakage_sign(1.0) == 0
    for q in (1.1, 1.5, 2.0, 10.0, inf):
        assert symmetric_two_query_leakage_sign(q) == 1


def test_no_query_declares_joint_prerequisites_but_nonshannon_joint_dividend_exists() -> None:
    queries = _witness_queries()
    assert all(query.required_interfaces != frozenset((H, THETA)) for query in queries)

    ps = (0.5, 0.5)
    grand = frozenset((H, THETA, F))
    shannon = mobius_transform(
        prospective_renyi_game(ps, queries, (H, THETA, F), 1.0)
    )
    hartley = mobius_transform(
        prospective_renyi_game(ps, queries, (H, THETA, F), 0.0)
    )
    collision = mobius_transform(
        prospective_renyi_game(ps, queries, (H, THETA, F), 2.0)
    )

    assert shannon[grand] == pytest.approx(0.0, abs=1e-12)
    assert hartley[grand] < 0.0
    assert collision[grand] > 0.0
