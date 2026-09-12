"""Rényi-order leakage across CREST prerequisite supports.

At Shannon order, prospective information gains factor as weighted unanimity
games on declared prerequisite sets. For other Rényi orders, the logarithm of a
sum over selectively refined semantic cells is nonlinear and can create Möbius
interaction on a coalition that no query declares as a minimal prerequisite.

The two-cell theorem below is not restricted to equal occupancy or equal decoder
depth: for every p in (0,1) and positive depths a,b, the undeclared joint
interaction is negative below Shannon order, zero at q=1, and positive above it.
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


def prospective_renyi_gain(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    coalition: Iterable[str],
    q: float,
    *,
    future_label: str = "F",
) -> float:
    """Direct Rényi gain from all queries licensed by one coalition."""

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


def prospective_renyi_game(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    players: Iterable[str],
    q: float,
    *,
    future_label: str = "F",
) -> dict[frozenset[str], float]:
    """Return the direct prospective Rényi game on every coalition."""

    player_tuple = tuple(dict.fromkeys(players))
    if future_label not in player_tuple:
        raise ValueError("players must include the future responsibility")
    table: dict[frozenset[str], float] = {}
    for size in range(len(player_tuple) + 1):
        for subset in combinations(player_tuple, size):
            coalition = frozenset(subset)
            table[coalition] = prospective_renyi_gain(
                probabilities,
                queries,
                coalition,
                q,
                future_label=future_label,
            )
    return table


def two_cell_disjoint_query_leakage(
    occupancy_left: float,
    left_bits: float,
    right_bits: float,
    q: float,
) -> float:
    """Exact undeclared joint dividend for two disjoint one-interface queries.

    Cell probabilities are p and 1-p. The left query refines only the first cell
    by ``left_bits`` and the right query only the second by ``right_bits``. Their
    prerequisite sets are distinct and neither query declares their union.

    For finite q != 1, put u=p**q, v=(1-p)**q,
    A=2**((1-q)*left_bits), and B=2**((1-q)*right_bits). Then

        D_q = 1/(1-q) log2(((u+v)(uA+vB))/((uA+v)(u+vB))).

    The numerator minus denominator inside the ratio is

        -u v (A-1)(B-1),

    so D_q < 0 for q<1 and D_q > 0 for q>1 whenever p is interior and both
    decoder depths are positive. At q=1, Shannon additivity gives D_1=0.
    """

    p = float(occupancy_left)
    a = float(left_bits)
    b = float(right_bits)
    q = float(q)
    if not 0.0 < p < 1.0:
        raise ValueError("occupancy_left must lie strictly between zero and one")
    if a <= 0.0 or b <= 0.0:
        raise ValueError("both decoder depths must be positive")
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if q == 1.0:
        return 0.0
    if isinf(q):
        # Evaluate the endpoint directly rather than relying on a finite-q limit.
        ps = (p, 1.0 - p)
        both = continuous_decoder_gain(ps, (a, b), inf)
        left = continuous_decoder_gain(ps, (a, 0.0), inf)
        right = continuous_decoder_gain(ps, (0.0, b), inf)
        return both - left - right

    u = p**q
    v = (1.0 - p) ** q
    A = 2.0 ** ((1.0 - q) * a)
    B = 2.0 ** ((1.0 - q) * b)
    ratio = ((u + v) * (u * A + v * B)) / ((u * A + v) * (u + v * B))
    return log2(ratio) / (1.0 - q)


def two_cell_disjoint_query_leakage_sign(
    occupancy_left: float,
    left_bits: float,
    right_bits: float,
    q: float,
) -> int:
    """Return the sign of the exact two-cell undeclared joint dividend."""

    value = two_cell_disjoint_query_leakage(occupancy_left, left_bits, right_bits, q)
    if isclose(value, 0.0, abs_tol=1e-12):
        return 0
    return 1 if value > 0.0 else -1


def symmetric_two_query_leakage(q: float) -> float:
    """Canonical p=1/2, one-bit specialization of the general theorem."""

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
    """Return -1 below Shannon order, 0 at Shannon order, +1 above it."""

    value = symmetric_two_query_leakage(q)
    if isclose(value, 0.0, abs_tol=1e-12):
        return 0
    return 1 if value > 0 else -1
