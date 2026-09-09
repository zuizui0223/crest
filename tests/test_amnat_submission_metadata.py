from __future__ import annotations

import json
import re
from pathlib import Path

from crest.amnat_submission import (
    AI_DISCLOSURE,
    MANUSCRIPT,
    METADATA,
    build_review_manuscript,
    submission_manuscript_text,
    text_word_count,
)


def test_amnat_submission_metadata_matches_current_requirements() -> None:
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    text = submission_manuscript_text()

    assert metadata["article_type"] == "Major Article"
    assert 1 <= len(metadata["keywords"]) <= 6
    assert metadata["keywords"] == [
        "ecological state",
        "temporal representation",
        "ecological memory",
        "state abstraction",
        "semantic access",
        "restoration",
    ]
    assert len(metadata["short_title"]) <= 40
    assert metadata["cover_letter_expected"] is False
    assert metadata["manuscript_elements"] == [
        "Abstract",
        "Main text",
        "1 table",
        "Literature Cited",
    ]
    assert metadata["text_word_count"] == 2434
    assert metadata["text_word_count"] == text_word_count(text)
    assert metadata["ai_disclosure_source"] == "docs/amnat_ai_disclosure_2026-09-09.md"


def test_metadata_is_consistent_with_canonical_science_surface() -> None:
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    text = MANUSCRIPT.read_text(encoding="utf-8")
    title = text.splitlines()[0].removeprefix("# ").strip()
    keywords_line = next(line for line in text.splitlines() if line.startswith("**Keywords:**"))
    keyword_text = keywords_line.removeprefix("**Keywords:**").strip()
    manuscript_keywords = [item.strip() for item in keyword_text.split(";")]

    assert 8 <= len(re.findall(r"\b[\w-]+\b", title)) <= 10
    assert manuscript_keywords == metadata["keywords"]
    assert "## Abstract" in text
    assert "## Literature Cited" in text
    assert "| \\(m\\) | grand classes | grand bits | three-way dividend |" in text
    assert "AI-assisted development" not in text


def test_review_manuscript_inserts_transparent_ai_methods_before_discussion(tmp_path: Path) -> None:
    disclosure = AI_DISCLOSURE.read_text(encoding="utf-8").strip()
    text = submission_manuscript_text()

    assert disclosure in text
    assert text.index("### 11.1 Reproducibility methods and AI-assisted development") < text.index(
        "## 12. Discussion"
    )
    assert "Generative AI tools were used" in text
    assert "AI outputs were treated as provisional" in text
    assert "independent recomputation of key finite-state numerical claims" in text
    assert "submitting authorship retains full responsibility" in text

    output = build_review_manuscript(tmp_path / "review.md")
    assert output.read_text(encoding="utf-8") == text
