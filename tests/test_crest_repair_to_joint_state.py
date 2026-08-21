from __future__ import annotations

from crest.carrier import (
    ComponentCoverage,
    SynchronizedLiftProblem,
    maximal_common_lift,
)
from crest.carrier_repair import (
    CommonLiftRelaxationCosts,
    minimum_common_lift_relaxation,
)
from crest.joint_state import AuditRefinement, JointCRESTContract, solve_joint_crest_state


def _problem() -> SynchronizedLiftProblem:
    return SynchronizedLiftProblem(
        worlds=("needed", "bridge", "stable", "bad"),
        compatible=(True, True, True, False),
        actions=("step",),
        successors=((1,), (3,), (2,), (3,)),
        components=(
            ComponentCoverage(
                "future",
                ("needed", "bridge", "stable", "bad"),
                ("needed", "stable"),
            ),
        ),
    )


def _costs(problem: SynchronizedLiftProblem) -> CommonLiftRelaxationCosts:
    return CommonLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=(0, 0, 0, 5),
        disable_transition_costs=((10,), (1,), (10,), (10,)),
        drop_coverage_costs=((20, 20),),
    )


def _joint_contract(plan, *, coarse_evidence: bool) -> JointCRESTContract:
    kernel = plan.verified_kernel()
    ambient = kernel.viable_indices
    local = {ambient_index: position for position, ambient_index in enumerate(ambient)}
    repaired_problem = plan.repaired_problem()

    future_rows = []
    for ambient_index in ambient:
        row = []
        for successor in repaired_problem.successors[ambient_index]:
            row.append(None if successor is None else local[successor])
        future_rows.append(tuple(row))

    size = len(ambient)
    same = ("same",) * size
    empty_rows = tuple(() for _ in range(size))
    worlds = kernel.worlds
    evidence = ("one-record",) * size if coarse_evidence else worlds

    return JointCRESTContract(
        worlds=worlds,
        base_labels=("base",) * size,
        evidence_labels=evidence,
        target_labels=("survives",) * size,
        audits=(
            AuditRefinement(
                "future",
                same,
                repaired_problem.actions,
                tuple(future_rows),
            ),
            AuditRefinement("semantic", same, (), empty_rows),
            AuditRefinement("mechanism", same, (), empty_rows),
            AuditRefinement("target", same, (), empty_rows),
        ),
    )


def test_j4_repair_restores_gate_a_then_j1_constructs_a_joint_state() -> None:
    problem = _problem()
    original = maximal_common_lift(problem)

    # Before repair the maximal closed kernel survives only on ``stable`` and
    # therefore fails the declared coverage contract.
    assert original.worlds == ("stable",)
    assert original.exists
    assert not original.coverage_complete
    assert not original.admissible
    assert original.missing_coverage == (("future", ("needed",)),)

    repair = minimum_common_lift_relaxation(_costs(problem))
    assert repair.minimum_cost == 1
    assert repair.unique
    plan = repair.canonical_plan
    assert plan.disabled_transitions == ((1, 0),)
    assert plan.dropped_coverage == ()

    repaired = plan.verified_kernel()
    assert repaired.admissible
    assert repaired.worlds == ("needed", "bridge", "stable")

    state = solve_joint_crest_state(_joint_contract(plan, coarse_evidence=False))
    assert state.blocks == (("needed",), ("bridge",), ("stable",))
    assert state.full_state_licensed
    assert state.target_report_licensed


def test_j4_repair_restores_state_existence_but_does_not_by_itself_license_the_state() -> None:
    plan = minimum_common_lift_relaxation(_costs(_problem())).canonical_plan
    assert plan.verified_kernel().admissible

    state = solve_joint_crest_state(_joint_contract(plan, coarse_evidence=True))

    # Structural repair has made the full declared carrier admissible, so J1 can
    # define the required state.  Evidence remains a separate gate.
    assert state.blocks == (("needed",), ("bridge",), ("stable",))
    assert not state.full_state_licensed
    assert state.target_report_licensed
    assert state.sharp_state_report == ((0, 1, 2),)
    assert state.sharp_target_report == (("survives",),)
