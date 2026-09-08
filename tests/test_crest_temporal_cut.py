from __future__ import annotations

import pytest

from crest.temporal_cut import TemporalCutContract
from crest.temporal_interaction import temporal_three_way_cascade


def _canonical_cut(bit_depth: int) -> TemporalCutContract:
    baseline, audits = temporal_three_way_cascade(bit_depth)
    worlds = tuple(f"w{index}" for index in range(len(baseline)))
    history, latent_present, future = audits
    return TemporalCutContract(
        worlds=worlds,
        cut_observations=tuple("same-visible-cut" for _ in baseline),
        history=history,
        latent_present=latent_present,
        future=future,
    )


def test_present_is_an_observation_cut_not_an_extra_axis() -> None:
    contract = _canonical_cut(4)

    assert contract.baseline == tuple("same-visible-cut" for _ in contract.worlds)
    assert contract.fiber("same-visible-cut") == contract.worlds
    assert contract.fiber("missing") == ()


def test_latent_fiber_can_hide_large_joint_state_resolution() -> None:
    contract = _canonical_cut(10)
    report = contract.spectrum()

    assert len(contract.fiber("same-visible-cut")) == 2**10 + 1
    assert report.baseline_blocks == 1
    assert report.joint_blocks == 2**10
    assert report.joint_debt == pytest.approx(10.0)
    assert report.delta == pytest.approx(9.0)


def test_temporal_cut_validates_carrier_alignment_and_names() -> None:
    baseline, audits = temporal_three_way_cascade(2)
    history, latent_present, future = audits
    worlds = tuple(range(len(baseline)))

    with pytest.raises(ValueError, match="cut observations"):
        TemporalCutContract(
            worlds=worlds,
            cut_observations=("x",),
            history=history,
            latent_present=latent_present,
            future=future,
        )
