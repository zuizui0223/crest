from __future__ import annotations

from random import Random

from crest.joint_state import AuditRefinement, JointCRESTContract, solve_joint_crest_state


def _partitions(size: int):
    """Enumerate canonical restricted-growth partition labels."""

    if size <= 0:
        yield ()
        return

    def visit(prefix: list[int], maximum: int):
        if len(prefix) == size:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from visit(prefix, max(maximum, value))
            prefix.pop()

    yield from visit([0], 0)


def _canonical(values) -> tuple[int, ...]:
    labels = {}
    result = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    return tuple(result)


def _refines(fine, coarse) -> bool:
    fine = _canonical(fine)
    coarse = _canonical(coarse)
    return all(
        fine[i] != fine[j] or coarse[i] == coarse[j]
        for i in range(len(fine))
        for j in range(i + 1, len(fine))
    )


def _audit_fixed_direct(audit: AuditRefinement, partition) -> bool:
    """Independent fixed-point predicate, without calling AuditRefinement.close."""

    labels = _canonical(partition)
    for left in range(len(labels)):
        for right in range(left + 1, len(labels)):
            if labels[left] != labels[right]:
                continue
            if audit.static_labels[left] != audit.static_labels[right]:
                return False
            for action_index in range(len(audit.actions)):
                left_successor = audit.successors[left][action_index]
                right_successor = audit.successors[right][action_index]
                if (left_successor is None) != (right_successor is None):
                    return False
                if left_successor is not None:
                    assert right_successor is not None
                    if labels[left_successor] != labels[right_successor]:
                        return False
    return True


def _random_partition(rng: Random, size: int, categories: int = 3):
    return _canonical(rng.randrange(categories) for _ in range(size))


def _random_audit(rng: Random, name: str, size: int) -> AuditRefinement:
    action_count = rng.randrange(3)  # 0, 1, or 2 actions
    actions = tuple(f"{name}-a{index}" for index in range(action_count))
    successors = tuple(
        tuple(rng.choice((None, *range(size))) for _ in range(action_count))
        for _ in range(size)
    )
    return AuditRefinement(
        name=name,
        static_labels=_random_partition(rng, size),
        actions=actions,
        successors=successors,
    )


def _oracle_joint_state(contract: JointCRESTContract) -> tuple[int, ...]:
    candidates = []
    for partition in _partitions(len(contract.worlds)):
        if not _refines(partition, contract.base_labels):
            continue
        if all(_audit_fixed_direct(audit, partition) for audit in contract.audits):
            candidates.append(partition)

    assert candidates, "the discrete partition must always be a common fixed point"
    least = [
        candidate
        for candidate in candidates
        if all(_refines(other, candidate) for other in candidates)
    ]
    assert len(least) == 1
    return least[0]


def _licensed_direct(values, evidence) -> bool:
    return all(
        evidence[i] != evidence[j] or values[i] == values[j]
        for i in range(len(values))
        for j in range(i + 1, len(values))
    )


def test_j1_matches_independent_bruteforce_oracle_across_small_contracts() -> None:
    rng = Random(20260821)

    # Bell(4)=15, so each generated four-world contract can be checked against
    # every partition without making the regression suite expensive.
    for case in range(96):
        size = 1 + case % 4
        worlds = tuple(f"w{index}" for index in range(size))
        audits = tuple(
            _random_audit(rng, name, size)
            for name in ("future", "semantic", "mechanism", "target")
        )
        contract = JointCRESTContract(
            worlds=worlds,
            base_labels=_random_partition(rng, size),
            evidence_labels=_random_partition(rng, size),
            target_labels=tuple(rng.randrange(3) for _ in range(size)),
            audits=audits,
        )

        expected = _oracle_joint_state(contract)
        forward = solve_joint_crest_state(contract)
        reverse = solve_joint_crest_state(
            contract,
            audit_order=tuple(reversed([audit.name for audit in audits])),
        )

        assert forward.class_labels == expected
        assert reverse.class_labels == expected
        assert all(_audit_fixed_direct(audit, expected) for audit in audits)
        assert _refines(expected, contract.base_labels)

        assert forward.full_state_licensed == _licensed_direct(
            expected, contract.evidence_labels
        )
        assert forward.target_report_licensed == _licensed_direct(
            contract.target_labels, contract.evidence_labels
        )
