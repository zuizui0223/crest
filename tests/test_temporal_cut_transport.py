from __future__ import annotations

from itertools import product

import pytest

from crest.temporal_cut_transport import (
    compose_state_transitions,
    compose_world_maps,
    identity_world_map,
    induced_state_transition,
    transition_respects_state,
)


def test_transport_exists_exactly_when_source_classes_have_single_target_class() -> None:
    source = ("a", "b", "c", "d")
    target = ("x", "y", "z")
    source_state = (frozenset({"a", "b"}), frozenset({"c"}), frozenset({"d"}))
    target_state = (frozenset({"x", "y"}), frozenset({"z"}))

    for images in product(target, repeat=len(source)):
        world_map = dict(zip(source, images))
        expected = (
            ({world_map["a"], world_map["b"]} <= {"x", "y"})
            or (world_map["a"] == world_map["b"] == "z")
        )
        assert transition_respects_state(
            source, target, source_state, target_state, world_map
        ) is expected
        if expected:
            quotient_map = induced_state_transition(
                source, target, source_state, target_state, world_map
            )
            assert len(quotient_map) == len(source_state)
        else:
            with pytest.raises(ValueError, match="does not descend"):
                induced_state_transition(
                    source, target, source_state, target_state, world_map
                )


def test_identity_world_evolution_descends_to_identity_state_transition() -> None:
    worlds = (0, 1, 2, 3)
    state = (frozenset({0, 1}), frozenset({2}), frozenset({3}))
    induced = induced_state_transition(
        worlds, worlds, state, state, identity_world_map(worlds)
    )
    assert induced == {block: block for block in state}


def test_compatible_composition_descends_functorially() -> None:
    omega0 = ("a", "b", "c", "d")
    omega1 = ("u", "v", "w")
    omega2 = ("p", "q")

    q0 = (frozenset({"a", "b"}), frozenset({"c"}), frozenset({"d"}))
    q1 = (frozenset({"u", "v"}), frozenset({"w"}))
    q2 = (frozenset({"p"}), frozenset({"q"}))

    phi = {"a": "u", "b": "v", "c": "w", "d": "w"}
    psi = {"u": "p", "v": "p", "w": "q"}
    composite = compose_world_maps(phi, psi)

    bar_phi = induced_state_transition(omega0, omega1, q0, q1, phi)
    bar_psi = induced_state_transition(omega1, omega2, q1, q2, psi)
    bar_composite = induced_state_transition(omega0, omega2, q0, q2, composite)

    assert bar_composite == compose_state_transitions(bar_phi, bar_psi)


def test_transport_failure_is_a_real_obstruction_not_an_exception_to_hide() -> None:
    source = ("a", "b")
    target = ("x", "y")
    source_state = (frozenset({"a", "b"}),)
    target_state = (frozenset({"x"}), frozenset({"y"}))
    world_map = {"a": "x", "b": "y"}

    assert not transition_respects_state(
        source, target, source_state, target_state, world_map
    )
    with pytest.raises(ValueError, match="does not descend"):
        induced_state_transition(
            source, target, source_state, target_state, world_map
        )


def test_world_map_validation_rejects_partial_or_out_of_carrier_maps() -> None:
    source = (1, 2)
    target = (3, 4)
    state_source = (frozenset({1}), frozenset({2}))
    state_target = (frozenset({3}), frozenset({4}))

    with pytest.raises(ValueError, match="every source world"):
        transition_respects_state(
            source, target, state_source, state_target, {1: 3}
        )
    with pytest.raises(ValueError, match="target carrier"):
        transition_respects_state(
            source, target, state_source, state_target, {1: 3, 2: 9}
        )
