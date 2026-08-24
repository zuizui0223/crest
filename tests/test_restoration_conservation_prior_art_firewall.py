from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "docs" / "restoration_conservation_prior_art_positioning_2026-08-24.md").read_text(encoding="utf-8")


def test_nearest_neighbor_families_are_explicit() -> None:
    for term in (
        "Society for Ecological Restoration standards",
        "Ecological memory, history and legacy",
        "State-and-Transition Models and threshold frameworks",
        "Restoration as an experimental test of ecological theory",
    ):
        assert term in DOC


def test_key_prior_art_sources_are_recorded() -> None:
    for term in (
        "10.1111/rec.70441",
        "10.1016/j.biocon.2014.05.007",
        "10.1111/rec.13411",
        "10.2307/4003893",
        "10.1111/2041-210X.70164",
        "10.1111/j.1461-0248.2005.00764.x",
    ):
        assert term in DOC


def test_safe_novelty_is_cross_gate_not_generic_restoration_state() -> None:
    assert "cross-gate formal separation and no-bound construction" in DOC
    assert "not the individual ecological ingredients" in DOC
    assert "\\Delta|K^*|=1" in DOC
    assert "\\Delta K_{U_0}=m" in DOC


def test_blocked_overclaims_are_retained() -> None:
    for term in (
        "CREST shows for the first time that restoration depends on history",
        "CREST introduces intervention-dependent ecological states",
        "CREST is the first framework to connect states and restoration management",
        "CREST discovers that monitoring requirements depend on restoration goals",
        "CREST proves that real restoration projects have unbounded monitoring cost",
    ):
        assert term in DOC
