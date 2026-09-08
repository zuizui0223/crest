from __future__ import annotations

from math import log2, sqrt

import pytest

from crest.obstruction_distance import (
    compare_obstruction_profiles,
    distance_contract_payloads,
)
from crest.obstruction_io import spectrum_from_payload


def _contract(*, mltr_active: bool, mrm_active: bool) -> dict[str, object]:
    return {
        "baseline": [0, 1, 1, 1, 1, 1],
        "audits": [
            {
                "name": "CCOC",
                "static_labels": ["same"] * 6,
                "actions": ["future"],
                "successors": [[0], [0], [4], [4], [4], [4]],
            },
            {
                "name": "MLTR",
                "static_labels": ["same"] * 6,
                "actions": ["inheritance"],
                "successors": [
                    [0],
                    [4],
                    [1 if mltr_active else 4],
                    [4],
                    [4],
                    [4],
                ],
            },
            {
                "name": "MRM",
                "static_labels": ["same"] * 6,
                "actions": ["mechanism"],
                "successors": [
                    [0],
                    [4],
                    [4],
                    [2 if mrm_active else 4],
                    [4],
                    [4],
                ],
            },
        ],
    }


def test_distance_is_interaction_only_for_canonical_activation() -> None:
    inert = _contract(mltr_active=False, mrm_active=False)
    full = _contract(mltr_active=True, mrm_active=True)
    result = distance_contract_payloads(inert, full)["distance"]

    capacity = log2(3)
    pair = log2(4 / 3)
    triple = log2(5 / 4)
    raw_l1 = pair + triple
    raw_l2 = sqrt(pair * pair + triple * triple)

    assert result["difference_class"] == "interaction-only"
    assert result["raw_l1_bits"] == pytest.approx(raw_l1)
    assert result["raw_l2_bits"] == pytest.approx(raw_l2)
    assert result["normalized_l1"] == pytest.approx(raw_l1 / capacity)
    assert result["normalized_l2"] == pytest.approx(raw_l2 / capacity)
    assert result["direct_raw_l1_bits"] == pytest.approx(0.0)
    assert result["interaction_raw_l1_bits"] == pytest.approx(raw_l1)
    assert result["direct_normalized_l1"] == pytest.approx(0.0)
    assert result["interaction_normalized_l1"] == pytest.approx(raw_l1 / capacity)
    assert result["dominant_changed_coalition"] == ["CCOC", "MLTR"]


def test_distance_is_symmetric_and_zero_on_identical_profile() -> None:
    inert = spectrum_from_payload(_contract(mltr_active=False, mrm_active=False))
    full = spectrum_from_payload(_contract(mltr_active=True, mrm_active=True))

    forward = compare_obstruction_profiles(inert, full)
    reverse = compare_obstruction_profiles(full, inert)
    identity = compare_obstruction_profiles(full, full)

    assert forward.raw_l1_bits == pytest.approx(reverse.raw_l1_bits)
    assert forward.raw_l2_bits == pytest.approx(reverse.raw_l2_bits)
    assert forward.normalized_l1 == pytest.approx(reverse.normalized_l1)
    assert forward.normalized_l2 == pytest.approx(reverse.normalized_l2)
    assert forward.difference_class() == reverse.difference_class() == "interaction-only"

    assert identity.raw_l1_bits == pytest.approx(0.0)
    assert identity.raw_l2_bits == pytest.approx(0.0)
    assert identity.normalized_l1 == pytest.approx(0.0)
    assert identity.normalized_l2 == pytest.approx(0.0)
    assert identity.difference_class() == "null"
    assert identity.dominant_changed_coalition() is None


def test_l1_profile_distance_obeys_triangle_inequality_on_cascade_path() -> None:
    inert = spectrum_from_payload(_contract(mltr_active=False, mrm_active=False))
    pair_only = spectrum_from_payload(_contract(mltr_active=True, mrm_active=False))
    full = spectrum_from_payload(_contract(mltr_active=True, mrm_active=True))

    d02 = compare_obstruction_profiles(inert, full)
    d01 = compare_obstruction_profiles(inert, pair_only)
    d12 = compare_obstruction_profiles(pair_only, full)

    assert d02.raw_l1_bits <= d01.raw_l1_bits + d12.raw_l1_bits + 1e-12
    assert d02.normalized_l1 <= d01.normalized_l1 + d12.normalized_l1 + 1e-12
    assert d02.raw_l1_bits == pytest.approx(d01.raw_l1_bits + d12.raw_l1_bits)
    assert d02.normalized_l1 == pytest.approx(d01.normalized_l1 + d12.normalized_l1)


def test_distance_requires_same_named_responsibilities() -> None:
    before = spectrum_from_payload(_contract(mltr_active=False, mrm_active=False))
    after = spectrum_from_payload(_contract(mltr_active=True, mrm_active=True))
    after["audit_names"] = ["CCOC", "MLTR", "OTHER"]

    with pytest.raises(ValueError, match="same audit names"):
        compare_obstruction_profiles(before, after)
