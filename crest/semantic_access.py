"""Semantic-access construction for CREST v0.7.

CREST consumes *completed semantic outputs* from the companion theories before any
future decoder is introduced.

- On the MLTR side, a ``ReplacementRoute`` carries the complete terminal map that
  MLTR's replacement-relation machinery has already derived for that route. CREST
  does not recompute relation composition here; it quotients routes by equality of
  those carried maps, exactly the minimum history-mode criterion after route
  incoherence has been detected upstream.
- On the MRM side, a ``CandidateLaw`` carries its complete declared response table.
  CREST quotients primitive candidates by equality of those tables, the exact
  candidate-safe response-type criterion.

A future decoder can then depend on specific semantic history-mode x response-type
pairs rather than merely on the presence of abstract H and THETA axis labels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, TypeVar


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


T = TypeVar("T")


def _group_named_primitives_by_signature(
    primitives: Iterable[T],
    *,
    name_of: Callable[[T], str],
    signature_of: Callable[[T], tuple[int, ...]],
) -> tuple[tuple[tuple[int, ...], tuple[str, ...]], ...]:
    """Shared finite quotient helper; domain semantics live in the wrappers below."""

    buckets: dict[tuple[int, ...], list[str]] = {}
    for primitive in primitives:
        buckets.setdefault(signature_of(primitive), []).append(name_of(primitive))
    return tuple((key, tuple(sorted(names))) for key, names in sorted(buckets.items()))


def minimum_history_modes(routes: Iterable[ReplacementRoute]) -> tuple[HistoryMode, ...]:
    """Quotient MLTR routes by complete carried terminal semantics.

    The carried maps are companion outputs, not route labels.  Distinct raw routes
    collapse exactly when MLTR says their complete carried terminal maps agree.
    CREST intentionally does not reimplement the upstream replacement-relation
    composition that produced those maps.
    """

    grouped = _group_named_primitives_by_signature(
        routes,
        name_of=lambda route: route.name,
        signature_of=lambda route: route.carried_map,
    )
    return tuple(HistoryMode(carried_map=key, routes=names) for key, names in grouped)


def candidate_safe_response_types(candidates: Iterable[CandidateLaw]) -> tuple[ResponseType, ...]:
    """Quotient primitive candidate laws by complete declared response tables."""

    grouped = _group_named_primitives_by_signature(
        candidates,
        name_of=lambda candidate: candidate.name,
        signature_of=lambda candidate: candidate.response_table,
    )
    return tuple(ResponseType(response_table=key, candidates=names) for key, names in grouped)


def route_mode(route: ReplacementRoute, modes: tuple[HistoryMode, ...]) -> HistoryMode:
    return next(mode for mode in modes if mode.carried_map == route.carried_map)


def candidate_type(candidate: CandidateLaw, types: tuple[ResponseType, ...]) -> ResponseType:
    return next(kind for kind in types if kind.response_table == candidate.response_table)


def decoder_can_address(
    world: SemanticWorld,
    model: SemanticAccessModel,
) -> bool:
    """Whether the world's *derived semantic pair* licenses the future decoder."""

    h = route_mode(world.route, model.history_modes).carried_map
    theta = candidate_type(world.candidate, model.response_types).response_table
    return (h, theta) in model.access_relation


def semantic_trace(
    world: SemanticWorld,
    model: SemanticAccessModel,
    query_index: int,
) -> int | None:
    """Evaluate one exterior query under semantic access.

    ``None`` means that the query is not addressable from this semantic history x
    response-type pair.  When addressable, the decoder returns the requested
    exterior bit.
    """

    if not 0 <= query_index < len(world.exterior):
        raise ValueError("query_index out of range")
    if not decoder_can_address(world, model):
        return None
    return world.exterior[query_index]


def canonical_nontrivial_companion_model() -> tuple[
    tuple[ReplacementRoute, ...], tuple[CandidateLaw, ...], SemanticAccessModel
]:
    """Return a small model with nontrivial companion semantic quotients.

    MLTR-facing input: three declared routes whose *already-derived* carried maps
    yield two minimum history modes (two routes share one carried map, the third
    has another).

    MRM-facing input: three primitive candidate laws whose complete response tables
    yield two candidate-safe response types (two candidates are response-equivalent,
    the third is distinct).

    The semantic access relation is sparse: only one of the four derived semantic
    history-mode x response-type pairs licenses the exterior decoder.  Decoder
    availability therefore depends on which semantic classes are present, not on
    raw route/candidate identity.
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
    "candidate_type",
    "canonical_nontrivial_companion_model",
    "decoder_can_address",
    "minimum_history_modes",
    "route_mode",
    "semantic_trace",
]
