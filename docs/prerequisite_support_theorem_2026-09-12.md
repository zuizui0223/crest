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

## Novelty boundary

Möbius/Harsanyi inversion, unanimity games, and Shannon conditional-information additivity are standard and are not claimed as new mathematics. The CREST-specific contribution is the exact factorization of the declared prerequisite/access architecture: prerequisite hyperedges determine dividend support, whereas semantic-access occupancy determines dividend weights. This theorem formalizes the paper's qualitative distinction that prerequisite order determines **where** the prospective burden appears and semantic coverage determines **how large** it is.

## Executable verification

- `crest/prerequisite_access_game.py`
- `tests/test_prerequisite_access_game.py`

The tests compare the closed-form query sum with direct cellwise combined refinement for every coalition, apply Möbius inversion to the full game, verify zero leakage to an irrelevant interface, verify aggregation of queries with identical prerequisite sets, and recover the canonical pure three-way Shannon support.
