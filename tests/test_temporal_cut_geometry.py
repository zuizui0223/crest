from itertools import combinations

from crest.semantic_access import canonical_nontrivial_companion_model
from crest.semantic_temporal_quotient import semantic_induced_classes
from crest.temporal_cut_geometry import (
    CUT_DIRECTIONS,
    PROSPECTIVE,
    RETROSPECTIVE,
    TRANSVERSE,
    TemporalCutObservation,
    induced_cut_state_classes,
    transverse_present_type,
)


def _normalized_partition(classes):
    return {
        frozenset((w.route.name, w.candidate.name, w.exterior) for w in block)
        for block in classes
    }


def test_present_cut_is_a_fiber_not_an_adequate_state() -> None:
    cut = TemporalCutObservation(
        (("w1", "same-now"), ("w2", "same-now"), ("w3", "other-now"))
    )
    assert cut.fiber("same-now") == frozenset(("w1", "w2"))
    assert cut.fiber("other-now") == frozenset(("w3",))


def test_transverse_present_is_mrm_response_type_inside_cut() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    from crest.semantic_temporal_quotient import semantic_worlds

    worlds = semantic_worlds(routes, candidates, bit_depth=1)
    values = {transverse_present_type(world, model) for world in worlds}
    assert values == {kind.response_table for kind in model.response_types}


def test_geometric_cut_quotient_is_exactly_existing_semantic_quotient() -> None:
    routes, candidates, model = canonical_nontrivial_companion_model()
    directions = (RETROSPECTIVE, TRANSVERSE, PROSPECTIVE)
    for size in range(4):
        for coalition in combinations(directions, size):
            geometric = induced_cut_state_classes(
                routes, candidates, model, 3, coalition
            )
            semantic = semantic_induced_classes(
                routes, candidates, model, 3, coalition
            )
            assert _normalized_partition(geometric) == _normalized_partition(semantic)


def test_direction_names_are_only_a_reinterpretation_of_existing_axes() -> None:
    assert CUT_DIRECTIONS == (RETROSPECTIVE, TRANSVERSE, PROSPECTIVE)
