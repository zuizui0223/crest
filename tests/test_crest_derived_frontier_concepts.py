from __future__ import annotations

from itertools import product

from crest.joint_state import (
    compatible_values_by_evidence,
    evidence_licenses,
    partition_refines,
)


def _canonical(values: tuple[object, ...]) -> tuple[int, ...]:
    labels: dict[object, int] = {}
    out: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        out.append(labels[value])
    return tuple(out)


def _partitions(size: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate canonical restricted-growth strings for all set partitions."""

    if size <= 0:
        raise ValueError("size must be positive")
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


def _common_refinement(*partitions: tuple[int, ...]) -> tuple[int, ...]:
    if not partitions:
        raise ValueError("at least one partition is required")
    size = len(partitions[0])
    if any(len(partition) != size for partition in partitions):
        raise ValueError("partitions must share a carrier")
    return _canonical(
        tuple(partition[index] for partition in partitions)
        for index in range(size)
    )


def _block_count(partition: tuple[int, ...]) -> int:
    return max(partition) + 1


def test_monitoring_adequacy_envelope_is_downward_closed() -> None:
    """Exhaust the four-world lattice for the M1 lower-set theorem."""

    partitions = _partitions(4)
    for evidence, coarse, fine in product(partitions, repeat=3):
        if not partition_refines(fine, coarse):
            continue
        if evidence_licenses(fine, evidence):
            assert evidence_licenses(coarse, evidence)
        if not evidence_licenses(coarse, evidence):
            assert not evidence_licenses(fine, evidence)


def test_counterfactual_obsolescence_pair_criterion_is_exact() -> None:
    """Check C1 against every ordered pair of four-world partitions/evidence."""

    partitions = _partitions(4)
    for evidence, old_state, new_state in product(partitions, repeat=3):
        if not partition_refines(new_state, old_state):
            continue
        if not evidence_licenses(old_state, evidence):
            continue

        activated_inside_evidence = any(
            evidence[left] == evidence[right]
            and old_state[left] == old_state[right]
            and new_state[left] != new_state[right]
            for left in range(4)
            for right in range(left + 1, 4)
        )
        assert (not evidence_licenses(new_state, evidence)) == activated_inside_evidence


def test_anticipatory_state_is_unique_coarsest_common_refinement() -> None:
    """Exhaust all three-world contract families and candidate partitions."""

    partitions = _partitions(3)
    for first, second, third in product(partitions, repeat=3):
        anticipatory = _common_refinement(first, second, third)
        assert partition_refines(anticipatory, first)
        assert partition_refines(anticipatory, second)
        assert partition_refines(anticipatory, third)

        for candidate in partitions:
            if all(
                partition_refines(candidate, required)
                for required in (first, second, third)
            ):
                assert partition_refines(candidate, anticipatory)


def test_state_shadow_equals_pairs_activated_by_some_contemplated_contract() -> None:
    partitions = _partitions(4)
    for current, future_a, future_b in product(partitions, repeat=3):
        anticipatory = _common_refinement(current, future_a, future_b)
        for left in range(4):
            for right in range(left + 1, 4):
                in_shadow = (
                    current[left] == current[right]
                    and anticipatory[left] != anticipatory[right]
                )
                activated_somewhere = (
                    current[left] == current[right]
                    and (
                        future_a[left] != future_a[right]
                        or future_b[left] != future_b[right]
                    )
                )
                assert in_shadow == activated_somewhere


def test_shadow_burden_cannot_decrease_when_future_family_expands() -> None:
    partitions = _partitions(4)
    for current, future_a, future_b in product(partitions, repeat=3):
        first_envelope = _common_refinement(current, future_a)
        expanded_envelope = _common_refinement(current, future_a, future_b)
        assert partition_refines(expanded_envelope, first_envelope)
        assert _block_count(expanded_envelope) >= _block_count(first_envelope)


def test_decision_safe_ignorance_has_exact_sharp_report_form() -> None:
    """Exhaust the three-world state/evidence/target lattice for D1."""

    partitions = _partitions(3)
    for state, evidence, target in product(partitions, repeat=3):
        decision_safe_ignorance = (
            evidence_licenses(target, evidence)
            and not evidence_licenses(state, evidence)
        )
        state_reports = compatible_values_by_evidence(state, evidence)
        target_reports = compatible_values_by_evidence(target, evidence)
        sharp_form = (
            any(len(report) > 1 for report in state_reports)
            and all(len(report) == 1 for report in target_reports)
        )
        assert decision_safe_ignorance == sharp_form


def test_minimal_monitoring_refinement_is_common_refinement() -> None:
    """Exhaust R1: E ∨ J is the unique coarsest evidence refinement licensing J."""

    partitions = _partitions(4)
    for evidence, state in product(partitions, repeat=2):
        required = _common_refinement(evidence, state)
        assert partition_refines(required, evidence)
        assert evidence_licenses(state, required)

        for candidate in partitions:
            if partition_refines(candidate, evidence) and evidence_licenses(
                state, candidate
            ):
                assert partition_refines(candidate, required)


def test_monitoring_resolution_debt_has_exact_zero_criterion() -> None:
    partitions = _partitions(4)
    for evidence, state in product(partitions, repeat=2):
        required = _common_refinement(evidence, state)
        zero_debt = _block_count(required) == _block_count(evidence)
        assert zero_debt == evidence_licenses(state, evidence)


def test_monitoring_resolution_debt_is_monotone_under_state_refinement() -> None:
    partitions = _partitions(4)
    for evidence, coarse_state, fine_state in product(partitions, repeat=3):
        if not partition_refines(fine_state, coarse_state):
            continue
        coarse_required = _common_refinement(evidence, coarse_state)
        fine_required = _common_refinement(evidence, fine_state)
        assert partition_refines(fine_required, coarse_required)
        assert _block_count(fine_required) >= _block_count(coarse_required)


def test_decision_safe_ignorance_is_positive_state_debt_zero_target_debt() -> None:
    partitions = _partitions(3)
    for evidence, state, target in product(partitions, repeat=3):
        state_required = _common_refinement(evidence, state)
        target_required = _common_refinement(evidence, target)
        positive_state_debt = _block_count(state_required) > _block_count(evidence)
        zero_target_debt = _block_count(target_required) == _block_count(evidence)
        assert (positive_state_debt and zero_target_debt) == (
            evidence_licenses(target, evidence)
            and not evidence_licenses(state, evidence)
        )
