from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.5_compositional.md"
TEXT = MANUSCRIPT.read_text(encoding="utf-8")
PLAIN = TEXT.replace("**", "").replace("*", "")


def _section_between(start: str, end: str) -> str:
    body = TEXT.split(start, 1)[1]
    return body.split(end, 1)[0].strip()


def _word_count(text: str) -> int:
    return len(re.findall(r"\b[\w-]+\b", text))


def test_amnat_title_is_concise_and_searchable() -> None:
    title = TEXT.splitlines()[0].removeprefix("# ").strip()
    assert title == "Ecological State at a Temporal Cut: Compositional Interaction Across Time"
    assert 8 <= _word_count(title) <= 10


def test_amnat_major_article_abstract_is_within_200_words() -> None:
    abstract = _section_between("## Abstract", "**Keywords:**")
    assert _word_count(abstract) <= 200
    assert "4096" in abstract
    assert "1024-fold" in abstract
    assert "10 of 12 bits" in abstract
    assert "temporal cut" in abstract


def test_amnat_keywords_do_not_exceed_six() -> None:
    keyword_line = next(line for line in TEXT.splitlines() if line.startswith("**Keywords:**"))
    keywords = [item.strip() for item in keyword_line.split(":", 1)[1].split(";") if item.strip()]
    assert 1 <= len(keywords) <= 6


def test_methods_precede_results() -> None:
    assert TEXT.index("## 3. Methods:") < TEXT.index("## 4. Results I:")


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


def test_manuscript_separates_abstract_extrema_from_literal_companion_claim() -> None:
    assert "strict realizability" in TEXT.lower()
    assert "cannot simply be renamed as literal MLTR, MRM, and CCOC interactions" in TEXT
    assert "abstract fixed-closure" in TEXT.lower()
    assert "pure literal three-way compositional interaction" in TEXT.lower()
    assert "m(H,\\Theta,F)=m" in TEXT
    assert "pairwise" in TEXT.lower() and "zero" in TEXT.lower()


def test_novelty_firewall_distinguishes_prior_art_from_crest_claim() -> None:
    assert "CREST does not claim novelty" in PLAIN
    assert "The question here is narrower" in PLAIN
    assert "genuine three-way interaction" in PLAIN
    assert "asymptotically dominate" in PLAIN
