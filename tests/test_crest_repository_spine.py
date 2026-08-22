from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text()
PHILOSOPHY = (ROOT / "docs" / "contract_relative_ecological_state_theory.md").read_text()
MATH = (ROOT / "docs" / "crest_mathematical_spine.md").read_text()
ECOLOGY = (ROOT / "docs" / "crest_ecological_projection.md").read_text()
ARCHITECTURE = (
    ROOT / "docs" / "trajectory_first_program_architecture_2026-08-22.md"
).read_text()
DOC_MAP = (ROOT / "docs" / "README.md").read_text()


def test_root_readme_exposes_trajectory_first_state_question() -> None:
    assert "Why can a finite ecological state exist at all" in README
    assert "scientifically licensed compression of a temporally extended ecological world" in README
    assert "Snapshot sufficiency" in README
    for term in (
        "future sufficiency",
        "semantic coherence",
        "mechanism robustness",
        "evidence licensing",
    ):
        assert term in README
    for path in (
        "docs/contract_relative_ecological_state_theory.md",
        "docs/crest_mathematical_spine.md",
        "docs/crest_ecological_projection.md",
    ):
        assert path in README


def test_philosophy_doc_keeps_world_level_frame_and_finite_firewall_separate() -> None:
    assert "The starting point: world before state" in PHILOSOPHY
    assert "Snapshot sufficiency" in PHILOSOPHY
    assert "Three finite gates" in PHILOSOPHY
    assert "What CREST does not claim" in PHILOSOPHY
    assert "general continuous/stochastic trajectory theorem" in PHILOSOPHY


def test_mathematical_spine_prioritizes_gates_and_cross_gate_scaling() -> None:
    for term in (
        "Gate A — carrier feasibility",
        "Gate B — unique least-information state",
        "Gate C — evidence licensing",
        "Cross-gate monotonicity — qualitative action expansion",
        "Cross-gate scaling — capability–resolution divergence",
        "viability gain alone cannot upper-bound representational burden",
        "Supporting theorem infrastructure",
    ):
        assert term in MATH
    assert "J2" in MATH and "J4" in MATH and "J5" in MATH and "J7" in MATH


def test_ecological_projection_contains_trajectory_quotient_and_stability_layers() -> None:
    for term in (
        "A state is a compression of a temporally extended world",
        "Structural monitoring debt",
        "Management can change the state before changing the ecosystem",
        "Dynamical, evolutionary, and representational stability",
        "Ecological rules as quotient laws",
    ):
        assert term in ECOLOGY


def test_architecture_routes_structural_obstructions_before_evidence_licensing() -> None:
    for term in (
        "temporally extended possible worlds",
        "CCOC — future/composition",
        "MLTR — inherited semantics/history",
        "MRM  — retained mechanisms",
        "CED",
        "Why CED is not on the same ontic level",
    ):
        assert term in ARCHITECTURE


def test_document_map_demotes_derived_concepts_from_headline_status() -> None:
    assert "Derived concepts — retained, not promoted" in DOC_MAP
    assert "Development stop rule" in DOC_MAP
