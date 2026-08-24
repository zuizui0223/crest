from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = (ROOT / "docs" / "restoration_conservation_cross_domain_validation_2026-08-24.md").read_text(encoding="utf-8")
INSERT = (ROOT / "manuscript" / "restoration_conservation_examples_insert.md").read_text(encoding="utf-8")
MANUSCRIPT = (ROOT / "manuscript" / "crest_philosophy_biology_philosophy.md").read_text(encoding="utf-8")


def test_restoration_mainline_has_four_independent_domains() -> None:
    for term in (
        "Case R1 — Dam removal",
        "Case R2 — Invasive-plant removal",
        "Case R3 — Peatland rewetting",
        "Case R4 — Prescribed-fire reintroduction",
    ):
        assert term in REGISTRY


def test_each_case_maps_to_crest_layers() -> None:
    for term in (
        "Feasible ecological worlds",
        "Required state",
        "Evidence-identified state",
        "Reportable target",
    ):
        assert REGISTRY.count(term) >= 4


def test_primary_source_anchors_are_recorded() -> None:
    for term in (
        "10.1111/rec.70441",
        "10.1002/edn3.134",
        "10.1111/j.1365-2664.2009.01610.x",
        "10.1007/s10530-008-9295-1",
        "10.1111/avsc.12626",
        "10.1016/j.ecoleng.2020.105852",
        "10.1038/s41598-024-60462-3",
        "10.1139/X06-315",
    ):
        assert term in REGISTRY
        assert term in INSERT

    assert "Urbanová and Bárta 2020" in INSERT
    assert "Juottonen et al. 2020" not in INSERT


def test_cross_domain_motif_is_not_generic_heterogeneity() -> None:
    assert "The recurring pattern is therefore not merely `restoration outcomes vary`" in REGISTRY
    assert "new restoration capability" in REGISTRY
    assert "new response-relevant distinctions" in REGISTRY
    assert "required-state refinement" in REGISTRY
    assert "possible monitoring inadequacy" in REGISTRY


def test_island_urban_are_explicitly_demoted_from_primary_arc() -> None:
    assert "Island and urban cases remain useful application material" in REGISTRY
    assert "no longer the primary ecological narrative" in REGISTRY


def test_empirical_cases_do_not_claim_theorem_proof() -> None:
    for text in (REGISTRY, INSERT):
        lower = text.lower()
        assert "do not prove" in lower or "does not prove" in lower
        assert "finite" in lower


def test_manuscript_insert_has_three_main_and_one_replication() -> None:
    for term in (
        "Dam removal",
        "Invasive-species control",
        "Peatland rewetting",
        "Independent recurrence in prescribed fire",
    ):
        assert term in INSERT


def test_restoration_projection_is_integrated_into_canonical_manuscript() -> None:
    assert "### 3.5 Restoration as a cross-domain ecological projection" in MANUSCRIPT
    assert "stronger than the generic observation that restoration outcomes vary" in MANUSCRIPT
    assert "weaker than an end-to-end empirical test of CREST" in MANUSCRIPT
    assert "Urbanová and Bárta 2020" in MANUSCRIPT
    assert "Juottonen et al. 2020" not in MANUSCRIPT
