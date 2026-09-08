"""Compare finite CREST obstruction spectra across two declared contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .obstruction_io import spectrum_from_payload


def _float_map_delta(
    before: Mapping[str, float], after: Mapping[str, float], names: tuple[str, ...]
) -> dict[str, float]:
    return {name: float(after[name]) - float(before[name]) for name in names}


def _interaction_map(payload: Mapping[str, Any]) -> dict[tuple[str, ...], float]:
    result: dict[tuple[str, ...], float] = {}
    for row in payload["interaction_dividends"]:
        result[tuple(row["audits"])] = float(row["bits"])
    return result


def _direction(value: float, *, tolerance: float = 1e-12) -> str:
    if value > tolerance:
        return "increase"
    if value < -tolerance:
        return "decrease"
    return "unchanged"


@dataclass(frozen=True)
class SpectrumComparison:
    audit_names: tuple[str, ...]
    baseline_blocks_before: int
    baseline_blocks_after: int
    joint_blocks_before: int
    joint_blocks_after: int
    joint_debt_change_bits: float
    delta_change_bits: float
    standalone_change_bits: dict[str, float]
    shapley_change_bits: dict[str, float]
    interaction_attribution_change_bits: dict[str, float]
    interaction_dividend_change_bits: dict[tuple[str, ...], float]

    @property
    def joint_block_change(self) -> int:
        return self.joint_blocks_after - self.joint_blocks_before

    @property
    def direct_change_bits(self) -> float:
        """Net change in responsibility-wise standalone debt."""

        return sum(self.standalone_change_bits.values())

    @property
    def interaction_change_bits(self) -> float:
        """Net change in non-additive interaction debt."""

        return self.delta_change_bits

    def joint_debt_direction(self, *, tolerance: float = 1e-12) -> str:
        return _direction(self.joint_debt_change_bits, tolerance=tolerance)

    def direct_direction(self, *, tolerance: float = 1e-12) -> str:
        return _direction(self.direct_change_bits, tolerance=tolerance)

    def interaction_direction(self, *, tolerance: float = 1e-12) -> str:
        return _direction(self.interaction_change_bits, tolerance=tolerance)

    def interaction_order_change_bits(self) -> dict[int, float]:
        """Aggregate Möbius-dividend change by coalition order."""

        result: dict[int, float] = {}
        for coalition, value in self.interaction_dividend_change_bits.items():
            order = len(coalition)
            result[order] = result.get(order, 0.0) + value
        return dict(sorted(result.items()))

    def active_interaction_orders(self, *, tolerance: float = 1e-12) -> tuple[int, ...]:
        return tuple(
            order
            for order, value in self.interaction_order_change_bits().items()
            if order >= 2 and abs(value) > tolerance
        )

    def dominant_interaction_order(self, *, tolerance: float = 1e-12) -> int | None:
        active = {
            order: value
            for order, value in self.interaction_order_change_bits().items()
            if order >= 2 and abs(value) > tolerance
        }
        if not active:
            return None
        return min(active, key=lambda order: (-abs(active[order]), order))

    def change_class(self, *, tolerance: float = 1e-12) -> str:
        """Classify the source of before/after state-debt change.

        Returns one of ``direct-only``, ``interaction-only``, ``mixed``, or
        ``null``. ``direct`` means at least one standalone debt changed;
        ``interaction`` means the non-additive excess Delta changed.
        """

        direct_changed = any(
            abs(value) > tolerance for value in self.standalone_change_bits.values()
        )
        interaction_changed = abs(self.delta_change_bits) > tolerance
        if direct_changed and interaction_changed:
            return "mixed"
        if direct_changed:
            return "direct-only"
        if interaction_changed:
            return "interaction-only"
        return "null"

    def verify(self, *, tolerance: float = 1e-12) -> bool:
        """Verify the exact before/after accounting identities."""

        higher_order_change = sum(
            value
            for coalition, value in self.interaction_dividend_change_bits.items()
            if len(coalition) >= 2
        )
        order_change = self.interaction_order_change_bits()
        return (
            abs(
                self.joint_debt_change_bits
                - (self.direct_change_bits + self.delta_change_bits)
            )
            <= tolerance
            and abs(higher_order_change - self.delta_change_bits) <= tolerance
            and abs(sum(order_change.values()) - self.joint_debt_change_bits)
            <= tolerance
            and (
                self.change_class(tolerance=tolerance) != "interaction-only"
                or abs(self.joint_debt_change_bits - self.delta_change_bits)
                <= tolerance
            )
        )

    def to_payload(self) -> dict[str, Any]:
        if not self.verify():
            raise ValueError("spectrum comparison failed accounting verification")
        order_change = self.interaction_order_change_bits()
        dominant_order = self.dominant_interaction_order()
        return {
            "audit_names": list(self.audit_names),
            "change_class": self.change_class(),
            "joint_debt_direction": self.joint_debt_direction(),
            "direct_direction": self.direct_direction(),
            "interaction_direction": self.interaction_direction(),
            "baseline_blocks": {
                "before": self.baseline_blocks_before,
                "after": self.baseline_blocks_after,
                "change": self.baseline_blocks_after - self.baseline_blocks_before,
            },
            "joint_blocks": {
                "before": self.joint_blocks_before,
                "after": self.joint_blocks_after,
                "change": self.joint_block_change,
            },
            "joint_debt_change_bits": self.joint_debt_change_bits,
            "direct_change_bits": self.direct_change_bits,
            "interaction_change_bits": self.interaction_change_bits,
            "delta_change_bits": self.delta_change_bits,
            "standalone_change_bits": self.standalone_change_bits,
            "shapley_change_bits": self.shapley_change_bits,
            "interaction_attribution_change_bits": self.interaction_attribution_change_bits,
            "interaction_order_change_bits": [
                {
                    "order": order,
                    "change_bits": value,
                    "direction": _direction(value),
                }
                for order, value in order_change.items()
            ],
            "active_interaction_orders": list(self.active_interaction_orders()),
            "dominant_interaction_order": dominant_order,
            "dominant_interaction_order_change_bits": (
                None if dominant_order is None else order_change[dominant_order]
            ),
            "interaction_dividend_change_bits": [
                {"audits": list(coalition), "order": len(coalition), "change_bits": value}
                for coalition, value in sorted(
                    self.interaction_dividend_change_bits.items(),
                    key=lambda item: (len(item[0]), item[0]),
                )
            ],
        }


def compare_spectrum_payloads(
    before: Mapping[str, Any], after: Mapping[str, Any]
) -> SpectrumComparison:
    before_names = tuple(before["audit_names"])
    after_names = tuple(after["audit_names"])
    if set(before_names) != set(after_names):
        raise ValueError("before and after spectra must contain the same audit names")
    names = before_names

    before_dividends = _interaction_map(before)
    after_dividends = _interaction_map(after)
    all_coalitions = set(before_dividends) | set(after_dividends)

    comparison = SpectrumComparison(
        audit_names=names,
        baseline_blocks_before=int(before["baseline_blocks"]),
        baseline_blocks_after=int(after["baseline_blocks"]),
        joint_blocks_before=int(before["joint_blocks"]),
        joint_blocks_after=int(after["joint_blocks"]),
        joint_debt_change_bits=float(after["joint_debt_bits"])
        - float(before["joint_debt_bits"]),
        delta_change_bits=float(after["delta_bits"]) - float(before["delta_bits"]),
        standalone_change_bits=_float_map_delta(
            before["standalone_debts_bits"], after["standalone_debts_bits"], names
        ),
        shapley_change_bits=_float_map_delta(
            before["shapley_contributions_bits"],
            after["shapley_contributions_bits"],
            names,
        ),
        interaction_attribution_change_bits=_float_map_delta(
            before["interaction_attributions_bits"],
            after["interaction_attributions_bits"],
            names,
        ),
        interaction_dividend_change_bits={
            coalition: after_dividends.get(coalition, 0.0)
            - before_dividends.get(coalition, 0.0)
            for coalition in all_coalitions
        },
    )
    if not comparison.verify():
        raise AssertionError("constructed spectrum comparison did not verify")
    return comparison


def compare_contract_payloads(
    before_contract: dict[str, Any], after_contract: dict[str, Any]
) -> dict[str, Any]:
    before = spectrum_from_payload(before_contract)
    after = spectrum_from_payload(after_contract)
    comparison = compare_spectrum_payloads(before, after)
    return {
        "before": before,
        "after": after,
        "comparison": comparison.to_payload(),
    }


__all__ = [
    "SpectrumComparison",
    "compare_contract_payloads",
    "compare_spectrum_payloads",
]
