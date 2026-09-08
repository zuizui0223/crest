"""Normalized diagnostics for finite CREST obstruction spectra."""

from __future__ import annotations

from dataclasses import dataclass
from math import log2

from .obstruction_spectrum import ObstructionSpectrumReport


@dataclass(frozen=True)
class NormalizedObstructionMetrics:
    carrier_worlds: int
    baseline_blocks: int
    capacity_bits: float
    normalized_joint_burden: float
    interaction_fraction_of_joint: float
    direct_fraction_of_joint: float
    interaction_order_bits: dict[int, float]
    interaction_order_absolute_shares: dict[int, float]
    active_interaction_orders: tuple[int, ...]
    dominant_interaction_order: int | None

    def verify(self, *, tolerance: float = 1e-12) -> bool:
        if self.carrier_worlds < 1 or self.baseline_blocks < 1:
            return False
        if self.baseline_blocks > self.carrier_worlds:
            return False
        if self.capacity_bits < -tolerance:
            return False
        if self.normalized_joint_burden < -tolerance:
            return False
        if self.normalized_joint_burden > 1.0 + tolerance:
            return False
        if abs(
            self.direct_fraction_of_joint + self.interaction_fraction_of_joint - 1.0
        ) > tolerance and self.normalized_joint_burden > tolerance:
            return False
        if self.active_interaction_orders != tuple(
            sorted(
                order
                for order, value in self.interaction_order_bits.items()
                if abs(value) > tolerance
            )
        ):
            return False
        if (
            self.dominant_interaction_order is not None
            and self.dominant_interaction_order not in self.active_interaction_orders
        ):
            return False
        if self.interaction_order_absolute_shares:
            total = sum(self.interaction_order_absolute_shares.values())
            if abs(total - 1.0) > tolerance:
                return False
        return True

    def to_payload(self) -> dict[str, object]:
        if not self.verify():
            raise ValueError("normalized obstruction metrics failed verification")
        return {
            "carrier_worlds": self.carrier_worlds,
            "baseline_blocks": self.baseline_blocks,
            "capacity_bits": self.capacity_bits,
            "normalized_joint_burden": self.normalized_joint_burden,
            "interaction_fraction_of_joint": self.interaction_fraction_of_joint,
            "direct_fraction_of_joint": self.direct_fraction_of_joint,
            "interaction_order_bits": {
                str(order): value
                for order, value in sorted(self.interaction_order_bits.items())
            },
            "interaction_order_absolute_shares": {
                str(order): value
                for order, value in sorted(
                    self.interaction_order_absolute_shares.items()
                )
            },
            "active_interaction_orders": list(self.active_interaction_orders),
            "dominant_interaction_order": self.dominant_interaction_order,
        }


def normalized_obstruction_metrics(
    report: ObstructionSpectrumReport, *, carrier_worlds: int
) -> NormalizedObstructionMetrics:
    """Normalize a finite obstruction spectrum by available refinement capacity.

    The maximum possible debt from a baseline with B blocks on a carrier with N
    worlds is log2(N/B), attained by the discrete partition. The normalized joint
    burden is therefore D_joint / log2(N/B). Interaction fractions use signed
    debt accounting, while order shares use absolute interaction magnitude so
    cancellation across orders does not obscure which order dominates.
    """

    if not report.verify():
        raise ValueError("obstruction spectrum report failed verification")
    if carrier_worlds < report.joint_blocks:
        raise ValueError(
            "carrier_worlds must be at least the realized joint block count"
        )

    capacity_bits = log2(carrier_worlds / report.baseline_blocks)
    if capacity_bits <= 1e-12:
        normalized_joint = 0.0
    else:
        normalized_joint = report.joint_debt / capacity_bits

    if report.joint_debt <= 1e-12:
        interaction_fraction = 0.0
        direct_fraction = 0.0
    else:
        interaction_fraction = report.delta / report.joint_debt
        direct_fraction = sum(report.standalone_debts) / report.joint_debt

    order_bits: dict[int, float] = {}
    for dividend in report.interaction_dividends:
        if dividend.order >= 2:
            order_bits[dividend.order] = (
                order_bits.get(dividend.order, 0.0) + dividend.bits
            )

    active_orders = tuple(
        sorted(order for order, value in order_bits.items() if abs(value) > 1e-12)
    )
    abs_total = sum(abs(order_bits[order]) for order in active_orders)
    order_shares = (
        {order: abs(order_bits[order]) / abs_total for order in active_orders}
        if abs_total > 1e-12
        else {}
    )
    dominant_order = (
        max(active_orders, key=lambda order: (abs(order_bits[order]), -order))
        if active_orders
        else None
    )

    metrics = NormalizedObstructionMetrics(
        carrier_worlds=carrier_worlds,
        baseline_blocks=report.baseline_blocks,
        capacity_bits=capacity_bits,
        normalized_joint_burden=normalized_joint,
        interaction_fraction_of_joint=interaction_fraction,
        direct_fraction_of_joint=direct_fraction,
        interaction_order_bits=order_bits,
        interaction_order_absolute_shares=order_shares,
        active_interaction_orders=active_orders,
        dominant_interaction_order=dominant_order,
    )
    if not metrics.verify():
        raise AssertionError("constructed normalized obstruction metrics did not verify")
    return metrics


__all__ = ["NormalizedObstructionMetrics", "normalized_obstruction_metrics"]
