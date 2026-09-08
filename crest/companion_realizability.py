"""Exact checks for literal companion realizability at a temporal cut.

The temporal interaction witnesses in :mod:`crest.temporal_interaction` are exact
closure-theoretic constructions.  This module asks a stricter question: when may
one interpret those closures literally as MLTR history, MRM latent response type,
and CCOC future responsibility without violating the companion quantifiers?

The results here are deliberately conservative.  They identify two no-go facts:

1. an immutable past label cannot activate a future-stability closure that is
   already inert on the visible baseline when all post-cut transitions preserve
   that past label; and
2. a nontrivial fixed-grammar MRM response-type family cannot have zero
   candidate-safe debt relative to its own observable-state partition.

These facts do not invalidate the generic CREST closure theorems.  They delimit
what still requires a cross-companion bridge construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log2
from typing import Hashable, Iterable, Mapping, Sequence

from .joint_state import AuditRefinement
from .temporal_interaction import past_future_cycle, temporal_three_way_cascade


def _canonical(values: Iterable[Hashable]) -> tuple[int, ...]:
    labels: dict[Hashable, int] = {}
    result: list[int] = []
    for value in values:
        if value not in labels:
            labels[value] = len(labels)
        result.append(labels[value])
    if not result:
        raise ValueError("partition must be nonempty")
    return tuple(result)


def block_count(values: Iterable[Hashable]) -> int:
    labels = _canonical(values)
    return max(labels) + 1


def common_refinement(*partitions: Sequence[Hashable]) -> tuple[int, ...]:
    """Common refinement of fixed partitions on one finite carrier."""

    if not partitions:
        raise ValueError("at least one partition is required")
    width = len(partitions[0])
    if width == 0 or any(len(partition) != width for partition in partitions):
        raise ValueError("partitions must share one nonempty carrier")
    return _canonical(tuple(partition[index] for partition in partitions) for index in range(width))


def one_block_fixed_partition_interaction_bits(
    partitions: Sequence[Sequence[Hashable]],
) -> float:
    """Interaction debt for precomputed fixed responsibility partitions.

    The baseline is one visible class.  For fixed partitions P_i, their common
    refinement has at most the product of the individual block counts.  Hence the
    returned value is always nonpositive.  Positive CREST interaction on a
    one-block baseline therefore requires state-dependent obligations rather than
    merely intersecting precomputed companion quotients.
    """

    if not partitions:
        raise ValueError("at least one fixed responsibility partition is required")
    counts = tuple(block_count(partition) for partition in partitions)
    joint = block_count(common_refinement(*partitions))
    return log2(joint) - sum(log2(count) for count in counts)


def audit_preserves_label(audit: AuditRefinement, labels: Sequence[Hashable]) -> bool:
    """Whether every legal transition of ``audit`` preserves ``labels``."""

    if len(labels) != audit.world_count:
        raise ValueError("labels must align with audit carrier")
    return all(
        successor is None or labels[successor] == labels[index]
        for index, row in enumerate(audit.successors)
        for successor in row
    )


def inert_on_indiscrete(audit: AuditRefinement) -> bool:
    baseline = (0,) * audit.world_count
    return audit.close(baseline) == baseline


def immutable_history_blocks_activation(
    history_labels: Sequence[Hashable],
    post_cut_audit: AuditRefinement,
) -> bool:
    """Check the immutable-history no-activation theorem hypotheses/conclusion.

    If a post-cut audit is inert on the one-class visible baseline and every legal
    post-cut transition preserves the declared history type, then the history
    partition is already fixed by that audit.  In that strict setting a zero-debt
    future/latent audit cannot be activated merely by retaining immutable history.
    """

    if len(history_labels) != post_cut_audit.world_count:
        raise ValueError("history labels must align with audit carrier")
    if not inert_on_indiscrete(post_cut_audit):
        return False
    if not audit_preserves_label(post_cut_audit, history_labels):
        return False
    history_partition = _canonical(history_labels)
    return post_cut_audit.close(history_partition) == history_partition


def response_type_count(
    transition_tables: Mapping[Hashable, Mapping[Hashable, Sequence[Hashable]]],
) -> int:
    """Number of distinct complete MRM response tables.

    ``transition_tables[candidate][action][q_index]`` is the next observable
    macrostate value.  Candidates with identical complete tables are one response
    type, matching the MRM definition.
    """

    if not transition_tables:
        raise ValueError("at least one candidate mechanism is required")
    candidates = tuple(transition_tables)
    first = transition_tables[candidates[0]]
    actions = tuple(first)
    if not actions:
        raise ValueError("at least one declared action is required")
    width = len(first[actions[0]])
    if width == 0:
        raise ValueError("observable macrostate set must be nonempty")

    signatures: set[tuple[tuple[Hashable, ...], ...]] = set()
    for candidate in candidates:
        table = transition_tables[candidate]
        if tuple(table) != actions:
            raise ValueError("all candidates must use the same ordered action set")
        rows = tuple(tuple(table[action]) for action in actions)
        if any(len(row) != width for row in rows):
            raise ValueError("all transition rows must share the same observable-state width")
        signatures.add(rows)
    return len(signatures)


def mrm_observation_partition_is_candidate_safe(
    transition_tables: Mapping[Hashable, Mapping[Hashable, Sequence[Hashable]]],
) -> bool:
    """Whether the observable-state partition needs no candidate refinement."""

    if not transition_tables:
        raise ValueError("at least one candidate mechanism is required")
    candidates = tuple(transition_tables)
    first = transition_tables[candidates[0]]
    actions = tuple(first)
    if not actions:
        raise ValueError("at least one declared action is required")
    width = len(first[actions[0]])
    for action in actions:
        for q_index in range(width):
            outcomes = {transition_tables[candidate][action][q_index] for candidate in candidates}
            if len(outcomes) != 1:
                return False
    return True


def mrm_zero_debt_implies_single_response_type(
    transition_tables: Mapping[Hashable, Mapping[Hashable, Sequence[Hashable]]],
) -> bool:
    """Executable form of the fixed-grammar MRM zero-debt no-go.

    If the observable partition is already candidate-safe, every candidate has the
    same transition table and hence there is exactly one MRM response type.
    """

    if not mrm_observation_partition_is_candidate_safe(transition_tables):
        return True
    return response_type_count(transition_tables) == 1


@dataclass(frozen=True)
class SharpFamilyCompanionAudit:
    bit_depth: int
    pairwise_future_preserves_history: bool
    pairwise_future_is_inert: bool
    pairwise_literal_immutable_history_realizable: bool
    triple_latent_preserves_history: bool
    triple_latent_is_inert: bool
    triple_literal_immutable_history_realizable: bool


def sharp_family_companion_audit(bit_depth: int) -> SharpFamilyCompanionAudit:
    """Audit the existing sharp temporal cascades against immutable MLTR history."""

    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 2:
        raise ValueError("bit_depth must be an integer at least two")

    pair_baseline, pair_audits = past_future_cycle(2**bit_depth)
    pair_history, pair_future = pair_audits
    pair_labels = pair_history.static_labels
    pair_preserves = audit_preserves_label(pair_future, pair_labels)
    pair_inert = pair_future.close(pair_baseline) == pair_baseline

    triple_baseline, triple_audits = temporal_three_way_cascade(bit_depth)
    triple_history, triple_latent, _ = triple_audits
    triple_labels = triple_history.static_labels
    triple_preserves = audit_preserves_label(triple_latent, triple_labels)
    triple_inert = triple_latent.close(triple_baseline) == triple_baseline

    return SharpFamilyCompanionAudit(
        bit_depth=bit_depth,
        pairwise_future_preserves_history=pair_preserves,
        pairwise_future_is_inert=pair_inert,
        pairwise_literal_immutable_history_realizable=(
            pair_preserves
            and immutable_history_blocks_activation(pair_labels, pair_future)
            and pair_future.close(_canonical(pair_labels)) != _canonical(pair_labels)
        ),
        triple_latent_preserves_history=triple_preserves,
        triple_latent_is_inert=triple_inert,
        triple_literal_immutable_history_realizable=(
            triple_preserves
            and immutable_history_blocks_activation(triple_labels, triple_latent)
            and triple_latent.close(_canonical(triple_labels)) != _canonical(triple_labels)
        ),
    )


__all__ = [
    "SharpFamilyCompanionAudit",
    "audit_preserves_label",
    "block_count",
    "common_refinement",
    "immutable_history_blocks_activation",
    "inert_on_indiscrete",
    "mrm_observation_partition_is_candidate_safe",
    "mrm_zero_debt_implies_single_response_type",
    "one_block_fixed_partition_interaction_bits",
    "response_type_count",
    "sharp_family_companion_audit",
]
