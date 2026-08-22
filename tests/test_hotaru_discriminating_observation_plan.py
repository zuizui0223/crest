import json
from pathlib import Path


PLAN = Path("artifacts/hotarubukuro_discriminating_observation_plan_2026-08-22.json")


def load_plan() -> dict:
    return json.loads(PLAN.read_text(encoding="utf-8"))


def test_bombus_claim_escalation_requires_new_causal_channels() -> None:
    branch = load_plan()["branches"]["bombus"]
    assert branch["immediate_priority"] == ["B1", "B2"]
    assert set(branch["selection_claim_requires"]) == {"B2", "B3", "B4"}
    assert "more_species_distribution_model_replication_implies_pollination_effectiveness" in branch["forbidden_shortcuts"]
    channels = {row["id"]: row["channel"] for row in branch["steps"]}
    assert channels["B2"] == "single_visit_conspecific_pollen_deposition"
    assert channels["B4"] == "colour_causal_intervention_or_equivalent"


def test_human_provenance_claim_does_not_collapse_context_to_origin() -> None:
    branch = load_plan()["branches"]["human_provenance"]
    assert branch["immediate_priority"] == ["H2", "H3"]
    assert set(branch["human_establishment_claim_requires"]) == {"H2", "H3"}
    assert "genetic_assignment_alone_implies_intentional_planting" in branch["forbidden_shortcuts"]
    channels = {row["id"]: row["channel"] for row in branch["steps"]}
    assert channels["H2"] == "dated_occurrence_and_historical_provenance"
    assert channels["H3"] == "reference_aware_population_genetic_assignment"


def test_plan_is_prospective_not_an_empirical_result() -> None:
    plan = load_plan()
    assert plan["status"] == "prospective_evidence_design"
    assert "does not estimate" in plan["claim_ceiling"]
