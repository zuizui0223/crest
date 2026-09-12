"""Rényi-order leakage across CREST prerequisite supports.

At Shannon order, prospective information gains factor as weighted unanimity
games on declared prerequisite sets. For other Rényi orders, the logarithm of a
sum over selectively refined semantic cells is nonlinear and can create Möbius
interaction on a coalition that no query declares as a minimal prerequisite.

The disjoint-access theorem below is not restricted to two semantic cells,
equal occupancy, or equal decoder depth. For any positive occupancy vector,
any two nonempty disjoint access sets, and positive depths a,b, the undeclared
joint interaction is negative below Shannon order, zero at q=1, and positive at
every finite order above it.
"""

from __future__ import annotations

from itertools import combinations
from math import inf, isclose, isinf, log2
from typing import Iterable, Sequence

from .prerequisite_access_game import ProspectiveQuery
from .renyi_access import continuous_decoder_gain


def _probabilities(probabilities: Sequence[float]) -> tuple[float, ...]:
    ps = tuple(float(p) for p in probabilities)
    if not ps:
        raise ValueError("probabilities must be nonempty")
    if any(p <= 0.0 for p in ps):
        raise ValueError("probabilities must be positive")
    if not isclose(sum(ps), 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return ps


def prospective_renyi_gain(probabilities: Sequence[float], queries: Sequence[ProspectiveQuery], coalition: Iterable[str], q: float, *, future_label: str = "F") -> float:
    ps = _probabilities(probabilities)
    members = frozenset(coalition)
    local_bits = [0.0 for _ in ps]
    for query in queries:
        if future_label in query.required_interfaces:
            raise ValueError("future label must not appear inside required_interfaces")
        if any(i < 0 or i >= len(ps) for i in query.accessible_cells):
            raise ValueError("accessible cell index out of range")
        if future_label in members and query.required_interfaces.issubset(members):
            for i in query.accessible_cells:
                local_bits[i] += query.bit_depth
    return continuous_decoder_gain(ps, local_bits, q)


def prospective_renyi_game(probabilities: Sequence[float], queries: Sequence[ProspectiveQuery], players: Iterable[str], q: float, *, future_label: str = "F") -> dict[frozenset[str], float]:
    player_tuple = tuple(dict.fromkeys(players))
    if future_label not in player_tuple:
        raise ValueError("players must include the future responsibility")
    table: dict[frozenset[str], float] = {}
    for size in range(len(player_tuple) + 1):
        for subset in combinations(player_tuple, size):
            coalition = frozenset(subset)
            table[coalition] = prospective_renyi_gain(probabilities, queries, coalition, q, future_label=future_label)
    return table


def _validate_disjoint_access_inputs(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> tuple[tuple[float, ...], frozenset[int], frozenset[int], float, float, float]:
    ps = _probabilities(probabilities)
    left = frozenset(int(i) for i in left_cells)
    right = frozenset(int(i) for i in right_cells)
    a, b, order = map(float, (left_bits, right_bits, q))
    if not left or not right:
        raise ValueError("both access sets must be nonempty")
    if left & right:
        raise ValueError("access sets must be disjoint")
    if any(i < 0 or i >= len(ps) for i in left | right):
        raise ValueError("accessible cell index out of range")
    if a <= 0.0 or b <= 0.0:
        raise ValueError("both decoder depths must be positive")
    if order < 0.0:
        raise ValueError("q must be nonnegative")
    return ps, left, right, a, b, order


def disjoint_access_set_leakage(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> float:
    """Exact undeclared joint dividend for two disjoint access channels.

    Let U=sum_{i in L} p_i**q, V=sum_{i in R} p_i**q, and W be the q-power
    mass of all residual cells. With A=2**((1-q)*a) and
    B=2**((1-q)*b), the finite-q joint dividend is

        D_q = 1/(1-q) log2(
            ((U*A + V*B + W) * (U+V+W)) /
            ((U*A + V + W) * (U + V*B + W))
        ).

    The numerator minus denominator inside the ratio factors exactly as

        -U*V*(A-1)*(B-1).

    Hence every positive occupancy vector and every pair of nonempty disjoint
    access sets obey the same strict finite-q sign law: negative below Shannon,
    zero at Shannon, positive above Shannon. Residual cells cancel from the sign.
    """

    ps, left, right, a, b, q = _validate_disjoint_access_inputs(
        probabilities, left_cells, right_cells, left_bits, right_bits, q
    )
    if q == 1.0:
        return 0.0
    if isinf(q):
        local_left = [a if i in left else 0.0 for i in range(len(ps))]
        local_right = [b if i in right else 0.0 for i in range(len(ps))]
        local_both = [local_left[i] + local_right[i] for i in range(len(ps))]
        both = continuous_decoder_gain(ps, local_both, inf)
        left_gain = continuous_decoder_gain(ps, local_left, inf)
        right_gain = continuous_decoder_gain(ps, local_right, inf)
        return both - left_gain - right_gain

    U = sum(ps[i] ** q for i in left)
    V = sum(ps[i] ** q for i in right)
    W = sum(ps[i] ** q for i in range(len(ps)) if i not in left and i not in right)
    A = 2.0 ** ((1.0 - q) * a)
    B = 2.0 ** ((1.0 - q) * b)
    ratio = ((U * A + V * B + W) * (U + V + W)) / (
        (U * A + V + W) * (U + V * B + W)
    )
    return log2(ratio) / (1.0 - q)


def disjoint_access_set_leakage_sign(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> int:
    """Return the theorem's exact sign for finite q, avoiding cancellation."""

    _, _, _, _, _, q = _validate_disjoint_access_inputs(
        probabilities, left_cells, right_cells, left_bits, right_bits, q
    )
    if q == 1.0:
        return 0
    if not isinf(q):
        return -1 if q < 1.0 else 1
    value = disjoint_access_set_leakage(
        probabilities, left_cells, right_cells, left_bits, right_bits, q
    )
    if isclose(value, 0.0, abs_tol=1e-12):
        return 0
    return 1 if value > 0.0 else -1


def _validate_two_cell_inputs(occupancy_left: float, left_bits: float, right_bits: float, q: float) -> tuple[float, float, float, float]:
    p, a, b, order = map(float, (occupancy_left, left_bits, right_bits, q))
    if not 0.0 < p < 1.0:
        raise ValueError("occupancy_left must lie strictly between zero and one")
    if a <= 0.0 or b <= 0.0:
        raise ValueError("both decoder depths must be positive")
    if order < 0.0:
        raise ValueError("q must be nonnegative")
    return p, a, b, order


def two_cell_disjoint_query_leakage(occupancy_left: float, left_bits: float, right_bits: float, q: float) -> float:
    """Two-cell specialization of :func:`disjoint_access_set_leakage`."""

    p, a, b, q = _validate_two_cell_inputs(occupancy_left, left_bits, right_bits, q)
    return disjoint_access_set_leakage((p, 1.0 - p), (0,), (1,), a, b, q)


def two_cell_disjoint_query_leakage_sign(occupancy_left: float, left_bits: float, right_bits: float, q: float) -> int:
    """Two-cell specialization of the exact disjoint-access sign law."""

    p, a, b, q = _validate_two_cell_inputs(occupancy_left, left_bits, right_bits, q)
    return disjoint_access_set_leakage_sign((p, 1.0 - p), (0,), (1,), a, b, q)


def symmetric_two_query_leakage(q: float) -> float:
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if q == 1.0:
        return 0.0
    if isinf(q):
        return 1.0
    single = log2(0.5 + (2.0 ** (-q))) / (1.0 - q)
    return 1.0 - 2.0 * single


def symmetric_two_query_leakage_sign(q: float) -> int:
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if q == 1.0:
        return 0
    if not isinf(q):
        return -1 if q < 1.0 else 1
    return 1
