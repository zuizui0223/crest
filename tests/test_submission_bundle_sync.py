from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_philosophy_biology_philosophy.md"
HANDOFF = ROOT / "manuscript" / "biology_philosophy_submission_handoff.md"
SUBMISSION_README = ROOT / "manuscript" / "SUBMISSION_README.md"
TITLE_PAGE = ROOT / "manuscript" / "title_page_template.md"
REPORT = ROOT / "artifacts" / "crest_philosophy_submission_report.json"
OBSOLETE_INSERT = ROOT / "manuscript" / "adequacy_frontier_insert.md"


def test_submission_handoff_matches_generated_report_and_current_headline() -> None:
    handoff = HANDOFF.read_text(encoding="utf-8")
    report = json.loads(REPORT.read_text(encoding="utf-8"))

    assert f"abstract: **{report['abstract_words']} words**" in handoff
    assert (
        f"visible words before References: **{report['manuscript_words_before_references']:,}**"
        in handoff
    )
    assert "theorem/regression suite: **93 tests PASS**" in handoff
    assert "\\Delta |K^*|=1" in handoff
    assert "\\Delta K_{U_0}=m" in handoff
    assert "CED is downstream" in handoff

    for stale in (
        "four currently formalized obligations",
        "abstract: **234 words**",
        "5,942",
        "one strict cross-gate ecological result",
    ):
        assert stale not in handoff


def test_title_page_and_review_manuscript_use_the_same_title() -> None:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    title_page = TITLE_PAGE.read_text(encoding="utf-8")
    first = "What Counts as the Same Ecological State?"
    second = "A Contract-Relative Theory of Temporally Extended Ecological States"
    assert f"# {first}\n## {second}" in manuscript
    assert f"**{first} {second}**" in title_page


def test_submission_readme_records_math_first_finished_state() -> None:
    text = SUBMISSION_README.read_text(encoding="utf-8")
    assert "connected capability–resolution divergence theorem" in text
    assert "Existing conceptual and real-data ecology cases are optional illustrations" in text
    assert "Repository-controlled scientific development is closed" in text
    assert "verify the integrated trajectory-first manuscript" not in text


def test_obsolete_frontier_insert_is_not_in_submission_bundle() -> None:
    assert not OBSOLETE_INSERT.exists()
