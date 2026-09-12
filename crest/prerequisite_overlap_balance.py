"""Exact overlap-balance law for CREST prerequisite leakage.

For two prospective queries with distinct prerequisite channels, semantic access
sets may overlap.  At Shannon order the prospective game remains additive and
there is no undeclared joint-prerequisite dividend.  Away from Shannon order,
the cross-difference is controlled exactly by four q-power masses: left-only,
right-only, overlap, and residual.

This module isolates that finite-state law.  It deliberately does not claim a
new characterization of Shannon or of Renyi entropy.
"""

from __future__ import annotations

from math import inf, isclose, isinf, log2
from typing import Iterable, Sequence

from .renyi_access import continuous_decoder_gain


def _probabilities(probabilities: Sequence[float]) -> tuple[float, ...]:
    ps = tuple(float(p) for p in probabilities)
    if not ps:
        raise ValueError("probabilities must be nonempty")
    if any(p <= 0.0 for p in ps):
        raise ValueError("probabilities must be positive")
    if not isclose(sum(ps), 1.0, rel_tol=0.0, abs_tol=1e-12):
        raise ValueError("probabilities must sum to one")
    return ps


def _validate(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> tuple[tuple[float, ...], frozenset[int], frozenset[int], float, float, float]:
    ps = _probabilities(probabilities)
    left = frozenset(int(i) for i in left_cells)
    right = frozenset(int(i) for i in right_cells)
    a, b, order = map(float, (left_bits, right_bits, q))
    if not left or not right:
        raise ValueError("both access sets must be nonempty")
    if any(i < 0 or i >= len(ps) for i in left | right):
        raise ValueError("accessible cell index out of range")
    if a <= 0.0 or b <= 0.0:
        raise ValueError("both decoder depths must be positive")
    if order < 0.0:
        raise ValueError("q must be nonnegative")
    return ps, left, right, a, b, order


def overlap_region_q_masses(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    q: float,
) -> tuple[float, float, float, float]:
    """Return (X_q, Y_q, Z_q, W_q) for the four access regions.

    X is left-only, Y is right-only, Z is overlap, and W is residual.
    """

    ps = _probabilities(probabilities)
    left = frozenset(int(i) for i in left_cells)
    right = frozenset(int(i) for i in right_cells)
    order = float(q)
    if order < 0.0 or isinf(order):
        raise ValueError("region q-masses require finite nonnegative q")
    if not left or not right:
        raise ValueError("both access sets must be nonempty")
    if any(i < 0 or i >= len(ps) for i in left | right):
        raise ValueError("accessible cell index out of range")

    left_only = left - right
    right_only = right - left
    overlap = left & right
    residual = frozenset(range(len(ps))) - (left | right)
    power = lambda cells: sum(ps[i] ** order for i in cells)
    return power(left_only), power(right_only), power(overlap), power(residual)


def overlap_balance(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    q: float,
) -> float:
    """Return B_q = W_q Z_q - X_q Y_q."""

    X, Y, Z, W = overlap_region_q_masses(probabilities, left_cells, right_cells, q)
    return W * Z - X * Y


def overlapping_access_leakage(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> float:
    """Exact undeclared joint dividend for two possibly overlapping access sets.

    For finite q != 1, let X,Y,Z,W be the q-power masses of left-only,
    right-only, overlap, and residual cells, and let

        A = 2**((1-q)*left_bits), B = 2**((1-q)*right_bits).

    Then the cross-difference is

        D_q = 1/(1-q) log2(
            ((X*A + Y*B + Z*A*B + W) * (X+Y+Z+W)) /
            ((A*(X+Z)+Y+W) * (B*(Y+Z)+X+W))
        ).

    The numerator-minus-denominator inside this ratio factors as

        (A-1)*(B-1)*(W*Z - X*Y).

    Hence Shannon always gives zero leakage.  For finite q != 1, additional
    zero-leakage points occur exactly on the overlap-balance surface WZ=XY.
    """

    ps, left, right, a, b, q = _validate(
        probabilities, left_cells, right_cells, left_bits, right_bits, q
    )
    if q == 1.0:
        return 0.0
    if isinf(q):
        left_local = [a if i in left else 0.0 for i in range(len(ps))]
        right_local = [b if i in right else 0.0 for i in range(len(ps))]
        both_local = [left_local[i] + right_local[i] for i in range(len(ps))]
        return (
            continuous_decoder_gain(ps, both_local, inf)
            - continuous_decoder_gain(ps, left_local, inf)
            - continuous_decoder_gain(ps, right_local, inf)
        )

    X, Y, Z, W = overlap_region_q_masses(ps, left, right, q)
    A = 2.0 ** ((1.0 - q) * a)
    B = 2.0 ** ((1.0 - q) * b)
    baseline = X + Y + Z + W
    both = X * A + Y * B + Z * A * B + W
    left_sum = A * (X + Z) + Y + W
    right_sum = B * (Y + Z) + X + W
    ratio = (both * baseline) / (left_sum * right_sum)
    return log2(ratio) / (1.0 - q)


def overlapping_access_leakage_sign(
    probabilities: Sequence[float],
    left_cells: Iterable[int],
    right_cells: Iterable[int],
    left_bits: float,
    right_bits: float,
    q: float,
) -> int:
    """Return the exact finite-q sign from the overlap-balance factorization."""

    ps, left, right, _, _, q = _validate(
        probabilities, left_cells, right_cells, left_bits, right_bits, q
    )
    if q == 1.0:
        return 0
    if isinf(q):
        value = overlapping_access_leakage(ps, left, right, left_bits, right_bits, q)
        if isclose(value, 0.0, abs_tol=1e-12):
            return 0
        return 1 if value > 0.0 else -1

    balance = overlap_balance(ps, left, right, q)
    if isclose(balance, 0.0, abs_tol=1e-15):
        return 0
    balance_sign = 1 if balance > 0.0 else -1
    return balance_sign if q < 1.0 else -balance_sign
