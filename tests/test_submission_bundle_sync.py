from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_DIR = ROOT / "manuscript"
ARCHIVE = ROOT / "archive" / "graphify-cleanup-2026-08-24"
CANONICAL = {
    "crest_biology_philosophy_blinded_submission.md",
    "biology_philosophy_title_page_TEMPLATE.md",
    "SUBMISSION_README.md",
    "SUBMISSION_BLOCKERS_2026-08-24.md",
    "crest_canonical_scope_2026-08-24.md",
}


def test_manuscript_surface_is_single_and_canonical() -> None:
    assert {p.name for p in MANUSCRIPT_DIR.iterdir() if p.is_file()} == CANONICAL


def test_submission_entrypoints_name_the_blinded_candidate() -> None:
    readme = (MANUSCRIPT_DIR / "SUBMISSION_README.md").read_text(encoding="utf-8")
    verifier = (ROOT / "scripts" / "verify_crest_philosophy_submission.py").read_text(encoding="utf-8")
    assert "crest_biology_philosophy_blinded_submission.md" in readme
    assert 'TARGET = Path("manuscript/crest_biology_philosophy_blinded_submission.md")' in verifier
    assert "crest_philosophy_biology_philosophy.md" not in readme
    assert "crest_philosophy_biology_philosophy.md" not in verifier


def test_superseded_submission_material_is_archived() -> None:
    assert (ARCHIVE / "manuscript" / "crest_philosophy_biology_philosophy.md").is_file()
    assert (ARCHIVE / "manuscript" / "biology_philosophy_submission_handoff.md").is_file()
    assert (ARCHIVE / "tests" / "test_crest_frontier_manuscript_surface.py").is_file()
