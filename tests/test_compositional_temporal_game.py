from __future__ import annotations

import pytest

from crest.compositional_temporal_game import (
    AXES,
    FUTURE,
    HISTORY,
    MECHANISM,
    compositional_contract_bits,
    compositional_contract_classes,
    compositional_temporal_summary,
    mobius_dividend,
)


def test_exact_coalition_values() -> None:
    m = 7
    assert compositional_contract_bits(m, ()) == 0
    assert compositional_contract_bits(m, (HISTORY,)) == 1
    assert compositional_contract_bits(m, (MECHANISM,)) == 1
    assert compositional_contract_bits(m, (FUTURE,)) == 0
    assert compositional_contract_bits(m, (HISTORY, MECHANISM)) == 2
    assert compositional_contract_bits(m, (HISTORY, FUTURE)) == 1
    assert compositional_contract_bits(m, (MECHANISM, FUTURE)) == 1
    assert compositional_contract_bits(m, AXES) == 9


def test_pairwise_dividends_zero_and_three_way_exact_m() -> None:
    for m in (1, 2, 5, 10, 18):
        assert mobius_dividend(m, (HISTORY, MECHANISM)) == 0
        assert mobius_dividend(m, (HISTORY, FUTURE)) == 0
        assert mobius_dividend(m, (MECHANISM, FUTURE)) == 0
        assert mobius_dividend(m, AXES) == m


def test_m10_endpoint_is_4096_classes_and_1024x_amplification() -> None:
    summary = compositional_temporal_summary(10)
    assert summary.history_bits == 1
    assert summary.mechanism_bits == 1
    assert summary.future_bits == 0
    assert summary.history_mechanism_bits == 2
    assert summary.history_future_bits == 1
    assert summary.mechanism_future_bits == 1
    assert summary.joint_bits == 12
    assert summary.interaction_bits == 10
    assert summary.three_way_bits == 10
    assert summary.history_mechanism_classes == 4
    assert summary.joint_classes == 4096
    assert summary.state_count_amplification == 1024
    assert summary.three_way_fraction_of_joint == pytest.approx(10 / 12)


def test_three_way_share_tends_to_one() -> None:
    assert compositional_temporal_summary(18).three_way_fraction_of_joint == pytest.approx(0.9)
    assert compositional_temporal_summary(98).three_way_fraction_of_joint == pytest.approx(0.98)


def test_class_count_matches_bit_count() -> None:
    for m in (1, 4, 9):
        for coalition in ((), (HISTORY,), (MECHANISM,), (FUTURE,), (HISTORY, MECHANISM), AXES):
            bits = compositional_contract_bits(m, coalition)
            assert compositional_contract_classes(m, coalition) == 2**bits


def test_unknown_axis_rejected() -> None:
    with pytest.raises(ValueError):
        compositional_contract_bits(3, ("UNKNOWN",))
