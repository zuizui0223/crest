from __future__ import annotations

import json
from math import log2
from pathlib import Path

import pytest

from crest.joint_debt import marked_cycle_report
from crest.sequential_witnesses import sharp_sequential_problem
from crest.temporal_interaction import temporal_three_way_closed_form

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"
SECTION = ROOT / "docs" / "flagship_integration" / "joint_debt_delta_section.md"
TEMPORAL_SECTION = ROOT / "docs" / "flagship_integration" / "temporal_cut_state_section.md"


def test_flagship_headline_is_temporal_cut_state_interaction() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 7
    assert manifest["canonical_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.4_positioned.md"
    )
    assert manifest["previous_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.3_temporal_cut.md"
    )
    assert (ROOT / manifest["canonical_flagship_manuscript"]).is_file()
    assert manifest["canonical_title"] == (
        "Ecological State at a Temporal Cut: Interaction Across Time"
    )
    assert manifest["headline"] == "interaction-generated ecological state at a temporal cut"
    assert manifest["headline_quantity"] == "Delta = D_joint - sum_i D_i"
    assert manifest["headline_extremum"] == "Delta = log2(n) - 1"
    assert "past-by-future interaction" in manifest["headline_temporal_result"]
    assert "b - log2(3)" in manifest["headline_temporal_extremum"]
    assert "prior substrate" in manifest["novelty_boundary"]
    assert any("H log2(r)" in item for item in manifest["supporting_results"])


def test_flagship_temporal_geometry_keeps_present_as_cut() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    geometry = manifest["temporal_geometry"]
    assert "cut O_t" in geometry["present"]
    assert "not a finite-width temporal axis" in geometry["present"]
    assert "left of the cut" in geometry["past"]
    assert "O_t^{-1}(y)" in geometry["latent_present"]
    assert "transverse to the cut" in geometry["latent_present"]
    assert "right of the cut" in geometry["future"]


def test_flagship_submission_constraints_are_pinned() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    constraints = manifest["submission_constraints"]
    assert constraints["abstract_word_limit"] == 200
    assert constraints["keyword_max"] == 6
    assert constraints["current_abstract_words"] <= constraints["abstract_word_limit"]
    assert constraints["current_keywords"] <= constraints["keyword_max"]
    assert constraints["current_title_words"] == 9

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


def test_flagship_section_preserves_claim_firewall() -> None:
    text = SECTION.read_text(encoding="utf-8")
    assert "integration-only quantity" in text
    assert "responsibility-wise additive accounting" in text
    assert "does not claim that phenomenon itself as novel" in text
    assert "carrier-gain no-bound" in text
    assert "H\\log_2 r" in text

    temporal = TEMPORAL_SECTION.read_text(encoding="utf-8")
    assert "temporal cut" in temporal
    assert "latent" in temporal
    assert "continuous-time" in temporal
    assert "statistical confounding" in temporal


def test_flagship_marked_cycle_matches_declared_extremum() -> None:
    for n in (2, 3, 4, 8, 17, 32):
        report = marked_cycle_report(n)
        assert report.individual_debts == pytest.approx((1.0, 0.0))
        assert report.joint_debt == pytest.approx(log2(n))
        assert report.delta == pytest.approx(log2(n) - 1.0)


def test_flagship_temporal_anchor_matches_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    anchor = manifest["numeric_closure"]
    assert anchor["temporal_anchor_b"] == 10

    closed = temporal_three_way_closed_form(anchor["temporal_anchor_b"])
    assert closed["joint_blocks"] == 1024
    assert closed["joint_debt_bits"] == pytest.approx(10.0)
    assert closed["interaction_bits"] == pytest.approx(9.0)
    assert closed["three_way_bits"] == pytest.approx(8.415037499278844)
    assert closed["three_way_fraction_of_joint"] == pytest.approx(
        0.8415037499278844
    )


def test_sharp_sequential_family_is_exposed_from_package_surface() -> None:
    old_problem, addresses, _ = sharp_sequential_problem(3, 2, False)
    new_problem, new_addresses, _ = sharp_sequential_problem(3, 2, True)
    assert addresses == new_addresses
    assert len(addresses) == 9
    assert old_problem.controllable_actions == ("hold",)
    assert new_problem.controllable_actions == ("hold", "probe")
