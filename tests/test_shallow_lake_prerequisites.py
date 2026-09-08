from crest.shallow_lake_prerequisites import (
    HISTORY,
    LAKE_WORLDS,
    MECHANISM,
    canonical_target_prerequisites,
    composed_restoration_policy_target,
    counterfactual_substitution_changes_target,
    current_status_target,
    legacy_sensitive_recovery_target,
    mechanism_specific_intervention_target,
)


def test_target_relative_prerequisites_are_executable() -> None:
    expected = {
        "current_status": (frozenset(),),
        "legacy_sensitive_recovery": (frozenset({HISTORY}),),
        "mechanism_specific_intervention": (frozenset({MECHANISM}),),
        "composed_restoration_policy": (frozenset({HISTORY, MECHANISM}),),
    }
    assert canonical_target_prerequisites() == expected


def test_current_status_is_invariant_to_both_counterfactual_substitutions() -> None:
    for world in LAKE_WORLDS:
        assert not counterfactual_substitution_changes_target(current_status_target, world, HISTORY)
        assert not counterfactual_substitution_changes_target(current_status_target, world, MECHANISM)


def test_legacy_target_changes_only_under_history_substitution() -> None:
    for world in LAKE_WORLDS:
        assert counterfactual_substitution_changes_target(legacy_sensitive_recovery_target, world, HISTORY)
        assert not counterfactual_substitution_changes_target(legacy_sensitive_recovery_target, world, MECHANISM)


def test_mechanism_target_changes_only_under_response_type_substitution() -> None:
    for world in LAKE_WORLDS:
        assert not counterfactual_substitution_changes_target(mechanism_specific_intervention_target, world, HISTORY)
        assert counterfactual_substitution_changes_target(mechanism_specific_intervention_target, world, MECHANISM)


def test_composed_target_requires_both_interfaces_by_counterfactual_substitution() -> None:
    for world in LAKE_WORLDS:
        assert counterfactual_substitution_changes_target(composed_restoration_policy_target, world, HISTORY)
        assert counterfactual_substitution_changes_target(composed_restoration_policy_target, world, MECHANISM)
