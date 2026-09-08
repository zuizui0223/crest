#!/usr/bin/env python3
"""Generate the anonymous AmNat review title page from canonical metadata."""

from __future__ import annotations

import argparse
from pathlib import Path

from scripts.amnat_submission_metadata import MANUSCRIPT, load_metadata, text_word_count

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "amnat_anonymous_title_page.md"


def build_title_page(output: Path = DEFAULT_OUTPUT) -> Path:
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(build_title_page(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
