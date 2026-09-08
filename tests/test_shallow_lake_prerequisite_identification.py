from pathlib import Path


DOC = Path("docs/shallow_lake_interface_prerequisite_identification_2026-09-08.md").read_text(
    encoding="utf-8"
)


def test_shallow_lake_worked_identification_contains_target_relative_prerequisites() -> None:
    for token in (
        r"R_A=\varnothing",
        r"R_B=\{H\}",
        r"R_C=\{\Theta\}",
        r"R_D=\{H,\Theta\}",
        "target-relative model identification",
        "counterfactual substitution",
    ):
        assert token in DOC


def test_shallow_lake_note_does_not_claim_empirical_universal_r() -> None:
    assert "not an empirical estimate of a universal prerequisite set" in DOC
    assert "does not claim" in DOC.lower()
    assert "universal across lakes" in DOC
