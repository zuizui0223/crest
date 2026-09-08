from __future__ import annotations

from math import log2

import pytest

from crest.obstruction_normalized import normalized_obstruction_metrics
from crest.obstruction_spectrum import three_obstruction_spectrum


def test_canonical_normalized_obstruction_metrics() -> None:
    report = three_obstruction_spectrum()
    metrics = normalized_obstruction_metrics(report, carrier_worlds=6)

    capacity = log2(6 / 2)
    joint = log2(5 / 2)
    delta = log2(5 / 3)
    order2 = log2(4 / 3)
    order3 = log2(5 / 4)

    assert metrics.capacity_bits == pytest.approx(capacity)
    assert metrics.normalized_joint_burden == pytest.approx(joint / capacity)
    assert metrics.interaction_fraction_of_joint == pytest.approx(delta / joint)
    assert metrics.direct_fraction_of_joint == pytest.approx((log2(3 / 2)) / joint)
    assert metrics.interaction_order_bits == pytest.approx({2: order2, 3: order3})
    assert metrics.interaction_order_absolute_shares == pytest.approx(
        {2: order2 / delta, 3: order3 / delta}
    )
    assert metrics.active_interaction_orders == (2, 3)
    assert metrics.dominant_interaction_order == 2
    assert metrics.verify()


def test_normalized_joint_burden_is_one_at_discrete_limit() -> None:
    report = three_obstruction_spectrum()
    metrics = normalized_obstruction_metrics(report, carrier_worlds=5)
    assert metrics.normalized_joint_burden == pytest.approx(1.0)


def test_normalization_rejects_impossible_carrier_size() -> None:
    report = three_obstruction_spectrum()
    with pytest.raises(ValueError, match="carrier_worlds"):
        normalized_obstruction_metrics(report, carrier_worlds=1)
