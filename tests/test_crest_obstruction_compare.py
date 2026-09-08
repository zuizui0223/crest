from __future__ import annotations

from math import log2

import pytest

from crest.obstruction_compare import compare_contract_payloads, compare_spectrum_payloads
from crest.obstruction_io import spectrum_from_payload


def _contract(*, cascade: bool) -> dict[str, object]:
    mltr_successor = 1 if cascade else 4
    mrm_successor = 2 if cascade else 4
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
                "successors": [[0], [4], [mltr_successor], [4], [4], [4]],
            },
            {
                "name": "MRM",
                "static_labels": ["same"] * 6,
                "actions": ["mechanism"],
                "successors": [[0], [4], [4], [mrm_successor], [4], [4]],
            },
        ],
    }


def test_compare_contracts_quantifies_emergent_interaction_burden() -> None:
    result = compare_contract_payloads(_contract(cascade=False), _contract(cascade=True))
    comparison = result["comparison"]

    assert comparison["joint_blocks"] == {"before": 3, "after": 5, "change": 2}
    assert comparison["joint_debt_change_bits"] == pytest.approx(log2(5 / 3))
    assert comparison["delta_change_bits"] == pytest.approx(log2(5 / 3))
    assert comparison["standalone_change_bits"] == pytest.approx(
        {"CCOC": 0.0, "MLTR": 0.0, "MRM": 0.0}
    )

    dividends = {
        tuple(row["audits"]): row["change_bits"]
        for row in comparison["interaction_dividend_change_bits"]
    }
    assert dividends[("CCOC", "MLTR")] == pytest.approx(log2(4 / 3))
    assert dividends[("CCOC", "MLTR", "MRM")] == pytest.approx(log2(5 / 4))
    assert sum(value for coalition, value in dividends.items() if len(coalition) >= 2) == pytest.approx(
        comparison["delta_change_bits"]
    )


def test_compare_spectra_requires_same_named_responsibilities() -> None:
    before = spectrum_from_payload(_contract(cascade=False))
    after = spectrum_from_payload(_contract(cascade=True))
    after["audit_names"] = ["CCOC", "MLTR", "OTHER"]
    with pytest.raises(ValueError, match="same audit names"):
        compare_spectrum_payloads(before, after)
