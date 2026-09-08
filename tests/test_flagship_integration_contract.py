from __future__ import annotations

import json
from math import log2
from pathlib import Path

import pytest

from crest.compositional_temporal_game import compositional_temporal_summary
from crest.conditioned_temporal_bridges import paired_bridge_summary
from crest.joint_debt import marked_cycle_report
from crest.temporal_interaction import temporal_three_way_closed_form

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"


def test_flagship_headline_is_literal_compositional_temporal_interaction() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 8
    assert manifest["canonical_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.5_compositional.md"
    )
    assert manifest["previous_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.4_positioned.md"
    )
    assert (ROOT / manifest["canonical_flagship_manuscript"]).is_file()
    assert manifest["canonical_title"] == (
        "Ecological State at a Temporal Cut: Compositional Interaction Across Time"
    )
    assert "pure compositional three-way" in manifest["headline"]
    assert "v_m(S)" in manifest["headline_quantity"]
    assert "zero pairwise" in manifest["headline_temporal_result"]
    assert "m(H,Theta,F) = m" in manifest["headline_temporal_extremum"]
    assert "literal conditioned cross-contract" in manifest["novelty_boundary"]


def test_flagship_temporal_geometry_uses_non_circular_companion_primitives() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    geometry = manifest["temporal_geometry"]
    assert "cut O_t" in geometry["present"]
    assert "immutable" in geometry["past"]
    assert "primitive candidate law" in geometry["latent_present"]
    assert "query grammar" in geometry["future"]

    boundaries = manifest["strict_realizability_boundaries"]
    assert "cannot have positive interaction" in boundaries["fixed_partition_bound"]
    assert "preserve MLTR history" in boundaries["immutable_history_no_activation"]
    assert "singleton" in boundaries["fixed_grammar_mrm_zero_debt"]
    assert "abstract fixed-closure" in boundaries["interpretation"]


def test_flagship_submission_constraints_are_pinned() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    constraints = manifest["submission_constraints"]
    assert constraints["abstract_word_limit"] == 200
    assert constraints["keyword_max"] == 6
    assert constraints["current_abstract_words"] <= constraints["abstract_word_limit"]
    assert constraints["current_keywords"] <= constraints["keyword_max"]
    assert constraints["current_title_words"] == 10

    literature = manifest["literature_positioning"]
    for key in (
        "ecological_memory",
        "hysteresis_and_state_shifts",
        "transient_ecology",
        "causal_predictive_states",
        "predictive_state_representations",
        "bisimulation_and_state_abstraction",
    ):
        assert literature[key]


def test_literal_pairwise_bridge_matches_manifest() -> None:
    bridge = paired_bridge_summary(10)
    assert bridge["history_closed_classes"] == 1
    assert bridge["history_open_classes"] == 1024
    assert bridge["history_inflation_bits"] == pytest.approx(10.0)
    assert bridge["mechanism_closed_response_types"] == 1
    assert bridge["mechanism_open_response_types"] == 1024
    assert bridge["mechanism_inflation_bits"] == pytest.approx(10.0)


def test_literal_three_way_anchor_matches_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    anchor = manifest["numeric_closure"]
    assert anchor["anchor_m"] == 10

    summary = compositional_temporal_summary(anchor["anchor_m"])
    assert summary.history_mechanism_classes == 4
    assert summary.joint_classes == 4096
    assert summary.history_mechanism_bits == 2
    assert summary.joint_bits == 12
    assert summary.interaction_bits == 10
    assert summary.three_way_bits == 10
    assert summary.state_count_amplification == 1024
    assert summary.three_way_fraction_of_joint == pytest.approx(10 / 12)
    assert anchor["pairwise_interaction_bits"] == 0
    assert anchor["three_way_share_of_interaction"] == pytest.approx(1.0)


def test_old_fixed_closure_extrema_remain_supporting_results_only() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    supporting = "\n".join(manifest["supporting_results"])
    assert "abstract fixed-closure marked-cycle" in supporting
    assert "abstract fixed-closure three-audit" in supporting

    for n in (2, 3, 4, 8, 17, 32):
        report = marked_cycle_report(n)
        assert report.individual_debts == pytest.approx((1.0, 0.0))
        assert report.joint_debt == pytest.approx(log2(n))
        assert report.delta == pytest.approx(log2(n) - 1.0)

    old = temporal_three_way_closed_form(10)
    assert old["joint_blocks"] == 1024
    assert old["three_way_bits"] == pytest.approx(8.415037499278844)
