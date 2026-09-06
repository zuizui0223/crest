"""Sharp sequential counterfactual state-debt bounds for CREST.

The elementary product/counting substrate is classical.  The CREST role of
this module is to express the existing response-capacity result as a directly
interpretable depth law: along one sequential intervention channel, H stages
with at most r distinguishable responses per stage can add at most
H*log2(r) bits, and a connected CREST family attains equality.
"""

from __future__ import annotations

from math import ceil, log2, prod
from typing import Iterable


def _positive_integer(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _nonnegative_integer(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def sequential_split_class_bound(
    response_cardinality: int,
    horizon: int,
) -> int:
    """Maximum classes exposed by H sequential r-ary response stages."""

    response_cardinality = _positive_integer(
        "response_cardinality", response_cardinality
    )
    horizon = _nonnegative_integer("horizon", horizon)
    return response_cardinality**horizon


def sequential_split_bit_bound(
    response_cardinality: int,
    horizon: int,
) -> float:
    """Information form of :func:`sequential_split_class_bound`."""

    response_cardinality = _positive_integer(
        "response_cardinality", response_cardinality
    )
    horizon = _nonnegative_integer("horizon", horizon)
    return horizon * log2(response_cardinality)


def heterogeneous_sequential_class_bound(
    stage_cardinalities: Iterable[int],
) -> int:
    """Product bound when stage h has at most r_h distinguishable responses."""

    cardinalities = tuple(stage_cardinalities)
    for value in cardinalities:
        _positive_integer("stage cardinality", value)
    return prod(cardinalities, start=1)


def heterogeneous_sequential_bit_bound(
    stage_cardinalities: Iterable[int],
) -> float:
    """Sum-of-bits form of the heterogeneous sequential product bound."""

    cardinalities = tuple(stage_cardinalities)
    for value in cardinalities:
        _positive_integer("stage cardinality", value)
    return sum(log2(value) for value in cardinalities)


def minimum_sequential_horizon_for_classes(
    required_classes: int,
    response_cardinality: int,
) -> int:
    """Smallest H for which r**H can represent ``required_classes`` classes."""

    required_classes = _positive_integer("required_classes", required_classes)
    response_cardinality = _positive_integer(
        "response_cardinality", response_cardinality
    )
    if required_classes == 1:
        return 0
    if response_cardinality == 1:
        raise ValueError(
            "response_cardinality=1 cannot expose more than one class"
        )
    horizon = 0
    capacity = 1
    while capacity < required_classes:
        capacity *= response_cardinality
        horizon += 1
    return horizon


def minimum_sequential_horizon_for_bits(
    required_bits: float,
    response_cardinality: int,
) -> int:
    """Necessary horizon to expose at least ``required_bits`` in an r-ary path."""

    if isinstance(required_bits, bool) or required_bits < 0:
        raise ValueError("required_bits must be nonnegative")
    response_cardinality = _positive_integer(
        "response_cardinality", response_cardinality
    )
    if required_bits == 0:
        return 0
    if response_cardinality == 1:
        raise ValueError("response_cardinality=1 has zero bit capacity")
    return ceil(required_bits / log2(response_cardinality))
