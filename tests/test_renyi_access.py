from itertools import combinations
from math import inf, log2

import pytest

from crest.renyi_access import (
    asymptotic_limit_q_above_one,
    asymptotic_offset_q_below_one,
    asymptotic_slope,
    continuous_decoder_gain,
    fixed_budget_extrema,
    heterogeneous_renyi_access_gain,
    optimal_decoder_allocation,
    optimal_integer_decoder_allocation,
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


def test_min_entropy_endpoint_is_exact() -> None:
    ps = (0.50, 0.30, 0.20)
    # Splitting the dominant cell four ways makes 0.30 the largest remaining atom.
    assert renyi_access_gain(ps, {0}, 2, q=inf) == pytest.approx(log2(0.50 / 0.30))
    # If the dominant cell is inaccessible, min-entropy cannot improve.
    assert renyi_access_gain(ps, {1, 2}, 8, q=inf) == pytest.approx(0.0)


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
    for q in (0.0, 0.25, 0.9, 1.0, 2.0, 5.0, inf):
        for access in ({0}, {3}, {0, 2}, {0, 1, 2, 3}):
            gain = renyi_access_gain(ps, access, 7, q)
            assert -1e-12 <= gain <= 7 + 1e-12


def test_three_regime_asymptotic_slopes() -> None:
    ps = (0.1, 0.2, 0.3, 0.4)
    access = {0, 3}
    assert asymptotic_slope(ps, access, 0.5) == 1.0
    assert asymptotic_slope(ps, access, 1.0) == pytest.approx(0.5)
    assert asymptotic_slope(ps, access, 2.0) == 0.0
    assert asymptotic_slope(ps, access, inf) == 0.0


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
    for q in (0.0, 0.5, 1.0, 2.0, inf):
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
            assert high >= low


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
    for q in (0.0, 0.5, 1.0, 2.0, inf):
        assert heterogeneous_renyi_access_gain(ps, multiplicities, q) == pytest.approx(
            renyi_access_gain(ps, access, m, q), abs=1e-12
        )


def _simplex_grid(budget: float, step: float) -> list[tuple[float, float, float]]:
    units = round(budget / step)
    return [
        (i * step, j * step, (units - i - j) * step)
        for i in range(units + 1)
        for j in range(units - i + 1)
    ]


def test_optimal_budget_concentrates_for_q_at_or_below_one() -> None:
    ps = (0.50, 0.30, 0.20)
    budget = 2.0
    grid = _simplex_grid(budget, 0.25)
    for q in (0.0, 0.5, 1.0):
        optimum = optimal_decoder_allocation(ps, budget, q)
        optimum_gain = continuous_decoder_gain(ps, optimum, q)
        brute = max(continuous_decoder_gain(ps, candidate, q) for candidate in grid)
        assert sum(optimum) == pytest.approx(budget, abs=1e-12)
        assert optimum_gain == pytest.approx(brute, abs=1e-12)
        if q > 0.0:
            assert optimum == pytest.approx((budget, 0.0, 0.0), abs=1e-12)


def test_q_above_one_water_filling_is_globally_optimal_on_grid() -> None:
    ps = (0.50, 0.30, 0.20)
    budget = 2.0
    q = 2.0
    optimum = optimal_decoder_allocation(ps, budget, q)
    optimum_gain = continuous_decoder_gain(ps, optimum, q)
    brute = max(
        continuous_decoder_gain(ps, candidate, q)
        for candidate in _simplex_grid(budget, 0.05)
    )
    assert sum(optimum) == pytest.approx(budget, abs=1e-12)
    assert optimum_gain >= brute - 1e-12
    assert optimum[0] > 0.0
    assert optimum[1] > 0.0


def test_water_filling_equalizes_active_weighted_residuals() -> None:
    ps = (0.50, 0.30, 0.15, 0.05)
    q = 2.0
    allocation = optimal_decoder_allocation(ps, 4.0, q)
    residuals = [
        (p**q) * (2.0 ** ((1.0 - q) * x))
        for p, x in zip(ps, allocation)
    ]
    active = [r for r, x in zip(residuals, allocation) if x > 1e-10]
    assert max(active) - min(active) < 1e-10
    inactive = [r for r, x in zip(residuals, allocation) if x <= 1e-10]
    assert all(r <= active[0] + 1e-10 for r in inactive)


def test_min_entropy_budget_limit_is_water_filling_on_log_probability() -> None:
    ps = (0.50, 0.30, 0.20)
    budget = 2.0
    allocation = optimal_decoder_allocation(ps, budget, inf)
    gain = continuous_decoder_gain(ps, allocation, inf)
    brute = max(
        continuous_decoder_gain(ps, candidate, inf)
        for candidate in _simplex_grid(budget, 0.05)
    )
    assert gain >= brute - 1e-12
    assert sum(allocation) == pytest.approx(budget, abs=1e-12)


def _integer_compositions(total: int, parts: int) -> list[tuple[int, ...]]:
    if parts == 1:
        return [(total,)]
    out: list[tuple[int, ...]] = []
    for first in range(total + 1):
        for rest in _integer_compositions(total - first, parts - 1):
            out.append((first,) + rest)
    return out


def test_integer_budget_greedy_is_exact_by_exhaustive_enumeration() -> None:
    ps = (0.50, 0.30, 0.20)
    budget = 6
    candidates = _integer_compositions(budget, len(ps))
    for q in (0.0, 0.5, 1.0, 1.5, 2.0, 4.0, inf):
        optimum = optimal_integer_decoder_allocation(ps, budget, q)
        optimum_gain = continuous_decoder_gain(ps, optimum, q)
        brute = max(continuous_decoder_gain(ps, candidate, q) for candidate in candidates)
        assert sum(optimum) == budget
        assert optimum_gain == pytest.approx(brute, abs=1e-12)
        if 0.0 < q <= 1.0:
            assert optimum == (budget, 0, 0)


def test_integer_q_above_one_allocation_has_no_profitable_one_bit_exchange() -> None:
    ps = (0.50, 0.30, 0.15, 0.05)
    budget = 9
    for q in (1.25, 2.0, 5.0, inf):
        optimum = optimal_integer_decoder_allocation(ps, budget, q)
        gain = continuous_decoder_gain(ps, optimum, q)
        for donor, depth in enumerate(optimum):
            if depth == 0:
                continue
            for receiver in range(len(ps)):
                if receiver == donor:
                    continue
                moved = list(optimum)
                moved[donor] -= 1
                moved[receiver] += 1
                assert gain >= continuous_decoder_gain(ps, moved, q) - 1e-12
