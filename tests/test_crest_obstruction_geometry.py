from __future__ import annotations

from math import log2

import pytest

from crest.obstruction_geometry import pairwise_obstruction_distances


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
                    [0], [4], [1 if mltr_active else 4], [4], [4], [4]
                ],
            },
            {
                "name": "MRM",
                "static_labels": ["same"] * 6,
                "actions": ["mechanism"],
                "successors": [
                    [0], [4], [4], [2 if mrm_active else 4], [4], [4]
                ],
            },
        ],
    }


def test_pairwise_geometry_orders_cascade_path() -> None:
    result = pairwise_obstruction_distances(
        {
            "inert": _contract(mltr_active=False, mrm_active=False),
            "pair": _contract(mltr_active=True, mrm_active=False),
            "full": _contract(mltr_active=True, mrm_active=True),
        }
    )

    matrix = result["matrix"]
    capacity = log2(3)
    pair_step = log2(4 / 3) / capacity
    triple_step = log2(5 / 4) / capacity

    assert result["metric"] == "normalized_l1"
    assert matrix["inert"]["inert"] == pytest.approx(0.0)
    assert matrix["inert"]["pair"] == pytest.approx(pair_step)
    assert matrix["pair"]["full"] == pytest.approx(triple_step)
    assert matrix["inert"]["full"] == pytest.approx(pair_step + triple_step)
    assert matrix["inert"]["full"] == pytest.approx(matrix["full"]["inert"])

    assert result["nearest_neighbors"]["inert"]["name"] == "pair"
    assert result["nearest_neighbors"]["pair"]["name"] == "full"
    assert result["nearest_neighbors"]["full"]["name"] == "pair"


def test_pairwise_geometry_can_use_raw_bits() -> None:
    result = pairwise_obstruction_distances(
        {
            "inert": _contract(mltr_active=False, mrm_active=False),
            "full": _contract(mltr_active=True, mrm_active=True),
        },
        metric="raw_l1_bits",
    )
    assert result["matrix"]["inert"]["full"] == pytest.approx(log2(5 / 3))


def test_pairwise_geometry_requires_same_responsibility_names() -> None:
    other = _contract(mltr_active=True, mrm_active=True)
    other["audits"][2]["name"] = "OTHER"  # type: ignore[index]
    with pytest.raises(ValueError, match="same audit names"):
        pairwise_obstruction_distances(
            {
                "a": _contract(mltr_active=False, mrm_active=False),
                "b": other,
            }
        )


def test_pairwise_geometry_rejects_unknown_metric() -> None:
    with pytest.raises(ValueError, match="metric"):
        pairwise_obstruction_distances(
            {"a": _contract(mltr_active=False, mrm_active=False)},
            metric="unknown",
        )
