from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
AUDIT = ROOT / "docs" / "paper_a_mathematical_closure_audit_2026-09-15.md"
FIREWALL = ROOT / "docs" / "temporal_cut_companion_definition_firewall_2026-09-08.md"
NO_GO = ROOT / "docs" / "crest_companion_realizability_no_go_2026-09-08.md"


def test_paper_a_keeps_pre_state_to_state_dependency_direction() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    assert "Retrospective, transverse, and prospective structures are pre-state" in manuscript
    assert "There is no reverse dependence from the final state into these primitives." in manuscript
    assert "primitive history / candidate law / future grammar" in manuscript
    assert "semantic or response equivalence" in manuscript
    assert "adequate state" in manuscript


def test_paper_a_preserves_strict_realizability_no_go() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    no_go = NO_GO.read_text(encoding="utf-8")
    assert "Fixed-partition no-go" in manuscript
    assert "Immutable-history no-activation result" in manuscript
    assert "Fixed-grammar MRM zero-debt result" in manuscript
    assert "not yet strict simultaneous MLTR x MRM x CCOC realizations" in no_go
    assert "a simultaneous canonical companion realization with an unbounded genuine three-way interaction" in no_go


def test_shannon_support_is_not_used_to_define_its_own_prerequisites() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    audit = AUDIT.read_text(encoding="utf-8")
    assert "a query with prerequisite set" in manuscript
    assert "The prerequisite set determines **where** a Shannon dividend can occur" in manuscript
    assert "prerequisite set is inferred from the same Möbius support" in audit
    assert "It must not define `R_f` from `supp(d_1)`" in audit


def test_closure_audit_records_open_bridge_as_non_required() -> None:
    audit = AUDIT.read_text(encoding="utf-8")
    firewall = FIREWALL.read_text(encoding="utf-8")
    assert "Definition DAG: **closed / acyclic**" in audit
    assert "Strict arbitrary-companion common-realization theorem: **open and explicitly non-required**" in audit
    assert "No companion responsibility may depend definitionally on `J_t`." in firewall
