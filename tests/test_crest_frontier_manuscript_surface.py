from pathlib import Path


MANUSCRIPT = Path("manuscript/crest_philosophy_biology_philosophy.md")


def test_cross_gate_scaling_result_is_part_of_the_target_manuscript() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    lower = text.lower()
    assert "### 4.4 Cross-gate direction — capability can enlarge the carrier and refine the state" in text
    assert "### 4.5 Cross-gate scale separation — capability–resolution divergence" in text
    assert "The future does not have to happen to change the present scientific state" in text
    assert "\\Delta |K^*|=1" in text
    assert "\\Delta K_{U_0}=m" in text
    assert "full-state licensing changes from yes to no" in lower
    assert "coarse target" in lower and "remains reportable" in lower
    assert "no universal finite function" in lower
    assert "viability gain alone therefore cannot upper-bound" in lower


def test_cross_gate_section_keeps_priority_and_scope_firewalls() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    lower = text.lower()
    assert "The common-refinement calculation itself is classical" in text
    assert "J1 is foundational" in text
    assert "Konidaris (2019)" in text
    assert "The CREST result is therefore **not** the qualitative proposition" in text
    assert "No claim of historical priority for the generic equivalence-class idea is needed." in text
    assert "no backward causation" in lower
