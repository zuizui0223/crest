from __future__ import annotations

from math import log2

import pytest

from crest.joint_state import AuditRefinement
from crest.obstruction_spectrum_v1 import obstruction_spectrum


def _three_obstruction_cascade():
    """Five-world CCOC -> MLTR -> MRM activation cascade.

    Baseline has two classes: z | a,b,c,r.
    CCOC marks a; MLTR can then distinguish b because b points to a;
    MRM can then distinguish c because c points to b.
    """

    baseline = (0, 1, 1, 1, 1)

    ccoc = AuditRefinement(
        "CCOC",
        ("ordinary", "future-mark", "ordinary", "ordinary", "ordinary"),
        (),
        ((), (), (), (), ()),
    )

    mltr = AuditRefinement(
        "MLTR",
        ("same",) * 5,
        ("history",),
        (
            (0,),  # z -> z
            (4,),  # a -> r
            (1,),  # b -> a; activated once CCOC separates a
            (4,),  # c -> r
            (4,),  # r -> r
        ),
    )

    mrm = AuditRefinement(
        "MRM",
        ("same",) * 5,
        ("mechanism",),
        (
            (0,),  # z -> z
            (4,),  # a -> r
            (4,),  # b -> r
            (2,),  # c -> b; activated once MLTR separates b
            (4,),  # r -> r
        ),
    )
    return baseline, (ccoc, mltr, mrm)


def _coalition_map(report):
    return {names: debt for names, debt in report.coalition_debts}


def test_three_obstruction_cascade_has_numeric_spectrum() -> None:
    baseline, audits = _three_obstruction_cascade()
    report = obstruction_spectrum(audits, baseline)
    coalition = _coalition_map(report)

    assert report.baseline_blocks == 2
    assert report.joint_blocks == 5
    assert report.standalone_debts == pytest.approx((log2(3 / 2), 0.0, 0.0))
    assert coalition[("CCOC", "MLTR")] == pytest.approx(1.0)
    assert coalition[("CCOC", "MRM")] == pytest.approx(log2(3 / 2))
    assert coalition[("MLTR", "MRM")] == pytest.approx(0.0)
    assert report.joint_debt == pytest.approx(log2(5 / 2))
    assert report.delta == pytest.approx(log2(5 / 3))

    # Exact Shapley attribution over all 3! insertion orders.
    expected_ccoc = (
        log2(3 / 2) / 3
        + (1.0 + log2(3 / 2)) / 6
        + log2(5 / 2) / 3
    )
    expected_mltr = (1.0 - log2(3 / 2)) / 6 + log2(5 / 3) / 3
    expected_mrm = log2(5 / 4) / 3
    assert report.shapley_contributions == pytest.approx(
        (expected_ccoc, expected_mltr, expected_mrm)
    )
    assert sum(report.shapley_contributions) == pytest.approx(report.joint_debt)
    assert sum(report.interaction_allocations) == pytest.approx(report.delta)


def test_spectrum_is_invariant_to_supplied_audit_order_up_to_name_reindexing() -> None:
    baseline, audits = _three_obstruction_cascade()
    forward = obstruction_spectrum(audits, baseline)
    reverse = obstruction_spectrum(tuple(reversed(audits)), baseline)

    forward_by_name = dict(zip(forward.audit_names, forward.shapley_contributions))
    reverse_by_name = dict(zip(reverse.audit_names, reverse.shapley_contributions))
    assert reverse_by_name == pytest.approx(forward_by_name)
    assert reverse.joint_debt == pytest.approx(forward.joint_debt)
    assert reverse.delta == pytest.approx(forward.delta)
