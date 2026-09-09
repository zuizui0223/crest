from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
TEXT = MANUSCRIPT.read_text(encoding="utf-8")


def _between(start: str, end: str) -> str:
    return TEXT.split(start, 1)[1].split(end, 1)[0]


def test_present_is_a_zero_duration_cut_not_a_pregiven_state() -> None:
    assert "zero-duration temporal cut" in TEXT
    assert "not yet an adequate state" in TEXT
    assert "L_t(y)=O_t^{-1}(y)" in TEXT
    assert "not a proved limit of shrinking continuous-time windows" in TEXT


def test_cut_state_has_an_explicit_universal_property() -> None:
    section = _between(
        "## 2. State at a zero-duration temporal cut",
        "## 3. Retrospective, transverse, and prospective structures are pre-state",
    )
    assert "g_i:\\Omega\\to Z_i" in section
    assert "\\omega\\sim_*\\omega'" in section
    assert "unique coarsest admissible quotient" in section
    assert "once those signatures are fixed the least compatible state is not freely chosen" in section


def test_three_roles_are_left_transverse_right_constraints() -> None:
    section = _between(
        "## 3. Retrospective, transverse, and prospective structures are pre-state",
        "## 4. Realizability boundaries",
    )
    assert "retrospective carried semantics from the left" in section
    assert "transverse latent-present response structure" in section
    assert "prospective query structure to the right" in section
    assert "not a claim to recover complete causal or ontic mechanism identity" in section
    assert "not three independent state coordinates" in section


def test_core_claim_is_minimal_cut_quotient_not_design_prescription() -> None:
    intro = _between("## 1. Introduction", "## 2. State at a zero-duration temporal cut")
    meaning = _between("## 9. What the cut-state result means", "## 10. Relation to existing state concepts")
    conclusion = _between("## 13. Conclusion", "## Literature Cited")
    for block in (intro, meaning, conclusion):
        assert "modeling architecture" not in block
        assert "modular state design" not in block
        assert "identification discipline" not in block
    assert "least quotient on the cut" in intro
    assert "mathematical consequences rather than design choices" in meaning
    assert "equivalence geometry induced across a temporal boundary" in conclusion


def test_continuous_time_limit_is_explicitly_out_of_scope() -> None:
    scope = _between("## 11. Scope and supporting mathematics", "## 12. Discussion")
    assert "zero-duration cut" in scope
    assert "continuous-time germ theorem" in scope
    assert "\\varepsilon\\to0" in scope


def test_shallow_lake_remains_interpretation_not_source_of_theory() -> None:
    shallow = _between(
        "## 8. Target-relative shallow-lake prerequisite identification",
        "## 9. What the cut-state result means",
    )
    assert "worked ecological interpretation of the abstract cut geometry" in shallow
    assert "formal witness of joint dependence" in shallow
    assert "not a biological law asserted by the restoration literature" in shallow
