#!/usr/bin/env python3
"""Reproducible submission-metadata checks for the CREST AmNat manuscript."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"

WORD_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9'’-]*\b")
DISPLAY_MATH_RE = re.compile(r"\\\[.*?\\\]", re.DOTALL)
INLINE_MATH_RE = re.compile(r"\\\(.*?\\\)", re.DOTALL)


def main_text(text: str) -> str:
    """Return Introduction-through-Conclusion text used for the title-page count.

    The count excludes the abstract, Literature Cited, display/inline mathematics,
    and markdown table rows.  The rule is deliberately simple and reproducible;
    the journal does not prescribe a specific word-count algorithm.
    """

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


def main() -> int:
    print(json.dumps(current_report(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
