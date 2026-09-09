from __future__ import annotations

from itertools import combinations, product

from crest.cut_state_quotient import (
    induced_cut_state,
    is_admissible_cut_state,
    labels_from_partition,
    partition_from_labels,
    partition_refines,
    partitions_equal_up_to_relabeling,
    state_information_bits,
)


def _set_partitions(items: tuple[int, ...]):
    """Generate each set partition once for a small ordered carrier."""
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in _set_partitions(rest):
        # Put first in its own leading block.
        yield (frozenset((first,)), *partition)
        # Or insert it into each existing block.
        for i in range(len(partition)):
            blocks = list(partition)
            blocks[i] = frozenset((*blocks[i], first))
            yield tuple(blocks)


def _canonical(partition):
    return frozenset(frozenset(block) for block in partition)


def test_every_refinement_of_the_cut_is_realizable_by_one_signature() -> None:
    worlds = (0, 1, 2, 3)
    cut_labels = ("A", "A", "B", "B")
    cut = partition_from_labels(worlds, cut_labels)

    seen = set()
    admissible = 0
    for partition in _set_partitions(worlds):
        key = _canonical(partition)
        if key in seen:
            continue
        seen.add(key)
        if not partition_refines(worlds, partition, cut):
            continue
        admissible += 1
        labels = labels_from_partition(worlds, partition)
        induced = induced_cut_state(worlds, cut_labels, (labels,))
        assert partitions_equal_up_to_relabeling(worlds, induced, partition)
        assert is_admissible_cut_state(worlds, cut_labels, induced)

    # Refinements of {0,1}|{2,3}: independently split either two-element block.
    assert admissible == 4


def test_every_signature_family_lands_inside_the_cut_refinement_interval() -> None:
    worlds = (0, 1, 2, 3)
    cut_labels = (0, 0, 1, 1)
    binary = tuple(tuple(bits) for bits in product((0, 1), repeat=4))

    families = [()]
    families += [(sig,) for sig in binary]
    families += [(binary[i], binary[j]) for i, j in combinations(range(len(binary)), 2)]

    for family in families:
        state = induced_cut_state(worlds, cut_labels, family)
        assert is_admissible_cut_state(worlds, cut_labels, state)


def test_signature_extension_is_monotone_in_refinement_and_information() -> None:
    worlds = (0, 1, 2, 3)
    cut_labels = (0, 0, 0, 0)
    signatures = (
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
    )

    for mask in range(1 << len(signatures)):
        base = tuple(signatures[i] for i in range(len(signatures)) if mask & (1 << i))
        base_state = induced_cut_state(worlds, cut_labels, base)
        for j, signature in enumerate(signatures):
            if mask & (1 << j):
                continue
            extended_state = induced_cut_state(worlds, cut_labels, (*base, signature))
            assert partition_refines(worlds, extended_state, base_state)
            assert state_information_bits(worlds, extended_state) >= state_information_bits(worlds, base_state)


def test_information_order_of_signature_classes_matches_partition_refinement() -> None:
    worlds = (0, 1, 2, 3)
    cut_labels = (0, 0, 0, 0)
    signatures = (
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
    )

    families = [()]
    for r in (1, 2, 3):
        families.extend(combinations(signatures, r))

    states = [induced_cut_state(worlds, cut_labels, family) for family in families]
    for i, left in enumerate(states):
        for j, right in enumerate(states):
            # Define the information order by right carrying at least as much
            # distinction as left. It is exactly partition refinement.
            more_or_equal_information = partition_refines(worlds, right, left)
            assert more_or_equal_information is (
                state_information_bits(worlds, right) >= state_information_bits(worlds, left)
                if partitions_equal_up_to_relabeling(worlds, left, right)
                or partition_refines(worlds, right, left)
                else False
            )
