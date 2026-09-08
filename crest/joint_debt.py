"""Non-additive debt induced by interacting CREST audit closures.

For a common finite carrier and baseline partition B, audit i has individual debt

    D_i = log2 |C_i(B)| - log2 |B|,

where C_i is its exact refinement closure.  The joint debt uses the least common
fixed point reached by fair iteration of all audit closures.  The excess

    Delta = D_joint - sum_i D_i

measures closure interaction that is invisible to responsibility-by-responsibility
budgeting.  The underlying closure/fixed-point machinery is classical; CREST uses
Delta as an accounting diagnostic for joint scientific responsibility.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log2
from typing import Hashable, Iterable

from .joint_state import AuditRefinement

PartitionLike = Iterable[Hashable]


def _canonical(values: PartitionLike) -> tuple[int, ...]:
    labels: dict[Hashable, int] = {}
    result: list[int] = []
    for value in values:
        try:
            hash(value)
        except TypeError as error:
            raise ValueError("partition labels must be hashable") from error
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    if not result:
        raise ValueError("partition must be nonempty")
    return tuple(result)


def state_bits(partition: PartitionLike) -> float:
    """Log2 of the number of blocks in a finite partition."""

    labels = _canonical(partition)
    return log2(max(labels) + 1)


def audit_debt(audit: AuditRefinement, baseline: PartitionLike) -> float:
    """Debt created by one audit acting alone on the baseline partition."""

    base = _canonical(baseline)
    if len(base) != audit.world_count:
        raise ValueError("baseline must align with the audit carrier")
    return state_bits(audit.close(base)) - state_bits(base)


def joint_partition(
    audits: Iterable[AuditRefinement], baseline: PartitionLike
) -> tuple[int, ...]:
    """Least common fixed point reached by fair cyclic refinement."""

    audit_tuple = tuple(audits)
    if not audit_tuple:
        raise ValueError("at least one audit is required")
    base = _canonical(baseline)
    if any(audit.world_count != len(base) for audit in audit_tuple):
        raise ValueError("all audits and baseline must share one finite carrier")

    labels = base
    while True:
        before = labels
        for audit in audit_tuple:
            labels = audit.close(labels)
        if labels == before:
            return labels


def joint_debt(audits: Iterable[AuditRefinement], baseline: PartitionLike) -> float:
    """Debt of the least state satisfying all audits simultaneously."""

    audit_tuple = tuple(audits)
    base = _canonical(baseline)
    return state_bits(joint_partition(audit_tuple, base)) - state_bits(base)


@dataclass(frozen=True)
class JointDebtReport:
    """Individual, joint, and non-additive CREST state debt."""

    individual_debts: tuple[float, ...]
    joint_debt: float
    delta: float
    baseline_blocks: int
    joint_blocks: int

    def verify(self, *, tolerance: float = 1e-12) -> bool:
        return (
            self.baseline_blocks >= 1
            and self.joint_blocks >= self.baseline_blocks
            and all(value >= -tolerance for value in self.individual_debts)
            and self.joint_debt >= -tolerance
            and abs(self.delta - (self.joint_debt - sum(self.individual_debts)))
            <= tolerance
        )


def debt_report(
    audits: Iterable[AuditRefinement], baseline: PartitionLike
) -> JointDebtReport:
    audit_tuple = tuple(audits)
    base = _canonical(baseline)
    if not audit_tuple:
        raise ValueError("at least one audit is required")
    individual = tuple(audit_debt(audit, base) for audit in audit_tuple)
    joint = joint_partition(audit_tuple, base)
    result = JointDebtReport(
        individual_debts=individual,
        joint_debt=state_bits(joint) - state_bits(base),
        delta=(state_bits(joint) - state_bits(base)) - sum(individual),
        baseline_blocks=max(base) + 1,
        joint_blocks=max(joint) + 1,
    )
    if not result.verify():
        raise AssertionError("constructed joint-debt report did not verify")
    return result


def zero_individual_debt_implies_zero_joint(
    audits: Iterable[AuditRefinement], baseline: PartitionLike
) -> bool:
    """Executable form of the zero-debt lemma.

    If every audit fixes B individually, B is already a common fixed point, so
    fair joint iteration cannot refine it and Delta is zero.
    """

    report = debt_report(audits, baseline)
    if any(abs(value) > 1e-12 for value in report.individual_debts):
        return True
    return abs(report.joint_debt) <= 1e-12 and abs(report.delta) <= 1e-12


def marked_cycle_audits(
    state_count: int,
) -> tuple[tuple[int, ...], tuple[AuditRefinement, AuditRefinement]]:
    """Sharp cyclic family with Delta = log2(n) - 1.

    One audit marks a single state, costing exactly one bit from an indiscrete
    baseline.  A second audit is a deterministic cycle and costs zero alone.
    Once the mark exists, repeated successor-stability around the cycle forces
    every state to become distinct.  Thus D_joint=log2(n), sum D_i=1.
    """

    if not isinstance(state_count, int) or isinstance(state_count, bool) or state_count < 2:
        raise ValueError("state_count must be an integer at least two")
    baseline = (0,) * state_count
    seed = AuditRefinement(
        "seed-mark",
        tuple("marked" if index == 0 else "unmarked" for index in range(state_count)),
        (),
        tuple(() for _ in range(state_count)),
    )
    cycle = AuditRefinement(
        "cycle-propagation",
        ("same",) * state_count,
        ("step",),
        tuple((((index + 1) % state_count),) for index in range(state_count)),
    )
    return baseline, (seed, cycle)


def marked_cycle_report(state_count: int) -> JointDebtReport:
    baseline, audits = marked_cycle_audits(state_count)
    return debt_report(audits, baseline)


__all__ = [
    "JointDebtReport",
    "audit_debt",
    "debt_report",
    "joint_debt",
    "joint_partition",
    "marked_cycle_audits",
    "marked_cycle_report",
    "state_bits",
    "zero_individual_debt_implies_zero_joint",
]
