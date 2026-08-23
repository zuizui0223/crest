from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SYNTHESIS = (ROOT / "docs" / "world_law_stability_synthesis_2026-08-23.md").read_text(encoding="utf-8")
DOC_MAP = (ROOT / "docs" / "README.md").read_text(encoding="utf-8")
MANUSCRIPT_CONTRACT = (
    ROOT / "manuscript" / "trajectory_first_manuscript_contract_2026-08-22.md"
).read_text(encoding="utf-8")


def test_synthesis_places_world_before_state_and_law() -> None:
    for term in (
        "How can ecological states and ecological laws exist at all",
        "q_{\\mathcal C,V}:\\Omega\\to Q_{\\mathcal C,V}",
        "R_{\\mathcal C}=L_{\\mathcal C,V}\\circ q_{\\mathcal C,V}",
        "domain-relative law validity",
        "representational instability",
    ):
        assert term in SYNTHESIS


def test_physics_firewall_separates_trajectory_representation_from_metaphysics() -> None:
    assert "not a metaphysical commitment that future events already exist" in SYNTHESIS
    assert "Eternalism/block-universe views and causal determinism are distinct claims" in SYNTHESIS
    assert "CREST requires neither" in SYNTHESIS
    assert "quantum mechanics is simply \u201call random\u201d" in SYNTHESIS


def test_ecological_direction_is_local_not_global_teleology() -> None:
    assert "stochastic variation" in SYNTHESIS
    assert "local adaptive bias" in SYNTHESIS
    assert "endogenous change of the selective environment" in SYNTHESIS
    assert "one universal arrow of increasing global fitness" in SYNTHESIS
    assert "mathematical chaos" in SYNTHESIS


def test_microdonta_bridge_uses_three_existing_hidden_structure_witnesses() -> None:
    for term in (
        "Hidden basin position and history",
        "Hidden causal programs",
        "Structural observational symmetry",
        "s\\in\\{0,1\\}^K",
        "W(z)=F(z)E(z)",
    ):
        assert term in SYNTHESIS
    assert "not a proof foundation for the general CREST theorem" in SYNTHESIS


def test_docs_map_and_manuscript_contract_promote_synthesis_without_new_theorem_family() -> None:
    assert "world_law_stability_synthesis_2026-08-23.md" in DOC_MAP
    assert "interpretive unification" in DOC_MAP
    assert "How can state and law be well-defined" in MANUSCRIPT_CONTRACT
    assert "Law portability" in MANUSCRIPT_CONTRACT
    assert "do not add another theorem family" in MANUSCRIPT_CONTRACT
