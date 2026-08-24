import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = json.loads((ROOT / "data" / "restoration_conservation_crest_motif_registry.json").read_text(encoding="utf-8"))


def test_registry_uses_six_common_crest_criteria() -> None:
    assert REGISTRY["motif_criteria"] == [
        "capability_change",
        "feasible_future_expansion",
        "previously_ignorable_distinction_becomes_response_relevant",
        "response_divergence_within_old_coarse_state",
        "old_or_coarse_monitoring_can_be_insufficient",
        "coarse_management_target_can_remain_reportable",
    ]


def test_three_cases_meet_full_motif_and_fire_is_partial_replication() -> None:
    statuses = {case["id"]: case["motif_status"] for case in REGISTRY["cases"]}
    assert sum(status == "full" for status in statuses.values()) == 3
    assert statuses["R4_prescribed_fire_reintroduction"] == "strong_partial_replication"
    assert REGISTRY["summary"]["full_motif_cases"] == 3
    assert REGISTRY["summary"]["strong_partial_replications"] == 1


def test_full_motif_cases_satisfy_all_six_boolean_criteria() -> None:
    criteria = REGISTRY["motif_criteria"]
    for case in REGISTRY["cases"]:
        if case["motif_status"] == "full":
            assert all(case[key] is True for key in criteria)


def test_partial_replication_explains_what_is_not_integrated() -> None:
    fire = next(case for case in REGISTRY["cases"] if case["id"] == "R4_prescribed_fire_reintroduction")
    assert "assembled across studies" in fire["partial_reason"]
    assert "one integrated monitoring experiment" in fire["partial_reason"]


def test_empirical_registry_keeps_finite_theorem_firewall() -> None:
    assert "does not" in REGISTRY["summary"]["theorem_firewall"].lower() or "no empirical" in REGISTRY["summary"]["theorem_firewall"].lower()
    assert "arbitrary-m" in REGISTRY["summary"]["theorem_firewall"]
