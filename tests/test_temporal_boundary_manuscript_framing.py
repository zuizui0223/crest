from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
TEXT = MANUSCRIPT.read_text(encoding="utf-8")


def _between(start: str, end: str) -> str:
    return TEXT.split(start, 1)[1].split(end, 1)[0]


def test_present_is_a_zero_duration_cut_not_a_pregiven_state() -> None:
    assert "zero-duration temporal cut" in TEXT
    assert "visible configuration and ecological state need not coincide" in TEXT
    assert "L_t(y)=O_t^{-1}(y)" in TEXT
    assert "not a proved limit of shrinking continuous-time windows" in TEXT


def test_cut_state_has_universal_invariance_lattice_and_transport_structure() -> None:
    section = _between(
        "## 2. State at a zero-duration temporal cut",
        "## 3. Retrospective, transverse, and prospective structures are pre-state",
    )
    assert "g_i:\\Omega\\to Z_i" in section
    assert "\\omega\\sim_*\\omega'" in section
    assert "unique coarsest admissible quotient" in section
    assert "once those signatures are fixed the least compatible state is not freely chosen" in section
    assert "This conclusion is representation invariant" in section
    assert "every signature in each family factors through the state induced by the other" in section
    assert "adding any signature already determined by the existing cut-state is redundant" in section
    assert "equivalence relation generated jointly with the cut" in section
    assert "representation classes exhaust the entire finite state space" in section
    assert "one-to-one correspondence with partitions that refine \\(B_t\\)" in section
    assert "Ordering states by retained information is therefore exactly partition refinement" in section
    assert "\\log_2|Q|" in section
    assert "monotone nondecreasing" in section
    assert "States at different cuts can be connected only when" in section
    assert "\\phi_{t\\to s}:\\Omega_t\\to\\Omega_s" in section
    assert "\\omega\\sim_t\\omega'" in section
    assert "\\phi(\\omega)\\sim_s\\phi(\\omega')" in section
    assert "identity and composition descend" in section
    assert "state-sufficiency obstruction" in section
    assert "does not imply temporal monotonicity" in section


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


def test_core_claim_is_ecological_state_theory_not_design_prescription() -> None:
    intro = _between("## 1. Introduction", "## 2. State at a zero-duration temporal cut")
    meaning = _between(
        "## 9. Why ecological state requires a temporal cut",
        "## 10. Relation to existing state concepts",
    )
    conclusion = _between("## 13. Conclusion", "## Literature Cited")
    for block in (intro, meaning, conclusion):
        assert "modeling architecture" not in block
        assert "modular state design" not in block
        assert "monitoring design" not in block
    assert "visible configuration and ecological state need not coincide" in intro
    assert "ecological present can contain distinctions with three different temporal origins" in meaning
    assert "Ecological state is therefore not located entirely in the instantaneous visible present" in conclusion


def test_continuous_time_limit_is_explicitly_out_of_scope() -> None:
    scope = _between("## 11. Scope and supporting mathematics", "## 12. Discussion")
    assert "zero-duration cut" in scope
    assert "continuous-time germ theorem" in scope
    assert "\\varepsilon\\to0" in scope


def test_shallow_lake_remains_biological_witness_not_source_of_theory() -> None:
    shallow = _between(
        "## 8. Shallow lakes as a biological witness of a non-instantaneous present",
        "## 9. Why ecological state requires a temporal cut",
    )
    assert "concrete reason not to identify ecological state with a coarse instantaneous configuration" in shallow
    assert "one visible present can conceal several states" in shallow
    assert "formal witness of joint dependence" in shallow
    assert "not a biological law asserted by the restoration literature" in shallow
    assert "target-relative prerequisite calculation is secondary evidence" in shallow
