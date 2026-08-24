from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "docs" / "urban_pollinator_closure_reanalysis_2026-08-24.md").read_text(encoding="utf-8")


def test_three_independent_urban_pollinator_tests_are_present() -> None:
    for term in (
        "Test 1 — Geometric isolation does not certify causal closure",
        "Test 2 — One connection action does not have one mechanism-independent effect",
        "Test 3 — Habitat label is weaker than quality/network role for city-scale persistence",
    ):
        assert term in DOC


def test_primary_design_counts_are_locked() -> None:
    for term in (
        "four isolated urban green patches",
        "six artificial linear features",
        "30 m long",
        "seven plant species",
        "105 sampling sites",
        "six urban habitat types",
    ):
        assert term in DOC


def test_coarse_state_failures_are_explicit() -> None:
    for term in (
        "geometric isolation as a sufficient closure state",
        "pollinator-guild identity changes the response",
        "habitat identity itself was relatively weak compared with resource quality",
        "geometric state",
        "functional-connectivity state",
        "response-oriented state",
    ):
        assert term in DOC


def test_public_source_identifiers_are_recorded() -> None:
    for term in (
        "10.1016/j.actao.2024.103985",
        "10.1007/s00442-026-05899-1",
        "10.1016/j.biocon.2025.111680",
        "10.5281/zenodo.18059923",
    ):
        assert term in DOC


def test_empirical_claim_firewall_is_present() -> None:
    lower = DOC.lower()
    assert "do **not** prove the finite crest theorem" in lower
    assert "leaving the finite crest theorem untouched" in lower
    assert "does not establish the least crest quotient" in lower


def test_next_exact_analysis_is_preregistered() -> None:
    assert "M0 — label-only" in DOC
    assert "M1 — response-aware" in DOC
    assert "held-out-site or bootstrap removal prediction" in DOC
