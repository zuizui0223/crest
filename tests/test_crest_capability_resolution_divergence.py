from __future__ import annotations

from itertools import product
from math import log2

from crest.carrier import ComponentCoverage
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import AuditRefinement, evidence_licenses

World = tuple[str, tuple[int, ...], int]


def _ambient_problem(
    m: int, include_probe: bool
) -> tuple[ControlledSynchronizedLiftProblem, tuple[tuple[int, ...], ...], dict[World, int]]:
    assert m >= 1
    addresses = tuple(product((0, 1), repeat=m))
    worlds: list[World] = []
    index: dict[World, int] = {}

    for address in addresses:
        for j in range(m + 1):
            world = ("p", address, j)
            index[world] = len(worlds)
            worlds.append(world)
        for j in range(m):
            world = ("q", address, j)
            index[world] = len(worlds)
            worlds.append(world)

    safe: World = ("safe", (), 0)
    fragile: World = ("fragile", (), 0)
    index[safe] = len(worlds)
    worlds.append(safe)
    index[fragile] = len(worlds)
    worlds.append(fragile)

    actions = ("hold", "probe") if include_probe else ("hold",)
    rows: list[tuple[int | None, ...]] = []

    for world in worlds:
        kind, address, j = world
        if kind == "p":
            hold = index[world]
            if include_probe:
                probe = (
                    index[("q", address, j)]
                    if j < m
                    else index[fragile]
                )
                rows.append((hold, probe))
            else:
                rows.append((hold,))
        elif kind == "q":
            hold = index[world]
            if include_probe:
                rows.append((hold, index[("p", address, j + 1)]))
            else:
                rows.append((hold,))
        elif kind == "safe":
            rows.append((index[safe], index[safe]) if include_probe else (index[safe],))
        else:
            # `fragile` is compatible but has no safe old control. The newly
            # admitted probe both rescues it and is the same action that reads
            # the latent address family.
            rows.append((None, index[safe]) if include_probe else (None,))

    problem = ControlledSynchronizedLiftProblem(
        worlds=tuple(worlds),
        compatible=(True,) * len(worlds),
        uncontrollable_actions=(),
        controllable_actions=actions,
        uncontrollable_successors=tuple(() for _ in worlds),
        controllable_successors=tuple(rows),
        components=(
            ComponentCoverage(
                "compatibility-role",
                ("live",) * len(worlds),
                ("live",),
            ),
        ),
    )
    return problem, addresses, index


def _static_label(world: World, m: int) -> str:
    kind, address, j = world
    if kind == "p":
        return "done" if j == m else "neutral"
    if kind == "q":
        return f"bit{address[j]}"
    return "done"


def _state_on_controlled_kernel(
    m: int, include_probe: bool
) -> tuple[
    ControlledSynchronizedLiftProblem,
    tuple[World, ...],
    tuple[int, ...],
]:
    problem, addresses, index = _ambient_problem(m, include_probe)
    kernel = maximal_controlled_common_lift(problem)
    viable_ambient = kernel.viable_indices
    local_index = {
        ambient_index: local
        for local, ambient_index in enumerate(viable_ambient)
    }

    static = tuple(
        _static_label(problem.worlds[ambient_index], m)
        for ambient_index in viable_ambient
    )
    successors: list[tuple[int | None, ...]] = []
    for ambient_index in viable_ambient:
        row: list[int | None] = []
        for successor in problem.controllable_successors[ambient_index]:
            row.append(
                None
                if successor is None or successor not in local_index
                else local_index[successor]
            )
        successors.append(tuple(row))

    audit = AuditRefinement(
        "future",
        static,
        problem.controllable_actions,
        tuple(successors),
    )
    state = audit.close((0,) * len(viable_ambient))
    present_labels = tuple(
        state[local_index[index[("p", address, 0)]]]
        for address in addresses
    )
    return problem, kernel.worlds, present_labels


def test_connected_probe_action_creates_arbitrary_present_state_bits() -> None:
    for m in range(1, 7):
        old_problem, old_worlds, old_present = _state_on_controlled_kernel(m, False)
        new_problem, new_worlds, new_present = _state_on_controlled_kernel(m, True)

        assert len(set(old_present)) == 1
        assert len(set(new_present)) == 2**m
        assert log2(len(set(new_present))) - log2(len(set(old_present))) == m

        assert set(_static_label(world, m) for world in new_problem.worlds) <= {
            "neutral",
            "bit0",
            "bit1",
            "done",
        }
        assert old_problem.controllable_actions == ("hold",)
        assert new_problem.controllable_actions == ("hold", "probe")
        assert len(new_worlds) == len(old_worlds) + 1


def test_same_connected_probe_action_rescues_exactly_fragile_world() -> None:
    for m in range(1, 6):
        old_problem, addresses, old_index = _ambient_problem(m, False)
        new_problem, _, new_index = _ambient_problem(m, True)
        old = maximal_controlled_common_lift(old_problem)
        new = maximal_controlled_common_lift(new_problem)

        fragile: World = ("fragile", (), 0)
        safe: World = ("safe", (), 0)
        assert set(old.worlds).issubset(new.worlds)
        assert set(new.worlds) - set(old.worlds) == {fragile}
        assert len(new.worlds) - len(old.worlds) == 1

        # The readout chains terminate in the rescued world, so carrier gain and
        # state refinement are not disjoint-union gadgets.
        probe_column = new_problem.controllable_actions.index("probe")
        for address in addresses:
            terminal = new_index[("p", address, m)]
            assert new_problem.controllable_successors[terminal][probe_column] == new_index[fragile]
        assert new_problem.controllable_successors[new_index[fragile]][probe_column] == new_index[safe]
        assert old_problem.controllable_successors[old_index[fragile]][0] is None


def test_fixed_present_evidence_loses_full_state_but_keeps_constant_target() -> None:
    for m in range(1, 7):
        _, _, old_present = _state_on_controlled_kernel(m, False)
        _, _, new_present = _state_on_controlled_kernel(m, True)
        evidence = ("same-record",) * (2**m)
        target = ("same-target",) * (2**m)

        assert evidence_licenses(old_present, evidence)
        assert not evidence_licenses(new_present, evidence)
        assert evidence_licenses(target, evidence)

        monitoring_debt_bits = log2(len(set(new_present))) - log2(len(set(evidence)))
        assert monitoring_debt_bits == m
