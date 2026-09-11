# Supplementary Information: Information spectra of sparse semantic access

This supplement extends the main-text sparse semantic-access result from support size to nonuniform occupancy, heterogeneous decoder capacity, and constrained decoder allocation. Rényi entropy, Shannon entropy, Hill numbers, monotonicity under ordinary partition refinement, convex optimization, KKT conditions, and water-filling methods are standard and are **not** claimed here as new mathematics. The contribution is narrower: the CREST semantic-access operator refines only declared retrospective-by-transverse semantic cells, and the results below give its exact finite information spectrum, asymptotic regimes, sharp placement bounds, and optimal allocation structure under a fixed decoder budget.

## S1. Setup

Let the pre-future semantic state have \(N\) cells indexed by \(i=1,\ldots,N\), with positive occupancy probabilities

\[
p_i>0,\qquad \sum_{i=1}^{N}p_i=1.
\]

Let \(A\subseteq\{1,\ldots,N\}\) denote the semantic cells on which a prospective decoder is licensed. In the common-depth case, every \(i\in A\) is refined into \(2^m\) equiprobable descendants, while every \(i\notin A\) remains one inaccessible trace class. Thus

\[
i\notin A:\quad p_i,
\]

whereas

\[
i\in A:\quad
\underbrace{p_i/2^m,\ldots,p_i/2^m}_{2^m\text{ descendants}}.
\]

For \(q\ge0\), let \(H_q(P)\) denote Rényi entropy in bits, with the usual continuous extension to Shannon entropy at \(q=1\), Hartley support entropy at \(q=0\), and min-entropy at \(q=\infty\). Define the access information gain

\[
G_q=H_q(P^{\mathrm{ref}})-H_q(P).
\]

The main text uses support size only. The present supplement asks what changes when semantic pairs are not equiprobable and when decoder capacity itself is a design variable.

## S2. Theorem S1: exact Rényi access spectrum

For finite \(q\neq1\), define

\[
S_q=\sum_{i=1}^{N}p_i^q,
\qquad
S_q(A)=\sum_{i\in A}p_i^q.
\]

Because an accessible parent cell contributes

\[
2^m\left(\frac{p_i}{2^m}\right)^q
=p_i^q2^{m(1-q)},
\]

the refined \(q\)-power sum is

\[
S_q^{\mathrm{ref}}
=
\sum_{i\notin A}p_i^q
+2^{m(1-q)}\sum_{i\in A}p_i^q.
\]

Therefore

\[
\boxed{
G_q(m;A,P)
=
\frac{1}{1-q}
\log_2
\frac{
\sum_{i\notin A}p_i^q
+2^{m(1-q)}\sum_{i\in A}p_i^q
}{
\sum_{i=1}^{N}p_i^q
}
}
\qquad(q\neq1).
\]

This formula is finite and exact.

### Corollary S1.1: recovery of the main-text Hartley result

At \(q=0\), if \(|A|=k\),

\[
\boxed{
G_0(m)
=
\log_2\frac{(N-k)+k2^m}{N}.
}
\]

This is exactly the three-way state dividend reported in the main text. For the canonical witness \(N=4,k=1,m=10\),

\[
G_0=\log_2(1027/4)\approx8.004220466\ \text{bits}.
\]

### Corollary S1.2: Shannon occupancy theorem

Taking \(q\to1\),

\[
\boxed{
G_1(m;A,P)=m\sum_{i\in A}p_i=mP_A,
}
\]

where \(P_A=\Pr(i\in A)\). Thus equal combinatorial coverage \(k/N\) need not imply equal realized information gain.

## S3. Theorem S2: three asymptotic regimes

Assume both \(A\) and \(A^c\) are nonempty.

For \(0\le q<1\),

\[
G_q(m)=m-C_q(A,P)+o(1),
\]

with

\[
\boxed{
C_q(A,P)=\frac{1}{1-q}\log_2\frac{S_q}{S_q(A)}.
}
\]

Hence

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}m=1,
\qquad 0\le q<1.
}
\]

At \(q=0\), \(C_0=\log_2(N/k)\), recovering the main-text sparse-access penalty.

At Shannon order,

\[
\boxed{
\lim_{m\to\infty}\frac{G_1(m)}m=P_A.
}
\]

For finite \(q>1\),

\[
\boxed{
G_q(\infty)
=
\frac{1}{q-1}
\log_2\frac{S_q}{S_q(A^c)},
}
\]

so

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}m=0.
}
\]

Combining the cases,

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}m
=
\begin{cases}
1,&0\le q<1,\\[4pt]
P_A,&q=1,\\[4pt]
0,&q>1.
\end{cases}
}
\]

The same access relation therefore appears nearly fully informative to rare-state-sensitive orders, occupancy-weighted at Shannon order, and capacity-saturated to dominant-state-sensitive orders.

## S4. Theorem S3: sharp fixed-cardinality placement law

Suppose \(|A|=k\) is fixed but its locations may vary, and order

\[
p_{(1)}\ge p_{(2)}\ge\cdots\ge p_{(N)}.
\]

For every finite \(q>0\) and fixed \(m>0\), \(G_q\) is strictly increasing in \(S_q(A)\) (and at \(q=1\), in \(P_A\)). Hence access to the \(k\) most occupied cells maximizes gain, whereas access to the \(k\) least occupied cells minimizes it. Thus

\[
\boxed{
G_q(A_{\min})\le G_q(A)\le G_q(A_{\max}).
}
\]

At \(q=1\),

\[
\boxed{
m\sum_{j=N-k+1}^{N}p_{(j)}
\le G_1\le
m\sum_{j=1}^{k}p_{(j)}.
}
\]

At \(q=0\), placement is irrelevant: only \(k\) matters. This separates coverage size, coverage occupancy, and coverage placement.

## S5. Theorem S4: heterogeneous local decoder capacity

Let semantic cell \(i\) be refined into \(M_i\ge1\) equiprobable descendants. Then for finite \(q\neq1\),

\[
\boxed{
G_q
=
\frac{1}{1-q}
\log_2
\frac{\sum_i p_i^qM_i^{1-q}}
{\sum_i p_i^q}.
}
\]

The Shannon limit is

\[
\boxed{
G_1=\sum_i p_i\log_2M_i.
}
\]

Thus realized future information decomposes into occupancy-weighted local decoder capacities. The common-depth sparse model is recovered by setting \(M_i=2^m\) on \(A\) and \(M_i=1\) elsewhere.

## S6. Theorem S5: min-entropy endpoint

At \(q=\infty\), Rényi entropy is min-entropy,

\[
H_\infty(P)=-\log_2\max_i p_i.
\]

Under common-depth selective refinement,

\[
\boxed{
G_\infty(m;A,P)
=
\log_2
\frac{\max_i p_i}
{\max\left\{
\max_{i\notin A}p_i,
2^{-m}\max_{i\in A}p_i
\right\}}.
}
\]

Thus dominant-state information improves only if refinement reaches a currently dominant atom strongly enough to push its descendant probability below the largest remaining unsplit atom. For sparse access and \(m\to\infty\),

\[
\boxed{
G_\infty(\infty)
=
\log_2
\frac{\max_i p_i}{\max_{i\notin A}p_i},
}
\]

provided at least one inaccessible cell remains. This is the exact endpoint of the \(q>1\) saturation regime.

## S7. Theorem S6: optimal allocation under a total decoder budget

The heterogeneous formula allows decoder depth itself to be optimized. Introduce a continuous relaxation in which cell \(i\) receives \(x_i\ge0\) decoder bits, corresponding formally to local multiplicity \(M_i=2^{x_i}\), under

\[
\sum_i x_i=B.
\]

For \(0\le q<1\), maximizing \(G_q\) is equivalent to maximizing

\[
\sum_i p_i^q2^{(1-q)x_i},
\]

a convex function over the budget simplex. Therefore a maximum occurs at a vertex. For \(0<q<1\), the optimal vertex assigns all budget to a most-occupied cell; at \(q=0\), all vertices are equivalent.

At \(q=1\),

\[
G_1=\sum_i p_ix_i,
\]

so the same concentration rule holds: all budget is assigned to a most-occupied cell.

For finite \(q>1\), maximizing \(G_q\) is equivalent to minimizing the strictly convex function

\[
F_q(x)=\sum_i p_i^q2^{-(q-1)x_i}.
\]

The KKT conditions therefore give a unique optimum of water-filling form

\[
\boxed{
x_i^*
=
\left[
\frac{q}{q-1}\log_2p_i-\tau
\right]_+,
}
\]

where \([z]_+=\max(z,0)\) and \(\tau\) is the unique threshold satisfying

\[
\sum_i x_i^*=B.
\]

At min-entropy order, the limiting allocation is

\[
\boxed{
x_i^*
=
[\log_2p_i-\tau]_+.
}
\]

Hence the optimal design changes qualitatively at \(q=1\): support- and occupancy-sensitive objectives concentrate a finite decoder budget on a most-occupied semantic state, whereas dominant-state-sensitive objectives \(q>1\) progressively spread budget across high-occupancy states to equalize their weighted residual dominance. Water-filling itself is standard optimization machinery; the result here is its appearance as the exact optimum of the CREST selective semantic-access objective.

## S8. Finite bounds

For common depth,

\[
\boxed{0\le G_q(m;A,P)\le m}
\]

for every \(q\in[0,\infty]\). Sparse access cannot create more information than the decoder depth it exposes.

## S9. Ecological interpretation

The order \(q\) specifies which parts of the ecological state distribution receive weight. This parallels Rényi/Hill diversity analysis, but the object here is not species diversity: it is the information gain produced by selectively accessible future refinement of semantic state cells.

- \(q=0\): potential state diversity; all possible semantic cells count equally.
- \(q=1\): realized or experienced state information; cells are weighted by occupancy.
- \(q>1\): dominant-state prediction; common semantic states receive increasing weight.
- \(q=\infty\): worst-dominant-atom control; only the largest remaining semantic probability matters.

The budget theorem adds an operational distinction. If the scientific objective values support or average occupancy, a constrained intervention/measurement budget is best concentrated on the most occupied semantic state. If the objective emphasizes dominant-state predictability, the optimum becomes water-filling: once the leading state has been sufficiently refined, capacity should spill to the next most dominant state rather than continue deepening one state indefinitely.

## S10. Novelty boundary

The following are standard and are not claimed as new: Rényi, Shannon, Hartley, and min-entropy; Hill-number interpretation; ordinary partition-refinement monotonicity; convex optimization; KKT conditions; and generic water-filling arguments. The results claimed here concern the CREST selective semantic-access operator:

1. the exact finite \(G_q\) spectrum for selectively refined semantic cells;
2. recovery of the main-text \(\log_2(N/k)\) theorem as the \(q=0\) endpoint;
3. the \(q<1/q=1/q>1\) asymptotic regime split;
4. sharp fixed-cardinality placement extrema under nonuniform occupancy;
5. heterogeneous local decoder capacity;
6. the exact min-entropy endpoint; and
7. the decoder-budget design transition from concentration at \(q\le1\) to water-filling at \(q>1\).

These remain finite-state or finite-dimensional relaxed-design statements. They do not establish stochastic-process convergence, continuous-time limits, or empirical occupancy distributions for any particular ecosystem.

## S11. Reproducibility

The formulas are implemented in `crest/renyi_access.py` and tested in `tests/test_renyi_access.py`. Tests include direct expansion of refined distributions, exact recovery of the main-text \(N=4,k=1,m=10\) benchmark, numerical asymptotic convergence, brute-force fixed-cardinality placement checks, the min-entropy endpoint, grid verification of the budget optimum, and KKT residual equalization for the water-filling solution.

## Supplementary references

Boyd, S., and L. Vandenberghe. 2004. *Convex Optimization*. Cambridge University Press, Cambridge.

Jost, L. 2006. Entropy and diversity. *Oikos* 113:363–375.

Rényi, A. 1961. On measures of entropy and information. Pages 547–561 in *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, Volume 1. University of California Press, Berkeley.
