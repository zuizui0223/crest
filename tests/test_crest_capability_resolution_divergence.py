from __future__ import annotations

from itertools import product
from math import log2

from crest.carrier import ComponentCoverage
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)
from crest.joint_state import AuditRefinement, evidence_licenses


def _probe_family(m: int, include_probe: bool):
    assert m >= 1
    addresses = tuple(product((0, 1), repeat=m))
    worlds: list[tuple[str, tuple[int, ...], int]] = []
    index: dict[tuple[str, tuple[int, ...], int], int] = {}

    for address in addresses:
        for j in range(m + 1):
            world = ("p", address, j)
            index[world] = len(worlds)
            worlds.append(world)
        for j in range(m):
            world = ("q", address, j)
            index[world] = len(worlds)
            worlds.append(world)

    static: list[str] = []
    successors: list[tuple[int, ...]] = []
    actions = ("hold", "probe") if include_probe else ("hold",)

    for world in worlds:
        kind, address, j = world
        if kind == "p":
            static.append("done" if j == m else "neutral")
        else:
            static.append(f"bit{address[j]}")

        row = [index[world]]  # hold
        if include_probe:
            if kind == "p":
                row.append(index[("q", address, j)] if j < m else index[world])
            else:
                row.append(index[("p", address, j + 1)])
        successors.append(tuple(row))

    audit = AuditRefinement(
        "future",
        tuple(static),
        actions,
        tuple(successors),
    )
    state = audit.close((0,) * len(worlds))
    present_indices = tuple(index[("p", address, 0)] for address in addresses)
    present_labels = tuple(state[i] for i in present_indices)
    return worlds, index, state, present_indices, present_labels


def _combined_carrier_problem(m: int, include_probe: bool) -> ControlledSynchronizedLiftProblem:
    chain_worlds, chain_index, _, _, _ = _probe_family(m, include_probe=True)
    world_names = tuple(str(world) for world in chain_worlds) + ("safe", "fragile", "bad")
    safe = len(chain_worlds)
    fragile = safe + 1
    bad = safe + 2

    compatible = tuple(True for _ in chain_worlds) + (True, True, False)
    components = (
        ComponentCoverage(
            "compatibility-role",
            tuple("live" if flag else "bad" for flag in compatible),
            ("live",),
        ),
    )

    old_rows: list[tuple[int, ...]] = []
    new_rows: list[tuple[int, ...]] = []

    for i, world in enumerate(chain_worlds):
        kind, address, j = world
        hold = i
        if kind == "p":
            probe = chain_index[("q", address, j)] if j < m else i
        else:
            probe = chain_index[("p", address, j + 1)]
        old_rows.append((hold,))
        new_rows.append((hold, probe))

    old_rows.extend(((safe,), (bad,), (bad,)))
    new_rows.extend(((safe, safe), (bad, safe), (bad, bad)))

    actions = ("hold", "probe") if include_probe else ("hold",)
    rows = tuple(new_rows if include_probe else old_rows)

    return ControlledSynchronizedLiftProblem(
        worlds=world_names,
        compatible=compatible,
        uncontrollable_actions=(),
        controllable_actions=actions,
        uncontrollable_successors=tuple(() for _ in world_names),
        controllable_successors=rows,
        components=components,
    )


def test_one_added_probe_action_creates_arbitrary_present_state_bits() -> None:
    for m in range(1, 7):
        _, _, _, old_indices, old_present = _probe_family(m, include_probe=False)
        _, _, _, new_indices, new_present = _probe_family(m, include_probe=True)
        assert len(old_indices) == len(new_indices) == 2**m
        assert len(set(old_present)) == 1
        assert len(set(new_present)) == 2**m
        assert log2(len(set(new_present))) - log2(len(set(old_present))) == m


def test_same_probe_action_enlarges_controlled_carrier_by_exactly_one_world() -> None:
    for m in range(1, 6):
        old = maximal_controlled_common_lift(_combined_carrier_problem(m, False))
        new = maximal_controlled_common_lift(_combined_carrier_problem(m, True))
        assert set(old.worlds).issubset(new.worlds)
        assert set(new.worlds) - set(old.worlds) == {"fragile"}
        assert len(new.worlds) - len(old.worlds) == 1


def test_fixed_present_evidence_loses_full_state_but_keeps_constant_target() -> None:
    for m in range(1, 7):
        _, _, _, _, old_present = _probe_family(m, include_probe=False)
        _, _, _, _, new_present = _probe_family(m, include_probe=True)
        evidence = ("same-record",) * (2**m)
        target = ("same-target",) * (2**m)

        assert evidence_licenses(old_present, evidence)
        assert not evidence_licenses(new_present, evidence)
        assert evidence_licenses(target, evidence)

        monitoring_debt_bits = log2(len(set(new_present))) - log2(len(set(evidence)))
        assert monitoring_debt_bits == m
