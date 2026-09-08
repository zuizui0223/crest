"""Pairwise geometry for named finite CREST obstruction contracts."""

from __future__ import annotations

from typing import Any, Mapping

from .obstruction_distance import compare_obstruction_profiles
from .obstruction_io import spectrum_from_payload


_ALLOWED_METRICS = {
    "raw_l1_bits",
    "raw_l2_bits",
    "normalized_l1",
    "normalized_l2",
}


def pairwise_obstruction_distances(
    contracts: Mapping[str, dict[str, Any]],
    *,
    metric: str = "normalized_l1",
) -> dict[str, Any]:
    """Return a symmetric pairwise distance matrix and nearest neighbors.

    The matrix is a geometry of obstruction-accounting profiles only. The same
    responsibility names are required mechanically. Cross-system scientific
    interpretation additionally requires commensurable responsibility meaning,
    carrier construction, and baseline semantics.
    """

    if not contracts:
        raise ValueError("at least one named contract is required")
    if metric not in _ALLOWED_METRICS:
        raise ValueError(f"metric must be one of {sorted(_ALLOWED_METRICS)}")

    names = sorted(contracts)
    if any(not isinstance(name, str) or not name.strip() for name in names):
        raise ValueError("contract names must be nonempty strings")

    spectra = {name: spectrum_from_payload(contracts[name]) for name in names}
    audit_sets = {name: set(spectra[name]["audit_names"]) for name in names}
    reference = audit_sets[names[0]]
    if any(audit_sets[name] != reference for name in names[1:]):
        raise ValueError("all contracts must contain the same audit names")

    matrix: dict[str, dict[str, float]] = {
        name: {other: 0.0 for other in names} for name in names
    }
    pair_details: list[dict[str, Any]] = []
    for left_index, left in enumerate(names):
        for right in names[left_index + 1 :]:
            distance = compare_obstruction_profiles(spectra[left], spectra[right])
            value = float(getattr(distance, metric))
            matrix[left][right] = value
            matrix[right][left] = value
            pair_details.append(
                {
                    "left": left,
                    "right": right,
                    "distance": value,
                    "difference_class": distance.difference_class(),
                    "dominant_changed_coalition": (
                        None
                        if distance.dominant_changed_coalition() is None
                        else list(distance.dominant_changed_coalition() or ())
                    ),
                }
            )

    nearest: dict[str, dict[str, Any] | None] = {}
    for name in names:
        candidates = [(matrix[name][other], other) for other in names if other != name]
        if not candidates:
            nearest[name] = None
            continue
        value, other = min(candidates, key=lambda item: (item[0], item[1]))
        nearest[name] = {"name": other, "distance": value}

    return {
        "metric": metric,
        "audit_names": sorted(reference),
        "names": names,
        "matrix": matrix,
        "nearest_neighbors": nearest,
        "pairs": pair_details,
        "comparability_firewall": (
            "matrix geometry is profile-relative; interpret across systems only when "
            "responsibility, carrier, and baseline semantics are commensurable"
        ),
    }


__all__ = ["pairwise_obstruction_distances"]
