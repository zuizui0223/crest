# Supplementary Information II: Prerequisite support and Rényi-order leakage

This supplement isolates the CREST-specific link between declared prerequisite order and semantic-access coverage. Möbius/Harsanyi inversion, unanimity games, Shannon additivity, and Rényi entropy are standard and are not claimed here as new mathematics. The contribution is the exact factorization of CREST's prospective information game at Shannon order and a sharp disjoint-access law showing why the same support interpretation fails outside Shannon order.

## SII.1. Setup

Let `U` be the retained pre-future interfaces and `F` the prospective responsibility. Each future query `f` declares a minimal prerequisite set \(R_f\subseteq U\), an addressable semantic-cell set \(A_f\), and a decoder depth \(m_f\ge0\) bits. Let semantic-cell occupancies be \(p_i>0\), with \(\sum_i p_i=1\), and define \(P(A_f)=\sum_{i\in A_f}p_i\). Simultaneously licensed refinements compose by multiplying local descendant multiplicities, equivalently by adding local decoder depths.

## SII.2. Theorem S8: prerequisite-support factorization at Shannon order

For coalition \(S\subseteq U\cup\{F\}\),

\[
\boxed{
v_1(S)=\sum_f m_fP(A_f)\,\mathbf 1\{R_f\cup\{F\}\subseteq S\}.
}
\]

Thus \(v_1\) is a weighted sum of unanimity games, and its Boolean-lattice Möbius transform is

\[
\boxed{
d_1(T)=\sum_{f:R_f\cup\{F\}=T}m_fP(A_f).
}
\]

Hence prerequisite order determines **where** prospective Shannon information appears, while semantic coverage and occupancy determine **how much** appears there. Interfaces absent from every \(R_f\) cannot acquire spurious prospective Shannon interaction; queries with identical prerequisites aggregate; and overlapping access sets create no extra Shannon interaction under multiplicative local refinement.

For the canonical CREST witness, one query requires \(\{H,\Theta\}\), one of four uniformly occupied semantic cells is addressable, and \(m=10\), giving

\[
\boxed{d_1(\{H,\Theta,F\})=10/4=2.5\text{ bits}.}
\]

This is distinct from the main-text Hartley/support-count dividend \(\log_2(1027/4)\approx8.004220466\) bits.

### Proof

Query \(f\) is licensed iff \(F\in S\) and \(R_f\subseteq S\). It contributes \(m_f\) Shannon bits on every addressable cell and zero elsewhere, so its expected gain is \(m_fP(A_f)\). Summing gives the weighted-unanimity representation. A unanimity game's Möbius transform is supported only on its defining coalition; linearity gives the coefficient formula.

## SII.3. Theorem S9: general disjoint-access Shannon-uniqueness law

Consider any finite semantic state space with positive occupancies \(p_i\). Let two future queries have distinct prerequisite channels, with one requiring only \(H\) and the other only \(\Theta\). Let their semantic access sets be nonempty and disjoint,

\[
L\cap R=\varnothing,
\]

and let their decoder depths be \(a,b>0\). No query declares the joint prerequisite \(\{H,\Theta\}\). Cells outside \(L\cup R\) may remain unrefined and may carry arbitrary positive occupancy.

For finite Rényi order \(q\ne1\), define the three \(q\)-power masses

\[
U_q=\sum_{i\in L}p_i^q,\qquad
V_q=\sum_{i\in R}p_i^q,\qquad
W_q=\sum_{i\notin L\cup R}p_i^q,
\]

and

\[
A_q=2^{(1-q)a},\qquad B_q=2^{(1-q)b}.
\]

The undeclared \(H\times\Theta\times F\) Möbius dividend is exactly

\[
\boxed{
D_q=
\frac{1}{1-q}
\log_2
\frac{
(U_qA_q+V_qB_q+W_q)(U_q+V_q+W_q)
}{
(U_qA_q+V_q+W_q)(U_q+V_qB_q+W_q)
}.
}
\]

The sign is determined without approximation. The difference between the numerator and denominator inside the logarithmic ratio factors as

\[
\boxed{
(U_qA_q+V_qB_q+W_q)(U_q+V_q+W_q)
-
(U_qA_q+V_q+W_q)(U_q+V_qB_q+W_q)
=
-U_qV_q(A_q-1)(B_q-1).
}
\]

The residual mass \(W_q\) cancels completely from this sign determinant. Since both access sets are nonempty and all occupancies are positive, \(U_q,V_q>0\). Therefore

\[
\boxed{
D_q<0\quad(0\le q<1),\qquad
D_1=0,\qquad
D_q>0\quad(1<q<\infty).
}
\]

Thus, for **every positive finite occupancy distribution, every pair of nonempty disjoint semantic access sets, arbitrary unrefined residual cells, and every positive pair of decoder depths**, Shannon order is the unique finite Rényi order at which the undeclared joint-prerequisite interaction vanishes.

At \(q=1\), Shannon additivity gives directly

\[
G_1(L,R)=aP(L)+bP(R)=G_1(L,\varnothing)+G_1(\varnothing,R),
\]

so the cross-difference is exactly zero.

### Two-cell and symmetric corollaries

If \(L\) and \(R\) each contain one cell and no residual cells remain, the theorem reduces to the two-cell law. Writing the left occupancy as \(p\in(0,1)\) gives

\[
D_q(p,a,b)=
\frac{1}{1-q}
\log_2
\frac{(u+v)(uA+vB)}{(uA+v)(u+vB)},
\]

with \(u=p^q\), \(v=(1-p)^q\), \(A=2^{(1-q)a}\), and \(B=2^{(1-q)b}\).

Setting further \(p=1/2\) and \(a=b=1\) recovers

\[
D_q=1-\frac{2}{1-q}\log_2\left(\frac12+2^{-q}\right),
\]

with \(D_\infty=1\) bit for this symmetric endpoint witness.

The theorem separates:

- **structural interaction**: interaction implied by declared prerequisite sets and recovered exactly by Shannon prospective dividends;
- **distributional interaction**: additional interaction induced by nonlinear weighting of selectively refined semantic cells at non-Shannon Rényi orders.

## SII.4. Relation to Supplementary Information I

Supplementary Information I asks how much information selective refinement carries under different Rényi orders. Supplement II asks when an interaction coefficient can be read literally as prerequisite structure. Theorem S8 establishes exact Shannon support fidelity for arbitrary query families. Theorem S9 shows that even the cleanest pair of disjoint prerequisite channels generates undeclared joint interaction at every finite \(q\ne1\), regardless of occupancy heterogeneity, access-set cardinality, unrefined residual cells, or positive decoder-depth asymmetry.

Accordingly, prerequisite topology should be diagnosed with the Shannon prospective game. Non-Shannon spectra remain useful distribution-sensitive summaries, but their higher-order coefficients cannot in general be interpreted as literal prerequisite hyperedges.

## SII.5. Novelty boundary

The following are standard and are not claimed as new: Möbius/Harsanyi inversion, unanimity games, Shannon entropy and additivity, Rényi entropy, and Boolean-lattice coalition accounting. The CREST-specific results are:

1. the exact Shannon factorization linking prerequisite hyperedges to Möbius support and semantic-access occupancy to coefficient weights; and
2. the exact disjoint-access leakage law showing that, for arbitrary positive finite occupancy distributions, nonempty disjoint access sets, residual unrefined cells, and positive decoder depths, \(q=1\) is the unique finite Rényi order with zero undeclared joint-prerequisite interaction.

These are finite-state statements. They do not establish continuous-time limits, stochastic-process generality, or empirical occupancy distributions for any particular ecosystem.

## SII.6. Reproducibility

The factorization is implemented in `crest/prerequisite_access_game.py` and tested in `tests/test_prerequisite_access_game.py`. The disjoint-access leakage law is implemented in `crest/prerequisite_renyi_leakage.py` and tested in `tests/test_prerequisite_renyi_leakage.py`.

Tests compare the closed form with direct cellwise refinement and full Möbius inversion for multi-cell disjoint access sets with residual cells; verify the strict sign law on both sides of \(q=1\); recover unequal two-cell occupancies and asymmetric decoder depths as special cases; recover the symmetric canonical formula; and retain the canonical 2.5-bit pure three-way Shannon dividend.
