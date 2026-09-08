from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.6_addressability.md"
TEXT = MANUSCRIPT.read_text(encoding="utf-8")
PLAIN = TEXT.replace("**", "").replace("*", "")


def _section_between(start: str, end: str) -> str:
    body = TEXT.split(start, 1)[1]
    return body.split(end, 1)[0].strip()


def _word_count(text: str) -> int:
    return len(re.findall(r"\b[\w-]+\b", text))


def test_amnat_title_is_concise_and_searchable() -> None:
    title = TEXT.splitlines()[0].removeprefix("# ").strip()
    assert title == "Ecological State at a Temporal Cut: Interface-Dependent Interaction"
    assert 8 <= _word_count(title) <= 10


def test_amnat_major_article_abstract_is_within_200_words() -> None:
    abstract = _section_between("## Abstract", "**Keywords:**")
    assert _word_count(abstract) <= 200
    assert "explicit finite grammar" in abstract
    assert "minimal interface prerequisite set" in abstract
    assert "pure three-way" in abstract
    assert "compositional access structure" in abstract


def test_amnat_keywords_do_not_exceed_six() -> None:
    keyword_line = next(line for line in TEXT.splitlines() if line.startswith("**Keywords:**"))
    keywords = [item.strip() for item in keyword_line.split(":", 1)[1].split(";") if item.strip()]
    assert 1 <= len(keywords) <= 6


def test_model_and_explicit_grammar_precede_main_result() -> None:
    assert TEXT.index("## 2. State at an observational temporal cut") < TEXT.index(
        "## 5. Explicit grammar and trace quotient"
    )
    assert TEXT.index("## 5. Explicit grammar and trace quotient") < TEXT.index(
        "## 6. Main theorem: interface prerequisites determine interaction order"
    )


def test_submission_manuscript_has_literature_positioning() -> None:
    required = (
        "Ogle et al. 2015",
        "Scheffer et al. 2001",
        "Hastings et al. 2018",
        "Shalizi and Crutchfield 2001",
        "Littman, Sutton, and Singh 2001",
        "Givan, Dean, and Greig 2003",
        "Li, Walsh, and Littman 2006",
        "## Literature Cited",
    )
    for token in required:
        assert token in TEXT


def test_manuscript_makes_three_way_claim_conditional_and_falsifiable() -> None:
    assert "Fixed-partition no-go" in TEXT
    assert "decoder prerequisite set" in TEXT.lower()
    assert "formula is now a theorem" in TEXT.lower()
    assert "If \\(F\\) can decode the exterior signature alone, the three-way dividend is zero" in TEXT
    assert "pure three-way interaction is conditional, not automatic" in TEXT.lower()


def test_novelty_firewall_distinguishes_prior_art_from_crest_claim() -> None:
    assert "CREST does not claim novelty" in PLAIN
    assert "composition layer" in PLAIN
    assert "minimal interface set required to address that information" in PLAIN
    assert "Higher-order state debt is therefore not assumed" in PLAIN
