from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = (ROOT / "manuscript" / "crest_biology_philosophy_blinded_submission.md").read_text(encoding="utf-8")


def test_blinded_candidate_has_no_empirical_validation_arc() -> None:
    blocked = (
        "Izu Campanula",
        "end-to-end empirical test of CREST",
        "Elwha River dams",
        "Acacia longifolia",
        "Phragmites australis",
        "peatland rewetting",
        "prescribed fire supplies independent",
        "empirical validation of the capability–resolution theorem",
    )
    for term in blocked:
        assert term not in MANUSCRIPT


def test_worked_ecology_is_present_but_bounded() -> None:
    required = (
        "## 3. A worked ecological case: shallow-lake restoration",
        "sediment legacy",
        "food-web feedback",
        "not an empirical performance test of CREST",
    )
    for term in required:
        assert term in MANUSCRIPT


def test_canonical_story_is_capacity_state_theorem_consequence() -> None:
    required = (
        "## 1. The ecological state problem begins with a conservation paradox",
        "## 2. Ecological state as scientifically constrained equivalence",
        "## 4. The finite CREST architecture",
        "## 5. Main result: capability–resolution divergence",
        "## 6. Conservation capacity can outgrow conservation knowledge",
        "## 8. Limits and conclusion",
    )
    for term in required:
        assert term in MANUSCRIPT


def test_same_state_question_and_capacity_paradox_are_explicit() -> None:
    assert "When should different ecological worlds count as the same ecological state?" in MANUSCRIPT
    assert "conservation capacity can outgrow conservation knowledge" in MANUSCRIPT
    assert "which differences may be forgotten without invalidating" not in MANUSCRIPT


def test_math_headline_is_preserved() -> None:
    for term in (
        "\\Delta|K^*|=1",
        "\\Delta K_{U_0}=m",
        "full state: yes}\\to\\text{no",
        "target: yes}\\to\\text{yes",
    ):
        assert term in MANUSCRIPT


def test_philosophy_positioning_is_present() -> None:
    for term in (
        "Potochnik",
        "Odenbaugh",
        "Batterman",
        "Wimsatt",
        "adequacy-for-purpose",
        "multiple realization",
    ):
        assert term in MANUSCRIPT


def test_contract_well_posedness_is_explicit() -> None:
    for term in (
        "Independent responsibility",
        "Non-vacuous domain",
        "Response testability",
        "Evidence accountability",
    ):
        assert term in MANUSCRIPT


def test_yates_is_cited_in_body() -> None:
    body = MANUSCRIPT.split("## References", 1)[0]
    assert "Yates et al. 2018" in body


def test_figure_is_referenced() -> None:
    assert "crest_capacity_knowledge_paradox.svg" in MANUSCRIPT


def test_no_author_identity_or_author_declarations_in_blinded_file() -> None:
    for term in (
        "Corresponding author",
        "Competing Interests",
        "Funding",
        "Acknowledgements",
        "OpenAI ChatGPT was used",
        "AUTHOR INPUT REQUIRED",
    ):
        assert term not in MANUSCRIPT
