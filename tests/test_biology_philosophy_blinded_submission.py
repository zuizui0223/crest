from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = (ROOT / "manuscript" / "crest_biology_philosophy_blinded_submission.md").read_text(encoding="utf-8")


def test_blinded_candidate_has_no_empirical_validation_arc() -> None:
    blocked = (
        "Restoration as a cross-domain ecological projection",
        "Izu Campanula",
        "end-to-end empirical test of CREST",
        "Elwha River dams",
        "Acacia longifolia",
        "Phragmites australis",
        "peatland rewetting",
        "prescribed fire supplies independent",
    )
    for term in blocked:
        assert term not in MANUSCRIPT


def test_canonical_story_is_problem_formal_answer_ecological_consequence() -> None:
    required = (
        "## 1. The ecological state problem",
        "## 2. Contract-relative ecological state",
        "## 4. The finite mathematical answer",
        "## 5. Ecological consequences",
        "## 8. Conclusion",
    )
    for term in required:
        assert term in MANUSCRIPT


def test_same_state_question_replaces_forgetting_headline() -> None:
    assert "when different ecological worlds should count as the same ecological state" in MANUSCRIPT
    assert "which differences may be forgotten without invalidating" not in MANUSCRIPT


def test_math_headline_is_preserved() -> None:
    for term in (
        "\\Delta|K^*|=1",
        "\\Delta K_{U_0}=m",
        "full state: yes}\\to\\text{no",
        "target: yes}\\to\\text{yes",
    ):
        assert term in MANUSCRIPT


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
