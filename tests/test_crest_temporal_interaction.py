from __future__ import annotations

from math import log2

import pytest

from crest.temporal_interaction import (
    FUTURE,
    HISTORY,
    LATENT_PRESENT,
    past_future_report,
    temporal_three_way_closed_form,
    temporal_three_way_report,
)


def _dividend_map(report):
    return {tuple(row.audits): row.bits for row in report.interaction_dividends}


def _coalition_blocks(report):
    return {tuple(row.audits): row.blocks for row in report.coalition_debts}


def test_past_future_interaction_is_unbounded() -> None:
    for state_count in (2, 3, 4, 8, 17, 1024):
        report = past_future_report(state_count)
        dividends = _dividend_map(report)

        assert report.audit_names == (HISTORY, FUTURE)
        assert report.baseline_blocks == 1
        assert report.joint_blocks == state_count
        assert report.standalone_debts == pytest.approx((1.0, 0.0))
        assert report.joint_debt == pytest.approx(log2(state_count))
        assert report.delta == pytest.approx(log2(state_count) - 1.0)
        assert dividends[(HISTORY, FUTURE)] == pytest.approx(
            log2(state_count) - 1.0
        )


def test_temporal_three_way_family_has_exact_coalition_structure() -> None:
    for bit_depth in (2, 3, 4, 6, 10):
        report = temporal_three_way_report(bit_depth)
        blocks = _coalition_blocks(report)

        assert report.audit_names == (HISTORY, LATENT_PRESENT, FUTURE)
        assert report.baseline_blocks == 1
        assert report.joint_blocks == 2**bit_depth
        assert report.standalone_debts == pytest.approx((1.0, 0.0, 0.0))
        assert report.joint_debt == pytest.approx(float(bit_depth))
        assert report.delta == pytest.approx(float(bit_depth - 1))
        assert blocks == {
            (): 1,
            (HISTORY,): 2,
            (LATENT_PRESENT,): 1,
            (FUTURE,): 1,
            (HISTORY, LATENT_PRESENT): 3,
            (HISTORY, FUTURE): 2,
            (LATENT_PRESENT, FUTURE): 1,
            (HISTORY, LATENT_PRESENT, FUTURE): 2**bit_depth,
        }


def test_genuine_three_way_temporal_dividend_is_unbounded() -> None:
    for bit_depth in (2, 3, 4, 6, 10):
        report = temporal_three_way_report(bit_depth)
        dividends = _dividend_map(report)

        assert dividends[(HISTORY,)] == pytest.approx(1.0)
        assert dividends[(LATENT_PRESENT,)] == pytest.approx(0.0)
        assert dividends[(FUTURE,)] == pytest.approx(0.0)
        assert dividends[(HISTORY, LATENT_PRESENT)] == pytest.approx(
            log2(3.0 / 2.0)
        )
        assert dividends[(HISTORY, FUTURE)] == pytest.approx(0.0)
        assert dividends[(LATENT_PRESENT, FUTURE)] == pytest.approx(0.0)
        assert dividends[(HISTORY, LATENT_PRESENT, FUTURE)] == pytest.approx(
            bit_depth - log2(3.0)
        )


def test_three_way_interaction_asymptotically_dominates_joint_debt() -> None:
    previous = 0.0
    for bit_depth in (2, 3, 4, 6, 10, 20):
        closed = temporal_three_way_closed_form(bit_depth)
        share = closed["three_way_fraction_of_joint"]
        assert share >= previous
        previous = share

    closed_10 = temporal_three_way_closed_form(10)
    assert closed_10["joint_blocks"] == 1024
    assert closed_10["joint_debt_bits"] == pytest.approx(10.0)
    assert closed_10["interaction_bits"] == pytest.approx(9.0)
    assert closed_10["interaction_fraction_of_joint"] == pytest.approx(0.9)
    assert closed_10["three_way_bits"] == pytest.approx(8.415037499278844)
    assert closed_10["three_way_fraction_of_joint"] == pytest.approx(
        0.8415037499278844
    )
    assert closed_10["three_way_fraction_of_interaction"] == pytest.approx(
        0.9350041665865382
    )


def test_temporal_family_validation() -> None:
    for value in (0, 1, -1, True):
        with pytest.raises(ValueError):
            temporal_three_way_report(value)
    for value in (0, 1, -1, True):
        with pytest.raises(ValueError):
            past_future_report(value)
