from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = (ROOT / "docs" / "island_urban_ecological_validation_registry_2026-08-24.md").read_text(encoding="utf-8")
INSERT = (ROOT / "manuscript" / "island_urban_examples_insert.md").read_text(encoding="utf-8")


def test_registry_contains_two_island_and_two_urban_cases() -> None:
    for heading in (
        "Case I-A — Mauritius",
        "Case I-B — Izu Islands",
        "Case U-A — White clover across 160 cities",
        "Case U-B — Urban pollinator connectivity",
    ):
        assert heading in REGISTRY


def test_every_case_uses_the_same_crest_validation_axes() -> None:
    for term in (
        "Present snapshot / tempting state",
        "Hidden distinction",
        "Future grammar",
        "Candidate coarse law",
        "CREST relevance",
        "Evidence grade",
    ):
        assert REGISTRY.count(term) >= 4


def test_primary_cases_have_direct_empirical_anchor_and_source_dois() -> None:
    for term in (
        "10.1016/j.cub.2011.03.042",
        "10.1038/s41467-023-36669-9",
        "10.1126/science.abk0989",
        "110,019",
        "6,169",
        "160 cities",
    ):
        assert term in REGISTRY
        assert term in INSERT or term in {"110,019", "6,169", "160 cities"}


def test_island_urban_pair_targets_different_but_comparable_failures() -> None:
    assert "interaction replaced = function restored" in REGISTRY
    assert "urban = one fitness law" in REGISTRY
    assert "physically isolated urban patches are functionally closed" in REGISTRY
    assert "Different fragmentation and replacement mechanisms can generate the same representational failure" in REGISTRY


def test_examples_are_not_misrepresented_as_mathematical_proof() -> None:
    for text in (REGISTRY, INSERT):
        lower = text.lower()
        assert "do not" in lower or "does not" in lower
        assert "proof of the finite crest theorem" in lower or "proof of the finite crest theorems" in lower


def test_insert_prioritizes_mauritius_and_white_clover_for_main_text() -> None:
    assert "**Island interaction replacement in Mauritius.**" in INSERT
    assert "**Adaptive law portability across cities.**" in INSERT
    assert "## Optional supporting box" in INSERT
    assert "Izu Islands *Campanula*" in INSERT
    assert "Urban pollinator connectivity" in INSERT
