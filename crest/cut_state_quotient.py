"""Least finite quotient induced at an observational temporal cut.

This module is deliberately independent of CREST's particular MLTR/MRM/CCOC
semantics. It states the finite set-theoretic core used by the pure temporal-
boundary formulation.

Let Omega be a finite carrier, O_t an observation signature, and g_i any finite
family of pre-state distinguishability/access signatures on Omega. The induced
cut state is the common-refinement quotient

    omega ~* omega'
    iff O_t(omega) = O_t(omega') and g_i(omega) = g_i(omega') for every i.

Among all partitions that preserve the observation and every declared
signature, this quotient is the unique coarsest one (up to block relabeling).
Equivalently, it retains the least information compatible with the declared
constraints.

The quotient is representation invariant: two different signature families
induce the same cut state exactly when each family factors through the state
induced by the other. In particular, adding a signature that already factors
through the induced state cannot change that state.

For a fixed cut, representation-equivalence classes of finite signature
families correspond exactly to partitions refining the cut partition. This
identifies the finite CREST state space with the refinement interval above the
visible cut in the partition lattice.

No temporal-continuum or epsilon->0 limit is used here.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Sequence
from math import log2

Partition = tuple[frozenset[Hashable], ...]


def _validated_worlds(worlds: Sequence[Hashable]) -> tuple[Hashable, ...]:
    carrier = tuple(worlds)
    if not carrier:
        raise ValueError("cut-state carrier must be nonempty")
    if len(set(carrier)) != len(carrier):
        raise ValueError("cut-state worlds must be unique")
    for world in carrier:
        try:
            hash(world)
        except TypeError as error:
            raise ValueError("cut-state worlds must be hashable") from error
    return carrier


def partition_from_labels(
    worlds: Sequence[Hashable],
    labels: Sequence[Hashable],
) -> Partition:
    """Return the kernel partition of one extensional signature map."""

    carrier = _validated_worlds(worlds)
    values = tuple(labels)
    if len(values) != len(carrier):
        raise ValueError("signature labels must align with the cut-state carrier")

    buckets: dict[Hashable, set[Hashable]] = {}
    for world, label in zip(carrier, values):
        try:
            hash(label)
        except TypeError as error:
            raise ValueError("signature labels must be hashable") from error
        buckets.setdefault(label, set()).add(world)
    return tuple(frozenset(block) for block in buckets.values())


def validate_partition(worlds: Sequence[Hashable], partition: Iterable[Iterable[Hashable]]) -> Partition:
    """Validate and normalize a partition of ``worlds``."""

    carrier = _validated_worlds(worlds)
    carrier_set = set(carrier)
    blocks = tuple(frozenset(block) for block in partition)
    if not blocks or any(not block for block in blocks):
        raise ValueError("a partition must contain only nonempty blocks")
    union: set[Hashable] = set()
    for block in blocks:
        if not block.issubset(carrier_set):
            raise ValueError("partition contains a world outside the carrier")
        if union & set(block):
            raise ValueError("partition blocks must be disjoint")
        union.update(block)
    if union != carrier_set:
        raise ValueError("partition blocks must cover the carrier")
    return blocks


def labels_from_partition(
    worlds: Sequence[Hashable],
    partition: Iterable[Iterable[Hashable]],
) -> tuple[int, ...]:
    """Encode a partition as one signature aligned with ``worlds``.

    The particular integer labels have no mathematical significance; only their
    kernel partition matters. This supplies the constructive surjectivity step
    in the cut-state lattice representation theorem.
    """

    carrier = _validated_worlds(worlds)
    blocks = validate_partition(carrier, partition)
    index: dict[Hashable, int] = {}
    for position, block in enumerate(blocks):
        for world in block:
            index[world] = position
    return tuple(index[world] for world in carrier)


def partition_refines(
    worlds: Sequence[Hashable],
    finer: Iterable[Iterable[Hashable]],
    coarser: Iterable[Iterable[Hashable]],
) -> bool:
    """Return whether ``finer`` refines ``coarser``.

    Thus every block of ``finer`` must be contained in one block of ``coarser``.
    """

    fine = validate_partition(worlds, finer)
    coarse = validate_partition(worlds, coarser)
    return all(any(block <= parent for parent in coarse) for block in fine)


def partitions_equal_up_to_relabeling(
    worlds: Sequence[Hashable],
    left: Iterable[Iterable[Hashable]],
    right: Iterable[Iterable[Hashable]],
) -> bool:
    """Return whether two partitions have exactly the same blocks."""

    lhs = validate_partition(worlds, left)
    rhs = validate_partition(worlds, right)
    return frozenset(lhs) == frozenset(rhs)


def least_common_refinement(
    worlds: Sequence[Hashable],
    partitions: Iterable[Iterable[Iterable[Hashable]]],
) -> Partition:
    """Return the unique coarsest partition refining every supplied partition."""

    carrier = _validated_worlds(worlds)
    normalized = tuple(validate_partition(carrier, partition) for partition in partitions)
    if not normalized:
        return (frozenset(carrier),)

    block_index: list[dict[Hashable, int]] = []
    for partition in normalized:
        index: dict[Hashable, int] = {}
        for position, block in enumerate(partition):
            for world in block:
                index[world] = position
        block_index.append(index)

    buckets: dict[tuple[int, ...], set[Hashable]] = {}
    for world in carrier:
        signature = tuple(index[world] for index in block_index)
        buckets.setdefault(signature, set()).add(world)
    return tuple(frozenset(block) for block in buckets.values())


def induced_cut_state(
    worlds: Sequence[Hashable],
    cut_observations: Sequence[Hashable],
    constraint_signatures: Iterable[Sequence[Hashable]],
) -> Partition:
    """Return the least-information cut-state preserving all declared signatures."""

    carrier = _validated_worlds(worlds)
    baseline = partition_from_labels(carrier, cut_observations)
    constraints = tuple(
        partition_from_labels(carrier, signature) for signature in constraint_signatures
    )
    return least_common_refinement(carrier, (baseline, *constraints))


def is_admissible_cut_state(
    worlds: Sequence[Hashable],
    cut_observations: Sequence[Hashable],
    candidate_partition: Iterable[Iterable[Hashable]],
) -> bool:
    """Return whether a partition refines the visible cut partition."""

    carrier = _validated_worlds(worlds)
    candidate = validate_partition(carrier, candidate_partition)
    cut = partition_from_labels(carrier, cut_observations)
    return partition_refines(carrier, candidate, cut)


def state_information_bits(
    worlds: Sequence[Hashable],
    state_partition: Iterable[Iterable[Hashable]],
) -> float:
    """Return log2 of the number of quotient classes."""

    blocks = validate_partition(worlds, state_partition)
    return log2(len(blocks))


def preserves_signature(
    worlds: Sequence[Hashable],
    state_partition: Iterable[Iterable[Hashable]],
    labels: Sequence[Hashable],
) -> bool:
    """Return whether a signature is constant on every state block.

    This is the finite factorization criterion: the signature factors through the
    quotient map exactly when this function returns ``True``.
    """

    carrier = _validated_worlds(worlds)
    state = validate_partition(carrier, state_partition)
    signature = partition_from_labels(carrier, labels)
    return partition_refines(carrier, state, signature)


def signature_family_factors_through(
    worlds: Sequence[Hashable],
    state_partition: Iterable[Iterable[Hashable]],
    signatures: Iterable[Sequence[Hashable]],
) -> bool:
    """Return whether every signature in a family factors through one state."""

    family = tuple(tuple(signature) for signature in signatures)
    return all(preserves_signature(worlds, state_partition, signature) for signature in family)


def signature_families_equivalent(
    worlds: Sequence[Hashable],
    cut_observations: Sequence[Hashable],
    left_signatures: Iterable[Sequence[Hashable]],
    right_signatures: Iterable[Sequence[Hashable]],
) -> bool:
    """Return whether two pre-state signature families induce the same cut state.

    For a fixed carrier and cut observation, the following are equivalent:

    1. both families induce the same quotient partition (up to block relabeling);
    2. every left signature factors through the state induced by the right family,
       and every right signature factors through the state induced by the left.

    The implementation checks the mutual-factorization characterization. This
    makes representation invariance explicit without privileging signature names,
    codomain labels, order, duplication, or decomposition into coordinates.
    """

    carrier = _validated_worlds(worlds)
    left = tuple(tuple(signature) for signature in left_signatures)
    right = tuple(tuple(signature) for signature in right_signatures)
    left_state = induced_cut_state(carrier, cut_observations, left)
    right_state = induced_cut_state(carrier, cut_observations, right)
    return signature_family_factors_through(carrier, right_state, left) and signature_family_factors_through(
        carrier, left_state, right
    )


def extension_is_redundant(
    worlds: Sequence[Hashable],
    cut_observations: Sequence[Hashable],
    base_signatures: Iterable[Sequence[Hashable]],
    added_signatures: Iterable[Sequence[Hashable]],
) -> bool:
    """Return whether adding signatures leaves the induced cut state unchanged.

    By the invariance theorem this holds exactly when every added signature
    already factors through the state induced by the base family.
    """

    carrier = _validated_worlds(worlds)
    base = tuple(tuple(signature) for signature in base_signatures)
    added = tuple(tuple(signature) for signature in added_signatures)
    base_state = induced_cut_state(carrier, cut_observations, base)
    return signature_family_factors_through(carrier, base_state, added)


def satisfies_cut_universal_property(
    worlds: Sequence[Hashable],
    cut_observations: Sequence[Hashable],
    constraint_signatures: Iterable[Sequence[Hashable]],
    candidate_partition: Iterable[Iterable[Hashable]],
) -> bool:
    """Check the universal-property implication for one candidate partition.

    If ``candidate_partition`` preserves the visible cut and every declared
    signature, then it must refine the induced cut state. This function returns
    True when the implication holds for the supplied candidate.
    """

    carrier = _validated_worlds(worlds)
    signatures = tuple(tuple(signature) for signature in constraint_signatures)
    candidate = validate_partition(carrier, candidate_partition)
    preserves_all = preserves_signature(carrier, candidate, cut_observations) and all(
        preserves_signature(carrier, candidate, signature) for signature in signatures
    )
    if not preserves_all:
        return True
    induced = induced_cut_state(carrier, cut_observations, signatures)
    return partition_refines(carrier, candidate, induced)


__all__ = [
    "Partition",
    "extension_is_redundant",
    "induced_cut_state",
    "is_admissible_cut_state",
    "labels_from_partition",
    "least_common_refinement",
    "partition_from_labels",
    "partition_refines",
    "partitions_equal_up_to_relabeling",
    "preserves_signature",
    "satisfies_cut_universal_property",
    "signature_families_equivalent",
    "signature_family_factors_through",
    "state_information_bits",
    "validate_partition",
]
