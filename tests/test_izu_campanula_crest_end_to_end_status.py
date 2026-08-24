import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads(
    (ROOT / "data" / "izu_campanula_crest_end_to_end_status.json").read_text(encoding="utf-8")
)


def test_declared_response_grammar_matches_prospective_crest_contract() -> None:
    assert REGISTRY["declared_response_grammar"] == [
        "ambient_open",
        "bagged_autonomous",
        "supplemental_outcross",
        "visitor_group_single_visit_pollen_deposition",
    ]


def test_end_to_end_chain_keeps_source_measurement_gate_upstream() -> None:
    gates = REGISTRY["end_to_end_gates"]
    assert gates["G0_source_measurement_admission"]["status"] == "blocked_field_collection"
    assert gates["G1_snapshot_merge_defined"]["status"] == "ready_protocol"
    assert gates["G2_response_disagreement_testable"]["status"] == "blocked_by_G0"
    assert gates["G3_snapshot_insufficiency_demonstrated"]["status"] == "unresolved"


def test_no_empirical_validation_is_promoted_before_field_admission() -> None:
    assert "designed but not yet open" in REGISTRY["current_conclusion"]
    assert REGISTRY["minimum_crest_validation"]["required_gates"] == [
        "G0_source_measurement_admission",
        "G1_snapshot_merge_defined",
        "G2_response_disagreement_testable",
        "G3_snapshot_insufficiency_demonstrated",
    ]


def test_claim_firewalls_block_historical_and_theorem_overreach() -> None:
    firewalls = "\n".join(REGISTRY["claim_firewalls"])
    assert "historical Bombus loss" in firewalls
    assert "does not prove the arbitrary-m finite theorem" in firewalls
    assert "subsamples, not independent n" in firewalls
    assert "separate izu-core repeated-final-estimand gate" in firewalls


def test_stronger_validation_preserves_state_evidence_target_separation() -> None:
    assert REGISTRY["minimum_crest_validation"]["stronger_validation_adds"] == [
        "G4_interpretable_refinement_repairs_disagreement",
        "G5_evidence_licenses_refined_state",
        "G6_coarse_target_retained",
    ]
