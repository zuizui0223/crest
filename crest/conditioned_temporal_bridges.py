"""Positive finite bridges from companion primitives to temporal-cut relevance.

This module keeps raw history and mechanism identity fixed while allowing the
*relevance equivalence* to depend on a declared future/intervention grammar.
That distinction avoids the immutable-history and fixed-grammar no-go results in
``companion_realizability``.

Two exact m-bit families are exposed:

* future-conditioned MLTR history relevance: after k addressable terminal queries,
  exactly 2**k history classes remain scientifically distinct;
* grammar-conditioned MRM response types: after k declared binary probes, exactly
  2**k mechanism response types remain distinct.

Both frontiers therefore add exactly one bit per newly declared binary query, but
they act on different primitive objects.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log2


def _validate_depth(bit_depth: int) -> None:
    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")


def _validate_k(bit_depth: int, query_count: int) -> None:
    _validate_depth(bit_depth)
    if (
        not isinstance(query_count, int)
        or isinstance(query_count, bool)
        or not 0 <= query_count <= bit_depth
    ):
        raise ValueError("query_count must lie between zero and bit_depth")


def binary_signatures(bit_depth: int) -> tuple[tuple[int, ...], ...]:
    _validate_depth(bit_depth)
    return tuple(product((0, 1), repeat=bit_depth))


@dataclass(frozen=True)
class RelevanceFrontierPoint:
    query_count: int
    equivalence_classes: int
    information_bits: float


def future_conditioned_history_profile(
    signature: tuple[int, ...], query_count: int
) -> tuple[int, ...]:
    """Reachable carried-label profile under the first ``query_count`` probes.

    In the canonical bridge construction, each MLTR history carries one complete
    terminal map whose m addressable coordinates are ``signature``.  The closed
    grammar sees only a common anchor; opening probe i exposes coordinate i.  The
    target-specific history equivalence is therefore equality of the queried
    prefix.  Raw replacement history itself is never changed by a post-cut action.
    """

    bit_depth = len(signature)
    _validate_k(bit_depth, query_count)
    if any(bit not in (0, 1) for bit in signature):
        raise ValueError("history signature must be binary")
    return signature[:query_count]


def future_conditioned_history_point(
    bit_depth: int, query_count: int
) -> RelevanceFrontierPoint:
    _validate_k(bit_depth, query_count)
    profiles = {
        future_conditioned_history_profile(signature, query_count)
        for signature in binary_signatures(bit_depth)
    }
    count = len(profiles)
    return RelevanceFrontierPoint(query_count, count, log2(count))


def future_conditioned_history_frontier(
    bit_depth: int,
) -> tuple[RelevanceFrontierPoint, ...]:
    _validate_depth(bit_depth)
    return tuple(
        future_conditioned_history_point(bit_depth, k)
        for k in range(bit_depth + 1)
    )


def grammar_conditioned_mechanism_profile(
    signature: tuple[int, ...], query_count: int
) -> tuple[int, ...]:
    """MRM response-table signature under the first ``query_count`` probes.

    A common ``hold`` action is identical for every candidate and contributes no
    response-type separation.  Probe i returns signature[i] from either visible
    macrostate.  Restricting the action grammar to the first k probes therefore
    identifies response types exactly by the first k bits.
    """

    bit_depth = len(signature)
    _validate_k(bit_depth, query_count)
    if any(bit not in (0, 1) for bit in signature):
        raise ValueError("mechanism signature must be binary")
    return signature[:query_count]


def grammar_conditioned_mechanism_point(
    bit_depth: int, query_count: int
) -> RelevanceFrontierPoint:
    _validate_k(bit_depth, query_count)
    profiles = {
        grammar_conditioned_mechanism_profile(signature, query_count)
        for signature in binary_signatures(bit_depth)
    }
    count = len(profiles)
    return RelevanceFrontierPoint(query_count, count, log2(count))


def grammar_conditioned_mechanism_frontier(
    bit_depth: int,
) -> tuple[RelevanceFrontierPoint, ...]:
    _validate_depth(bit_depth)
    return tuple(
        grammar_conditioned_mechanism_point(bit_depth, k)
        for k in range(bit_depth + 1)
    )


def paired_bridge_summary(bit_depth: int) -> dict[str, float | int]:
    """Closed/open endpoints for the two positive companion bridges."""

    _validate_depth(bit_depth)
    history_closed = future_conditioned_history_point(bit_depth, 0)
    history_open = future_conditioned_history_point(bit_depth, bit_depth)
    mechanism_closed = grammar_conditioned_mechanism_point(bit_depth, 0)
    mechanism_open = grammar_conditioned_mechanism_point(bit_depth, bit_depth)
    return {
        "bit_depth": bit_depth,
        "history_closed_classes": history_closed.equivalence_classes,
        "history_open_classes": history_open.equivalence_classes,
        "history_inflation_bits": history_open.information_bits - history_closed.information_bits,
        "mechanism_closed_response_types": mechanism_closed.equivalence_classes,
        "mechanism_open_response_types": mechanism_open.equivalence_classes,
        "mechanism_inflation_bits": mechanism_open.information_bits - mechanism_closed.information_bits,
    }


__all__ = [
    "RelevanceFrontierPoint",
    "binary_signatures",
    "future_conditioned_history_frontier",
    "future_conditioned_history_point",
    "future_conditioned_history_profile",
    "grammar_conditioned_mechanism_frontier",
    "grammar_conditioned_mechanism_point",
    "grammar_conditioned_mechanism_profile",
    "paired_bridge_summary",
]
