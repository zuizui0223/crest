from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "crest_canonical_scope_2026-08-24.md").read_text(encoding="utf-8")


def test_ecology_first_manuscript_spine_is_explicit() -> None:
    for phrase in (
        "ecological problem → philosophical/formal analysis → finite theorem → conservation consequence",
        "conservation capacity can outgrow conservation knowledge",
        "shallow-lake restoration",
        "capability–resolution divergence",
    ):
        assert phrase in DOC


def test_empirical_validation_is_outside_manuscript_spine_but_worked_case_is_allowed() -> None:
    plain_text = DOC.replace("**", "")
    assert "not an empirical validation paper" in plain_text
    assert "ecology-grounded worked case" in DOC
    assert "not empirical validation of the capability–resolution theorem" in DOC
    assert "Izu/Campanula field validation" in DOC


def test_mathematical_headline_is_preserved() -> None:
    assert "\\Delta|K^*|=1" in DOC
    assert "\\Delta K_{U_0}=m" in DOC
    assert "no finite function" in DOC


def test_contract_well_posedness_is_explicit() -> None:
    for phrase in (
        "Independent responsibility",
        "Non-vacuous domain",
        "Response testability",
        "Evidence accountability",
    ):
        assert phrase in DOC


def test_conservation_projection_is_theoretical_not_validation() -> None:
    assert "new conservation capability" in DOC
    assert "state adequacy must be re-audited" in DOC
    assert "successful target reporting does not imply full state identification" in DOC


def test_novelty_positioning_is_explicit() -> None:
    for phrase in (
        "purpose-relative model adequacy",
        "idealization and abstraction",
        "multiple realization",
        "predictive state representations",
        "state/action abstraction coupling",
    ):
        assert phrase in DOC
