import json
from pathlib import Path


REPORT = Path("artifacts/hotarubukuro_empirical_crest_replay_2026-08-22.json")


def load_report() -> dict:
    return json.loads(REPORT.read_text(encoding="utf-8"))


def test_hotaru_replay_is_pinned_to_locked_source_results() -> None:
    report = load_report()
    assert report["source_repository"] == "zuizui0223/hotarubukuro"
    assert report["source_main_sha"] == "661321107ed47468a48e3be32a3461ebb5ca99a5"
    assert report["present_snapshot"]["cell_geometry"] == {
        "n_cells": 1305,
        "n_pigmented": 674,
        "n_white": 631,
    }


def test_binary_snapshot_is_useful_but_not_universally_adequate() -> None:
    report = load_report()
    broad = report["contracts"]["broad_environmental_differentiation"]
    human = report["contracts"]["human_context_within_pigmented"]
    outputs = report["crest_outputs"]

    assert broad["state_posterior_predictive_p"] < 0.05
    assert broad["conditional_intensity_posterior_predictive_p"] > 0.05

    assert human["relative_isolation_rho_pigmented_5km"] > human["relative_isolation_rho_white_5km"]
    assert human["pigmented_relative_natural_map_upper_tail_p"] < 0.01
    assert human["pigmented_relative_count_conditioned_upper_tail_p"] < 0.01
    assert human["direct_relative_colour_contrast_upper_tail_p"] > 0.05

    assert outputs["binary_snapshot_useful_for_broad_state_target"] is True
    assert outputs["binary_snapshot_universally_adequate_across_targets"] is False
    assert outputs["within_pigmented_context_axis_required_for_human_context_target"] is True


def test_mechanism_and_provenance_claims_remain_unlicensed() -> None:
    report = load_report()
    bombus = report["contracts"]["local_bombus_mechanism"]
    outputs = report["crest_outputs"]

    # The nominal 5-km mean is not enough to license a deterministic mechanism:
    # multiplicity-adjusted support and the raw-support sensitivity do not pass 0.05,
    # while the median and sign proportion do not show a pervasive positive effect.
    assert bombus["bh_q"] > 0.05
    assert bombus["raw_support_sensitivity_p"] > 0.05
    assert bombus["median_pigmented_minus_white_support"] <= 0
    assert 0.45 <= bombus["proportion_positive"] <= 0.55

    assert outputs["pollinator_mediated_selection_identified"] is False
    assert outputs["horticultural_or_human_origin_identified"] is False
    assert outputs["human_context_overlay_reportable"] is True


def test_required_identified_and_reportable_outputs_are_not_collapsed() -> None:
    outputs = load_report()["crest_outputs"]
    assert outputs["required_state_equals_identified_state"] is False
    assert outputs["identified_state_equals_reportable_target"] is False
