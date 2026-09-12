from math import inf

import pytest

from crest.prerequisite_access_game import ProspectiveQuery, mobius_transform
from crest.prerequisite_overlap_balance import (
    overlap_balance,
    overlap_region_q_masses,
    overlapping_access_leakage,
    overlapping_access_leakage_sign,
)
from crest.prerequisite_renyi_leakage import prospective_renyi_game


H = "H"
THETA = "THETA"
F = "F"
GRAND = frozenset((H, THETA, F))


def _queries(left_cells, right_cells, left_bits=1.0, right_bits=1.0):
    return (
        ProspectiveQuery("left", frozenset((H,)), frozenset(left_cells), left_bits),
        ProspectiveQuery("right", frozenset((THETA,)), frozenset(right_cells), right_bits),
    )


def test_overlap_closed_form_matches_direct_mobius_game() -> None:
    ps = (0.08, 0.17, 0.24, 0.11, 0.19, 0.21)
    left = (0, 1, 2)
    right = (2, 3, 4)
    for left_bits, right_bits in ((0.4, 0.9), (1.0, 1.0), (2.5, 0.75)):
        queries = _queries(left, right, left_bits, right_bits)
        for q in (0.0, 0.3, 0.8, 1.0, 1.4, 2.0, 5.0, inf):
            direct = mobius_transform(
                prospective_renyi_game(ps, queries, (H, THETA, F), q)
            )[GRAND]
            exact = overlapping_access_leakage(
                ps, left, right, left_bits, right_bits, q
            )
            assert direct == pytest.approx(exact, abs=1e-11)


def test_four_region_factorization_sign_with_positive_balance() -> None:
    ps = (0.10, 0.10, 0.40, 0.40)
    left = (0, 2)
    right = (1, 2)
    for q in (0.0, 0.2, 0.7):
        assert overlap_balance(ps, left, right, q) >= 0.0
        if q == 0.0:
            assert overlapping_access_leakage_sign(ps, left, right, 1.0, 2.0, q) == 0
        else:
            assert overlapping_access_leakage_sign(ps, left, right, 1.0, 2.0, q) == 1
    for q in (1.3, 2.0, 4.0):
        assert overlap_balance(ps, left, right, q) > 0.0
        assert overlapping_access_leakage_sign(ps, left, right, 1.0, 2.0, q) == -1


def test_four_region_factorization_sign_with_negative_balance() -> None:
    ps = (0.40, 0.40, 0.10, 0.10)
    left = (0, 2)
    right = (1, 2)
    for q in (0.2, 0.7):
        assert overlap_balance(ps, left, right, q) < 0.0
        assert overlapping_access_leakage_sign(ps, left, right, 1.0, 2.0, q) == -1
    for q in (1.3, 2.0, 4.0):
        assert overlap_balance(ps, left, right, q) < 0.0
        assert overlapping_access_leakage_sign(ps, left, right, 1.0, 2.0, q) == 1


def test_nonshannon_zero_leakage_exists_on_exact_balance_surface() -> None:
    ps = (0.25, 0.25, 0.25, 0.25)
    left = (0, 2)
    right = (1, 2)
    for q in (0.0, 0.2, 0.8, 1.0, 1.3, 2.0, 7.0):
        assert overlap_balance(ps, left, right, q) == pytest.approx(0.0, abs=1e-15)
        assert overlapping_access_leakage(ps, left, right, 0.7, 2.3, q) == pytest.approx(
            0.0, abs=1e-12
        )
        assert overlapping_access_leakage_sign(ps, left, right, 0.7, 2.3, q) == 0


def test_disjoint_case_is_recovered_when_overlap_mass_is_zero() -> None:
    ps = (0.2, 0.3, 0.5)
    left = (0,)
    right = (1,)
    X, Y, Z, W = overlap_region_q_masses(ps, left, right, 2.0)
    assert Z == 0.0
    assert W > 0.0
    assert X * Y > 0.0
    assert overlap_balance(ps, left, right, 2.0) < 0.0
    assert overlapping_access_leakage_sign(ps, left, right, 1.0, 1.0, 0.5) == -1
    assert overlapping_access_leakage_sign(ps, left, right, 1.0, 1.0, 2.0) == 1
