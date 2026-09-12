from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
TEXT = MANUSCRIPT.read_text(encoding="utf-8")
PLAIN = TEXT.replace("**", "").replace("*", "")


def _section_between(start: str, end: str) -> str:
    body = TEXT.split(start, 1)[1]
    return body.split(end, 1)[0].strip()


def _word_count(text: str) -> int:
    return len(re.findall(r"\b[\w-]+\b", text))


def test_amnat_title_is_concise_and_searchable() -> None:
    title = TEXT.splitlines()[0].removeprefix("# ").strip()
    assert title == "Ecological State at a Temporal Cut: Sparse Semantic Access"
    assert 8 <= _word_count(title) <= 10


def test_amnat_major_article_abstract_is_within_200_words() -> None:
    abstract = _section_between("## Abstract", "**Keywords:**")
    assert _word_count(abstract) <= 200
    assert "zero-duration temporal cut" in abstract
    assert "semantic pairs" in abstract
    assert "support future differentiation" in abstract
    assert "(N-k)+k2^m" in abstract
    assert "one visible present can conceal ecologically distinct recovery capacities" in abstract
    assert "does not claim a continuous-time epsilon-to-zero limit theorem" in abstract


def test_amnat_keywords_do_not_exceed_six() -> None:
    keyword_line = next(line for line in TEXT.splitlines() if line.startswith("**Keywords:**"))
    keywords = [item.strip() for item in keyword_line.split(":", 1)[1].split(";") if item.strip()]
    assert 1 <= len(keywords) <= 6


def test_scientific_spine_is_in_correct_order() -> None:
    assert TEXT.index("## 2. State at a zero-duration temporal cut") < TEXT.index(
        "## 4. Realizability boundaries"
    )
    assert TEXT.index("## 4. Realizability boundaries") < TEXT.index(
        "## 5. Activating companion semantics"
    )
    assert TEXT.index("## 5. Activating companion semantics") < TEXT.index(
        "## 6. Sparse semantic access"
    )
    assert TEXT.index("## 6. Sparse semantic access") < TEXT.index(
        "## 8. Shallow lakes as a biological witness of a non-instantaneous present"
    )


def test_submission_manuscript_has_literature_positioning() -> None:
    required = (
        "Ogle et al. 2015",
        "Scheffer et al. 2001",
        "Hastings et al. 2018",
        "Fukami 2015",
        "Beisner, Haydon, and Cuddington 2003",
        "Suding, Gross, and Houseman 2004",
        "Auger-Méthé et al. 2021",
        "Shalizi and Crutchfield 2001",
        "Littman, Sutton, and Singh 2001",
        "Givan, Dean, and Greig 2003",
        "Li, Walsh, and Littman 2006",
        "Søndergaard, Jensen, and Jeppesen 2003",
        "Søndergaard et al. 2007",
        "Jeppesen et al. 2012",
        "## Literature Cited",
    )
    for token in required:
        assert token in TEXT


def test_section10_distinguishes_four_neighboring_state_traditions() -> None:
    section = _section_between(
        "## 10. Relation to existing state concepts",
        "## 11. Scope and supporting mathematics",
    )
    assert "### 10.1 Ecological memory and historical contingency" in section
    assert "### 10.2 Hysteresis, alternative states, and restoration" in section
    assert "### 10.3 Latent ecological state in state-space models" in section
    assert "### 10.4 Predictive states and state abstraction" in section
    assert "CREST therefore does not equate ecological memory with retention of complete history" in section
    assert "A state-space model normally begins after the analyst has specified what variables constitute the latent state" in section
    assert "CREST instead asks what makes two possible ecological worlds the same state at the present boundary in the first place" in section
    assert "not a new generic theory of quotient states" in section
    assert "finite theory of the ecological present as a temporal boundary" in section


def test_sparse_access_and_full_access_boundary_are_both_explicit() -> None:
    assert "|Q_{H\\Theta F}|=(N-k)+k2^m" in TEXT
    assert "m-\\log_2(N/k)+o(1)" in TEXT
    assert "1027" in TEXT
    assert "8.00422" in TEXT
    assert "4096-class" in TEXT
    assert "full-access boundary" in TEXT


def test_novelty_firewall_distinguishes_theory_from_accounting() -> None:
    assert "does not claim mathematical novelty for Möbius inversion or unanimity games" in PLAIN
    assert "prerequisite set" in PLAIN
    assert "semantic access relation" in PLAIN
    assert "finite counting" in PLAIN
    assert "paper-level contribution" in PLAIN
    assert "structural support, not a claim of new partition theory" in PLAIN
    assert "modeling contribution" not in PLAIN


def test_shallow_lake_is_biological_witness_not_empirical_validation() -> None:
    shallow = _section_between(
        "## 8. Shallow lakes as a biological witness of a non-instantaneous present",
        "## 9. Why ecological state requires a temporal cut",
    )
    assert "concrete reason not to identify ecological state with a coarse instantaneous configuration" in shallow
    assert "one visible present can conceal several states" in shallow
    assert "R_{\\rm composed}=\\{H,\\Theta\\}" in shallow
    assert "only two outputs" in shallow
    assert "standard_pathway" in shallow
    assert "cross_interface_review" in shallow
    assert "formal witness of joint dependence" in shallow
    assert "not a biological law asserted by the restoration literature" in shallow
    assert "target-relative prerequisite calculation is secondary evidence" in shallow
    assert "Søndergaard, Jensen, and Jeppesen 2003" in shallow
    assert "Søndergaard et al. 2007" in shallow
    assert "Jeppesen et al. 2012" in shallow
