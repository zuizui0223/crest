from __future__ import annotations

from itertools import product
from math import log2
from random import Random

import pytest

from crest.joint_debt import (
    debt_report,
    joint_partition,
    marked_cycle_audits,
    marked_cycle_report,
    zero_individual_debt_implies_zero_joint,
)
from crest.joint_state import AuditRefinement, partition_refines


def _canonical(values: tuple[int, ...]) -> tuple[int, ...]:
    mapping: dict[int, int] = {}
    result: list[int] = []
    for value in values:
        if value not in mapping:
            mapping[value] = len(mapping)
        result.append(mapping[value])
    return tuple(result)


def _all_partitions(size: int) -> tuple[tuple[int, ...], ...]:
    seen = set()
    for raw in product(range(size), repeat=size):
        canonical = _canonical(raw)
        seen.add(canonical)
    return tuple(sorted(seen))


def _oracle_joint_partition(
    audits: tuple[AuditRefinement, ...], baseline: tuple[int, ...]
) -> tuple[int, ...]:
    candidates = []
    for partition in _all_partitions(len(baseline)):
        if not partition_refines(partition, baseline):
            continue
        if all(audit.is_fixed(partition) for audit in audits):
            candidates.append(partition)
    coarsest = [
        partition
        for partition in candidates
        if all(partition_refines(other, partition) for other in candidates)
    ]
    assert len(coarsest) == 1
    return coarsest[0]


def test_marked_cycle_attains_positive_unbounded_delta() -> None:
    for n in range(2, 18):
        report = marked_cycle_report(n)
        assert report.individual_debts == pytest.approx((1.0, 0.0))
        assert report.joint_blocks == n
        assert report.joint_debt == pytest.approx(log2(n))
        assert report.delta == pytest.approx(log2(n) - 1.0)


def test_zero_individual_debt_lemma() -> None:
    baseline = (0, 0, 1, 1)
    identity = AuditRefinement(
        "identity",
        ("same",) * 4,
        ("stay",),
        ((0,), (1,), (2,), (3,)),
    )
    assert zero_individual_debt_implies_zero_joint((identity,), baseline)
    report = debt_report((identity,), baseline)
    assert report.individual_debts == pytest.approx((0.0,))
    assert report.joint_debt == pytest.approx(0.0)
    assert report.delta == pytest.approx(0.0)


def test_joint_solver_matches_exhaustive_partition_oracle_on_128_small_problems() -> None:
    rng = Random(20260908)
    checked = 0
    while checked < 128:
        size = rng.randint(1, 4)
        baseline = _canonical(tuple(rng.randrange(2) for _ in range(size)))
        audits = []
        for audit_index in range(rng.randint(1, 3)):
            static = tuple(rng.randrange(2) for _ in range(size))
            successors = tuple((rng.randrange(size),) for _ in range(size))
            audits.append(
                AuditRefinement(
                    f"audit-{audit_index}",
                    static,
                    ("step",),
                    successors,
                )
            )
        audit_tuple = tuple(audits)
        assert joint_partition(audit_tuple, baseline) == _oracle_joint_partition(
            audit_tuple, baseline
        )
        checked += 1


def test_marked_cycle_input_validation() -> None:
    for value in (0, 1, -1, True):
        with pytest.raises(ValueError):
            marked_cycle_audits(value)
