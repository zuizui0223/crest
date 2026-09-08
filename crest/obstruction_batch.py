"""Batch comparison surfaces for finite CREST obstruction contracts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .obstruction_io import spectrum_from_payload


@dataclass(frozen=True)
class ObstructionProfileRow:
    name: str
    carrier_worlds: int
    baseline_blocks: int
    joint_blocks: int
    joint_debt_bits: float
    normalized_joint_burden: float
    interaction_fraction_of_joint: float
    direct_fraction_of_joint: float
    delta_bits: float
    active_interaction_orders: tuple[int, ...]
    dominant_interaction_order: int | None

    def to_payload(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "carrier_worlds": self.carrier_worlds,
            "baseline_blocks": self.baseline_blocks,
            "joint_blocks": self.joint_blocks,
            "joint_debt_bits": self.joint_debt_bits,
            "normalized_joint_burden": self.normalized_joint_burden,
            "interaction_fraction_of_joint": self.interaction_fraction_of_joint,
            "direct_fraction_of_joint": self.direct_fraction_of_joint,
            "delta_bits": self.delta_bits,
            "active_interaction_orders": list(self.active_interaction_orders),
            "dominant_interaction_order": self.dominant_interaction_order,
        }


def _row(name: str, contract: dict[str, Any]) -> tuple[ObstructionProfileRow, tuple[str, ...]]:
    spectrum = spectrum_from_payload(contract)
    normalized = spectrum["normalized"]
    return (
        ObstructionProfileRow(
            name=name,
            carrier_worlds=int(normalized["carrier_worlds"]),
            baseline_blocks=int(spectrum["baseline_blocks"]),
            joint_blocks=int(spectrum["joint_blocks"]),
            joint_debt_bits=float(spectrum["joint_debt_bits"]),
            normalized_joint_burden=float(normalized["normalized_joint_burden"]),
            interaction_fraction_of_joint=float(
                normalized["interaction_fraction_of_joint"]
            ),
            direct_fraction_of_joint=float(normalized["direct_fraction_of_joint"]),
            delta_bits=float(spectrum["delta_bits"]),
            active_interaction_orders=tuple(
                int(value) for value in normalized["active_interaction_orders"]
            ),
            dominant_interaction_order=(
                None
                if normalized["dominant_interaction_order"] is None
                else int(normalized["dominant_interaction_order"])
            ),
        ),
        tuple(str(value) for value in spectrum["audit_names"]),
    )


def rank_obstruction_contracts(
    contracts: Mapping[str, dict[str, Any]],
    *,
    rank_by: str = "normalized_joint_burden",
) -> dict[str, Any]:
    """Compute and rank obstruction profiles for named finite contracts.

    All contracts must use the same named responsibility set. This is a minimal
    machine-checkable comparability condition; scientific comparability still
    requires commensurable carrier construction and baseline semantics.
    """

    if not contracts:
        raise ValueError("at least one named contract is required")
    allowed = {
        "normalized_joint_burden",
        "joint_debt_bits",
        "interaction_fraction_of_joint",
        "delta_bits",
    }
    if rank_by not in allowed:
        raise ValueError(f"rank_by must be one of {sorted(allowed)}")

    rows: list[ObstructionProfileRow] = []
    reference_names: set[str] | None = None
    for name, contract in contracts.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("contract names must be nonempty strings")
        row, audit_names = _row(name, contract)
        audit_set = set(audit_names)
        if reference_names is None:
            reference_names = audit_set
        elif audit_set != reference_names:
            raise ValueError("all contracts must contain the same audit names")
        rows.append(row)

    rows.sort(key=lambda item: (-float(getattr(item, rank_by)), item.name))
    return {
        "rank_by": rank_by,
        "audit_names": sorted(reference_names or set()),
        "comparability_firewall": (
            "ranking is contract-relative; interpret across systems only when "
            "carrier construction and baseline semantics are commensurable"
        ),
        "rows": [row.to_payload() for row in rows],
    }


__all__ = ["ObstructionProfileRow", "rank_obstruction_contracts"]
