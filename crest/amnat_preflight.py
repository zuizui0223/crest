"""Machine-readable preflight for the AmNat flagship submission."""

from __future__ import annotations

import json
import re
from pathlib import Path

from crest.amnat_submission import MANUSCRIPT, METADATA, current_report, load_metadata

ROOT = Path(__file__).resolve().parents[1]
DECLARATIONS_TEMPLATE = ROOT / "manuscript" / "amnat_submission_declarations_TEMPLATE.md"
READINESS = ROOT / "manuscript" / "AMNAT_SUBMISSION_READINESS.md"
ANONYMOUS_BUNDLE_BUILDER = ROOT / "scripts" / "build_amnat_anonymous_bundle.py"
TITLE_PAGE_BUILDER = ROOT / "scripts" / "build_amnat_title_page.py"

PLACEHOLDER_RE = re.compile(r"\[[^\]\n]+\]")
WORD_RE = re.compile(r"\b[A-Za-z0-9][A-Za-z0-9'’-]*\b")

# These fields are explicitly conditional in the active readiness/template surface.
CONDITIONAL_INITIAL_PLACEHOLDERS = {
    "[ORCID]",
    "[ADDRESS]",
    "[NAME(S)]",
    "[NAME(S), IF APPLICABLE]",
}

# These belong to the publication/post-acceptance version and must not block
# double-anonymous initial submission.
POST_ACCEPTANCE_PLACEHOLDERS = {
    "[PUBLIC REPOSITORY OR DOI]",
    "[SOFTWARE CITATION]",
}


def _abstract_word_count(text: str) -> int:
    abstract = text.split("## Abstract", 1)[1].split("**Keywords:**", 1)[0]
    return len(WORD_RE.findall(abstract))


def unresolved_placeholders(path: Path = DECLARATIONS_TEMPLATE) -> list[str]:
    """Return semantic placeholders, excluding Markdown task-box syntax."""

    text = path.read_text(encoding="utf-8")
    return sorted({item for item in PLACEHOLDER_RE.findall(text) if item.strip() != "[ ]"})


def classify_placeholders(path: Path = DECLARATIONS_TEMPLATE) -> dict[str, list[str]]:
    placeholders = set(unresolved_placeholders(path))
    post_acceptance = sorted(placeholders & POST_ACCEPTANCE_PLACEHOLDERS)
    conditional = sorted(placeholders & CONDITIONAL_INITIAL_PLACEHOLDERS)
    required = sorted(placeholders - POST_ACCEPTANCE_PLACEHOLDERS - CONDITIONAL_INITIAL_PLACEHOLDERS)
    return {
        "required_initial_submission": required,
        "conditional_initial_submission": conditional,
        "post_acceptance": post_acceptance,
    }


def preflight(
    declarations: Path = DECLARATIONS_TEMPLATE,
    *,
    pdf_visual_and_font_gate_confirmed: bool = False,
) -> dict[str, object]:
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    metadata = load_metadata()
    report = current_report()

    repository_checks = {
        "canonical_manuscript_exists": MANUSCRIPT.is_file(),
        "metadata_exists": METADATA.is_file(),
        "readiness_surface_exists": READINESS.is_file(),
        "anonymous_bundle_builder_exists": ANONYMOUS_BUNDLE_BUILDER.is_file(),
        "title_page_builder_exists": TITLE_PAGE_BUILDER.is_file(),
        "article_type_is_major_article": metadata.get("article_type") == "Major Article",
        "word_count_matches_metadata": report["text_word_count"] == metadata.get("text_word_count"),
        "word_count_within_7500": int(report["text_word_count"]) <= 7500,
        "abstract_within_200": _abstract_word_count(manuscript) <= 200,
        "keywords_between_1_and_6": 1 <= len(metadata.get("keywords", [])) <= 6,
        "short_title_within_40_characters": int(report["short_title_characters"]) <= 40,
        "cover_letter_not_expected": metadata.get("cover_letter_expected") is False,
    }
    repository_ready = all(repository_checks.values())

    classified = classify_placeholders(declarations)
    required = classified["required_initial_submission"]
    author_fields_ready = len(required) == 0
    literal_upload_ready = (
        repository_ready and author_fields_ready and pdf_visual_and_font_gate_confirmed
    )

    return {
        "repository_ready": repository_ready,
        "repository_checks": repository_checks,
        "author_fields_ready": author_fields_ready,
        "unresolved_required_author_placeholders": required,
        "unresolved_conditional_author_placeholders": classified[
            "conditional_initial_submission"
        ],
        "unresolved_post_acceptance_placeholders": classified["post_acceptance"],
        "pdf_visual_and_font_gate_confirmed": pdf_visual_and_font_gate_confirmed,
        "literal_upload_ready": literal_upload_ready,
        "text_word_count": report["text_word_count"],
        "short_title_characters": report["short_title_characters"],
    }


def write_report(
    output: Path,
    declarations: Path = DECLARATIONS_TEMPLATE,
    *,
    pdf_visual_and_font_gate_confirmed: bool = False,
) -> Path:
    result = preflight(
        declarations,
        pdf_visual_and_font_gate_confirmed=pdf_visual_and_font_gate_confirmed,
    )
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output
