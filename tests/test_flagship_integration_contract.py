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
    mobius_three_way,
)
from crest.joint_debt import marked_cycle_report
from crest.semantic_access import canonical_nontrivial_companion_model
from crest.semantic_temporal_quotient import (
    semantic_pair_counts,
    semantic_quotient_size,
    semantic_three_way_dividend,
)
from crest.shallow_lake_prerequisites import (
    LAKE_WORLDS,
    canonical_target_prerequisites,
    composed_restoration_policy_target,
)
from crest.temporal_interaction import temporal_three_way_closed_form

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"


def test_flagship_headline_is_temporal_boundary_state_theory() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 12
    assert manifest["canonical_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.7_semantic_access.md"
    )
    assert manifest["previous_flagship_manuscript"] == (
        "manuscript/crest_flagship_amnat_v0.6_addressability.md"
    )
    assert (ROOT / manifest["canonical_flagship_manuscript"]).is_file()
    assert manifest["canonical_title"] == (
        "Ecological State at a Temporal Cut: Sparse Semantic Access"
    )
    assert "cut geometry" in manifest["headline"]
    assert "Shannon" in manifest["headline_quantity"]
    assert "Hartley" in manifest["headline_quantity"]
    assert "unique coarsest quotient" in manifest["theory_contribution"]
    assert "representation invariance" in manifest["theory_contribution"]
    assert "partition-refinement interval" in manifest["theory_contribution"]
    assert "transport between cuts by quotient descent" in manifest["theory_contribution"]
    assert "Shannon prerequisite-support fidelity" in manifest["theory_contribution"]
    assert "does not claim novelty" in manifest["novelty_boundary"]
    assert "epsilon-to-zero" in manifest["novelty_boundary"]
    assert "modeling_contribution" not in manifest

    geometry = manifest["temporal_boundary_geometry"]
    assert "zero-duration observational cut" in geometry["present"]
    assert geometry["visible_fiber"] == "L_t(y)=O_t^{-1}(y)"
    assert "not complete ontic mechanism identity" in geometry["transverse"]
    assert "present response capacity" in geometry["prospective"]
    assert "no shrinking-window epsilon-to-zero" in geometry["continuous_time_boundary"]

    order_split = manifest["information_order_split"]
    assert order_split["structural_order"] == "Shannon q=1"
    assert order_split["support_count_order"] == "Hartley q=0"
    assert "prerequisite hyperedges" in order_split["structural_interpretation"]
    assert "must not be read as prerequisite topology" in order_split["support_count_interpretation"]
    assert "non-Shannon zero interaction" in order_split["non_shannon_boundary"]

    invariance = manifest["representation_invariance"]
    assert "mutually factors through" in invariance["criterion"]
    assert "leaves the quotient unchanged" in invariance["redundancy_corollary"]
    assert "generated equivalence relation" in invariance["interpretation"]

    state_space = manifest["cut_state_space"]
    assert "representation-equivalence classes" in state_space["carrier"]
    assert "partitions refining the visible cut partition" in state_space["canonical_image"]
    assert "partition refinement" in state_space["order"]
    assert "every refinement of B_t is realizable" in state_space["realizability"]
    assert "nondecreasing" in state_space["complexity_monotonicity"]

    transport = manifest["temporal_cut_transport"]
    assert "source-equivalent worlds" in transport["criterion"]
    assert "unique" in transport["uniqueness"]
    assert "identity and composition descend" in transport["composition"]
    assert "multiple target state classes" in transport["obstruction"]
    assert "no temporal monotonicity" in transport["scope"]

    implementation = manifest["implementation"]
    assert implementation["least_cut_quotient_module"] == "crest/cut_state_quotient.py"
    assert implementation["renyi_access_module"] == "crest/renyi_access.py"
    assert implementation["prerequisite_support_module"] == "crest/prerequisite_access_game.py"
    assert implementation["renyi_leakage_module"] == "crest/prerequisite_renyi_leakage.py"
    assert implementation["overlap_balance_module"] == "crest/prerequisite_overlap_balance.py"
    assert implementation["least_cut_quotient_theorem"] == (
        "docs/crest_least_temporal_cut_quotient_theorem_2026-09-09.md"
    )
    assert implementation["signature_invariance_theorem"] == (
        "docs/crest_signature_family_invariance_theorem_2026-09-09.md"
    )
    assert implementation["cut_state_lattice_theorem"] == (
        "docs/crest_cut_state_partition_lattice_theorem_2026-09-09.md"
    )
    assert implementation["temporal_cut_transport_module"] == "crest/temporal_cut_transport.py"
    assert implementation["temporal_cut_transport_theorem"] == (
        "docs/crest_temporal_cut_transport_theorem_2026-09-09.md"
    )
    for key in (
        "least_cut_quotient_module",
        "least_cut_quotient_theorem",
        "signature_invariance_theorem",
        "cut_state_lattice_theorem",
        "temporal_cut_transport_module",
        "temporal_cut_transport_theorem",
        "renyi_access_module",
        "prerequisite_support_module",
        "renyi_leakage_module",
        "overlap_balance_module",
    ):
        assert (ROOT / implementation[key]).is_file()


def test_flagship_submission_constraints_are_pinned() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    constraints = manifest["submission_constraints"]
    assert constraints["abstract_word_limit"] == 200
    assert constraints["keyword_max"] == 6
    assert constraints["current_abstract_words"] <= constraints["abstract_word_limit"]
    assert constraints["current_abstract_words"] == 189
    assert constraints["current_keywords"] <= constraints["keyword_max"]
    assert constraints["current_title_words"] == 9
    assert constraints["current_main_text_words"] == 5265
    assert manifest["literature_positioning"]["resilience_and_present_response_capacity"] == "Walker et al. 2004"

    for value in manifest["literature_positioning"].values():
        assert value


def test_sparse_semantic_numeric_anchor_matches_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    anchor = manifest["canonical_numeric_witness"]
    routes, candidates, model = canonical_nontrivial_companion_model()
    m = anchor["anchor_m"]

    assert semantic_pair_counts(model) == (
        anchor["semantic_pairs"],
        anchor["addressable_pairs"],
    )
    assert semantic_quotient_size(
        routes, candidates, model, m, (HISTORY, MECHANISM, FUTURE)
    ) == anchor["grand_classes"]
    assert semantic_three_way_dividend(routes, candidates, model, m) == pytest.approx(
        anchor["hartley_three_way_bits"], abs=1e-9
    )
    assert anchor["grand_classes"] == 1027
    assert anchor["shannon_structural_three_way_bits"] == pytest.approx(2.5)
    assert anchor["hartley_three_way_bits"] == pytest.approx(8.004220466)
    assert anchor["asymptotic_sparsity_penalty_bits"] == 2
    assert "Shannon q=1" in manifest["sparse_semantic_access"]["interpretation"]
    assert "Hartley q=0" in manifest["sparse_semantic_access"]["interpretation"]


def test_shallow_lake_prerequisite_manifest_matches_executable_audit() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    audit = manifest["shallow_lake_prerequisite_audit"]
    observed = canonical_target_prerequisites()

    assert observed["current_status"] == (frozenset(),)
    assert observed["legacy_sensitive_recovery"] == (frozenset({HISTORY}),)
    assert observed["mechanism_specific_intervention"] == (frozenset({MECHANISM}),)
    assert observed["composed_restoration_policy"] == (
        frozenset({HISTORY, MECHANISM}),
    )
    assert audit["current_status"] == []
    assert audit["legacy_sensitive_recovery"] == ["H"]
    assert audit["mechanism_specific_intervention"] == ["THETA"]
    assert audit["composed_restoration_policy"] == ["H", "THETA"]

    outputs = {composed_restoration_policy_target(world) for world in LAKE_WORLDS}
    assert len(LAKE_WORLDS) == 4
    assert outputs == {"standard_pathway", "cross_interface_review"}
    assert audit["composed_target_output_cardinality"] == 2
    assert audit["single_interface_factorization"] is False
    assert "parity" in audit["literature_boundary"]
    assert "worked ecological interpretation" in audit["status"]
    assert (ROOT / "docs" / "shallow_lake_v07_prerequisite_identification_2026-09-08.md").is_file()


def test_v06_complete_access_is_retained_as_boundary_case() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    boundary = manifest["complete_access_boundary"]
    m = boundary["anchor_m"]
    rule = DecoderRule(frozenset((HISTORY, MECHANISM)))
    table = coalition_table(m, rule)

    assert table[frozenset((HISTORY, MECHANISM, FUTURE))] == pytest.approx(12.0)
    assert mobius_three_way(m, rule) == pytest.approx(boundary["three_way_bits"])
    assert boundary["grand_classes"] == 4096
    assert "boundary case" in boundary["status"]


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
