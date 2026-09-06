from __future__ import annotations

from itertools import product
from math import ceil, log2
from random import Random

from crest.joint_state import AuditRefinement
from crest.response_capacity import (
    action_expansion_split_factor_bound,
    horizon_state_class_bound,
    horizon_word_count,
    newly_admitted_word_count,
    response_basis_bit_bound,
    response_basis_split_bound,
    response_signature,
    signature_class_count,
    terminal_response,
    words_through_horizon,
)


def _random_audit(rng: Random, world_count: int, action_count: int) -> AuditRefinement:
    actions = tuple(f"a{index}" for index in range(action_count))
    static = tuple(rng.randrange(2) for _ in range(world_count))
    rows = []
    for _ in range(world_count):
        row = []
        for _action in actions:
            draw = rng.randrange(world_count + 1)
            row.append(None if draw == world_count else draw)
        rows.append(tuple(row))
    return AuditRefinement("random", static, actions, tuple(rows))


def test_raw_horizon_response_volume_bounds_random_partial_systems() -> None:
    rng = Random(2026090601)
    for action_count in range(3):
        for world_count in range(1, 7):
            for _case in range(12):
                audit = _random_audit(rng, world_count, action_count)
                observation_count = len(set(audit.static_labels))
                for horizon in range(4):
                    words = words_through_horizon(audit.actions, horizon)
                    actual = signature_class_count(
                        audit, range(world_count), words
                    )
                    assert len(words) == horizon_word_count(action_count, horizon)
                    assert actual <= horizon_state_class_bound(
                        observation_count, action_count, horizon
                    )


def test_new_word_volume_bounds_relative_action_expansion() -> None:
    rng = Random(2026090602)
    for world_count in range(2, 7):
        static = tuple(rng.randrange(2) for _ in range(world_count))
        old_rows = []
        new_rows = []
        for _ in range(world_count):
            old_successor = rng.randrange(world_count + 1)
            old_successor = None if old_successor == world_count else old_successor
            probe_successor = rng.randrange(world_count + 1)
            probe_successor = (
                None if probe_successor == world_count else probe_successor
            )
            old_rows.append((old_successor,))
            new_rows.append((old_successor, probe_successor))

        old = AuditRefinement("old", static, ("hold",), tuple(old_rows))
        new = AuditRefinement(
            "new", static, ("hold", "probe"), tuple(new_rows)
        )
        observation_count = len(set(static))

        for horizon in range(4):
            old_classes = signature_class_count(
                old,
                range(world_count),
                words_through_horizon(old.actions, horizon),
            )
            new_classes = signature_class_count(
                new,
                range(world_count),
                words_through_horizon(new.actions, horizon),
            )
            split_factor = action_expansion_split_factor_bound(
                observation_count,
                len(old.actions),
                len(new.actions),
                horizon,
            )
            assert new_classes <= old_classes * split_factor
            assert newly_admitted_word_count(1, 2, horizon) == sum(
                2**depth - 1 for depth in range(1, horizon + 1)
            )


def _connected_probe_audit(
    m: int,
) -> tuple[AuditRefinement, tuple[int, ...], tuple[tuple[int, ...], ...]]:
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

    safe = ("safe", (), 0)
    fragile = ("fragile", (), 0)
    index[safe] = len(worlds)
    worlds.append(safe)
    index[fragile] = len(worlds)
    worlds.append(fragile)

    static = []
    rows = []
    for kind, address, j in worlds:
        if kind == "p":
            static.append("done" if j == m else "neutral")
            probe = index[("q", address, j)] if j < m else index[fragile]
            rows.append((index[(kind, address, j)], probe))
        elif kind == "q":
            static.append(f"bit{address[j]}")
            rows.append((index[(kind, address, j)], index[("p", address, j + 1)]))
        elif kind == "safe":
            static.append("done")
            rows.append((index[safe], index[safe]))
        else:
            static.append("done")
            rows.append((None, index[safe]))

    starts = tuple(index[("p", address, 0)] for address in addresses)
    return (
        AuditRefinement(
            "future", tuple(static), ("hold", "probe"), tuple(rows)
        ),
        starts,
        addresses,
    )


def test_current_connected_family_saturates_binary_response_basis_capacity() -> None:
    for m in range(1, 7):
        audit, starts, addresses = _connected_probe_audit(m)
        basis = tuple(("probe",) * (2 * j + 1) for j in range(m))

        basis_classes = signature_class_count(audit, starts, basis)
        outcome_cardinalities = tuple(
            len({terminal_response(audit, start, word) for start in starts})
            for word in basis
        )

        assert basis_classes == 2**m
        assert outcome_cardinalities == (2,) * m
        assert response_basis_split_bound(outcome_cardinalities) == 2**m
        assert response_basis_bit_bound(outcome_cardinalities) == m

        signatures = {
            address: response_signature(audit, start, basis)
            for address, start in zip(addresses, starts)
        }
        assert len(set(signatures.values())) == len(addresses)

        exact = audit.close((0,) * audit.world_count)
        assert len({exact[start] for start in starts}) == basis_classes


def test_connected_family_accumulates_one_bit_every_two_probe_steps() -> None:
    for m in range(1, 7):
        audit, starts, _ = _connected_probe_audit(m)
        for horizon in range(0, 2 * m + 1):
            # `hold` is an inert self-loop on the retained present/readout chain,
            # so pure-probe prefixes already form a complete separating family
            # for this slice through the declared horizon.
            probe_prefixes = tuple(("probe",) * depth for depth in range(horizon + 1))
            classes = signature_class_count(audit, starts, probe_prefixes)
            expected_bits = min(m, ceil(horizon / 2))
            assert classes == 2**expected_bits
            assert log2(classes) == expected_bits
