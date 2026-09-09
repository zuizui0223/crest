from __future__ import annotations

from itertools import product

from crest.cut_state_quotient import (
    extension_is_redundant,
    induced_cut_state,
    partitions_equal_up_to_relabeling,
    signature_families_equivalent,
    signature_family_factors_through,
)


def _binary_signatures(n: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(bits) for bits in product((0, 1), repeat=n))


def test_relabeling_reordering_duplication_and_coordinate_repackaging_are_invariant() -> None:
    worlds = ("a", "b", "c", "d")
    cut = (0, 0, 0, 0)

    g1 = (0, 0, 1, 1)
    g2 = (0, 1, 0, 1)
    # Same joint information as (g1, g2), represented as one four-level signature.
    packed = ("00", "01", "10", "11")
    relabeled_g1 = ("left", "left", "right", "right")

    assert signature_families_equivalent(worlds, cut, (g1, g2), (packed,))
    assert signature_families_equivalent(
        worlds,
        cut,
        (g1, g2),
        (g2, relabeled_g1, g2),
    )
    assert partitions_equal_up_to_relabeling(
        worlds,
        induced_cut_state(worlds, cut, (g1, g2)),
        induced_cut_state(worlds, cut, (packed,)),
    )


def test_mutual_factorization_is_necessary_and_sufficient_for_equal_induced_state() -> None:
    worlds = (0, 1, 2, 3)
    cut = ("x", "x", "x", "x")
    all_signatures = _binary_signatures(len(worlds))

    # Exhaust over all one-signature families and selected two-signature families.
    families = [(sig,) for sig in all_signatures]
    families += [
        (all_signatures[i], all_signatures[j])
        for i in range(0, len(all_signatures), 3)
        for j in range(0, len(all_signatures), 5)
    ]

    for left in families:
        left_state = induced_cut_state(worlds, cut, left)
        for right in families:
            right_state = induced_cut_state(worlds, cut, right)
            equal = partitions_equal_up_to_relabeling(worlds, left_state, right_state)
            mutual = signature_family_factors_through(worlds, right_state, left) and signature_family_factors_through(
                worlds, left_state, right
            )
            assert mutual is equal
            assert signature_families_equivalent(worlds, cut, left, right) is equal


def test_redundant_extensions_do_not_change_state_but_new_information_does() -> None:
    worlds = ("a", "b", "c", "d")
    cut = (0, 0, 0, 0)
    base = ((0, 0, 1, 1),)

    redundant = (("L", "L", "R", "R"), (7, 7, 8, 8))
    genuinely_new = ((0, 1, 0, 1),)

    assert extension_is_redundant(worlds, cut, base, redundant)
    assert not extension_is_redundant(worlds, cut, base, genuinely_new)

    base_state = induced_cut_state(worlds, cut, base)
    redundant_state = induced_cut_state(worlds, cut, (*base, *redundant))
    expanded_state = induced_cut_state(worlds, cut, (*base, *genuinely_new))

    assert partitions_equal_up_to_relabeling(worlds, base_state, redundant_state)
    assert not partitions_equal_up_to_relabeling(worlds, base_state, expanded_state)


def test_cut_observation_is_part_of_the_invariant_not_optional_background() -> None:
    worlds = ("a", "b", "c", "d")
    family = ((0, 0, 1, 1),)
    cut1 = (0, 0, 0, 0)
    cut2 = (0, 1, 0, 1)

    state1 = induced_cut_state(worlds, cut1, family)
    state2 = induced_cut_state(worlds, cut2, family)
    assert not partitions_equal_up_to_relabeling(worlds, state1, state2)
