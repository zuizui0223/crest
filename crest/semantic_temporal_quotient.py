"""Semantic-access temporal quotient for CREST v0.7.

This module connects the MLTR/MRM semantic quotients in ``semantic_access`` to
CREST's coalition-state calculation.  Unlike the older axis-complete grammar,
future decoder traces may be licensed on only a subset of semantic
history-mode x response-type pairs.

The state value of a coalition is derived by enumerating raw routes, primitive
candidate laws, exterior signatures, legal traces, and the induced quotient.
No coalition bit value is assigned directly.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log2
from typing import Iterable

from .explicit_temporal_grammar import AXES, FUTURE, HISTORY, MECHANISM
from .semantic_access import (
    CandidateLaw,
    ReplacementRoute,
    SemanticAccessModel,
    candidate_type,
    decoder_can_address,
    route_mode,
)


@dataclass(frozen=True)
class SemanticQuotientWorld:
    route: ReplacementRoute
    candidate: CandidateLaw
    exterior: tuple[int, ...]


def _normalize_coalition(coalition: Iterable[str]) -> frozenset[str]:
    members = frozenset(coalition)
    if not members.issubset(AXES):
        raise ValueError("coalition contains an unknown responsibility")
    return members


def semantic_worlds(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    bit_depth: int,
) -> tuple[SemanticQuotientWorld, ...]:
    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")
    return tuple(
        SemanticQuotientWorld(route, candidate, exterior)
        for route in routes
        for candidate in candidates
        for exterior in product((0, 1), repeat=bit_depth)
    )


def semantic_profile(
    world: SemanticQuotientWorld,
    coalition: Iterable[str],
    model: SemanticAccessModel,
) -> tuple[object, ...]:
    """Return the complete legal trace profile for one coalition.

    H reveals the *derived* MLTR history mode, THETA reveals the *derived* MRM
    response type, and F reveals the exterior signature only when both semantic
    interfaces are retained and that particular semantic pair is licensed by the
    access relation.  Non-addressable exterior signatures therefore collapse.
    """

    members = _normalize_coalition(coalition)
    profile: list[object] = []

    if HISTORY in members:
        profile.append(route_mode(world.route, model.history_modes).carried_map)
    if MECHANISM in members:
        profile.append(candidate_type(world.candidate, model.response_types).response_table)

    if HISTORY in members and MECHANISM in members and FUTURE in members:
        # decoder_can_address expects SemanticWorld-shaped attributes only.
        if decoder_can_address(world, model):
            profile.extend(world.exterior)
        else:
            # One explicit inaccessible symbol is enough: all exterior signatures
            # behind this semantic pair are observationally merged.
            profile.append("INACCESSIBLE")
    return tuple(profile)


def semantic_induced_classes(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    model: SemanticAccessModel,
    bit_depth: int,
    coalition: Iterable[str],
) -> tuple[tuple[SemanticQuotientWorld, ...], ...]:
    buckets: dict[tuple[object, ...], list[SemanticQuotientWorld]] = {}
    for world in semantic_worlds(routes, candidates, bit_depth):
        key = semantic_profile(world, coalition, model)
        buckets.setdefault(key, []).append(world)
    return tuple(tuple(bucket) for bucket in buckets.values())


def semantic_quotient_size(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    model: SemanticAccessModel,
    bit_depth: int,
    coalition: Iterable[str],
) -> int:
    return len(semantic_induced_classes(routes, candidates, model, bit_depth, coalition))


def semantic_quotient_bits(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    model: SemanticAccessModel,
    bit_depth: int,
    coalition: Iterable[str],
) -> float:
    return log2(semantic_quotient_size(routes, candidates, model, bit_depth, coalition))


def semantic_coalition_table(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    model: SemanticAccessModel,
    bit_depth: int,
) -> dict[frozenset[str], float]:
    table: dict[frozenset[str], float] = {}
    for mask in range(1 << len(AXES)):
        coalition = frozenset(AXES[i] for i in range(len(AXES)) if mask & (1 << i))
        table[coalition] = semantic_quotient_bits(routes, candidates, model, bit_depth, coalition)
    return table


def semantic_three_way_dividend(
    routes: tuple[ReplacementRoute, ...],
    candidates: tuple[CandidateLaw, ...],
    model: SemanticAccessModel,
    bit_depth: int,
) -> float:
    v = semantic_coalition_table(routes, candidates, model, bit_depth)
    h = frozenset((HISTORY,))
    theta = frozenset((MECHANISM,))
    future = frozenset((FUTURE,))
    return (
        v[frozenset(AXES)]
        - v[h | theta]
        - v[h | future]
        - v[theta | future]
        + v[h]
        + v[theta]
        + v[future]
        - v[frozenset()]
    )


def semantic_pair_counts(model: SemanticAccessModel) -> tuple[int, int]:
    """Return (total semantic pairs, addressable semantic pairs)."""

    all_pairs = {
        (h.carried_map, theta.response_table)
        for h in model.history_modes
        for theta in model.response_types
    }
    addressable = all_pairs & set(model.access_relation)
    return len(all_pairs), len(addressable)


def predicted_grand_quotient_size(model: SemanticAccessModel, bit_depth: int) -> int:
    """Closed-form consequence of sparse semantic access.

    If N semantic pairs exist and k are addressable, each inaccessible pair gives
    one grand-coalition class while each addressable pair contributes 2^m classes.
    """

    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")
    total, addressable = semantic_pair_counts(model)
    return (total - addressable) + addressable * (2**bit_depth)


def predicted_three_way_dividend(model: SemanticAccessModel, bit_depth: int) -> float:
    total, _ = semantic_pair_counts(model)
    return log2(predicted_grand_quotient_size(model, bit_depth) / total)


__all__ = [
    "SemanticQuotientWorld",
    "predicted_grand_quotient_size",
    "predicted_three_way_dividend",
    "semantic_coalition_table",
    "semantic_induced_classes",
    "semantic_pair_counts",
    "semantic_profile",
    "semantic_quotient_bits",
    "semantic_quotient_size",
    "semantic_three_way_dividend",
    "semantic_worlds",
]
