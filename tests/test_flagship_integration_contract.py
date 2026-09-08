from __future__ import annotations

import json
from math import log2
from pathlib import Path

import pytest

from crest.joint_debt import marked_cycle_report
from crest.sequential_witnesses import sharp_sequential_problem

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"
SECTION = ROOT / "docs" / "flagship_integration" / "joint_debt_delta_section.md"


def test_flagship_headline_is_joint_delta_not_component_no_bound() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 3
    assert manifest["canonical_flagship_manuscript"] == "manuscript/crest_flagship_amnat_v0.2.md"
    assert (ROOT / manifest["canonical_flagship_manuscript"]).is_file()
    assert manifest["headline"] == "non-additive joint ecological state debt"
    assert manifest["headline_quantity"] == "Delta = D_joint - sum_i D_i"
    assert manifest["headline_extremum"] == "Delta = log2(n) - 1"
    assert "classical substrate" in manifest["novelty_boundary"]
    assert any("H log2(r)" in item for item in manifest["supporting_results"])


def test_flagship_section_preserves_claim_firewall() -> None:
    text = SECTION.read_text(encoding="utf-8")
    assert "integration-only quantity" in text
    assert "responsibility-wise additive accounting" in text
    assert "does not claim that phenomenon itself as novel" in text
    assert "carrier-gain no-bound" in text
    assert "H\\log_2 r" in text


def test_flagship_marked_cycle_matches_declared_extremum() -> None:
    for n in (2, 3, 4, 8, 17, 32):
        report = marked_cycle_report(n)
        assert report.individual_debts == pytest.approx((1.0, 0.0))
        assert report.joint_debt == pytest.approx(log2(n))
        assert report.delta == pytest.approx(log2(n) - 1.0)


def test_sharp_sequential_family_is_exposed_from_package_surface() -> None:
    old_problem, addresses, _ = sharp_sequential_problem(3, 2, False)
    new_problem, new_addresses, _ = sharp_sequential_problem(3, 2, True)
    assert addresses == new_addresses
    assert len(addresses) == 9
    assert old_problem.controllable_actions == ("hold",)
    assert new_problem.controllable_actions == ("hold", "probe")
