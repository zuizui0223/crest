# CREST prerequisite-support theorem

## Statement

Let `U` be retained pre-future interfaces and `F` the prospective responsibility. Each future query `f` declares:

- a minimal prerequisite set `R_f ⊆ U`;
- an addressable semantic-cell set `A_f`;
- decoder depth `m_f ≥ 0` bits.

Let semantic-cell occupancies be `p_i`, and let `P(A_f)=Σ_{i∈A_f} p_i`.
Assume that simultaneously licensed future refinements compose by multiplying local descendant multiplicities (equivalently, their local decoder depths add).

At Shannon order, the prospective information-gain game on coalition `S ⊆ U ∪ {F}` is

\[
v_1(S)=\sum_f m_f P(A_f)\,\mathbf 1\{R_f\cup\{F\}\subseteq S\}.
\]

Thus `v_1` is exactly a weighted sum of unanimity games. Its Boolean-lattice Möbius transform is

\[
\boxed{
d_1(T)=\sum_{f:R_f\cup\{F\}=T}m_f P(A_f),
}
\]

and `d_1(T)=0` for every coalition `T` that is not the minimal prerequisite support of at least one query.

## Consequences

1. **Prerequisite order determines where information can appear.** The support of the Möbius dividend is fixed by the declared minimal prerequisite hyperedges `R_f ∪ {F}`.
2. **Semantic coverage determines how much appears there.** Changing `A_f` or occupancy probabilities changes `P(A_f)` and therefore the dividend weight, but cannot move that query's Shannon dividend to another coalition.
3. **Irrelevant interfaces cannot acquire spurious prospective interaction.** Adding an interface not present in any `R_f` leaves every nonzero prospective dividend support unchanged.
4. **Queries sharing one prerequisite set aggregate.** Their weights add on the same Möbius coefficient.
5. **Overlapping semantic access sets do not create extra Shannon-order interaction terms** under the declared multiplicative-refinement composition: cellwise local depths add, so Shannon gain remains query-additive.

For the canonical CREST witness with one future query requiring `{H, THETA}`, uniform semantic occupancy over four cells, one addressable cell, and `m=10`, the prospective Shannon game has exactly one nonzero dividend:

\[
d_1(\{H,\Theta,F\})=10\times\frac14=2.5\text{ bits}.
\]

This is deliberately distinct from the main-text Hartley/support-count dividend `log2(1027/4) ≈ 8.00422` bits. The two quantities are different Rényi orders of the same sparse-access structure.

## Proof

For coalition `S`, query `f` is licensed iff `F∈S` and `R_f⊆S`. On every addressable cell it contributes `m_f` Shannon bits, and elsewhere zero. Therefore its expected gain is `m_f P(A_f)` when licensed and zero otherwise. Summing over queries gives the displayed weighted-unanimity representation.

The Möbius transform of a unanimity game supported on `T_f=R_f∪{F}` is one at `T_f` and zero elsewhere. Linearity of Möbius inversion therefore gives the coefficient formula above. The direct cellwise form gives the same result because overlapping licensed queries contribute additive local depths before taking the occupancy expectation.

## Shannon uniqueness: non-Shannon orders can leak across prerequisite support

The support theorem above is genuinely Shannon-specific. Consider the minimal symmetric witness with two equiprobable semantic cells. Query `a` requires only `H`, refines cell 0 by one bit, and query `b` requires only `THETA`, refines cell 1 by one bit. No query declares the joint prerequisite `{H, THETA}`.

For one licensed query, the refined distribution is `(1/4, 1/4, 1/2)`, whereas licensing both produces four atoms of probability `1/4`. For finite Rényi order `q != 1`, the single-query gain is

\[
g_q=\frac{1}{1-q}\log_2\left(\frac12+2^{-q}\right),
\]

and the two-query gain is exactly one bit. Therefore the `H × THETA × F` Möbius dividend is

\[
\boxed{
D_q
=1-\frac{2}{1-q}\log_2\left(\frac12+2^{-q}\right),
\qquad q\ne1.
}
\]

At `q=1`, each single query contributes `1/2` bit and the joint gain is one bit, so

\[
\boxed{D_1=0.}
\]

Moreover `D_q=0` has the unique solution `q=1`. Indeed, setting `D_q=0` is equivalent to

\[
\frac12+2^{-q}=2^{(1-q)/2}.
\]

Writing `t=2^{-q/2}` gives

\[
t^2-\sqrt2\,t+\frac12
=\left(t-\frac1{\sqrt2}\right)^2=0,
\]

hence `t=2^{-1/2}` and therefore `q=1`. The same identity shows the sign change:

\[
D_q<0\quad(0\le q<1),
\qquad
D_q>0\quad(q>1),
\]

with `D_infinity=1` bit.

Thus Shannon order is uniquely **prerequisite-support faithful** within this minimal Rényi witness: only at `q=1` does the prospective Möbius support coincide exactly with the declared prerequisite hyperedges. Other Rényi orders can generate emergent higher-order interaction from the nonlinear aggregation of selectively refined semantic cells even when no query declares that higher-order prerequisite.

This boundary is useful rather than pathological. It separates two notions that should not be conflated:

- **structural interaction**, fixed by declared prerequisite sets and recovered exactly by Shannon-order dividends; and
- **distributional interaction**, induced by nonlinear weighting of heterogeneous selectively refined cells at non-Shannon Rényi orders.

## Novelty boundary

Möbius/Harsanyi inversion, unanimity games, Shannon conditional-information additivity, and Rényi entropy itself are standard and are not claimed as new mathematics. The CREST-specific contribution is the exact factorization of the declared prerequisite/access architecture at Shannon order, together with the sharp boundary showing why this factorization cannot be extended indiscriminately across Rényi orders. Prerequisite hyperedges determine Shannon dividend support, semantic-access occupancy determines Shannon dividend weights, while non-Shannon orders can add distribution-induced interaction not present in the prerequisite graph.

## Executable verification

- `crest/prerequisite_access_game.py`
- `tests/test_prerequisite_access_game.py`
- `crest/prerequisite_renyi_leakage.py`
- `tests/test_prerequisite_renyi_leakage.py`

The tests compare the closed-form query sum with direct cellwise combined refinement for every coalition, apply Möbius inversion to the full game, verify zero leakage to an irrelevant interface, verify aggregation of queries with identical prerequisite sets, recover the canonical pure three-way Shannon support, match the exact two-query leakage formula to direct Möbius inversion across multiple Rényi orders, and verify that the leakage changes sign at the unique zero `q=1`.
