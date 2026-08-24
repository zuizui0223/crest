from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "docs" / "izu_campanula_snapshot_sufficiency_validation_2026-08-24.md").read_text(encoding="utf-8")


def test_historical_sources_and_oshima_exception_are_recorded() -> None:
    for term in (
        "10.1111/j.1442-1984.1986.tb00018.x",
        "10.1111/j.1442-1984.1988.tb00178.x",
        "Oshima",
    ):
        assert term in DOC
    assert "bumblebees were absent from the izu islands except oshima" in DOC.lower()


def test_existing_izu_core_channels_define_future_grammar() -> None:
    for term in (
        "ambient/open",
        "bagged autonomous",
        "supplemental outcross",
        "visitor-group SVD",
        "zero-visit windows",
    ):
        assert term in DOC


def test_multiple_snapshot_candidates_are_compared() -> None:
    for term in (
        "Q0 — island label only",
        "Q1 — morphology snapshot",
        "Q2 — morphology + current ambient performance",
        "M0",
        "M4",
    ):
        assert term in DOC


def test_snapshot_failure_is_defined_as_response_disagreement() -> None:
    assert "q_{\\rm snapshot}(\\omega)=q_{\\rm snapshot}(\\omega')" in DOC
    assert "R_{\\rm Izu}(\\omega)\\neq R_{\\rm Izu}(\\omega')" in DOC
    assert "same current reproductive output" in DOC
    assert "same reproductive state" in DOC


def test_measurement_admission_and_claim_firewalls_remain() -> None:
    for term in (
        "does not prove historical bumblebee loss caused the difference",
        "SVD requires no-visit/background controls",
        "parentage remains optional",
        "does not relax any biological measurement requirement",
        "It would not refute CREST as mathematics",
    ):
        assert term in DOC


def test_falsification_condition_allows_snapshot_sufficiency() -> None:
    assert "support snapshot sufficiency for this particular scientific contract" in DOC
    assert "CREST explicitly allows snapshot sufficiency to hold" in DOC
