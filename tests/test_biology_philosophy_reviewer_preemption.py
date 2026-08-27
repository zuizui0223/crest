from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT = (ROOT / "docs" / "biology_philosophy_reviewer_preemption_2026-08-24.md").read_text(encoding="utf-8")
MANUSCRIPT = (ROOT / "manuscript" / "crest_biology_philosophy_blinded_submission.md").read_text(encoding="utf-8")


def test_novelty_is_not_generic_purpose_relativism() -> None:
    assert "purpose-relativity itself is not the novelty" in AUDIT
    assert "Predictive State Representations" in AUDIT
    assert "state/action abstraction coupling" in AUDIT


def test_quantitative_headline_is_preserved() -> None:
    assert "\\Delta |K^*|=1" in AUDIT
    assert "\\Delta K_{U_0}=m" in AUDIT
    assert "2^m" in MANUSCRIPT
    assert "no universal finite" in MANUSCRIPT


def test_artificial_witness_claim_ceiling() -> None:
    assert "counterexample to a universal upper bound" in AUDIT
    assert "Do not infer exponential growth in real ecosystems" in AUDIT


def test_conservation_implications_are_theoretical_not_validation() -> None:
    for phrase in (
        "Present similarity does not by itself establish management-relevant state equivalence",
        "Target achievement is not full-state identification",
        "When the management repertoire changes, the adequacy of the state variables should be re-audited",
    ):
        assert phrase in AUDIT
    assert "CREST provides a validated conservation monitoring protocol" in AUDIT


def test_manuscript_keeps_clear_state_question() -> None:
    manuscript_lower = MANUSCRIPT.lower()
    assert "when should different ecological worlds count as the same ecological state?" in manuscript_lower
    assert "required state" in manuscript_lower
    assert "identified state" in manuscript_lower
    assert "reportable target" in manuscript_lower
