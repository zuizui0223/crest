"""Finite transport between quotient states at different temporal cuts.

This module extends the fixed-cut theory without introducing a continuous-time
limit.  Let ``phi: Omega_t -> Omega_s`` be a declared deterministic map between
finite world carriers and let ``Q_t`` and ``Q_s`` be partitions representing
cut states.  A quotient-level transition exists exactly when ``phi`` is
constant modulo ``Q_s`` on every ``Q_t`` block:

    x ~_t y  =>  phi(x) ~_s phi(y).

Equivalently, ``Q_t`` refines the pullback of ``Q_s`` along ``phi``.  Under this
condition there is a unique induced map ``bar(phi): Q_t -> Q_s`` satisfying
``bar(phi)([x]_t) = [phi(x)]_s``.  Identity and composition descend, so compatible
finite world evolutions act functorially on quotient states.

No stochastic, multivalued, continuous-time, or cardinality-monotonicity claim
is made here.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence

from crest.cut_state_quotient import Partition, validate_partition


def _validated_world_map(
    source_worlds: Sequence[Hashable],
    target_worlds: Sequence[Hashable],
    world_map: Mapping[Hashable, Hashable],
) -> dict[Hashable, Hashable]:
    source = tuple(source_worlds)
    target = tuple(target_worlds)
    if set(world_map) != set(source):
        raise ValueError("world map must be defined on every source world exactly once")
    target_set = set(target)
    mapped = dict(world_map)
    if any(value not in target_set for value in mapped.values()):
        raise ValueError("world map values must lie in the target carrier")
    return mapped


def _block_lookup(partition: Partition) -> dict[Hashable, frozenset[Hashable]]:
    return {world: block for block in partition for world in block}


def transition_respects_state(
    source_worlds: Sequence[Hashable],
    target_worlds: Sequence[Hashable],
    source_partition: Partition,
    target_partition: Partition,
    world_map: Mapping[Hashable, Hashable],
) -> bool:
    """Return whether a world map descends to the supplied quotient states."""

    source_state = validate_partition(source_worlds, source_partition)
    target_state = validate_partition(target_worlds, target_partition)
    mapped = _validated_world_map(source_worlds, target_worlds, world_map)
    target_lookup = _block_lookup(target_state)

    for block in source_state:
        image_blocks = {target_lookup[mapped[world]] for world in block}
        if len(image_blocks) != 1:
            return False
    return True


def induced_state_transition(
    source_worlds: Sequence[Hashable],
    target_worlds: Sequence[Hashable],
    source_partition: Partition,
    target_partition: Partition,
    world_map: Mapping[Hashable, Hashable],
) -> dict[frozenset[Hashable], frozenset[Hashable]]:
    """Return the unique quotient map induced by a compatible world map.

    Raises ``ValueError`` when the world evolution identifies one source state
    block with more than one target state block, because then no well-defined
    quotient-level transition exists.
    """

    source_state = validate_partition(source_worlds, source_partition)
    target_state = validate_partition(target_worlds, target_partition)
    mapped = _validated_world_map(source_worlds, target_worlds, world_map)
    target_lookup = _block_lookup(target_state)

    result: dict[frozenset[Hashable], frozenset[Hashable]] = {}
    for block in source_state:
        image_blocks = {target_lookup[mapped[world]] for world in block}
        if len(image_blocks) != 1:
            raise ValueError("world map does not descend to a well-defined state transition")
        result[block] = next(iter(image_blocks))
    return result


def identity_world_map(worlds: Sequence[Hashable]) -> dict[Hashable, Hashable]:
    """Return the identity map on a finite carrier."""

    return {world: world for world in worlds}


def compose_world_maps(
    first: Mapping[Hashable, Hashable],
    second: Mapping[Hashable, Hashable],
) -> dict[Hashable, Hashable]:
    """Return ``second o first`` after checking composability on the image."""

    if any(value not in second for value in first.values()):
        raise ValueError("world maps are not composable on the image of the first map")
    return {world: second[mid] for world, mid in first.items()}


def compose_state_transitions(
    first: Mapping[frozenset[Hashable], frozenset[Hashable]],
    second: Mapping[frozenset[Hashable], frozenset[Hashable]],
) -> dict[frozenset[Hashable], frozenset[Hashable]]:
    """Return quotient-map composition ``second o first``."""

    if any(block not in second for block in first.values()):
        raise ValueError("state transitions are not composable")
    return {block: second[mid] for block, mid in first.items()}


__all__ = [
    "compose_state_transitions",
    "compose_world_maps",
    "identity_world_map",
    "induced_state_transition",
    "transition_respects_state",
]
