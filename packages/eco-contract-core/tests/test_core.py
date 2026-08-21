import pytest

from eco_contract_core import (
    FiniteActionSystem,
    canonical_partition,
    deterministic_fingerprint,
    refine_partition,
    replay,
)


def demo_system():
    return FiniteActionSystem(
        states=("a", "b", "c"),
        actions=("go", "stay"),
        transitions={
            ("a", "go"): "c",
            ("b", "go"): "c",
            ("c", "stay"): "c",
        },
        outputs={"a": 0, "b": 0, "c": 1},
    )


def test_canonical_partition_rejects_overlap():
    with pytest.raises(ValueError):
        canonical_partition([("a", "b"), ("b", "c")])


def test_refinement_keeps_behaviorally_equal_states_together():
    system = demo_system()
    refined = refine_partition(system, canonical_partition([system.states]))
    assert frozenset({"a", "b"}) in refined
    assert frozenset({"c"}) in refined


def test_replay_is_deterministic():
    system = demo_system()
    assert replay(system, "a", ["go", "stay"]) == ("a", "c", "c")


def test_fingerprint_is_order_stable_for_mapping_keys():
    assert deterministic_fingerprint({"a": 1, "b": 2}) == deterministic_fingerprint({"b": 2, "a": 1})
