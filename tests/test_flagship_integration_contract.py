from __future__ import annotations

import json
from math import log2
from pathlib import Path

import pytest

from crest.explicit_temporal_grammar import (
    FUTURE,
    HISTORY,
    MECHANISM,
    DecoderRule,
    coalition_table,
    exclusive_joint_addressability,
    mobius_three_way,
)
from crest.joint_debt import marked_cycle_report
from crest.temporal_interaction import temporal_three_way_closed_form

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"


def test_flagship_headline_is_addressability_characterization() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 9
    assert manifest["canonical_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.6_addressability.md"
    )
    assert manifest["previous_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.5_compositional.md"
    )
    assert (ROOT / manifest["canonical_flagship_manuscript"]).is_file()
    assert manifest["canonical_title"] == (
        "Ecological State at a Temporal Cut: Interface-Dependent Interaction"
    )
    assert "prerequisite" in manifest["headline"]
    assert "explicit grammar traces" in manifest["headline_quantity"]
    assert "minimal prerequisite set R" in manifest["headline_theorem"]
    assert "R={H,Theta}" in manifest["headline_special_case"]


def test_flagship_temporal_geometry_and_realizability_boundaries() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    geometry = manifest["temporal_geometry"]
    assert "cut O_t" in geometry["present"]
    assert "primitive and immutable" in geometry["past"]
    assert "primitive candidate law" in geometry["latent_present"]
    assert "query grammar" in geometry["future"]

    boundaries = manifest["realizability_boundaries"]
    assert "cannot generate positive interaction" in boundaries["fixed_partition_bound"]
    assert "preserving raw MLTR history" in boundaries["immutable_history_no_activation"]
    assert "singleton MRM response type" in boundaries["fixed_grammar_mrm_zero_debt"]


def test_flagship_submission_constraints_are_pinned() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    constraints = manifest["submission_constraints"]
    assert constraints["abstract_word_limit"] == 200
    assert constraints["keyword_max"] == 6
    assert constraints["current_abstract_words"] <= constraints["abstract_word_limit"]
    assert constraints["current_keywords"] <= constraints["keyword_max"]
    assert constraints["current_title_words"] == 8

    for value in manifest["literature_positioning"].values():
        assert value


def test_explicit_grammar_numeric_anchor_matches_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    anchor = manifest["numeric_illustration"]
    m = anchor["anchor_m"]
    rule = DecoderRule(frozenset((HISTORY, MECHANISM)))
    table = coalition_table(m, rule)

    assert table[frozenset((HISTORY, MECHANISM))] == pytest.approx(2.0)
    assert table[frozenset((HISTORY, MECHANISM, FUTURE))] == pytest.approx(12.0)
    assert mobius_three_way(m, rule) == pytest.approx(anchor["genuine_three_way_bits"])
    assert exclusive_joint_addressability(m, rule)
    assert anchor["joint_classes"] == 4096
    assert anchor["state_count_amplification_from_history_mechanism"] == 1024


def test_decoder_requirement_classification_is_falsifiable() -> None:
    m = 7
    no_requirement = DecoderRule(frozenset())
    h_only = DecoderRule(frozenset((HISTORY,)))
    theta_only = DecoderRule(frozenset((MECHANISM,)))
    both = DecoderRule(frozenset((HISTORY, MECHANISM)))

    assert mobius_three_way(m, no_requirement) == pytest.approx(0.0)
    assert mobius_three_way(m, h_only) == pytest.approx(0.0)
    assert mobius_three_way(m, theta_only) == pytest.approx(0.0)
    assert mobius_three_way(m, both) == pytest.approx(m)

    table = coalition_table(m, no_requirement)
    assert table[frozenset((FUTURE,))] == pytest.approx(m)


def test_old_fixed_closure_extrema_remain_supporting_results_only() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    supporting = "\n".join(manifest["supporting_results"])
    assert "abstract fixed-closure marked-cycle" in supporting
    assert "abstract fixed-closure b-log2(3)" in supporting

    for n in (2, 3, 4, 8, 17, 32):
        report = marked_cycle_report(n)
        assert report.individual_debts == pytest.approx((1.0, 0.0))
        assert report.joint_debt == pytest.approx(log2(n))
        assert report.delta == pytest.approx(log2(n) - 1.0)

    old = temporal_three_way_closed_form(10)
    assert old["joint_blocks"] == 1024
    assert old["three_way_bits"] == pytest.approx(8.415037499278844)
