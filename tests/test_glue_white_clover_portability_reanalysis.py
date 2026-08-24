from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "docs" / "glue_white_clover_portability_reanalysis_2026-08-24.md").read_text(encoding="utf-8")


def test_glue_reanalysis_records_bidirectional_city_clines() -> None:
    for term in (
        "Albuquerque | -0.839",
        "Amsterdam | +0.800",
        "Beijing | -1.668",
        "Toronto | +1.463",
        "Uppsala | -1.704",
    ):
        assert term in DOC
    assert "response direction itself reverses" in DOC


def test_glue_reanalysis_records_environment_context_selection() -> None:
    for term in (
        "annualPET slope × summerNDVI mean | 100",
        "annualPET slope × GMIS mean | 94",
        "winterNDVI mean | 94",
        "NDSI mean | 91",
        "summerNDVI slope × annualAI mean | 91",
    ):
        assert term in DOC


def test_glue_reanalysis_keeps_empirical_claim_firewall() -> None:
    assert "urban-only quotient is demonstrably too coarse" in DOC
    assert "substantial city-to-city response variation remains unresolved" in DOC
    assert "unique minimal adequate state" in DOC
    assert "Not yet established" in DOC
    assert "not evidence for the mathematical correctness of J1" in DOC


def test_glue_next_validation_is_explicitly_predictive() -> None:
    assert "M0: city cline ~ one global urbanization law" in DOC
    assert "M1: city cline ~ environmental means/slopes and interactions" in DOC
    assert "Primary metric: out-of-city RMSE" in DOC
