# Supplementary Information II: Prerequisite support and Rényi-order leakage

This supplement isolates the CREST-specific link between declared prerequisite order and semantic-access coverage. Möbius/Harsanyi inversion, unanimity games, Shannon additivity, and Rényi entropy are standard and are not claimed here as new mathematics. The contribution is the exact factorization of CREST's prospective information game at Shannon order and sharp finite-state laws describing when non-Shannon interaction does or does not preserve declared prerequisite support.

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

Consider any finite semantic state space with positive occupancies \(p_i\). Let two future queries have distinct prerequisite channels, with one requiring only \(H\) and the other only \(\Theta\). Let their semantic access sets be nonempty and disjoint, \(L\cap R=\varnothing\), and let their decoder depths be \(a,b>0\). No query declares the joint prerequisite \(\{H,\Theta\}\). Cells outside \(L\cup R\) may remain unrefined.

For finite Rényi order \(q\ne1\), define

\[
U_q=\sum_{i\in L}p_i^q,\qquad
V_q=\sum_{i\in R}p_i^q,\qquad
W_q=\sum_{i\notin L\cup R}p_i^q,
\]

and \(A_q=2^{(1-q)a}\), \(B_q=2^{(1-q)b}\). The undeclared \(H\times\Theta\times F\) dividend is

\[
D_q=
\frac{1}{1-q}
\log_2
\frac{
(U_qA_q+V_qB_q+W_q)(U_q+V_q+W_q)
}{
(U_qA_q+V_q+W_q)(U_q+V_qB_q+W_q)
}.
\]

Its logarithmic numerator-minus-denominator factors exactly as

\[
\boxed{-U_qV_q(A_q-1)(B_q-1).}
\]

Therefore

\[
\boxed{
D_q<0\ (0\le q<1),\qquad D_1=0,\qquad D_q>0\ (1<q<\infty).
}
\]

Thus, under disjoint semantic access, Shannon order is the unique finite Rényi order with zero undeclared joint-prerequisite interaction. This **Shannon uniqueness** statement is exact for arbitrary positive occupancies, access-set cardinalities, residual cells, and positive decoder depths.

## SII.4. Theorem S10: overlapping-access balance law

The disjoint condition in Theorem S9 is substantive. If the two semantic access sets overlap, partition the semantic cells into four regions:

- left-only \(X=L\setminus R\),
- right-only \(Y=R\setminus L\),
- overlap \(Z=L\cap R\),
- residual \(W=(L\cup R)^c\).

For finite \(q\ne1\), write their \(q\)-power masses as

\[
X_q=\sum_{i\in X}p_i^q,\quad
Y_q=\sum_{i\in Y}p_i^q,\quad
Z_q=\sum_{i\in Z}p_i^q,\quad
W_q=\sum_{i\in W}p_i^q,
\]

and again \(A_q=2^{(1-q)a}\), \(B_q=2^{(1-q)b}\). Then

\[
\boxed{
D_q=
\frac{1}{1-q}\log_2
\frac{
(X_qA_q+Y_qB_q+Z_qA_qB_q+W_q)(X_q+Y_q+Z_q+W_q)
}{
(A_q(X_q+Z_q)+Y_q+W_q)(B_q(Y_q+Z_q)+X_q+W_q)
}.
}
\]

The decisive algebraic identity is

\[
\boxed{
\text{numerator}-\text{denominator}
=(A_q-1)(B_q-1)(W_qZ_q-X_qY_q).
}
\]

Define the **overlap balance**

\[
\mathcal B_q=W_qZ_q-X_qY_q.
\]

Because \((A_q-1)(B_q-1)>0\) for every finite \(q\ne1\), the leakage sign is

\[
\boxed{
\operatorname{sgn}(D_q)=
\begin{cases}
\operatorname{sgn}(\mathcal B_q), & 0\le q<1,\\
0, & q=1,\\
-\operatorname{sgn}(\mathcal B_q), & q>1.
\end{cases}
}
\]

Hence Shannon order always has zero leakage, but it is **not globally the unique zero once access sets overlap**. At any finite \(q\ne1\), a second zero occurs exactly on the balance surface

\[
\boxed{W_qZ_q=X_qY_q.}
\]

This is not a numerical accident. For example, four equally occupied cells with one cell in each region satisfy the balance equality for every finite \(q\), so all Rényi orders have zero undeclared joint-prerequisite dividend in that configuration.

Theorem S9 is recovered by setting \(Z_q=0\), for which \(\mathcal B_q=-X_qY_q<0\). Complete-overlap configurations instead have \(X_q=Y_q=0\), so \(\mathcal B_q=W_qZ_q\ge0\). Thus disjoint and strongly overlapping access occupy opposite sides of an exact interaction-sign boundary.

### Interpretation

Theorem S10 sharpens the structural/distributional distinction. At Shannon order, prerequisite support is faithful for arbitrary query families by Theorem S8. At non-Shannon orders, undeclared higher-order interaction is controlled not merely by whether access sets overlap, but by a four-region balance of \(q\)-weighted semantic mass. Non-Shannon zero interaction therefore does **not** imply prerequisite faithfulness: it can arise from exact cancellation on the overlap-balance surface.

## SII.5. Relation to Supplementary Information I

Supplementary Information I asks how much information selective refinement carries under different Rényi orders. Supplement II asks when an interaction coefficient can be read literally as prerequisite structure. Theorem S8 gives exact Shannon support fidelity. Theorem S9 gives strict non-Shannon leakage for disjoint channels. Theorem S10 shows the precise boundary of that strict law when semantic access overlaps.

Accordingly, prerequisite topology should be diagnosed with the Shannon prospective game. Non-Shannon spectra remain useful distribution-sensitive summaries, but their higher-order coefficients can reflect both genuine prerequisite structure and access-overlap balance.

## SII.6. Novelty boundary

The following are standard and are not claimed as new: Möbius/Harsanyi inversion, unanimity games, Shannon entropy and additivity, Rényi entropy, chain-rule characterizations of Shannon entropy, and Boolean-lattice coalition accounting. The CREST-specific results are:

1. the exact Shannon factorization linking prerequisite hyperedges to Möbius support and semantic-access occupancy to coefficient weights;
2. the exact disjoint-access leakage law and its Shannon-uniqueness corollary; and
3. the exact overlapping-access factorization showing that non-Shannon leakage is governed by \(W_qZ_q-X_qY_q\), including the balance surface on which non-Shannon leakage vanishes.

These are finite-state statements. They do not establish continuous-time limits, stochastic-process generality, or empirical occupancy distributions for any particular ecosystem.

## SII.7. Reproducibility

The Shannon factorization is implemented in `crest/prerequisite_access_game.py`. The disjoint law is implemented in `crest/prerequisite_renyi_leakage.py`. The overlapping-access balance law is implemented in `crest/prerequisite_overlap_balance.py`.

Tests compare all closed forms with direct cellwise refinement and full Möbius inversion; verify multi-cell disjoint and overlapping access sets, residual cells, strict sign laws, the exact non-Shannon balance-zero construction, the two-cell and symmetric corollaries, and the canonical 2.5-bit pure three-way Shannon dividend.
