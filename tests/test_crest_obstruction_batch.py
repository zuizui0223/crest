from __future__ import annotations

import pytest

from crest.obstruction_batch import rank_obstruction_contracts


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


def test_batch_ranks_cascade_above_inert_by_normalized_burden() -> None:
    result = rank_obstruction_contracts(
        {"inert": _contract(cascade=False), "cascade": _contract(cascade=True)}
    )
    rows = result["rows"]

    assert result["rank_by"] == "normalized_joint_burden"
    assert [row["name"] for row in rows] == ["cascade", "inert"]
    assert rows[0]["normalized_joint_burden"] == pytest.approx(0.8340437671464697)
    assert rows[0]["interaction_fraction_of_joint"] == pytest.approx(
        0.5574929506502401
    )
    assert rows[0]["active_interaction_orders"] == [2, 3]
    assert rows[0]["dominant_interaction_order"] == 2
    assert rows[1]["interaction_fraction_of_joint"] == pytest.approx(0.0)


def test_batch_can_rank_by_interaction_fraction() -> None:
    result = rank_obstruction_contracts(
        {"inert": _contract(cascade=False), "cascade": _contract(cascade=True)},
        rank_by="interaction_fraction_of_joint",
    )
    assert [row["name"] for row in result["rows"]] == ["cascade", "inert"]


def test_batch_requires_same_responsibility_names() -> None:
    other = _contract(cascade=False)
    other["audits"][2]["name"] = "OTHER"  # type: ignore[index]
    with pytest.raises(ValueError, match="same audit names"):
        rank_obstruction_contracts({"a": _contract(cascade=True), "b": other})


def test_batch_rejects_unknown_rank_key() -> None:
    with pytest.raises(ValueError, match="rank_by"):
        rank_obstruction_contracts({"a": _contract(cascade=True)}, rank_by="unknown")
