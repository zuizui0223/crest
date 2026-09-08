from __future__ import annotations

from crest.semantic_access import (
    SemanticWorld,
    canonical_nontrivial_companion_model,
    decoder_can_address,
    semantic_trace,
)


def test_companion_outputs_reduce_three_primitives_to_two_exact_classes() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()

    assert len(routes) == 3
    assert len(model.history_modes) == 2
    assert sorted(len(mode.routes) for mode in model.history_modes) == [1, 2]
    assert {mode.carried_map for mode in model.history_modes} == {(0, 1, 0), (1, 0, 1)}

    assert len(candidates) == 3
    assert len(model.response_types) == 2
    assert sorted(len(kind.candidates) for kind in model.response_types) == [1, 2]
    assert {kind.response_table for kind in model.response_types} == {
        (0, 0, 1, 1),
        (1, 0, 1, 0),
    }


def test_access_depends_on_semantics_not_route_or_candidate_identity() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    exterior = (1, 0, 1)

    # route_a and route_b are different raw histories but carry the same completed map.
    w_a = SemanticWorld(routes[0], candidates[2], exterior)
    w_b = SemanticWorld(routes[1], candidates[2], exterior)
    assert decoder_can_address(w_a, model) is False
    assert decoder_can_address(w_b, model) is False

    # candidate_a and candidate_b are distinct primitive laws but response-equivalent.
    w_c_a = SemanticWorld(routes[2], candidates[0], exterior)
    w_c_b = SemanticWorld(routes[2], candidates[1], exterior)
    assert decoder_can_address(w_c_a, model) is False
    assert decoder_can_address(w_c_b, model) is False

    # Only the distinct carried-map class crossed with the distinct response type is addressable.
    w_open = SemanticWorld(routes[2], candidates[2], exterior)
    assert decoder_can_address(w_open, model) is True
    assert tuple(semantic_trace(w_open, model, i) for i in range(3)) == exterior


def test_changing_carried_semantic_mode_changes_access_without_changing_raw_axis_count() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    exterior = (1, 1)

    shared_map_route = SemanticWorld(routes[0], candidates[2], exterior)
    distinct_map_route = SemanticWorld(routes[2], candidates[2], exterior)

    assert semantic_trace(shared_map_route, model, 0) is None
    assert semantic_trace(distinct_map_route, model, 0) == 1


def test_changing_candidate_safe_type_changes_access_at_fixed_history_mode() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    exterior = (0, 1)

    response_equivalent_candidate = SemanticWorld(routes[2], candidates[0], exterior)
    distinct_response_candidate = SemanticWorld(routes[2], candidates[2], exterior)

    assert semantic_trace(response_equivalent_candidate, model, 1) is None
    assert semantic_trace(distinct_response_candidate, model, 1) == 1
