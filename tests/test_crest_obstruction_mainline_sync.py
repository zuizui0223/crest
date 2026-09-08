from __future__ import annotations

from pathlib import Path


SURFACES = (
    Path("README.md"),
    Path("docs/crest_mathematical_spine.md"),
    Path("manuscript/crest_flagship_amnat_v0.2.md"),
)


def test_mainline_surfaces_share_canonical_obstruction_change_numbers() -> None:
    required_numeric = (
        "0.7369655942",
        "0.4150374993",
        "0.3219280949",
    )
    for path in SURFACES:
        text = path.read_text(encoding="utf-8")
        for token in required_numeric:
            assert token in text, f"{path} is missing canonical obstruction value {token}"
        assert "interaction-only" in text, f"{path} is missing interaction-only diagnosis"


def test_theorem_and_readme_surfaces_expose_order_diagnosis() -> None:
    readme = Path("README.md").read_text(encoding="utf-8")
    spine = Path("docs/crest_mathematical_spine.md").read_text(encoding="utf-8")

    for text in (readme, spine):
        assert "active_interaction_orders" in text or "active interaction orders" in text
        assert "dominant" in text.lower()
        assert "[2, 3]" in text


def test_flagship_keeps_static_delta_headline_and_change_as_follow_on() -> None:
    text = Path("manuscript/crest_flagship_amnat_v0.2.md").read_text(encoding="utf-8")
    assert "### Theorem 1 — unbounded non-additive joint debt" in text
    assert "### Theorem 2 — zero individual debt cannot hide joint debt" in text
    assert "### Quantitative corollary — representational change can be interaction-only" in text
    assert text.index("### Theorem 1") < text.index("### Quantitative corollary")
