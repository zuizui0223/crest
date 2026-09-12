# Supplementary Information II: Prerequisite support and Rényi-order leakage

This supplement isolates the CREST-specific link between declared prerequisite order and semantic-access coverage. Möbius/Harsanyi inversion, unanimity games, Shannon additivity, and Rényi entropy are standard and are not claimed here as new mathematics. The contribution is the exact factorization of CREST's prospective information game at Shannon order and the sharp boundary showing why the same support interpretation fails outside Shannon order.

## SII.1. Setup

Let `U` be the retained pre-future interfaces and `F` the prospective responsibility. Each future query `f` declares a minimal prerequisite set \(R_f\subseteq U\), an addressable semantic-cell set \(A_f\), and a decoder depth \(m_f\ge0\) bits. Let semantic-cell occupancies be \(p_i\), with \(\sum_i p_i=1\), and define \(P(A_f)=\sum_{i\in A_f}p_i\). Simultaneously licensed refinements compose by multiplying local descendant multiplicities, equivalently by adding local decoder depths.

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

## SII.3. Theorem S9: general two-cell Shannon-uniqueness law

The support factorization is not merely broken by one symmetric example outside Shannon order. Consider **any** two semantic cells with probabilities

\[
p\in(0,1),\qquad 1-p,
\]

and two positive decoder depths \(a,b>0\). One query requires only \(H\) and refines the first cell by \(a\) bits; a second query requires only \(\Theta\) and refines the second cell by \(b\) bits. No query declares the joint prerequisite \(\{H,\Theta\}\).

For finite \(q\ne1\), put

\[
u=p^q,\quad v=(1-p)^q,\quad
A=2^{(1-q)a},\quad B=2^{(1-q)b}.
\]

The undeclared \(H\times\Theta\times F\) Möbius dividend is exactly

\[
\boxed{
D_q(p,a,b)=
\frac{1}{1-q}
\log_2
\frac{(u+v)(uA+vB)}{(uA+v)(u+vB)}.
}
\]

The sign is determined without approximation because

\[
(u+v)(uA+vB)-(uA+v)(u+vB)
=-uv(A-1)(B-1).
\]

Since \(u,v>0\) and \(a,b>0\), for \(q<1\) we have \(A,B>1\), so the logarithmic ratio is below one and \(1/(1-q)>0\). For \(q>1\), \(A,B<1\), the ratio remains below one but \(1/(1-q)<0\). Therefore

\[
\boxed{
D_q(p,a,b)<0\quad(0\le q<1),\qquad
D_1(p,a,b)=0,\qquad
D_q(p,a,b)>0\quad(1<q<\infty).
}
\]

Thus for **every interior two-cell occupancy and every pair of positive decoder depths**, Shannon order is the unique finite Rényi order at which the undeclared joint-prerequisite interaction vanishes. This is stronger than a single symmetric witness: the zero is invariant to occupancy imbalance and decoder-depth asymmetry.

At \(q=1\), the result follows directly from Shannon additivity:

\[
G_1(a,b)=pa+(1-p)b=G_1(a,0)+G_1(0,b),
\]

so the cross-difference is exactly zero.

### Symmetric corollary

Setting \(p=1/2\) and \(a=b=1\) recovers

\[
D_q=1-\frac{2}{1-q}\log_2\left(\frac12+2^{-q}\right),
\]

with \(D_\infty=1\) bit. This is the canonical executable witness retained in the review bundle.

The theorem separates:

- **structural interaction**: interaction implied by declared prerequisite sets and recovered exactly by Shannon prospective dividends;
- **distributional interaction**: additional interaction induced by nonlinear weighting of selectively refined semantic cells at non-Shannon Rényi orders.

## SII.4. Relation to Supplementary Information I

Supplementary Information I asks how much information selective refinement carries under different Rényi orders. Supplement II asks when an interaction coefficient can be read literally as prerequisite structure. The answer is now stronger than the original minimal witness: Shannon support fidelity holds generally by Theorem S8, while the simplest possible pair of disjoint prerequisite channels exhibits nonzero leakage at every finite \(q\ne1\), regardless of interior occupancy or positive decoder-depth asymmetry.

Accordingly, prerequisite topology should be diagnosed with the Shannon prospective game. Non-Shannon spectra remain useful distribution-sensitive summaries, but their higher-order coefficients cannot in general be interpreted as literal prerequisite hyperedges.

## SII.5. Novelty boundary

The following are standard and are not claimed as new: Möbius/Harsanyi inversion, unanimity games, Shannon entropy and additivity, Rényi entropy, and Boolean-lattice coalition accounting. The CREST-specific results are:

1. the exact Shannon factorization linking prerequisite hyperedges to Möbius support and semantic-access occupancy to coefficient weights; and
2. the exact two-cell leakage law showing that, for every interior occupancy and every positive pair of disjoint decoder depths, \(q=1\) is the unique finite Rényi order with zero undeclared joint-prerequisite interaction.

These are finite-state statements. They do not establish continuous-time limits, stochastic-process generality, or empirical occupancy distributions for any particular ecosystem.

## SII.6. Reproducibility

The factorization is implemented in `crest/prerequisite_access_game.py` and tested in `tests/test_prerequisite_access_game.py`. The generalized leakage law is implemented in `crest/prerequisite_renyi_leakage.py` and tested in `tests/test_prerequisite_renyi_leakage.py`.

Tests compare the closed form with direct cellwise refinement and full Möbius inversion across unequal occupancies, asymmetric positive decoder depths, and multiple Rényi orders; verify the strict sign law on both sides of \(q=1\); recover the symmetric canonical formula; and retain the canonical 2.5-bit pure three-way Shannon dividend.
