"""Submission metadata and anonymous title-page helpers for the AmNat flagship."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"
DEFAULT_TITLE_PAGE = ROOT / "dist" / "amnat_anonymous_title_page.md"

WORD_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9'’-]*\b")


def main_text(text: str) -> str:
    """Return Introduction-through-Conclusion text for the reported word count."""

    body = text.split("## 1. Introduction", 1)[1]
    return body.split("## Literature Cited", 1)[0]


def text_word_count(text: str) -> int:
    """Count all word-like tokens in the main text, including math/table source."""

    return len(WORD_RE.findall(main_text(text)))


def load_metadata() -> dict[str, object]:
    return json.loads(METADATA.read_text(encoding="utf-8"))


def current_report() -> dict[str, object]:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    metadata = load_metadata()
    return {
        "article_type": metadata["article_type"],
        "short_title": metadata["short_title"],
        "short_title_characters": len(str(metadata["short_title"])),
        "text_word_count": text_word_count(text),
        "manuscript_elements": metadata["manuscript_elements"],
        "cover_letter_expected": metadata["cover_letter_expected"],
    }


def build_title_page(output: Path = DEFAULT_TITLE_PAGE) -> Path:
    metadata = load_metadata()
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    title = manuscript.splitlines()[0].removeprefix("# ").strip()
    words = text_word_count(manuscript)
    keywords = "; ".join(str(item) for item in metadata["keywords"])
    elements = "; ".join(str(item) for item in metadata["manuscript_elements"])

    text = (
        f"# {title}\n\n"
        f"**Article type:** {metadata['article_type']}\n\n"
        f"**Short title:** {metadata['short_title']}\n\n"
        f"**Keywords:** {keywords}\n\n"
        f"**Text word count:** {words}\n\n"
        f"**Manuscript elements:** {elements}\n"
    )
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    return output
