"""Submission metadata and anonymous review-manuscript helpers for the AmNat flagship."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"
AI_DISCLOSURE = ROOT / "docs" / "amnat_ai_disclosure_2026-09-09.md"
DEFAULT_TITLE_PAGE = ROOT / "dist" / "amnat_anonymous_title_page.md"
DEFAULT_REVIEW_MANUSCRIPT = ROOT / "dist" / "amnat_anonymous_review_manuscript.md"

WORD_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9'’-]*\b")
DISPLAY_MATH_RE = re.compile(r"\\\[.*?\\\]", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\\\(.*?\\\)", re.DOTALL)


def submission_manuscript_text() -> str:
    """Assemble the exact review manuscript from frozen science plus disclosure."""

    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    disclosure = AI_DISCLOSURE.read_text(encoding="utf-8").strip()
    marker = "## 12. Discussion"
    if marker not in manuscript:
        raise ValueError("Discussion marker missing from canonical manuscript")
    if "### 11.1 Reproducibility methods and AI-assisted development" in manuscript:
        raise ValueError("AI disclosure is already present in canonical manuscript")
    return manuscript.replace(marker, f"{disclosure}\n\n{marker}", 1)


def main_text(text: str) -> str:
    """Return Introduction-through-Conclusion text used for title-page counting."""

    body = text.split("## 1. Introduction", 1)[1]
    body = body.split("## Literature Cited", 1)[0]
    body = DISPLAY_MATH_RE.sub(" ", body)
    body = INLINE_MATH_RE.sub(" ", body)
    body = "\n".join(line for line in body.splitlines() if not line.lstrip().startswith("|"))
    return body


def text_word_count(text: str) -> int:
    return len(WORD_RE.findall(main_text(text)))


def load_metadata() -> dict[str, object]:
    return json.loads(METADATA.read_text(encoding="utf-8"))


def current_report() -> dict[str, object]:
    text = submission_manuscript_text()
    metadata = load_metadata()
    return {
        "article_type": metadata["article_type"],
        "short_title": metadata["short_title"],
        "short_title_characters": len(str(metadata["short_title"])),
        "text_word_count": text_word_count(text),
        "manuscript_elements": metadata["manuscript_elements"],
        "cover_letter_expected": metadata["cover_letter_expected"],
    }


def build_review_manuscript(output: Path = DEFAULT_REVIEW_MANUSCRIPT) -> Path:
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(submission_manuscript_text(), encoding="utf-8")
    return output


def build_title_page(output: Path = DEFAULT_TITLE_PAGE) -> Path:
    metadata = load_metadata()
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    submission_text = submission_manuscript_text()
    title = manuscript.splitlines()[0].removeprefix("# ").strip()
    words = text_word_count(submission_text)
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
