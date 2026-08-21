from __future__ import annotations

from crest.carrier import (
    ComponentCoverage,
    SynchronizedLiftProblem,
    maximal_common_lift,
)
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import AuditRefinement, JointCRESTContract, solve_joint_crest_state


def _carrier_problem(*, empty: bool = False, require_lost: bool = False) -> SynchronizedLiftProblem:
    worlds = ("stable", "lost", "bad")
    stable_successor = 2 if empty else 0
    components = (
        ComponentCoverage(
            "future",
            ("stable", "lost", "bad"),
            ("stable", "lost") if require_lost else ("stable",),
        ),
    )
    return SynchronizedLiftProblem(
        worlds=worlds,
        compatible=(True, True, False),
        actions=("step",),
        successors=((stable_successor,), (2,), (2,)),
        components=components,
    )


def _joint_contract(*, coarse_evidence: bool) -> JointCRESTContract:
    worlds = ("left", "right")
    future = AuditRefinement(
        "future",
        ("same", "same"),
        ("probe",),
        ((0,), (1,)),
    )
    semantic = AuditRefinement(
        "semantic",
        ("left", "right"),
        (),
        ((), ()),
    )
    evidence = ("same", "same") if coarse_evidence else ("left", "right")
    target = ("survives", "survives")
    return JointCRESTContract(
        worlds=worlds,
        base_labels=("candidate", "candidate"),
        evidence_labels=evidence,
        target_labels=target,
        audits=(future, semantic),
    )


def test_empty_maximal_carrier_is_contract_relative_state_no_go() -> None:
    result = maximal_common_lift(_carrier_problem(empty=True))

    assert not result.exists
    assert not result.admissible
    assert result.worlds == ()
    assert result.elimination_chain("stable") == ("stable", "bad")


def test_nonempty_but_coverage_incomplete_kernel_is_also_full_contract_no_go() -> None:
    problem = _carrier_problem(require_lost=True)
    result = maximal_common_lift(problem)

    assert result.worlds == ("stable",)
    assert result.exists
    assert not result.coverage_complete
    assert not result.admissible
    assert result.missing_coverage == (("future", ("lost",)),)

    # J3 returns the greatest closed subset. Since even the greatest one lacks
    # ``lost``, no smaller closed subset can restore the missing coverage contract.
    for mask in range(1 << len(problem.worlds)):
        subset = tuple(i for i in range(len(problem.worlds)) if mask & (1 << i))
        if problem.is_closed_subset(subset):
            assert set(subset).issubset(result.viable_indices)
            represented = {problem.components[0].labels[i] for i in subset}
            assert "lost" not in represented


def test_controlled_gate_can_prove_no_state_when_every_control_is_unsafe() -> None:
    problem = ControlledSynchronizedLiftProblem(
        worlds=("idleless",),
        compatible=(True,),
        uncontrollable_actions=(),
        controllable_actions=("act",),
        uncontrollable_successors=((),),
        controllable_successors=((None,),),
        components=(ComponentCoverage("role", ("idleless",), ("idleless",)),),
    )
    result = maximal_controlled_common_lift(problem)

    assert not result.exists
    assert not result.admissible
    certificate = result.elimination_certificate("idleless")
    assert certificate.kind == "no_safe_control"
    assert certificate.children == ()


def test_admissible_carrier_then_j1_yields_an_identified_joint_state() -> None:
    carrier = maximal_common_lift(_carrier_problem())
    assert carrier.admissible

    state = solve_joint_crest_state(_joint_contract(coarse_evidence=False))
    assert state.blocks == (("left",), ("right",))
    assert state.full_state_licensed
    assert state.target_report_licensed
    assert state.class_of("left") != state.class_of("right")


def test_admissible_carrier_can_yield_state_that_exists_but_is_unresolved() -> None:
    carrier = maximal_common_lift(_carrier_problem())
    assert carrier.admissible

    state = solve_joint_crest_state(_joint_contract(coarse_evidence=True))
    assert state.blocks == (("left",), ("right",))
    assert not state.full_state_licensed
    assert state.target_report_licensed
    assert state.sharp_state_report == ((0, 1),)
    assert state.sharp_target_report == (("survives",),)
