"""Semantic-access construction for CREST v0.7.

This module deliberately derives retained history and mechanism interfaces from
nontrivial companion semantics before any future decoder is introduced.

History modes are derived from complete MLTR-style carried maps of declared
replacement routes.  Mechanism response types are derived from complete MRM-style
candidate transition tables.  A future decoder is then allowed to depend on
specific semantic history/response-type pairs, rather than merely on the presence
of the abstract axes H and THETA.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ReplacementRoute:
    name: str
    carried_map: tuple[int, ...]


@dataclass(frozen=True)
class CandidateLaw:
    name: str
    response_table: tuple[int, ...]


@dataclass(frozen=True)
class HistoryMode:
    carried_map: tuple[int, ...]
    routes: tuple[str, ...]


@dataclass(frozen=True)
class ResponseType:
    response_table: tuple[int, ...]
    candidates: tuple[str, ...]


@dataclass(frozen=True)
class SemanticWorld:
    route: ReplacementRoute
    candidate: CandidateLaw
    exterior: tuple[int, ...]


@dataclass(frozen=True)
class SemanticAccessModel:
    history_modes: tuple[HistoryMode, ...]
    response_types: tuple[ResponseType, ...]
    access_relation: frozenset[tuple[tuple[int, ...], tuple[int, ...]]]


def minimum_history_modes(routes: Iterable[ReplacementRoute]) -> tuple[HistoryMode, ...]:
    """Derive the exact MLTR-style minimum history completion.

    Routes are equivalent exactly when their complete carried terminal maps agree.
    This is the route-coherence quotient used by MLTR; no mode labels are supplied
    by the caller.
    """

    buckets: dict[tuple[int, ...], list[str]] = {}
    for route in routes:
        buckets.setdefault(route.carried_map, []).append(route.name)
    return tuple(
        HistoryMode(carried_map=key, routes=tuple(sorted(names)))
        for key, names in sorted(buckets.items())
    )


def candidate_safe_response_types(candidates: Iterable[CandidateLaw]) -> tuple[ResponseType, ...]:
    """Derive exact MRM-style response types from complete transition tables."""

    buckets: dict[tuple[int, ...], list[str]] = {}
    for candidate in candidates:
        buckets.setdefault(candidate.response_table, []).append(candidate.name)
    return tuple(
        ResponseType(response_table=key, candidates=tuple(sorted(names)))
        for key, names in sorted(buckets.items())
    )


def route_mode(route: ReplacementRoute, modes: tuple[HistoryMode, ...]) -> HistoryMode:
    return next(mode for mode in modes if mode.carried_map == route.carried_map)


def candidate_type(candidate: CandidateLaw, types: tuple[ResponseType, ...]) -> ResponseType:
    return next(kind for kind in types if kind.response_table == candidate.response_table)


def decoder_can_address(
    world: SemanticWorld,
    model: SemanticAccessModel,
) -> bool:
    """Whether the world's semantic interface pair licenses the future decoder."""

    h = route_mode(world.route, model.history_modes).carried_map
    theta = candidate_type(world.candidate, model.response_types).response_table
    return (h, theta) in model.access_relation


def semantic_trace(
    world: SemanticWorld,
    model: SemanticAccessModel,
    query_index: int,
) -> int | None:
    """Evaluate one exterior query under semantic access.

    ``None`` means that the query is not addressable from the semantic history ×
    response-type interface carried by this world.  When addressable, the decoder
    returns the requested exterior bit.
    """

    if not 0 <= query_index < len(world.exterior):
        raise ValueError("query_index out of range")
    if not decoder_can_address(world, model):
        return None
    return world.exterior[query_index]


def canonical_nontrivial_companion_model() -> tuple[
    tuple[ReplacementRoute, ...], tuple[CandidateLaw, ...], SemanticAccessModel
]:
    """Return a small model whose companion semantics are genuinely nontrivial.

    MLTR side: three declared routes, two coherent with one another and one
    path-incoherent, yielding two minimum history modes from three raw histories.

    MRM side: three candidate laws, two candidate-safe equivalent and one distinct,
    yielding two response types from three primitive candidates.

    The semantic access relation is intentionally sparse: only the combination of
    the path-incoherent history mode and the distinct response type licenses the
    exterior decoder.  Thus decoder availability depends on *which* carried
    semantics and *which* response type are present, not merely on axis labels.
    """

    routes = (
        ReplacementRoute("route_a", (0, 1, 0)),
        ReplacementRoute("route_b", (0, 1, 0)),
        ReplacementRoute("route_c", (1, 0, 1)),
    )
    candidates = (
        CandidateLaw("candidate_a", (0, 0, 1, 1)),
        CandidateLaw("candidate_b", (0, 0, 1, 1)),
        CandidateLaw("candidate_c", (1, 0, 1, 0)),
    )
    modes = minimum_history_modes(routes)
    types = candidate_safe_response_types(candidates)
    access = frozenset({((1, 0, 1), (1, 0, 1, 0))})
    return routes, candidates, SemanticAccessModel(modes, types, access)


__all__ = [
    "CandidateLaw",
    "HistoryMode",
    "ReplacementRoute",
    "ResponseType",
    "SemanticAccessModel",
    "SemanticWorld",
    "candidate_safe_response_types",
    "canonical_nontrivial_companion_model",
    "decoder_can_address",
    "minimum_history_modes",
    "semantic_trace",
]
