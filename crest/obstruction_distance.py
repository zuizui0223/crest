"""Distances between finite CREST obstruction-accounting profiles.

For a fixed named responsibility set, the Möbius/Harsanyi dividends of the
coalition debt function form a complete coordinate representation of that
finite obstruction spectrum. This module compares those coordinates directly.

Two distance scales are reported:

- raw L1/L2 distances in bits between dividend vectors; and
- capacity-normalized L1/L2 distances after dividing each spectrum by its own
  available refinement capacity log2(N/B).

The resulting quantities are metrics on the corresponding profile vectors,
not on ecological worlds or dynamical systems themselves. Distinct contracts
can induce the same profile. Cross-system interpretation additionally requires
commensurable responsibility meanings, carrier construction, and baseline
semantics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from typing import Any, Mapping

from .obstruction_io import spectrum_from_payload


def _dividend_map(payload: Mapping[str, Any]) -> dict[frozenset[str], float]:
    result: dict[frozenset[str], float] = {}
    for row in payload["interaction_dividends"]:
        coalition = frozenset(str(name) for name in row["audits"])
        if not coalition:
            raise ValueError("interaction dividend coalitions must be nonempty")
        result[coalition] = float(row["bits"])
    return result


def _capacity(payload: Mapping[str, Any]) -> float:
    normalized = payload.get("normalized")
    if not isinstance(normalized, Mapping):
        raise ValueError("spectrum payload must include normalized metrics")
    return float(normalized["capacity_bits"])


def _normalize(value: float, capacity: float, *, tolerance: float = 1e-12) -> float:
    if capacity > tolerance:
        return value / capacity
    if abs(value) <= tolerance:
        return 0.0
    raise ValueError("nonzero obstruction dividend with zero refinement capacity")


@dataclass(frozen=True)
class CoalitionProfileChange:
    audits: tuple[str, ...]
    order: int
    before_bits: float
    after_bits: float
    change_bits: float
    before_normalized: float
    after_normalized: float
    change_normalized: float

    def to_payload(self) -> dict[str, Any]:
        return {
            "audits": list(self.audits),
            "order": self.order,
            "before_bits": self.before_bits,
            "after_bits": self.after_bits,
            "change_bits": self.change_bits,
            "before_normalized": self.before_normalized,
            "after_normalized": self.after_normalized,
            "change_normalized": self.change_normalized,
        }


@dataclass(frozen=True)
class ObstructionProfileDistance:
    audit_names: tuple[str, ...]
    capacity_before_bits: float
    capacity_after_bits: float
    raw_l1_bits: float
    raw_l2_bits: float
    normalized_l1: float
    normalized_l2: float
    direct_raw_l1_bits: float
    interaction_raw_l1_bits: float
    direct_normalized_l1: float
    interaction_normalized_l1: float
    coalition_changes: tuple[CoalitionProfileChange, ...]

    def difference_class(self, *, tolerance: float = 1e-12) -> str:
        direct = self.direct_raw_l1_bits > tolerance
        interaction = self.interaction_raw_l1_bits > tolerance
        if direct and interaction:
            return "mixed"
        if direct:
            return "direct-only"
        if interaction:
            return "interaction-only"
        return "null"

    def dominant_changed_coalition(self, *, tolerance: float = 1e-12) -> tuple[str, ...] | None:
        changed = [
            row for row in self.coalition_changes if abs(row.change_normalized) > tolerance
        ]
        if not changed:
            return None
        row = max(
            changed,
            key=lambda item: (abs(item.change_normalized), -item.order, item.audits),
        )
        return row.audits

    def verify(self, *, tolerance: float = 1e-12) -> bool:
        raw_abs = [abs(row.change_bits) for row in self.coalition_changes]
        norm_abs = [abs(row.change_normalized) for row in self.coalition_changes]
        raw_sq = [row.change_bits * row.change_bits for row in self.coalition_changes]
        norm_sq = [
            row.change_normalized * row.change_normalized
            for row in self.coalition_changes
        ]
        direct_raw = sum(
            abs(row.change_bits) for row in self.coalition_changes if row.order == 1
        )
        interaction_raw = sum(
            abs(row.change_bits) for row in self.coalition_changes if row.order >= 2
        )
        direct_norm = sum(
            abs(row.change_normalized)
            for row in self.coalition_changes
            if row.order == 1
        )
        interaction_norm = sum(
            abs(row.change_normalized)
            for row in self.coalition_changes
            if row.order >= 2
        )
        return (
            self.capacity_before_bits >= -tolerance
            and self.capacity_after_bits >= -tolerance
            and abs(self.raw_l1_bits - sum(raw_abs)) <= tolerance
            and abs(self.normalized_l1 - sum(norm_abs)) <= tolerance
            and abs(self.raw_l2_bits - sqrt(sum(raw_sq))) <= tolerance
            and abs(self.normalized_l2 - sqrt(sum(norm_sq))) <= tolerance
            and abs(self.direct_raw_l1_bits - direct_raw) <= tolerance
            and abs(self.interaction_raw_l1_bits - interaction_raw) <= tolerance
            and abs(self.direct_normalized_l1 - direct_norm) <= tolerance
            and abs(self.interaction_normalized_l1 - interaction_norm) <= tolerance
            and abs(
                self.raw_l1_bits
                - (self.direct_raw_l1_bits + self.interaction_raw_l1_bits)
            )
            <= tolerance
            and abs(
                self.normalized_l1
                - (self.direct_normalized_l1 + self.interaction_normalized_l1)
            )
            <= tolerance
        )

    def to_payload(self) -> dict[str, Any]:
        if not self.verify():
            raise ValueError("obstruction profile distance failed verification")
        dominant = self.dominant_changed_coalition()
        return {
            "audit_names": list(self.audit_names),
            "difference_class": self.difference_class(),
            "capacity_bits": {
                "before": self.capacity_before_bits,
                "after": self.capacity_after_bits,
            },
            "raw_l1_bits": self.raw_l1_bits,
            "raw_l2_bits": self.raw_l2_bits,
            "normalized_l1": self.normalized_l1,
            "normalized_l2": self.normalized_l2,
            "direct_raw_l1_bits": self.direct_raw_l1_bits,
            "interaction_raw_l1_bits": self.interaction_raw_l1_bits,
            "direct_normalized_l1": self.direct_normalized_l1,
            "interaction_normalized_l1": self.interaction_normalized_l1,
            "dominant_changed_coalition": None if dominant is None else list(dominant),
            "coalition_changes": [row.to_payload() for row in self.coalition_changes],
            "interpretation_firewall": (
                "distance is between obstruction-accounting profiles, not ecological "
                "worlds; cross-system use requires commensurable responsibility, "
                "carrier, and baseline semantics"
            ),
        }


def compare_obstruction_profiles(
    before: Mapping[str, Any], after: Mapping[str, Any]
) -> ObstructionProfileDistance:
    """Compare two already-computed finite obstruction spectrum payloads."""

    before_names = tuple(str(name) for name in before["audit_names"])
    after_names = tuple(str(name) for name in after["audit_names"])
    if set(before_names) != set(after_names):
        raise ValueError("before and after spectra must contain the same audit names")
    names = tuple(sorted(before_names))

    before_map = _dividend_map(before)
    after_map = _dividend_map(after)
    all_coalitions = set(before_map) | set(after_map)
    expected_singletons = {frozenset((name,)) for name in names}
    if not expected_singletons.issubset(all_coalitions):
        raise ValueError("spectrum payload is missing singleton dividend coordinates")

    before_capacity = _capacity(before)
    after_capacity = _capacity(after)
    rows: list[CoalitionProfileChange] = []
    for coalition in sorted(
        all_coalitions,
        key=lambda value: (len(value), tuple(sorted(value))),
    ):
        audits = tuple(sorted(coalition))
        before_bits = before_map.get(coalition, 0.0)
        after_bits = after_map.get(coalition, 0.0)
        before_norm = _normalize(before_bits, before_capacity)
        after_norm = _normalize(after_bits, after_capacity)
        rows.append(
            CoalitionProfileChange(
                audits=audits,
                order=len(audits),
                before_bits=before_bits,
                after_bits=after_bits,
                change_bits=after_bits - before_bits,
                before_normalized=before_norm,
                after_normalized=after_norm,
                change_normalized=after_norm - before_norm,
            )
        )

    raw_l1 = sum(abs(row.change_bits) for row in rows)
    raw_l2 = sqrt(sum(row.change_bits * row.change_bits for row in rows))
    normalized_l1 = sum(abs(row.change_normalized) for row in rows)
    normalized_l2 = sqrt(
        sum(row.change_normalized * row.change_normalized for row in rows)
    )
    direct_raw = sum(abs(row.change_bits) for row in rows if row.order == 1)
    interaction_raw = sum(abs(row.change_bits) for row in rows if row.order >= 2)
    direct_norm = sum(
        abs(row.change_normalized) for row in rows if row.order == 1
    )
    interaction_norm = sum(
        abs(row.change_normalized) for row in rows if row.order >= 2
    )

    distance = ObstructionProfileDistance(
        audit_names=names,
        capacity_before_bits=before_capacity,
        capacity_after_bits=after_capacity,
        raw_l1_bits=raw_l1,
        raw_l2_bits=raw_l2,
        normalized_l1=normalized_l1,
        normalized_l2=normalized_l2,
        direct_raw_l1_bits=direct_raw,
        interaction_raw_l1_bits=interaction_raw,
        direct_normalized_l1=direct_norm,
        interaction_normalized_l1=interaction_norm,
        coalition_changes=tuple(rows),
    )
    if not distance.verify():
        raise AssertionError("constructed obstruction profile distance did not verify")
    return distance


def distance_contract_payloads(
    before_contract: dict[str, Any], after_contract: dict[str, Any]
) -> dict[str, Any]:
    before = spectrum_from_payload(before_contract)
    after = spectrum_from_payload(after_contract)
    distance = compare_obstruction_profiles(before, after)
    return {
        "before": before,
        "after": after,
        "distance": distance.to_payload(),
    }


__all__ = [
    "CoalitionProfileChange",
    "ObstructionProfileDistance",
    "compare_obstruction_profiles",
    "distance_contract_payloads",
]
