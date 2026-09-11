"""Rényi/Hill information gain under sparse semantic access.

This module generalizes CREST's count-based sparse-access result from support
size (Rényi order q=0) to nonuniform semantic-pair occupancy. Rényi entropy
itself is standard; the object encoded here is CREST's selective refinement
operator: inaccessible semantic cells remain unsplit while accessible cells are
refined by a declared local decoder multiplicity.
"""

from __future__ import annotations

from math import inf, isclose, isfinite, isinf, log2
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
    descendants; inaccessible cells remain singletons. The returned value is
    refined Rényi entropy minus baseline Rényi entropy, in bits. ``q=inf``
    returns the min-entropy endpoint.
    """

    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 0:
        raise ValueError("bit_depth must be a nonnegative integer")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")

    ps = _probabilities(probabilities)
    access = set(_indices(accessible, len(ps)))
    multiplicity = 2**bit_depth

    if isinf(q):
        base_max = max(ps)
        refined_max = max(
            p / multiplicity if i in access else p for i, p in enumerate(ps)
        )
        return log2(base_max / refined_max)
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


def continuous_decoder_gain(
    probabilities: Sequence[float],
    decoder_bits: Sequence[float],
    q: float,
) -> float:
    """Rényi gain for a continuous decoder-depth relaxation.

    Cell ``i`` receives ``x_i >= 0`` bits and is idealized as splitting into
    ``2**x_i`` equiprobable descendants. Integer ``x_i`` recovers an ordinary
    finite split; noninteger values define the convex resource-allocation
    relaxation used by the supplementary optimal-design theorem.
    """

    ps = _probabilities(probabilities)
    xs = tuple(float(x) for x in decoder_bits)
    if len(xs) != len(ps):
        raise ValueError("one decoder depth is required per semantic cell")
    if any(x < 0.0 or not isfinite(x) for x in xs):
        raise ValueError("decoder depths must be finite and nonnegative")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")

    if isinf(q):
        return log2(max(ps) / max(p * (2.0 ** (-x)) for p, x in zip(ps, xs)))
    if q == 0.0:
        return log2(sum(2.0**x for x in xs) / len(xs))
    if q == 1.0:
        return sum(p * x for p, x in zip(ps, xs))

    base_power = sum(p**q for p in ps)
    refined_power = sum((p**q) * (2.0 ** ((1.0 - q) * x)) for p, x in zip(ps, xs))
    return log2(refined_power / base_power) / (1.0 - q)


def optimal_decoder_allocation(
    probabilities: Sequence[float],
    budget_bits: float,
    q: float,
) -> tuple[float, ...]:
    """Return one gain-maximizing allocation under ``sum(x_i)=budget_bits``.

    For ``0 <= q <= 1`` the convex/linear objective is maximized at a simplex
    vertex: all depth is assigned to a most-occupied cell (at ``q=0`` every
    vertex is equivalent, and the same deterministic choice is returned).

    For ``q>1`` the objective is strictly convex after reversing the negative
    Rényi prefactor, yielding the unique water-filling solution

        x_i = max(0, q/(q-1) * log2(p_i) - tau),

    where ``tau`` is chosen so that the depths sum to the budget. At ``q=inf``
    the limiting formula uses ``log2(p_i)`` in place of ``q/(q-1) log2(p_i)``.
    """

    ps = _probabilities(probabilities)
    budget = float(budget_bits)
    if budget < 0.0 or not isfinite(budget):
        raise ValueError("budget_bits must be finite and nonnegative")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if budget == 0.0:
        return tuple(0.0 for _ in ps)

    if q <= 1.0:
        target = max(range(len(ps)), key=lambda i: (ps[i], -i))
        return tuple(budget if i == target else 0.0 for i in range(len(ps)))

    coefficient = 1.0 if isinf(q) else q / (q - 1.0)
    scores = tuple(coefficient * log2(p) for p in ps)

    # Solve sum_i max(0, score_i - tau) = budget by monotone bisection.
    low = min(scores) - budget - 1.0
    high = max(scores)
    for _ in range(200):
        tau = (low + high) / 2.0
        allocated = sum(max(0.0, score - tau) for score in scores)
        if allocated > budget:
            low = tau
        else:
            high = tau
    tau = high
    allocation = [max(0.0, score - tau) for score in scores]
    # Absorb floating residual into the largest active coordinate.
    residual = budget - sum(allocation)
    target = max(range(len(ps)), key=lambda i: allocation[i])
    allocation[target] += residual
    return tuple(allocation)


def optimal_integer_decoder_allocation(
    probabilities: Sequence[float],
    budget_bits: int,
    q: float,
) -> tuple[int, ...]:
    """Return an exact gain-maximizing allocation of an integer bit budget.

    For ``0 <= q <= 1`` an optimum concentrates every bit on a most-occupied
    semantic cell (at ``q=0`` every simplex vertex is equivalent).

    For finite ``q>1``, after ``x_i`` bits have been assigned to cell ``i``, the
    next bit reduces the refined q-power sum by a constant multiple of

        p_i**q * 2**(-(q-1)*x_i).

    These marginal reductions decrease geometrically along each cell. Therefore
    selecting the largest currently available marginal reduction at every step
    is globally optimal for the separable integer resource-allocation problem.
    At ``q=inf`` the same rule acts on the current dominant residual
    ``p_i * 2**(-x_i)`` and exactly minimizes the largest refined atom.
    """

    ps = _probabilities(probabilities)
    if (
        not isinstance(budget_bits, int)
        or isinstance(budget_bits, bool)
        or budget_bits < 0
    ):
        raise ValueError("budget_bits must be a nonnegative integer")
    q = float(q)
    if q < 0.0:
        raise ValueError("q must be nonnegative")
    if budget_bits == 0:
        return tuple(0 for _ in ps)

    if q <= 1.0:
        target = max(range(len(ps)), key=lambda i: (ps[i], -i))
        return tuple(budget_bits if i == target else 0 for i in range(len(ps)))

    allocation = [0 for _ in ps]
    for _ in range(budget_bits):
        if isinf(q):
            score = lambda i: ps[i] * (2.0 ** (-allocation[i]))
        else:
            score = lambda i: (ps[i] ** q) * (2.0 ** (-(q - 1.0) * allocation[i]))
        target = max(range(len(ps)), key=lambda i: (score(i), -i))
        allocation[target] += 1
    return tuple(allocation)


def heterogeneous_renyi_access_gain(
    probabilities: Sequence[float],
    multiplicities: Sequence[int],
    q: float,
) -> float:
    """Exact gain when semantic cell i is split into ``multiplicities[i]`` cells.

    ``M_i=1`` represents no future refinement. Accessible descendants are
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

    if isinf(q):
        return log2(max(ps) / max(p / m for p, m in zip(ps, ms)))
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
    if q <= 1.0 or isinf(q):
        raise ValueError("finite-q saturation formula requires 1 < q < infinity")
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
