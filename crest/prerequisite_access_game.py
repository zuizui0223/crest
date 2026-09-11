"""CREST prerequisite-order / semantic-coverage coalition game at Shannon order.

The object here is the *prospective information gain* contributed by a family of
future queries. Each query has a declared minimal prerequisite interface set, a
semantic access set over pre-future cells, and a decoder depth. At Shannon order,
conditionally independent equal refinements add exactly, so the resulting
coalition game is a weighted sum of unanimity games.

Möbius/Harsanyi inversion itself is standard. The CREST-specific statement is
that prerequisite sets determine the exact support of the prospective dividend,
while semantic-access occupancy determines only its weight.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import isclose
from typing import Iterable, Mapping, Sequence


@dataclass(frozen=True)
class ProspectiveQuery:
    """One future query with declared prerequisites and semantic coverage."""

    name: str
    required_interfaces: frozenset[str]
    accessible_cells: frozenset[int]
    bit_depth: float

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("query name must be nonempty")
        if self.bit_depth < 0:
            raise ValueError("bit_depth must be nonnegative")


def _probabilities(probabilities: Sequence[float]) -> tuple[float, ...]:
    ps = tuple(float(p) for p in probabilities)
    if not ps:
        raise ValueError("probabilities must be nonempty")
    if any(p < 0.0 for p in ps):
        raise ValueError("probabilities must be nonnegative")
    if not isclose(sum(ps), 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return ps


def _validate_query(query: ProspectiveQuery, n_cells: int, future_label: str) -> None:
    if future_label in query.required_interfaces:
        raise ValueError("future label must not be repeated inside required_interfaces")
    if any(i < 0 or i >= n_cells for i in query.accessible_cells):
        raise ValueError("accessible cell index out of range")


def accessible_mass(probabilities: Sequence[float], query: ProspectiveQuery) -> float:
    """Probability mass of the semantic cells addressable by one query."""

    ps = _probabilities(probabilities)
    _validate_query(query, len(ps), "F")
    return sum(ps[i] for i in query.accessible_cells)


def query_weight(probabilities: Sequence[float], query: ProspectiveQuery) -> float:
    """Shannon information supplied by one licensed query."""

    ps = _probabilities(probabilities)
    if any(i < 0 or i >= len(ps) for i in query.accessible_cells):
        raise ValueError("accessible cell index out of range")
    return query.bit_depth * sum(ps[i] for i in query.accessible_cells)


def prospective_shannon_gain(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    coalition: Iterable[str],
    *,
    future_label: str = "F",
) -> float:
    """Prospective Shannon gain available to one coalition.

    Query ``f`` contributes iff the future responsibility is present and every
    declared interface in ``R_f`` is retained. Semantic coverage changes the
    contribution magnitude through the accessible occupancy mass.
    """

    ps = _probabilities(probabilities)
    members = frozenset(coalition)
    total = 0.0
    for query in queries:
        _validate_query(query, len(ps), future_label)
        if future_label in members and query.required_interfaces.issubset(members):
            total += query.bit_depth * sum(ps[i] for i in query.accessible_cells)
    return total


def prospective_game(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    players: Iterable[str],
    *,
    future_label: str = "F",
) -> dict[frozenset[str], float]:
    """Return prospective Shannon gain for every coalition of ``players``."""

    player_tuple = tuple(dict.fromkeys(players))
    if future_label not in player_tuple:
        raise ValueError("players must include the future responsibility")
    table: dict[frozenset[str], float] = {}
    for size in range(len(player_tuple) + 1):
        for subset in combinations(player_tuple, size):
            coalition = frozenset(subset)
            table[coalition] = prospective_shannon_gain(
                probabilities, queries, coalition, future_label=future_label
            )
    return table


def mobius_transform(
    game: Mapping[frozenset[str], float],
) -> dict[frozenset[str], float]:
    """Standard Boolean-lattice Möbius transform of a complete coalition game."""

    coalitions = set(game)
    players = frozenset().union(*coalitions) if coalitions else frozenset()
    expected = {
        frozenset(subset)
        for size in range(len(players) + 1)
        for subset in combinations(tuple(players), size)
    }
    if coalitions != expected:
        raise ValueError("game must contain every coalition on one player set")

    dividend: dict[frozenset[str], float] = {}
    for target in coalitions:
        total = 0.0
        target_tuple = tuple(target)
        for size in range(len(target_tuple) + 1):
            for subset in combinations(target_tuple, size):
                source = frozenset(subset)
                total += ((-1) ** (len(target) - len(source))) * game[source]
        dividend[target] = total
    return dividend


def predicted_dividends(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    *,
    future_label: str = "F",
) -> dict[frozenset[str], float]:
    """Closed-form CREST support theorem for prospective Shannon dividends."""

    ps = _probabilities(probabilities)
    out: dict[frozenset[str], float] = {}
    for query in queries:
        _validate_query(query, len(ps), future_label)
        support = query.required_interfaces | frozenset((future_label,))
        weight = query.bit_depth * sum(ps[i] for i in query.accessible_cells)
        out[support] = out.get(support, 0.0) + weight
    return out


def direct_refinement_shannon_gain(
    probabilities: Sequence[float],
    queries: Sequence[ProspectiveQuery],
    coalition: Iterable[str],
    *,
    future_label: str = "F",
) -> float:
    """Compute the same gain cell-by-cell from combined local multiplicities.

    If several licensed queries address the same semantic cell, their decoder
    depths add and their descendant multiplicities multiply. This direct form is
    useful as an independent check of the query-wise decomposition.
    """

    ps = _probabilities(probabilities)
    members = frozenset(coalition)
    total = 0.0
    for i, p in enumerate(ps):
        local_bits = 0.0
        for query in queries:
            _validate_query(query, len(ps), future_label)
            if (
                future_label in members
                and query.required_interfaces.issubset(members)
                and i in query.accessible_cells
            ):
                local_bits += query.bit_depth
        total += p * local_bits
    return total
