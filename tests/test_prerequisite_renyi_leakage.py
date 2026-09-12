from math import inf

import pytest

from crest.prerequisite_access_game import ProspectiveQuery, mobius_transform
from crest.prerequisite_renyi_leakage import (
    disjoint_access_set_leakage,
    disjoint_access_set_leakage_sign,
    prospective_renyi_game,
    symmetric_two_query_leakage,
    symmetric_two_query_leakage_sign,
    two_cell_disjoint_query_leakage,
    two_cell_disjoint_query_leakage_sign,
)


H = "H"
THETA = "THETA"
F = "F"


def _witness_queries(left_bits: float = 1.0, right_bits: float = 1.0) -> tuple[ProspectiveQuery, ...]:
    return (
        ProspectiveQuery("left", frozenset((H,)), frozenset((0,)), left_bits),
        ProspectiveQuery("right", frozenset((THETA,)), frozenset((1,)), right_bits),
    )


def test_closed_form_matches_direct_mobius_dividend() -> None:
    ps = (0.5, 0.5)
    grand = frozenset((H, THETA, F))
    for q in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 5.0, inf):
        game = prospective_renyi_game(ps, _witness_queries(), (H, THETA, F), q)
        dividend = mobius_transform(game)
        assert dividend[grand] == pytest.approx(symmetric_two_query_leakage(q), abs=1e-12)


def test_general_two_cell_formula_matches_direct_game_across_occupancies_and_depths() -> None:
    grand = frozenset((H, THETA, F))
    for p in (0.07, 0.2, 0.43, 0.71, 0.93):
        ps = (p, 1.0 - p)
        for left_bits, right_bits in ((0.25, 0.5), (1.0, 3.0), (2.5, 0.75), (5.0, 4.0)):
            queries = _witness_queries(left_bits, right_bits)
            for q in (0.0, 0.2, 0.7, 1.0, 1.3, 2.0, 6.0, inf):
                direct = mobius_transform(
                    prospective_renyi_game(ps, queries, (H, THETA, F), q)
                )[grand]
                exact = two_cell_disjoint_query_leakage(p, left_bits, right_bits, q)
                assert direct == pytest.approx(exact, abs=1e-11)


def test_general_disjoint_access_formula_matches_direct_game_with_residual_cells() -> None:
    ps = (0.05, 0.15, 0.20, 0.25, 0.35)
    left_cells = frozenset((0, 2))
    right_cells = frozenset((3, 4))
    residual_cell = 1
    assert residual_cell not in left_cells | right_cells
    left_bits, right_bits = 1.75, 0.6
    queries = (
        ProspectiveQuery("left", frozenset((H,)), left_cells, left_bits),
        ProspectiveQuery("right", frozenset((THETA,)), right_cells, right_bits),
    )
    grand = frozenset((H, THETA, F))
    for q in (0.0, 0.2, 0.7, 1.0, 1.3, 2.0, 6.0, inf):
        direct = mobius_transform(
            prospective_renyi_game(ps, queries, (H, THETA, F), q)
        )[grand]
        exact = disjoint_access_set_leakage(
            ps, left_cells, right_cells, left_bits, right_bits, q
        )
        assert direct == pytest.approx(exact, abs=1e-11)


def test_shannon_is_unique_finite_zero_for_arbitrary_nonempty_disjoint_access_sets() -> None:
    examples = (
        ((0.05, 0.15, 0.20, 0.25, 0.35), (0, 2), (3, 4), 1.75, 0.6),
        ((0.01, 0.09, 0.10, 0.30, 0.50), (0, 1, 3), (4,), 0.1, 3.5),
        ((0.12, 0.18, 0.22, 0.48), (0,), (1, 2), 8.0, 0.25),
    )
    for ps, left, right, left_bits, right_bits in examples:
        assert disjoint_access_set_leakage(ps, left, right, left_bits, right_bits, 1.0) == 0.0
        for q in (0.0, 0.1, 0.5, 0.9):
            assert disjoint_access_set_leakage_sign(
                ps, left, right, left_bits, right_bits, q
            ) == -1
        for q in (1.1, 1.5, 2.0, 10.0):
            assert disjoint_access_set_leakage_sign(
                ps, left, right, left_bits, right_bits, q
            ) == 1


def test_shannon_is_unique_finite_zero_for_every_interior_two_cell_occupancy_and_positive_depth() -> None:
    for p in (0.01, 0.1, 0.37, 0.5, 0.82, 0.99):
        for left_bits, right_bits in ((0.1, 0.2), (1.0, 1.0), (1.5, 4.0), (8.0, 0.5)):
            assert two_cell_disjoint_query_leakage(p, left_bits, right_bits, 1.0) == 0.0
            for q in (0.0, 0.1, 0.5, 0.9):
                assert two_cell_disjoint_query_leakage_sign(p, left_bits, right_bits, q) == -1
            for q in (1.1, 1.5, 2.0, 10.0):
                assert two_cell_disjoint_query_leakage_sign(p, left_bits, right_bits, q) == 1


def test_symmetric_specialization_is_unchanged() -> None:
    assert symmetric_two_query_leakage(1.0) == 0.0
    for q in (0.0, 0.1, 0.5, 0.9, 1.1, 1.5, 2.0, 10.0, inf):
        assert symmetric_two_query_leakage(q) == pytest.approx(
            two_cell_disjoint_query_leakage(0.5, 1.0, 1.0, q), abs=1e-12
        )


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
