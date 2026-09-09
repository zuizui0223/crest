from __future__ import annotations

from collections.abc import Hashable

from crest.cut_state_quotient import (
    induced_cut_state,
    partition_refines,
    preserves_signature,
    satisfies_cut_universal_property,
)
from crest.explicit_temporal_grammar import FUTURE, HISTORY, MECHANISM
from crest.semantic_access import (
    candidate_type,
    canonical_nontrivial_companion_model,
    decoder_can_address,
    route_mode,
)
from crest.semantic_temporal_quotient import semantic_induced_classes, semantic_worlds


def _all_partitions(items: tuple[Hashable, ...]):
    if not items:
        yield tuple()
        return
    first, *rest_list = items
    rest = tuple(rest_list)
    for partition in _all_partitions(rest):
        yield (frozenset((first,)), *partition)
        for index in range(len(partition)):
            blocks = list(partition)
            blocks[index] = frozenset((*blocks[index], first))
            yield tuple(blocks)


def _as_block_set(partition):
    return frozenset(frozenset(block) for block in partition)


def test_induced_cut_state_preserves_every_declared_signature() -> None:
    worlds = ("a", "b", "c", "d")
    visible = ("same", "same", "same", "same")
    retrospective = ("h0", "h0", "h1", "h1")
    transverse = ("t0", "t0", "t0", "t1")

    state = induced_cut_state(worlds, visible, (retrospective, transverse))

    assert _as_block_set(state) == frozenset(
        (frozenset(("a", "b")), frozenset(("c",)), frozenset(("d",)))
    )
    assert preserves_signature(worlds, state, visible)
    assert preserves_signature(worlds, state, retrospective)
    assert preserves_signature(worlds, state, transverse)


def test_induced_cut_state_is_the_unique_coarsest_admissible_partition_exhaustively() -> None:
    worlds = (0, 1, 2, 3)
    visible = ("y", "y", "y", "y")
    retrospective = (0, 0, 1, 1)
    transverse = (0, 0, 0, 1)
    signatures = (retrospective, transverse)
    induced = induced_cut_state(worlds, visible, signatures)

    admissible = []
    for candidate in _all_partitions(worlds):
        preserves_all = preserves_signature(worlds, candidate, visible) and all(
            preserves_signature(worlds, candidate, signature) for signature in signatures
        )
        assert satisfies_cut_universal_property(
            worlds,
            visible,
            signatures,
            candidate,
        )
        if preserves_all:
            admissible.append(candidate)
            assert partition_refines(worlds, candidate, induced)

    assert admissible
    assert any(_as_block_set(candidate) == _as_block_set(induced) for candidate in admissible)
    assert len(induced) == 3


def test_visible_cut_itself_is_part_of_the_universal_property() -> None:
    worlds = ("a", "b", "c", "d")
    visible = ("left", "left", "right", "right")
    extra = (0, 1, 0, 1)

    induced = induced_cut_state(worlds, visible, (extra,))

    assert len(induced) == 4
    assert preserves_signature(worlds, induced, visible)
    assert preserves_signature(worlds, induced, extra)


def test_v07_semantic_access_is_a_specialization_of_the_general_cut_quotient() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    worlds = semantic_worlds(routes, candidates, bit_depth=3)

    visible = tuple("same-cut-observation" for _ in worlds)
    retrospective = tuple(
        route_mode(world.route, model.history_modes).carried_map for world in worlds
    )
    transverse = tuple(
        candidate_type(world.candidate, model.response_types).response_table for world in worlds
    )
    prospective = tuple(
        ("ADDRESSABLE", world.exterior)
        if decoder_can_address(world, model)
        else ("INACCESSIBLE",)
        for world in worlds
    )

    generic = induced_cut_state(worlds, visible, (retrospective, transverse, prospective))
    semantic = semantic_induced_classes(
        routes,
        candidates,
        model,
        3,
        (HISTORY, MECHANISM, FUTURE),
    )

    assert _as_block_set(generic) == _as_block_set(semantic)
    assert len(generic) == 11  # (N-k)+k*2^m = 3 + 8
