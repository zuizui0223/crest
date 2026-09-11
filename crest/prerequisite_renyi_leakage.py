"""Rényi-order leakage across CREST prerequisite supports.

At Shannon order, prospective information gains factor as weighted unanimity
games on declared prerequisite sets. For other Rényi orders, the logarithm of a
sum over selectively refined semantic cells is nonlinear and can create Möbius
interaction on a coalition that no query declares as a minimal prerequisite.

This module provides the general direct game and the minimal two-cell witness in
which the leakage vanishes if and only if q=1.
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


def symmetric_two_query_leakage(q: float) -> float:
    """Closed-form H×THETA×F leakage for the minimal two-cell witness.

    Two equiprobable semantic cells are used. One one-bit query requires H and
    refines only cell 0; a second one-bit query requires THETA and refines only
    cell 1. No query requires H and THETA jointly.

    The H×THETA×F Möbius dividend is

        D_q = 1 - 2/(1-q) log2(1/2 + 2^{-q}),  q != 1,

    with continuous value D_1=0. At q=infinity the limit is 1.
    """

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
