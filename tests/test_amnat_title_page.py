from __future__ import annotations

from pathlib import Path

from crest.amnat_submission import MANUSCRIPT, build_title_page, load_metadata, text_word_count


def test_generated_title_page_contains_required_review_metadata(tmp_path: Path) -> None:
    output = build_title_page(tmp_path / "title_page.md")
    text = output.read_text(encoding="utf-8")
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    metadata = load_metadata()

    assert f"**Article type:** {metadata['article_type']}" in text
    assert f"**Short title:** {metadata['short_title']}" in text
    assert f"**Text word count:** {text_word_count(manuscript)}" in text
    assert "**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; semantic access; restoration" in text
    assert "**Manuscript elements:** Abstract; Main text; 1 table; Literature Cited" in text
    assert "zuizui0223" not in text.lower()
    assert "@" not in text
