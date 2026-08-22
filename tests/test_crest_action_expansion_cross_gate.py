from __future__ import annotations

from itertools import product

from crest.carrier import ComponentCoverage
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import AuditRefinement, evidence_licenses, partition_refines


def _partitions(size: int) -> tuple[tuple[int, ...], ...]:
    out: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...]) -> None:
        if len(prefix) == size:
            out.append(prefix)
            return
        maximum = max(prefix, default=-1)
        for label in range(maximum + 2):
            extend(prefix + (label,))

    extend((0,))
    return tuple(out)


def _problem(
    old_successors: tuple[int, int, int],
    rescue_successors: tuple[int, int, int] | None,
) -> ControlledSynchronizedLiftProblem:
    worlds = ("a", "b", "bad")
    components = (
        ComponentCoverage(
            "role",
            ("live", "live", "bad"),
            ("live",),
        ),
    )
    if rescue_successors is None:
        actions = ("hold",)
        controllable = tuple((old_successors[i],) for i in range(3))
    else:
        actions = ("hold", "rescue")
        controllable = tuple(
            (old_successors[i], rescue_successors[i]) for i in range(3)
        )
    return ControlledSynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, False),
        uncontrollable_actions=(),
        controllable_actions=actions,
        uncontrollable_successors=((), (), ()),
        controllable_successors=controllable,
        components=components,
    )


def test_control_action_expansion_cannot_shrink_the_j6_carrier() -> None:
    """Exhaust every deterministic 3-world old/new controllable successor table."""

    successors = tuple(product(range(3), repeat=3))
    for old_successors in successors:
        old = maximal_controlled_common_lift(_problem(old_successors, None))
        for rescue_successors in successors:
            new = maximal_controlled_common_lift(
                _problem(old_successors, rescue_successors)
            )
            assert set(old.worlds).issubset(new.worlds)


def test_future_action_expansion_can_only_refine_exact_state_closure() -> None:
    """Exhaust the 3-world partition lattice and deterministic action tables."""

    partitions = _partitions(3)
    successors = tuple(product(range(3), repeat=3))
    static = ("same", "same", "same")

    for old_successors in successors:
        old_audit = AuditRefinement(
            "future-old",
            static,
            ("hold",),
            tuple((old_successors[i],) for i in range(3)),
        )
        for rescue_successors in successors:
            new_audit = AuditRefinement(
                "future-new",
                static,
                ("hold", "rescue"),
                tuple(
                    (old_successors[i], rescue_successors[i])
                    for i in range(3)
                ),
            )
            for baseline in partitions:
                old_state = old_audit.close(baseline)
                new_state = new_audit.close(baseline)
                assert partition_refines(new_state, old_state)


def test_fixed_evidence_identifiability_is_antitone_under_state_refinement() -> None:
    """Exhaust every 4-world evidence/coarse/fine partition triple."""

    partitions = _partitions(4)
    for evidence, coarse, fine in product(partitions, repeat=3):
        if not partition_refines(fine, coarse):
            continue
        if evidence_licenses(fine, evidence):
            assert evidence_licenses(coarse, evidence)
        if not evidence_licenses(coarse, evidence):
            assert not evidence_licenses(fine, evidence)
