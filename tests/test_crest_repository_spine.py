from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text()
PHILOSOPHY = (ROOT / "docs" / "contract_relative_ecological_state_theory.md").read_text()
MATH = (ROOT / "docs" / "crest_mathematical_spine.md").read_text()
ECOLOGY = (ROOT / "docs" / "crest_ecological_projection.md").read_text()
DOC_MAP = (ROOT / "docs" / "README.md").read_text()


def test_root_readme_exposes_one_question_and_four_obligations() -> None:
    assert "What counts as the same ecological state?" in README
    for term in (
        "future sufficiency",
        "semantic coherence",
        "mechanism robustness",
        "evidential licensing",
    ):
        assert term in README
    for path in (
        "docs/contract_relative_ecological_state_theory.md",
        "docs/crest_mathematical_spine.md",
        "docs/crest_ecological_projection.md",
    ):
        assert path in README


def test_philosophy_doc_keeps_proved_and_future_claims_separate() -> None:
    assert "Three gates, not one ontology" in PHILOSOPHY
    assert "A temporally thick interpretation" in PHILOSOPHY
    assert "research direction" in PHILOSOPHY
    assert "What CREST does not claim" in PHILOSOPHY


def test_mathematical_spine_prioritizes_three_gates_and_cross_gate_result() -> None:
    for term in (
        "Gate A — carrier feasibility",
        "Gate B — unique least-information state",
        "Gate C — evidence licensing",
        "Cross-gate theorem — action expansion",
        "Supporting theorem infrastructure",
    ):
        assert term in MATH
    assert "J2" in MATH and "J4" in MATH and "J5" in MATH and "J7" in MATH


def test_ecological_projection_contains_temporal_observation_and_stability_layers() -> None:
    for term in (
        "A state is not automatically a snapshot",
        "Structural monitoring debt",
        "Management changes the state before changing the ecosystem",
        "Dynamical stability versus representational stability",
        "Ecological rules as quotient laws",
    ):
        assert term in ECOLOGY


def test_document_map_demotes_derived_concepts_from_headline_status() -> None:
    assert "Derived concepts — retained, not promoted" in DOC_MAP
    assert "Development stop rule" in DOC_MAP
