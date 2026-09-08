from __future__ import annotations

import json
import re
from pathlib import Path

from scripts.amnat_submission_metadata import MANUSCRIPT, METADATA, text_word_count

ROOT = Path(__file__).resolve().parents[1]


def test_amnat_submission_metadata_matches_current_requirements() -> None:
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    text = MANUSCRIPT.read_text(encoding="utf-8")

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
    assert metadata["text_word_count"] == text_word_count(text)


def test_metadata_is_consistent_with_manuscript_surface() -> None:
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    text = MANUSCRIPT.read_text(encoding="utf-8")
    title = text.splitlines()[0].removeprefix("# ").strip()
    keywords_line = next(line for line in text.splitlines() if line.startswith("**Keywords:**"))
    manuscript_keywords = [item.strip() for item in keywords_line.split(":", 1)[1].split(";")]

    assert 8 <= len(re.findall(r"\b[\w-]+\b", title)) <= 10
    assert manuscript_keywords == metadata["keywords"]
    assert "## Abstract" in text
    assert "## Literature Cited" in text
    assert "| \\(m\\) | grand classes | grand bits | three-way dividend |" in text
