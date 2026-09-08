"""Executable finite prerequisite audit for the shallow-lake CREST worked case.

This is a literature-grounded *decision model*, not an empirical fit.  The code
formalizes the manuscript's target-relative claim: the same coarse present lake
status can require no retained interface, history only, latent response only, or
both interfaces depending on the declared restoration target.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations
from typing import Callable, Hashable, Iterable

HISTORY = "H"
MECHANISM = "THETA"
INTERFACES = (HISTORY, MECHANISM)


@dataclass(frozen=True)
class LakeWorld:
    """One finite shallow-lake world behind the same coarse visible cut."""

    history_mode: str
    response_type: str
    visible_status: str = "turbid_eutrophic"


LAKE_WORLDS = tuple(
    LakeWorld(history_mode, response_type)
    for history_mode in ("no_retained_legacy", "retained_nutrient_legacy")
    for response_type in ("sediment_internal_p", "biological_feedback")
)


def current_status_target(world: LakeWorld) -> str:
    return world.visible_status


def legacy_sensitive_recovery_target(world: LakeWorld) -> str:
    return (
        "legacy_constraint_present"
        if world.history_mode == "retained_nutrient_legacy"
        else "no_retained_legacy_constraint"
    )


def mechanism_specific_intervention_target(world: LakeWorld) -> str:
    return (
        "sediment_focused_channel"
        if world.response_type == "sediment_internal_p"
        else "foodweb_macrophyte_channel"
    )


def composed_restoration_policy_target(world: LakeWorld) -> str:
    """Finite policy whose output genuinely depends on both semantic interfaces."""

    table = {
        ("no_retained_legacy", "sediment_internal_p"): "sediment_channel",
        ("no_retained_legacy", "biological_feedback"): "biological_channel",
        ("retained_nutrient_legacy", "sediment_internal_p"): "legacy_plus_sediment",
        ("retained_nutrient_legacy", "biological_feedback"): "legacy_plus_biological",
    }
    return table[(world.history_mode, world.response_type)]


def interface_signature(world: LakeWorld, retained: Iterable[str]) -> tuple[str, ...]:
    kept = frozenset(retained)
    if not kept.issubset(INTERFACES):
        raise ValueError("unknown retained interface")
    signature: list[str] = []
    if HISTORY in kept:
        signature.append(world.history_mode)
    if MECHANISM in kept:
        signature.append(world.response_type)
    return tuple(signature)


def interfaces_sufficient_for_target(
    target: Callable[[LakeWorld], Hashable], retained: Iterable[str]
) -> bool:
    """Whether target output factors through the retained interface signature."""

    outputs: dict[tuple[str, ...], Hashable] = {}
    for world in LAKE_WORLDS:
        key = interface_signature(world, retained)
        value = target(world)
        if key in outputs and outputs[key] != value:
            return False
        outputs[key] = value
    return True


def minimal_prerequisite_sets(
    target: Callable[[LakeWorld], Hashable],
) -> tuple[frozenset[str], ...]:
    """Return all inclusion-minimal interface sets sufficient for the target."""

    sufficient: list[frozenset[str]] = []
    for size in range(len(INTERFACES) + 1):
        for combo in combinations(INTERFACES, size):
            candidate = frozenset(combo)
            if interfaces_sufficient_for_target(target, candidate):
                if not any(previous < candidate for previous in sufficient):
                    sufficient.append(candidate)
    return tuple(sufficient)


def counterfactual_substitution_changes_target(
    target: Callable[[LakeWorld], Hashable],
    world: LakeWorld,
    interface: str,
) -> bool:
    """Test whether replacing one semantic interface can change target output.

    The other semantic interface and the visible cut are held fixed.
    """

    if interface == HISTORY:
        alternatives = {
            candidate.history_mode for candidate in LAKE_WORLDS
            if candidate.history_mode != world.history_mode
        }
        return any(target(replace(world, history_mode=value)) != target(world) for value in alternatives)
    if interface == MECHANISM:
        alternatives = {
            candidate.response_type for candidate in LAKE_WORLDS
            if candidate.response_type != world.response_type
        }
        return any(target(replace(world, response_type=value)) != target(world) for value in alternatives)
    raise ValueError("unknown interface")


def canonical_target_prerequisites() -> dict[str, tuple[frozenset[str], ...]]:
    return {
        "current_status": minimal_prerequisite_sets(current_status_target),
        "legacy_sensitive_recovery": minimal_prerequisite_sets(legacy_sensitive_recovery_target),
        "mechanism_specific_intervention": minimal_prerequisite_sets(mechanism_specific_intervention_target),
        "composed_restoration_policy": minimal_prerequisite_sets(composed_restoration_policy_target),
    }


__all__ = [
    "HISTORY",
    "INTERFACES",
    "LAKE_WORLDS",
    "LakeWorld",
    "MECHANISM",
    "canonical_target_prerequisites",
    "composed_restoration_policy_target",
    "counterfactual_substitution_changes_target",
    "current_status_target",
    "interface_signature",
    "interfaces_sufficient_for_target",
    "legacy_sensitive_recovery_target",
    "mechanism_specific_intervention_target",
    "minimal_prerequisite_sets",
]
