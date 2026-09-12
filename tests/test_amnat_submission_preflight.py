from pathlib import Path

from crest.amnat_preflight import classify_placeholders, preflight, unresolved_placeholders


def test_repository_preflight_is_green_while_author_template_remains_open() -> None:
    report = preflight()
    assert report["repository_ready"] is True
    assert report["author_fields_ready"] is False
    assert report["pdf_visual_and_font_gate_confirmed"] is False
    assert report["literal_upload_ready"] is False
    assert report["text_word_count"] == 4804
    assert report["unresolved_required_author_placeholders"]
    assert "[ANONYMOUS REVIEW ARCHIVE OR JOURNAL FILE IDENTIFIER]" not in report[
        "unresolved_required_author_placeholders"
    ]
    assert not any(
        item.startswith("[SELECT ALL THAT APPLY:")
        for item in report["unresolved_required_author_placeholders"]
    )


def test_placeholder_classification_excludes_task_boxes_and_post_acceptance_from_initial_blockers() -> None:
    placeholders = unresolved_placeholders()
    classified = classify_placeholders()

    assert "[ ]" not in placeholders
    assert "[PUBLIC REPOSITORY OR DOI]" in classified["post_acceptance"]
    assert "[SOFTWARE CITATION]" in classified["post_acceptance"]
    assert "[PUBLIC REPOSITORY OR DOI]" not in classified["required_initial_submission"]
    assert "[SOFTWARE CITATION]" not in classified["required_initial_submission"]
    assert "[ORCID]" in classified["conditional_initial_submission"]
    assert "[ADDRESS]" in classified["conditional_initial_submission"]


def test_literal_upload_requires_resolved_declarations_and_pdf_confirmation(tmp_path: Path) -> None:
    declarations = tmp_path / "resolved.md"
    declarations.write_text(
        "Data and code archive: journal file.\n"
        "AI disclosure: confirmed.\n"
        "Author metadata, funding, conflicts, and approvals: confirmed.\n",
        encoding="utf-8",
    )

    without_pdf = preflight(declarations)
    assert without_pdf["repository_ready"] is True
    assert without_pdf["author_fields_ready"] is True
    assert without_pdf["literal_upload_ready"] is False

    with_pdf = preflight(declarations, pdf_visual_and_font_gate_confirmed=True)
    assert with_pdf["literal_upload_ready"] is True
