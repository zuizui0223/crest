from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (ROOT / "manuscript" / "empirical_validation_bridge_note.md").read_text(encoding="utf-8")


def test_bridge_contains_city_sign_reversals_and_context_recovery() -> None:
    assert "varied in sign and strength" in NOTE
    assert "100/100 fits" in NOTE
    assert "coarse quotient is falsified" in NOTE
    assert "substantial unresolved state variation remains" in NOTE


def test_bridge_contains_mauritius_functional_replacement_contrast() -> None:
    assert "seed dispersal can be replaced by seed predation" in NOTE
    assert "Aldabra giant tortoises" in NOTE
    assert "interaction topology alone is too coarse" in NOTE


def test_bridge_preserves_empirical_theorem_firewall() -> None:
    assert "ecological anchors, not proofs of the finite CREST theorems" in NOTE
