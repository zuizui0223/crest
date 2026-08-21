from __future__ import annotations

from crest.carrier import ComponentCoverage
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import (
    AuditRefinement,
    JointCRESTContract,
    evidence_licenses,
    partition_refines,
    solve_joint_crest_state,
)


def _empty_rows(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(() for _ in range(size))


def _controlled_problem(*, enriched: bool) -> ControlledSynchronizedLiftProblem:
    worlds = ("a", "b", "c", "bad")
    components = (
        ComponentCoverage(
            "role",
            ("candidate", "candidate", "anchor", "bad"),
            ("candidate", "anchor"),
        ),
    )
    if enriched:
        actions = ("hold", "rescue")
        successors = (
            (0, 2),  # a: rescue is viable but exposes a different future
            (3, 1),  # b: only rescue keeps b inside the viable carrier
            (2, 2),
            (3, 3),
        )
    else:
        actions = ("hold",)
        successors = (
            (0,),
            (3,),
            (2,),
            (3,),
        )
    return ControlledSynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, True, False),
        uncontrollable_actions=(),
        controllable_actions=actions,
        uncontrollable_successors=((), (), (), ()),
        controllable_successors=successors,
        components=components,
    )


def _joint_contract(worlds: tuple[str, ...], *, enriched: bool) -> JointCRESTContract:
    if worlds == ("a", "c"):
        base = ("candidate", "anchor")
        evidence = ("live", "anchor")
        targets = ("survives", "anchor")
        future = AuditRefinement(
            "future",
            ("same", "same"),
            (),
            ((), ()),
        )
    elif worlds == ("a", "b", "c") and enriched:
        base = ("candidate", "candidate", "anchor")
        evidence = ("live", "live", "anchor")
        targets = ("survives", "survives", "anchor")
        future = AuditRefinement(
            "future",
            ("same", "same", "same"),
            ("rescue",),
            (
                (2,),  # a -> anchor block
                (1,),  # b -> candidate block
                (2,),
            ),
        )
    else:
        raise ValueError("unexpected carrier")

    size = len(worlds)
    empty = _empty_rows(size)
    same = ("same",) * size
    return JointCRESTContract(
        worlds=worlds,
        base_labels=base,
        evidence_labels=evidence,
        target_labels=targets,
        audits=(
            future,
            AuditRefinement("semantic", same, (), empty),
            AuditRefinement("mechanism", same, (), empty),
            AuditRefinement("target", same, (), empty),
        ),
    )


def test_one_new_management_action_can_expand_viability_and_create_information_debt() -> None:
    """A finite cross-gate witness for the CREST adequacy frontier.

    Adding one controllable action makes an additional ecological world viable, but
    that same action makes two previously observationally merged candidate worlds
    future-distinct.  The least-information state therefore becomes finer than the
    fixed monitoring system can identify, even though the requested target remains
    reportable.
    """

    before = maximal_controlled_common_lift(_controlled_problem(enriched=False))
    after = maximal_controlled_common_lift(_controlled_problem(enriched=True))

    assert before.admissible
    assert after.admissible
    assert before.worlds == ("a", "c")
    assert after.worlds == ("a", "b", "c")
    assert len(after.worlds) > len(before.worlds)

    before_state = solve_joint_crest_state(
        _joint_contract(before.worlds, enriched=False)
    )
    after_state = solve_joint_crest_state(
        _joint_contract(after.worlds, enriched=True)
    )

    assert before_state.blocks == (("a",), ("c",))
    assert before_state.full_state_licensed
    assert before_state.target_report_licensed

    assert after_state.blocks == (("a",), ("b",), ("c",))
    assert after_state.state_count > before_state.state_count
    assert not after_state.full_state_licensed
    assert after_state.target_report_licensed
    assert after_state.sharp_state_report == ((0, 1), (2,))
    assert after_state.sharp_target_report == (("survives",), ("anchor",))


def test_fixed_evidence_cannot_regain_full_state_identification_after_refinement() -> None:
    """Exhaust the small partition lattice to check the epistemic frontier order."""

    evidence = ("x", "x", "y", "y")
    partitions = (
        (0, 0, 0, 0),
        (0, 0, 1, 1),
        (0, 1, 2, 2),
        (0, 1, 2, 3),
        (0, 0, 1, 2),
    )
    for coarse in partitions:
        for fine in partitions:
            if not partition_refines(fine, coarse):
                continue
            if not evidence_licenses(coarse, evidence):
                assert not evidence_licenses(fine, evidence)
