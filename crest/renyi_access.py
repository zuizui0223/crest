"""Rényi/Hill information gain under sparse semantic access.

This module generalizes CREST's count-based sparse-access result from support
size (Rényi order q=0) to nonuniform semantic-pair occupancy.  Rényi entropy
itself is standard; the object encoded here is CREST's selective refinement
operator: inaccessible semantic cells remain unsplit while accessible cells are
refined by a declared local decoder multiplicity.
"""

from __future__ import annotations

from math import isclose, log2
from typing import Iterable, Sequence


def _probabilities(probabilities: Sequence[float]) -> tuple[float, ...]:
    ps = tuple(float(p) for p in probabilities)
    if not ps:
        raise ValueError("probabilities must be nonempty")
    if any(p <= 0.0 for p in ps):
        raise ValueError("all semantic-cell probabilities must be positive")
    total = sum(ps)
    if not isclose(total, 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return ps


def _indices(indices: Iterable[int], n: int) -> tuple[int, ...]:
    out = tuple(sorted(set(indices)))
    if any(i < 0 or i >= n for i in out):
        raise ValueError("accessible index out of range")
    return out


def renyi_access_gain(
    probabilities: Sequence[float],
    accessible: Iterable[int],
    bit_depth: int,
    q: float,
) -> float:
    """Exact information gain from selectively splitting accessible cells.

    Each accessible semantic cell is split uniformly into ``2**bit_depth``
    descendants; inaccessible cells remain singletons.  The returned value is
    refined Rényi entropy minus baseline Rényi entropy, in bits.
    """

    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 0:
        raise ValueError("bit_depth must be a nonnegative integer")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")

    ps = _probabilities(probabilities)
    access = set(_indices(accessible, len(ps)))
    multiplicity = 2**bit_depth

    if q == 0.0:
        refined_support = sum(multiplicity if i in access else 1 for i in range(len(ps)))
        return log2(refined_support / len(ps))
    if q == 1.0:
        accessible_mass = sum(ps[i] for i in access)
        return bit_depth * accessible_mass

    base_power = sum(p**q for p in ps)
    split_factor = multiplicity ** (1.0 - q)
    refined_power = sum(
        (p**q) * (split_factor if i in access else 1.0)
        for i, p in enumerate(ps)
    )
    return log2(refined_power / base_power) / (1.0 - q)


def heterogeneous_renyi_access_gain(
    probabilities: Sequence[float],
    multiplicities: Sequence[int],
    q: float,
) -> float:
    """Exact gain when semantic cell i is split into ``multiplicities[i]`` cells.

    ``M_i=1`` represents no future refinement.  Accessible descendants are
    equiprobable within each parent semantic cell.
    """

    ps = _probabilities(probabilities)
    ms = tuple(multiplicities)
    if len(ms) != len(ps):
        raise ValueError("one multiplicity is required per semantic cell")
    if any(not isinstance(m, int) or isinstance(m, bool) or m < 1 for m in ms):
        raise ValueError("multiplicities must be positive integers")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")

    if q == 0.0:
        return log2(sum(ms) / len(ms))
    if q == 1.0:
        return sum(p * log2(m) for p, m in zip(ps, ms))

    base_power = sum(p**q for p in ps)
    refined_power = sum((p**q) * (m ** (1.0 - q)) for p, m in zip(ps, ms))
    return log2(refined_power / base_power) / (1.0 - q)


def asymptotic_slope(
    probabilities: Sequence[float],
    accessible: Iterable[int],
    q: float,
) -> float:
    """Return lim_{m->infinity} G_q(m)/m for nontrivial sparse access."""

    ps = _probabilities(probabilities)
    access = set(_indices(accessible, len(ps)))
    if not access or len(access) == len(ps):
        raise ValueError("three-regime law requires both accessible and inaccessible cells")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if q < 1.0:
        return 1.0
    if q == 1.0:
        return sum(ps[i] for i in access)
    return 0.0


def asymptotic_offset_q_below_one(
    probabilities: Sequence[float],
    accessible: Iterable[int],
    q: float,
) -> float:
    """Return C_q in G_q(m)=m-C_q+o(1), valid for 0 <= q < 1."""

    ps = _probabilities(probabilities)
    access = set(_indices(accessible, len(ps)))
    q = float(q)
    if not (0.0 <= q < 1.0):
        raise ValueError("offset is defined here only for 0 <= q < 1")
    if not access:
        raise ValueError("at least one accessible cell is required")
    if q == 0.0:
        return log2(len(ps) / len(access))
    total_q = sum(p**q for p in ps)
    access_q = sum(ps[i] ** q for i in access)
    return log2(total_q / access_q) / (1.0 - q)


def asymptotic_limit_q_above_one(
    probabilities: Sequence[float],
    accessible: Iterable[int],
    q: float,
) -> float:
    """Return lim_{m->infinity} G_q(m), valid for q>1 with inaccessible mass."""

    ps = _probabilities(probabilities)
    access = set(_indices(accessible, len(ps)))
    q = float(q)
    if q <= 1.0:
        raise ValueError("finite saturation limit requires q > 1")
    inaccessible = [i for i in range(len(ps)) if i not in access]
    if not inaccessible:
        raise ValueError("at least one inaccessible cell is required")
    total_q = sum(p**q for p in ps)
    inaccessible_q = sum(ps[i] ** q for i in inaccessible)
    return log2(total_q / inaccessible_q) / (q - 1.0)


def fixed_budget_extrema(
    probabilities: Sequence[float],
    k: int,
    bit_depth: int,
    q: float,
) -> tuple[float, float]:
    """Sharp min/max gain over all accessible sets of cardinality k.

    For q>0, bottom-k occupancy minimizes and top-k occupancy maximizes gain.
    At q=0, placement is irrelevant and the two values coincide.
    """

    ps = _probabilities(probabilities)
    if not isinstance(k, int) or isinstance(k, bool) or not (0 <= k <= len(ps)):
        raise ValueError("k must be an integer between zero and the number of cells")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    bottom = order[:k]
    top = order[len(ps) - k :] if k else []
    low = renyi_access_gain(ps, bottom, bit_depth, q)
    high = renyi_access_gain(ps, top, bit_depth, q)
    return low, high
