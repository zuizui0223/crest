"""Pure temporal-cut geometry for CREST.

This module re-expresses the existing v0.7 semantic quotient as a theory of
state at a temporal boundary.

The present is represented by an observation cut, not by a finite-duration
interval.  The finite theory therefore treats the cut as primitive; it does
not claim a continuous-time epsilon->0 limit theorem.

Three kinds of distinguishability act on the cut:

- retrospective: carried history semantics arriving from the left of the cut;
- transverse: candidate-safe latent response structure inside one visible cut
  fiber;
- prospective: distinctions exposed by legal right-of-cut queries.

The adequate cut-state is the least quotient induced by the retained
constraints.  This module is a naming/geometry layer over the already tested
semantic-access quotient; it does not alter its mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable

from .explicit_temporal_grammar import FUTURE, HISTORY, MECHANISM
from .semantic_access import SemanticAccessModel
from .semantic_temporal_quotient import (
    SemanticQuotientWorld,
    semantic_induced_classes,
    semantic_profile,
)

RETROSPECTIVE = HISTORY
TRANSVERSE = MECHANISM
PROSPECTIVE = FUTURE
CUT_DIRECTIONS = (RETROSPECTIVE, TRANSVERSE, PROSPECTIVE)


@dataclass(frozen=True)
class TemporalCutObservation:
    """A zero-duration finite-theory observation cut.

    ``observe`` is represented extensionally by a mapping from raw-world keys to
    visible values.  Worlds with the same visible value lie in one cut fiber.
    """

    visible_by_world: tuple[tuple[Hashable, Hashable], ...]

    def visible_value(self, world_key: Hashable) -> Hashable:
        mapping = dict(self.visible_by_world)
        return mapping[world_key]

    def fiber(self, visible_value: Hashable) -> frozenset[Hashable]:
        return frozenset(
            world_key
            for world_key, value in self.visible_by_world
            if value == visible_value
        )


def transverse_present_type(
    world: SemanticQuotientWorld,
    model: SemanticAccessModel,
) -> tuple[int, ...]:
    """Return the MRM-derived response type hidden inside the visible cut fiber."""

    profile = semantic_profile(world, (TRANSVERSE,), model)
    if len(profile) != 1:
        raise RuntimeError("transverse profile must contain exactly one response type")
    value = profile[0]
    if not isinstance(value, tuple):
        raise RuntimeError("transverse response type must be represented by a tuple")
    return value


def cut_state_profile(
    world: SemanticQuotientWorld,
    retained_directions: Iterable[str],
    model: SemanticAccessModel,
) -> tuple[object, ...]:
    """Profile induced on the temporal cut by retained directional constraints."""

    return semantic_profile(world, retained_directions, model)


def induced_cut_state_classes(
    routes,
    candidates,
    model: SemanticAccessModel,
    bit_depth: int,
    retained_directions: Iterable[str],
):
    """Least cut-state quotient induced by the selected constraints.

    This is intentionally identical to the existing semantic trace quotient.
    The equality is regression-tested so the geometric reinterpretation cannot
    silently change the v0.7 theorem.
    """

    return semantic_induced_classes(
        routes,
        candidates,
        model,
        bit_depth,
        retained_directions,
    )


__all__ = [
    "CUT_DIRECTIONS",
    "PROSPECTIVE",
    "RETROSPECTIVE",
    "TRANSVERSE",
    "TemporalCutObservation",
    "cut_state_profile",
    "induced_cut_state_classes",
    "transverse_present_type",
]
