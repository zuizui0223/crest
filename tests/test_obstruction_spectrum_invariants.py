from __future__ import annotations

import pytest

from crest.joint_debt import marked_cycle_audits
from crest.obstruction_spectrum_v1 import obstruction_spectrum


def test_shapley_spectrum_sums_to_joint_debt_on_marked_cycle_family() -> None:
    for state_count in (2, 3, 4, 8, 17):
        baseline, audits = marked_cycle_audits(state_count)
        report = obstruction_spectrum(audits, baseline)
        assert sum(report.shapley_contributions) == pytest.approx(report.joint_debt)
        assert sum(report.interaction_allocations) == pytest.approx(report.delta)
        assert report.verify()
