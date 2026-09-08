from __future__ import annotations

from math import log2

import pytest

from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import AuditRefinement, evidence_licenses
from crest.response_capacity import response_signature
from crest.sequential_debt import (
    heterogeneous_sequential_bit_bound,
    heterogeneous_sequential_class_bound,
    minimum_sequential_horizon_for_bits,
    minimum_sequential_horizon_for_classes,
    sequential_split_bit_bound,
    sequential_split_class_bound,
)
from crest.sequential_witnesses import World, sharp_sequential_problem


def _label(world: World) -> str:
    kind, address, depth = world
    if kind == "path":
        if depth == 0:
            return "neutral"
        return f"response-{address[depth - 1]}"
    return "done"


def _audit_on_kernel(
    response_cardinality: int,
    horizon: int,
    include_probe: bool,
) -> tuple[
    ControlledSynchronizedLiftProblem,
    tuple[World, ...],
    tuple[tuple[int, ...], ...],
    tuple[int, ...],
    AuditRefinement,
    tuple[int, ...],
]:
    problem, addresses, index = sharp_sequential_problem(
        response_cardinality, horizon, include_probe
    )
    kernel = maximal_controlled_common_lift(problem)
    viable = kernel.viable_indices
    local = {ambient: position for position, ambient in enumerate(viable)}
    static = tuple(_label(problem.worlds[ambient]) for ambient in viable)

    rows: list[tuple[int | None, ...]] = []
    for ambient in viable:
        rows.append(
            tuple(
                None
                if successor is None or successor not in local
                else local[successor]
                for successor in problem.controllable_successors[ambient]
            )
        )

    audit = AuditRefinement(
        "future",
        static,
        problem.controllable_actions,
        tuple(rows),
    )
    state = audit.close((0,) * len(viable))
    starts = tuple(
        local[index[("path", address, 0)]] for address in addresses
    )
    labels = tuple(state[start] for start in starts)
    return problem, kernel.worlds, addresses, starts, audit, labels


def test_sequential_capacity_formula_and_inverse() -> None:
    assert sequential_split_class_bound(2, 10) == 1024
    assert sequential_split_bit_bound(2, 10) == 10
    assert sequential_split_class_bound(4, 3) == 64
    assert sequential_split_bit_bound(4, 3) == 6
    assert heterogeneous_sequential_class_bound((2, 3, 4)) == 24
    assert heterogeneous_sequential_bit_bound((2, 4)) == 3
    assert minimum_sequential_horizon_for_classes(33, 2) == 6
    assert minimum_sequential_horizon_for_bits(10, 2) == 10
    assert minimum_sequential_horizon_for_bits(6, 4) == 3

    with pytest.raises(ValueError):
        minimum_sequential_horizon_for_classes(2, 1)


def test_sharp_connected_family_attains_r_to_h_classes() -> None:
    for r, horizon in ((2, 1), (2, 4), (3, 3)):
        old_problem, old_worlds, addresses, old_starts, old_audit, old_labels = (
            _audit_on_kernel(r, horizon, False)
        )
        new_problem, new_worlds, new_addresses, starts, audit, new_labels = (
            _audit_on_kernel(r, horizon, True)
        )

        assert addresses == new_addresses
        assert len(set(old_labels)) == 1
        assert len(set(new_labels)) == r**horizon
        assert log2(len(set(new_labels))) == horizon * log2(r)
        assert len(new_worlds) == len(old_worlds) + 1
        assert old_problem.controllable_actions == ("hold",)
        assert new_problem.controllable_actions == ("hold", "probe")

        probe_words = tuple(("probe",) * depth for depth in range(1, horizon + 1))
        signatures = {
            response_signature(audit, start, probe_words) for start in starts
        }
        assert len(signatures) == r**horizon

        # Each additional response depth multiplies distinguishable present
        # states by exactly r until the declared horizon is exhausted.
        for depth in range(horizon + 1):
            words = tuple(("probe",) * step for step in range(1, depth + 1))
            depth_signatures = {
                response_signature(audit, start, words) for start in starts
            }
            assert len(depth_signatures) == r**depth


def test_same_probe_rescues_exactly_one_world_after_readout() -> None:
    r, horizon = 3, 4
    old_problem, addresses, old_index = sharp_sequential_problem(r, horizon, False)
    new_problem, _, new_index = sharp_sequential_problem(r, horizon, True)
    old = maximal_controlled_common_lift(old_problem)
    new = maximal_controlled_common_lift(new_problem)

    fragile: World = ("fragile", (), 0)
    safe: World = ("safe", (), 0)
    assert set(new.worlds) - set(old.worlds) == {fragile}

    probe_column = new_problem.controllable_actions.index("probe")
    for address in addresses:
        terminal = new_index[("path", address, horizon)]
        assert (
            new_problem.controllable_successors[terminal][probe_column]
            == new_index[fragile]
        )
    assert (
        new_problem.controllable_successors[new_index[fragile]][probe_column]
        == new_index[safe]
    )
    assert old_problem.controllable_successors[old_index[fragile]][0] is None


def test_sharp_family_creates_exact_monitoring_debt_but_keeps_target() -> None:
    for r, horizon in ((2, 5), (4, 2)):
        _, _, _, _, _, old_labels = _audit_on_kernel(r, horizon, False)
        _, _, _, _, _, new_labels = _audit_on_kernel(r, horizon, True)
        evidence = ("same-record",) * (r**horizon)
        target = ("same-target",) * (r**horizon)

        assert evidence_licenses(old_labels, evidence)
        assert not evidence_licenses(new_labels, evidence)
        assert evidence_licenses(target, evidence)
        assert (
            log2(len(set(new_labels))) - log2(len(set(evidence)))
            == horizon * log2(r)
        )
