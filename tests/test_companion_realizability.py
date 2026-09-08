from __future__ import annotations

import pytest

from crest.companion_realizability import (
    audit_preserves_label,
    immutable_history_blocks_activation,
    mrm_observation_partition_is_candidate_safe,
    mrm_zero_debt_implies_single_response_type,
    one_block_fixed_partition_interaction_bits,
    response_type_count,
    sharp_family_companion_audit,
)
from crest.joint_state import AuditRefinement


def test_fixed_precomputed_partitions_cannot_have_positive_interaction_from_one_cut_class() -> None:
    partitions = (
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
    )
    interaction = one_block_fixed_partition_interaction_bits(partitions)
    assert interaction == pytest.approx(-1.0)
    assert interaction <= 0.0


def test_immutable_history_prevents_zero_debt_future_activation() -> None:
    history = (0, 0, 1, 1)
    future = AuditRefinement(
        "FUTURE",
        ("same",) * 4,
        ("step",),
        (
            (1,),
            (0,),
            (3,),
            (2,),
        ),
    )
    assert audit_preserves_label(future, history)
    assert immutable_history_blocks_activation(history, future)
    assert future.close(history) == history


def test_existing_pairwise_sharp_cycle_is_not_literal_immutable_history() -> None:
    audit = sharp_family_companion_audit(4)
    assert audit.pairwise_future_is_inert
    assert not audit.pairwise_future_preserves_history
    assert not audit.pairwise_literal_immutable_history_realizable


def test_existing_three_way_latent_edge_is_not_literal_immutable_history() -> None:
    audit = sharp_family_companion_audit(4)
    assert audit.triple_latent_is_inert
    assert not audit.triple_latent_preserves_history
    assert not audit.triple_literal_immutable_history_realizable


def test_fixed_grammar_mrm_zero_debt_implies_one_response_type() -> None:
    tables = {
        "theta0": {"hold": (0, 1), "flip": (1, 0)},
        "theta1": {"hold": (0, 1), "flip": (1, 0)},
    }
    assert mrm_observation_partition_is_candidate_safe(tables)
    assert response_type_count(tables) == 1
    assert mrm_zero_debt_implies_single_response_type(tables)


def test_nontrivial_mrm_response_types_force_standalone_candidate_refinement() -> None:
    tables = {
        "theta0": {"probe": (0, 0)},
        "theta1": {"probe": (1, 1)},
    }
    assert response_type_count(tables) == 2
    assert not mrm_observation_partition_is_candidate_safe(tables)
    # The implication is true vacuously when zero-debt stability is false.
    assert mrm_zero_debt_implies_single_response_type(tables)


def test_sharp_family_audit_validates_input() -> None:
    with pytest.raises(ValueError):
        sharp_family_companion_audit(1)
