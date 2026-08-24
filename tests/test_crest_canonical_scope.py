from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "manuscript" / "crest_canonical_scope_2026-08-24.md").read_text(encoding="utf-8")


def test_three_stage_manuscript_spine_is_explicit() -> None:
    assert "philosophy → finite mathematics → ecological projection" in DOC
    assert "PHILOSOPHY" in DOC
    assert "MATHEMATICS" in DOC
    assert "ECOLOGY" in DOC


def test_empirical_validation_is_outside_manuscript_spine() -> None:
    assert "not an empirical validation paper" in DOC
    assert "Izu/Campanula empirical validation" in DOC
    assert "restoration/conservation case-study validation" in DOC
    assert "do not add" in DOC.lower()


def test_mathematical_headline_is_preserved() -> None:
    assert "\\Delta|K^*|=1" in DOC
    assert "\\Delta K_{U_0}=m" in DOC
    assert "no finite function" in DOC


def test_ecological_projection_is_conceptual_not_case_based() -> None:
    assert "Ecological projection — not empirical validation" in DOC
    assert "current functional equivalence" in DOC
    assert "future causal equivalence" in DOC
    assert "representational stability" in DOC


def test_novelty_firewall_is_explicit() -> None:
    for phrase in (
        "history dependence",
        "ecological memory",
        "adaptive monitoring",
        "predictive states",
        "purpose-relative model adequacy",
        "causal abstraction",
    ):
        assert phrase in DOC
