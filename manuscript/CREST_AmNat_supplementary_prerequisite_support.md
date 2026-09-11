# Supplementary Information II: Prerequisite support and Rényi-order leakage

This supplement isolates the CREST-specific link between declared prerequisite order and semantic-access coverage. Möbius/Harsanyi inversion, unanimity games, Shannon additivity, and Rényi entropy are standard and are not claimed here as new mathematics. The contribution is the exact factorization of CREST's prospective information game at Shannon order and the sharp boundary showing why the same support interpretation fails outside Shannon order.

## SII.1. Setup

Let `U` be the retained pre-future interfaces and `F` the prospective responsibility. Each future query `f` declares:

- a minimal prerequisite set \(R_f\subseteq U\);
- an addressable semantic-cell set \(A_f\);
- a decoder depth \(m_f\ge0\) bits.

Let semantic-cell occupancies be \(p_i\), with \(\sum_i p_i=1\), and define

\[
P(A_f)=\sum_{i\in A_f}p_i.
\]

Assume simultaneously licensed future refinements compose by multiplying local descendant multiplicities, equivalently by adding local decoder depths.

## SII.2. Theorem S8: prerequisite-support factorization at Shannon order

For coalition \(S\subseteq U\cup\{F\}\), the prospective Shannon information gain is

\[
\boxed{
v_1(S)=\sum_f m_fP(A_f)\,\mathbf 1\{R_f\cup\{F\}\subseteq S\}.
}
\]

Thus \(v_1\) is exactly a weighted sum of unanimity games. Its Boolean-lattice Möbius transform is

\[
\boxed{
d_1(T)=\sum_{f:R_f\cup\{F\}=T}m_fP(A_f),
}
\]

and \(d_1(T)=0\) for every coalition \(T\) that is not the minimal prerequisite support of at least one query.

### Consequences

1. **Prerequisite order determines where information appears.** The support of the prospective Shannon dividend is fixed by the declared hyperedges \(R_f\cup\{F\}\).
2. **Semantic coverage determines how much appears there.** Changing \(A_f\) or the occupancy distribution changes \(P(A_f)\), hence the coefficient weight, but cannot move that query's Shannon dividend to another coalition.
3. **Irrelevant interfaces cannot acquire spurious prospective interaction.** An interface absent from every \(R_f\) never appears in a nonzero prospective Shannon dividend.
4. **Queries with identical prerequisites aggregate.** Their weights add on the same coefficient.
5. **Overlapping access sets do not create extra Shannon interaction** under multiplicative local refinement, because local decoder depths add before taking the occupancy expectation.

For the canonical CREST witness, one future query requires \(\{H,\Theta\}\), one of four uniformly occupied semantic cells is addressable, and \(m=10\). Therefore

\[
\boxed{
d_1(\{H,\Theta,F\})=10\times\frac14=2.5\text{ bits},
}
\]

with every other prospective Shannon dividend equal to zero. This is deliberately distinct from the main-text Hartley/support-count dividend \(\log_2(1027/4)\approx8.004220466\) bits.

### Proof

Query \(f\) is licensed by coalition \(S\) iff \(F\in S\) and \(R_f\subseteq S\). On every addressable semantic cell it contributes \(m_f\) Shannon bits and elsewhere zero. Its expected information gain is therefore \(m_fP(A_f)\) when licensed and zero otherwise. Summing over queries gives the displayed weighted-unanimity representation. The Möbius transform of a unanimity game supported on \(T_f=R_f\cup\{F\}\) is one at \(T_f\) and zero elsewhere. Linearity of Möbius inversion gives the coefficient formula.

## SII.3. Theorem S9: Shannon uniqueness and non-Shannon prerequisite leakage

The support factorization is Shannon-specific. Consider two equiprobable semantic cells. One one-bit query requires only \(H\) and refines cell 0; a second one-bit query requires only \(\Theta\) and refines cell 1. No query declares the joint prerequisite \(\{H,\Theta\}\).

With one query licensed, the refined distribution is \((1/4,1/4,1/2)\). With both licensed, the refined distribution is four atoms of probability \(1/4\). For finite Rényi order \(q\ne1\), the single-query gain is

\[
g_q=\frac{1}{1-q}\log_2\left(\frac12+2^{-q}\right).
\]

The induced \(H\times\Theta\times F\) Möbius dividend is therefore

\[
\boxed{
D_q=1-\frac{2}{1-q}\log_2\left(\frac12+2^{-q}\right),\qquad q\ne1.
}
\]

At Shannon order, each single query contributes \(1/2\) bit and the joint gain is one bit, so

\[
\boxed{D_1=0.}
\]

Moreover, \(q=1\) is the unique zero of this leakage term. Setting \(D_q=0\) is equivalent to

\[
\frac12+2^{-q}=2^{(1-q)/2}.
\]

Writing \(t=2^{-q/2}\) gives

\[
t^2-\sqrt2\,t+\frac12=\left(t-\frac1{\sqrt2}\right)^2=0,
\]

hence \(q=1\). The sign changes at Shannon order:

\[
\boxed{
D_q<0\quad(0\le q<1),\qquad D_1=0,\qquad D_q>0\quad(q>1),
}
\]

with \(D_\infty=1\) bit.

Thus Shannon order is uniquely **prerequisite-support faithful** in this minimal witness. Only at \(q=1\) does the prospective Möbius support coincide exactly with the declared prerequisite hypergraph. Non-Shannon Rényi orders can generate a higher-order dividend even when no query declares the corresponding higher-order prerequisite.

This separates two notions:

- **structural interaction**: interaction implied by declared prerequisite sets and recovered exactly by Shannon prospective dividends;
- **distributional interaction**: additional interaction induced by nonlinear weighting of selectively refined semantic cells at non-Shannon Rényi orders.

## SII.4. Relation to Supplementary Information I

Supplementary Information I studies the Rényi spectrum, sparse-access asymptotics, placement extrema, heterogeneous decoder capacity, and optimal continuous/integer decoder allocation. Those results ask how much information a selective refinement carries under different Rényi orders. The present supplement asks a different question: when can a Rényi-order interaction coefficient be interpreted literally as the declared prerequisite structure?

The answer is sharp in the minimal witness above. Shannon order preserves the prerequisite support exactly; non-Shannon orders can mix structural and distributional interaction. Accordingly, prerequisite topology should be diagnosed with the Shannon prospective game, while non-Shannon spectra should be interpreted as distribution-sensitive summaries rather than literal prerequisite graphs.

## SII.5. Novelty boundary

The following are standard and are not claimed as new: Möbius/Harsanyi inversion, unanimity games, Shannon entropy and additivity, Rényi entropy, and Boolean-lattice coalition accounting. The CREST-specific results are:

1. the exact Shannon factorization linking prerequisite hyperedges to Möbius support and semantic-access occupancy to coefficient weights; and
2. the explicit Shannon-uniqueness boundary showing, in a minimal selectively refined witness, that \(q=1\) is the unique Rényi order with zero undeclared joint-prerequisite leakage.

These are finite-state statements. They do not establish continuous-time limits, stochastic-process generality, or empirical occupancy distributions for any particular ecosystem.

## SII.6. Reproducibility

The factorization is implemented in `crest/prerequisite_access_game.py` and tested in `tests/test_prerequisite_access_game.py`. The non-Shannon leakage boundary is implemented in `crest/prerequisite_renyi_leakage.py` and tested in `tests/test_prerequisite_renyi_leakage.py`.

Tests compare the closed-form Shannon query sum with direct cellwise combined refinement for every coalition, verify exact Möbius support and irrelevant-interface no-leakage, recover the canonical 2.5-bit pure three-way Shannon dividend, match the non-Shannon leakage formula to direct Möbius inversion across multiple Rényi orders, and verify its sign change and unique zero at \(q=1\).
