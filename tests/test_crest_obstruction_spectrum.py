from __future__ import annotations

from itertools import permutations
from math import log2

import pytest

from crest.joint_state import AuditRefinement
from crest.obstruction_spectrum import (
    obstruction_spectrum,
    three_obstruction_cascade,
    three_obstruction_spectrum,
)


def test_three_obstruction_cascade_has_numeric_spectrum() -> None:
    report = three_obstruction_spectrum()

    standalone_ccoc = log2(3) - 1.0
    joint = log2(5) - 1.0
    delta = joint - standalone_ccoc

    assert report.audit_names == ("CCOC", "MLTR", "MRM")
    assert report.baseline_blocks == 2
    assert report.joint_blocks == 5
    assert report.standalone_debts == pytest.approx(
        (standalone_ccoc, 0.0, 0.0)
    )
    assert report.joint_debt == pytest.approx(joint)
    assert report.delta == pytest.approx(delta)

    expected_shapley = (
        (standalone_ccoc / 3.0)
        + ((1.0 + standalone_ccoc) / 6.0)
        + (joint / 3.0),
        ((1.0 - standalone_ccoc) / 6.0)
        + ((joint - standalone_ccoc) / 3.0),
        (joint - 1.0) / 3.0,
    )
    assert report.shapley_contributions == pytest.approx(expected_shapley)
    assert sum(report.shapley_contributions) == pytest.approx(joint)
    assert sum(report.interaction_attributions) == pytest.approx(delta)
    assert sum(report.shapley_shares) == pytest.approx(1.0)


def test_three_obstruction_coalitions_show_activation_cascade() -> None:
    report = three_obstruction_spectrum()
    coalition_blocks = {row.audits: row.blocks for row in report.coalition_debts}

    assert coalition_blocks == {
        (): 2,
        ("CCOC",): 3,
        ("MLTR",): 2,
        ("MRM",): 2,
        ("CCOC", "MLTR"): 4,
        ("CCOC", "MRM"): 3,
        ("MLTR", "MRM"): 2,
        ("CCOC", "MLTR", "MRM"): 5,
    }


def test_shapley_spectrum_is_invariant_to_audit_input_order() -> None:
    baseline, audits = three_obstruction_cascade()
    reference = three_obstruction_spectrum()
    reference_shapley = dict(
        zip(reference.audit_names, reference.shapley_contributions)
    )
    reference_standalone = dict(
        zip(reference.audit_names, reference.standalone_debts)
    )

    for ordering in permutations(audits):
        report = obstruction_spectrum(ordering, baseline)
        assert report.joint_debt == pytest.approx(reference.joint_debt)
        assert report.delta == pytest.approx(reference.delta)
        assert dict(zip(report.audit_names, report.shapley_contributions)) == pytest.approx(
            reference_shapley
        )
        assert dict(zip(report.audit_names, report.standalone_debts)) == pytest.approx(
            reference_standalone
        )


def test_obstruction_spectrum_rejects_duplicate_audit_names() -> None:
    baseline, audits = three_obstruction_cascade()
    ccoc = audits[0]
    duplicate = AuditRefinement(
        ccoc.name,
        ccoc.static_labels,
        ccoc.actions,
        ccoc.successors,
    )
    with pytest.raises(ValueError, match="audit names must be unique"):
        obstruction_spectrum((ccoc, duplicate), baseline)
