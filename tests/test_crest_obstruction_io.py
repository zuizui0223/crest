from __future__ import annotations

from math import log2

import pytest

from crest.obstruction_io import parse_obstruction_contract, spectrum_from_payload


def _cascade_payload() -> dict[str, object]:
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
                "successors": [[0], [4], [1], [4], [4], [4]],
            },
            {
                "name": "MRM",
                "static_labels": ["same"] * 6,
                "actions": ["mechanism"],
                "successors": [[0], [4], [4], [2], [4], [4]],
            },
        ],
    }


def test_json_contract_reproduces_canonical_three_obstruction_spectrum() -> None:
    result = spectrum_from_payload(_cascade_payload())

    assert result["audit_names"] == ["CCOC", "MLTR", "MRM"]
    assert result["baseline_blocks"] == 2
    assert result["joint_blocks"] == 5
    assert result["standalone_debts_bits"] == pytest.approx(
        {"CCOC": log2(3) - 1.0, "MLTR": 0.0, "MRM": 0.0}
    )
    assert result["joint_debt_bits"] == pytest.approx(log2(5) - 1.0)
    assert result["delta_bits"] == pytest.approx(log2(5 / 3))

    dividends = {
        tuple(row["audits"]): row["bits"]
        for row in result["interaction_dividends"]
    }
    assert dividends[("CCOC", "MLTR")] == pytest.approx(log2(4 / 3))
    assert dividends[("CCOC", "MLTR", "MRM")] == pytest.approx(log2(5 / 4))


def test_json_contract_rejects_carrier_mismatch() -> None:
    payload = _cascade_payload()
    payload["baseline"] = [0, 1]
    with pytest.raises(ValueError, match="share one finite carrier"):
        parse_obstruction_contract(payload)


def test_json_contract_rejects_missing_audits() -> None:
    with pytest.raises(ValueError, match="audits must be a nonempty JSON array"):
        parse_obstruction_contract({"baseline": [0, 0]})
