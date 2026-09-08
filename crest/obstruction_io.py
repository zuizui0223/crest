"""JSON-facing adapter for finite CREST obstruction-spectrum contracts."""

from __future__ import annotations

from typing import Any

from .joint_state import AuditRefinement
from .obstruction_normalized import normalized_obstruction_metrics
from .obstruction_spectrum import ObstructionSpectrumReport, obstruction_spectrum


def _as_tuple(value: Any, *, name: str) -> tuple[Any, ...]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a JSON array")
    return tuple(value)


def parse_obstruction_contract(
    payload: dict[str, Any],
) -> tuple[tuple[Any, ...], tuple[AuditRefinement, ...]]:
    """Parse one explicit finite obstruction contract from a JSON-like mapping."""

    if not isinstance(payload, dict):
        raise ValueError("contract must be a JSON object")
    baseline = _as_tuple(payload.get("baseline"), name="baseline")
    if not baseline:
        raise ValueError("baseline must be nonempty")
    raw_audits = payload.get("audits")
    if not isinstance(raw_audits, list) or not raw_audits:
        raise ValueError("audits must be a nonempty JSON array")

    audits: list[AuditRefinement] = []
    for index, raw in enumerate(raw_audits):
        if not isinstance(raw, dict):
            raise ValueError(f"audits[{index}] must be a JSON object")
        name = raw.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"audits[{index}].name must be a nonempty string")
        static_labels = _as_tuple(
            raw.get("static_labels"), name=f"audits[{index}].static_labels"
        )
        actions = _as_tuple(raw.get("actions"), name=f"audits[{index}].actions")
        raw_successors = raw.get("successors")
        if not isinstance(raw_successors, list):
            raise ValueError(f"audits[{index}].successors must be a JSON array")
        successors = tuple(
            _as_tuple(row, name=f"audits[{index}].successors[{row_index}]")
            for row_index, row in enumerate(raw_successors)
        )
        audits.append(
            AuditRefinement(
                name=name,
                static_labels=static_labels,
                actions=actions,
                successors=successors,
            )
        )

    if any(audit.world_count != len(baseline) for audit in audits):
        raise ValueError("baseline and every audit must share one finite carrier")
    return baseline, tuple(audits)


def spectrum_payload(
    report: ObstructionSpectrumReport, *, carrier_worlds: int | None = None
) -> dict[str, Any]:
    """Convert a verified spectrum into a stable JSON-serializable payload."""

    if not report.verify():
        raise ValueError("obstruction spectrum report failed verification")
    payload: dict[str, Any] = {
        "audit_names": list(report.audit_names),
        "baseline_blocks": report.baseline_blocks,
        "joint_blocks": report.joint_blocks,
        "standalone_debts_bits": dict(
            zip(report.audit_names, report.standalone_debts)
        ),
        "shapley_contributions_bits": dict(
            zip(report.audit_names, report.shapley_contributions)
        ),
        "shapley_shares": dict(zip(report.audit_names, report.shapley_shares)),
        "interaction_attributions_bits": dict(
            zip(report.audit_names, report.interaction_attributions)
        ),
        "joint_debt_bits": report.joint_debt,
        "delta_bits": report.delta,
        "coalitions": [
            {"audits": list(row.audits), "blocks": row.blocks, "debt_bits": row.debt}
            for row in report.coalition_debts
        ],
        "interaction_dividends": [
            {"audits": list(row.audits), "order": row.order, "bits": row.bits}
            for row in report.interaction_dividends
        ],
    }
    if carrier_worlds is not None:
        payload["normalized"] = normalized_obstruction_metrics(
            report, carrier_worlds=carrier_worlds
        ).to_payload()
    return payload


def spectrum_from_payload(payload: dict[str, Any]) -> dict[str, Any]:
    baseline, audits = parse_obstruction_contract(payload)
    return spectrum_payload(
        obstruction_spectrum(audits, baseline), carrier_worlds=len(baseline)
    )


__all__ = [
    "parse_obstruction_contract",
    "spectrum_from_payload",
    "spectrum_payload",
]
