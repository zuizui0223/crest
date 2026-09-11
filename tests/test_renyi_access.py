from itertools import combinations
from math import log2

import pytest

from crest.renyi_access import (
    asymptotic_limit_q_above_one,
    asymptotic_offset_q_below_one,
    asymptotic_slope,
    fixed_budget_extrema,
    heterogeneous_renyi_access_gain,
    renyi_access_gain,
)


def test_hartley_endpoint_recovers_main_text_sparse_access_formula() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    m = 10
    gain = renyi_access_gain(ps, {0}, m, q=0)
    expected = log2((3 + 2**m) / 4)
    assert gain == pytest.approx(expected, abs=1e-12)
    assert gain == pytest.approx(8.004220466318195, abs=1e-12)


def test_shannon_gain_depends_on_accessible_probability_mass() -> None:
    ps = (0.05, 0.15, 0.30, 0.50)
    m = 8
    access = {1, 3}
    assert renyi_access_gain(ps, access, m, q=1) == pytest.approx(m * 0.65)


def test_uniform_occupancy_shannon_gain_is_m_times_k_over_n() -> None:
    ps = (0.25, 0.25, 0.25, 0.25)
    assert renyi_access_gain(ps, {2}, 10, q=1) == pytest.approx(2.5)


def test_exact_renyi_formula_agrees_with_explicit_refined_distribution() -> None:
    ps = (0.2, 0.3, 0.5)
    access = {0, 2}
    m = 3
    q = 0.5
    gain = renyi_access_gain(ps, access, m, q)

    refined = []
    for i, p in enumerate(ps):
        if i in access:
            refined.extend([p / (2**m)] * (2**m))
        else:
            refined.append(p)
    h_base = log2(sum(p**q for p in ps)) / (1 - q)
    h_refined = log2(sum(p**q for p in refined)) / (1 - q)
    assert gain == pytest.approx(h_refined - h_base, abs=1e-12)


def test_gain_is_between_zero_and_decoder_depth_for_common_depth() -> None:
    ps = (0.02, 0.08, 0.20, 0.70)
    for q in (0.0, 0.25, 0.9, 1.0, 2.0, 5.0):
        for access in ({0}, {3}, {0, 2}, {0, 1, 2, 3}):
            gain = renyi_access_gain(ps, access, 7, q)
            assert -1e-12 <= gain <= 7 + 1e-12


def test_three_regime_asymptotic_slopes() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    access = {0, 3}
    assert asymptotic_slope(ps, access, 0.5) == 1.0
    assert asymptotic_slope(ps, access, 1.0) == pytest.approx(0.5)
    assert asymptotic_slope(ps, access, 2.0) == 0.0


def test_q_below_one_offset_recovers_log_n_over_k_at_q_zero() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    assert asymptotic_offset_q_below_one(ps, {1}, 0.0) == pytest.approx(2.0)


def test_q_below_one_exact_gain_converges_to_m_minus_offset() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    access = {1, 3}
    q = 0.4
    c_q = asymptotic_offset_q_below_one(ps, access, q)
    for m in (20, 40, 80):
        residual = renyi_access_gain(ps, access, m, q) - (m - c_q)
        assert abs(residual) < 2 ** (-0.5 * m)


def test_q_above_one_gain_saturates_at_closed_form_limit() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    access = {0, 3}
    q = 2.0
    limit = asymptotic_limit_q_above_one(ps, access, q)
    assert renyi_access_gain(ps, access, 60, q) == pytest.approx(limit, abs=1e-12)


def test_fixed_budget_extrema_are_sharp_by_brute_force() -> None:
    ps = (0.05, 0.15, 0.30, 0.50)
    n = len(ps)
    k = 2
    m = 6
    for q in (0.0, 0.5, 1.0, 2.0):
        observed = [
            renyi_access_gain(ps, set(access), m, q)
            for access in combinations(range(n), k)
        ]
        low, high = fixed_budget_extrema(ps, k, m, q)
        assert low == pytest.approx(min(observed), abs=1e-12)
        assert high == pytest.approx(max(observed), abs=1e-12)
        if q == 0.0:
            assert low == pytest.approx(high, abs=1e-12)
        else:
            assert high > low


def test_heterogeneous_decoder_capacity_has_exact_shannon_formula() -> None:
    ps = (0.2, 0.3, 0.5)
    multiplicities = (1, 4, 16)
    expected = 0.3 * 2 + 0.5 * 4
    assert heterogeneous_renyi_access_gain(ps, multiplicities, q=1) == pytest.approx(expected)


def test_heterogeneous_formula_reduces_to_common_depth_formula() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    access = {0, 2}
    m = 5
    multiplicities = tuple(2**m if i in access else 1 for i in range(len(ps)))
    for q in (0.0, 0.5, 1.0, 2.0):
        assert heterogeneous_renyi_access_gain(ps, multiplicities, q) == pytest.approx(
            renyi_access_gain(ps, access, m, q), abs=1e-12
        )
