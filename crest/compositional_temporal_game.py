"""Conditional-contract three-way bridge for MLTR, MRM, and CCOC.

The fixed-closure temporal cascade is not a literal simultaneous companion model.
A literal positive three-way bridge is nevertheless possible when one respects
CCOC's own cross-grammar quantifier: separate component contracts are compared
with a jointly open composition contract.

The canonical family uses:

* one binary MLTR history-mode label H;
* one binary MRM response-type label Theta; and
* m binary CCOC exterior/addressability bits that are legal to decode only in the
  jointly open H+Theta+F contract.

Coalition contracts are declared exogenously.  The future grammar is not inferred
from the resulting state quotient, so the construction remains non-circular.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

HISTORY = "H"
MECHANISM = "THETA"
FUTURE = "F"
AXES = (HISTORY, MECHANISM, FUTURE)


def _validate_depth(bit_depth: int) -> None:
    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")


def _normalize_coalition(coalition: tuple[str, ...] | list[str] | set[str]) -> frozenset[str]:
    members = frozenset(coalition)
    if not members.issubset(AXES):
        raise ValueError("coalition contains an unknown temporal axis")
    return members


def compositional_contract_bits(
    bit_depth: int, coalition: tuple[str, ...] | list[str] | set[str]
) -> int:
    """Exact state bits required by one declared coalition contract.

    History contributes one bit when present; mechanism contributes one bit when
    present.  The m-bit exterior/addressability coordinate becomes a required
    response interface only in the jointly open contract containing H, Theta, and
    F.  This is the CCOC open-composition contribution.
    """

    _validate_depth(bit_depth)
    members = _normalize_coalition(coalition)
    bits = int(HISTORY in members) + int(MECHANISM in members)
    if members == frozenset(AXES):
        bits += bit_depth
    return bits


def compositional_contract_classes(
    bit_depth: int, coalition: tuple[str, ...] | list[str] | set[str]
) -> int:
    return 2 ** compositional_contract_bits(bit_depth, coalition)


def mobius_dividend(
    bit_depth: int, coalition: tuple[str, ...] | list[str] | set[str]
) -> int:
    """Exact Möbius/Harsanyi dividend in bits for the coalition game."""

    members = _normalize_coalition(coalition)
    if not members:
        return 0
    ordered = tuple(axis for axis in AXES if axis in members)
    total = 0
    for size in range(len(ordered) + 1):
        for subset in combinations(ordered, size):
            sign = -1 if (len(ordered) - size) % 2 else 1
            total += sign * compositional_contract_bits(bit_depth, subset)
    return total


@dataclass(frozen=True)
class CompositionalTemporalSummary:
    bit_depth: int
    history_bits: int
    mechanism_bits: int
    future_bits: int
    history_mechanism_bits: int
    history_future_bits: int
    mechanism_future_bits: int
    joint_bits: int
    interaction_bits: int
    three_way_bits: int
    joint_classes: int
    history_mechanism_classes: int
    state_count_amplification: int
    three_way_fraction_of_joint: float


def compositional_temporal_summary(bit_depth: int) -> CompositionalTemporalSummary:
    _validate_depth(bit_depth)
    h = compositional_contract_bits(bit_depth, (HISTORY,))
    theta = compositional_contract_bits(bit_depth, (MECHANISM,))
    future = compositional_contract_bits(bit_depth, (FUTURE,))
    htheta = compositional_contract_bits(bit_depth, (HISTORY, MECHANISM))
    hf = compositional_contract_bits(bit_depth, (HISTORY, FUTURE))
    thetaf = compositional_contract_bits(bit_depth, (MECHANISM, FUTURE))
    joint = compositional_contract_bits(bit_depth, AXES)
    interaction = joint - h - theta - future
    triple = mobius_dividend(bit_depth, AXES)
    joint_classes = 2**joint
    htheta_classes = 2**htheta
    return CompositionalTemporalSummary(
        bit_depth=bit_depth,
        history_bits=h,
        mechanism_bits=theta,
        future_bits=future,
        history_mechanism_bits=htheta,
        history_future_bits=hf,
        mechanism_future_bits=thetaf,
        joint_bits=joint,
        interaction_bits=interaction,
        three_way_bits=triple,
        joint_classes=joint_classes,
        history_mechanism_classes=htheta_classes,
        state_count_amplification=joint_classes // htheta_classes,
        three_way_fraction_of_joint=triple / joint,
    )


__all__ = [
    "AXES",
    "FUTURE",
    "HISTORY",
    "MECHANISM",
    "CompositionalTemporalSummary",
    "compositional_contract_bits",
    "compositional_contract_classes",
    "compositional_temporal_summary",
    "mobius_dividend",
]
