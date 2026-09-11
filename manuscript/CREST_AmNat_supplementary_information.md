# Supplementary Information: Information spectra of sparse semantic access

This supplement extends the main-text sparse semantic-access result from support size to nonuniform occupancy and heterogeneous decoder capacity. Rényi entropy, Shannon entropy, Hill numbers, and monotonicity under ordinary partition refinement are standard information-theoretic constructions and are **not** claimed here as new mathematics. The contribution is narrower: the CREST semantic-access operator refines only a declared subset of retrospective-by-transverse semantic cells, and the results below give its exact finite information spectrum, asymptotic regimes, and sharp fixed-budget placement bounds.

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

For \(q\ge0\), let \(H_q(P)\) denote Rényi entropy in bits, with the usual continuous extension to Shannon entropy at \(q=1\) and the Hartley support entropy at \(q=0\). Define the access information gain

\[
G_q(m;A,P)=H_q(P^{\mathrm{ref}})-H_q(P).
\]

The main text uses support size only. The present supplement asks what changes when semantic pairs are not equiprobable.

## S2. Theorem S1: exact Rényi access spectrum

For \(q\neq1\), define

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

Therefore the exact gain is

\[
\boxed{
G_q(m;A,P)
=
\frac{1}{1-q}
\log_2
\frac{
\displaystyle
\sum_{i\notin A}p_i^q
+2^{m(1-q)}\sum_{i\in A}p_i^q
}{
\displaystyle
\sum_{i=1}^{N}p_i^q
}
}
\qquad(q\neq1).
\]

This formula is finite and exact. It does not require an asymptotic approximation.

### Corollary S1.1: recovery of the main-text Hartley result

At \(q=0\), every positive-probability semantic cell contributes one unit to the support count. If \(|A|=k\), then

\[
\boxed{
G_0(m)
=
\log_2\frac{(N-k)+k2^m}{N}.
}
\]

This is exactly the three-way state dividend reported in the main text. Hence the main-text count theorem is the \(q=0\) endpoint of the access spectrum, not a separate construction.

For the canonical witness \(N=4,k=1,m=10\),

\[
G_0
=
\log_2(1027/4)
\approx8.004220466\ \text{bits}.
\]

### Corollary S1.2: Shannon occupancy theorem

Taking \(q\to1\), splitting parent \(i\) into \(2^m\) equal descendants adds exactly \(m\) conditional bits whenever that parent is occupied. Therefore

\[
\boxed{
G_1(m;A,P)
=
m\sum_{i\in A}p_i
=
mP_A,
}
\]

where

\[
P_A=\Pr(i\in A)
\]

is the accessible occupancy mass.

Thus two systems can have the same combinatorial coverage \(k/N\) but different realized information gains whenever the occupied mass of their accessible cells differs.

## S3. Theorem S2: three asymptotic regimes

Assume both \(A\) and \(A^c\) are nonempty. Then semantic sparsity produces three qualitatively different large-\(m\) regimes.

### S2a. Orders \(0\le q<1\)

For \(q<1\), \(2^{m(1-q)}\to\infty\), so the accessible contribution dominates. Hence

\[
G_q(m)
=
m-C_q(A,P)+o(1),
\]

with

\[
\boxed{
C_q(A,P)
=
\frac{1}{1-q}
\log_2\frac{S_q}{S_q(A)}.
}
\]

Therefore

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}{m}=1,
\qquad 0\le q<1.
}
\]

At \(q=0\),

\[
C_0=\log_2(N/k),
\]

recovering the main-text sparse-access penalty.

### S2b. Shannon order \(q=1\)

The exact result already gives

\[
\boxed{
\lim_{m\to\infty}\frac{G_1(m)}m=P_A.
}
\]

The asymptotic slope is therefore the probability mass on which future access is actually available.

### S2c. Orders \(q>1\)

For \(q>1\), \(2^{m(1-q)}\to0\). Accessible descendants become individually small in the high-order power sum, while inaccessible high-probability parents remain unsplit. The gain converges to the finite limit

\[
\boxed{
G_q(\infty)
=
\frac{1}{q-1}
\log_2
\frac{S_q}{S_q(A^c)}.
}
\]

Consequently

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}m=0,
\qquad q>1.
}
\]

Combining the three cases,

\[
\boxed{
\lim_{m\to\infty}\frac{G_q(m)}m
=
\begin{cases}
1, & 0\le q<1,\\[4pt]
P_A, & q=1,\\[4pt]
0, & q>1.
\end{cases}
}
\]

This phase change is the principal generalization beyond the support-count theorem. The same semantic-access relation can appear nearly fully informative to rare-state-sensitive orders \(q<1\), occupancy-weighted at \(q=1\), and capacity-saturated to dominant-state-sensitive orders \(q>1\).

## S4. Theorem S3: sharp fixed-budget placement law

Suppose the number of accessible semantic cells is fixed at \(|A|=k\), but their locations may vary. Order the occupancy probabilities as

\[
p_{(1)}\ge p_{(2)}\ge\cdots\ge p_{(N)}.
\]

For every \(q>0\) and fixed \(m>0\), the gain \(G_q(m;A,P)\) is strictly increasing in

\[
S_q(A)=\sum_{i\in A}p_i^q
\]

(and at \(q=1\), in \(P_A\)). Hence the maximum is achieved by assigning access to the \(k\) most occupied cells, while the minimum is achieved by assigning access to the \(k\) least occupied cells.

Writing \(A_{\max}\) for the top-\(k\) cells and \(A_{\min}\) for the bottom-\(k\) cells,

\[
\boxed{
G_q(m;A_{\min},P)
\le
G_q(m;A,P)
\le
G_q(m;A_{\max},P),
\qquad q>0.
}
\]

Both bounds are sharp because the extremizing sets themselves are admissible.

At \(q=1\), this reduces to

\[
\boxed{
m\sum_{j=N-k+1}^{N}p_{(j)}
\le
G_1
\le
m\sum_{j=1}^{k}p_{(j)}.
}
\]

At \(q=0\), placement is irrelevant: only \(k\) matters, so the two bounds coincide.

This separates three quantities that the support-count result cannot distinguish:

\[
\boxed{
\text{coverage size}
\neq
\text{coverage occupancy}
\neq
\text{coverage placement}.
}
\]

## S5. Theorem S4: heterogeneous local decoder capacity

The common-depth assumption can be removed. Let semantic cell \(i\) be refined into \(M_i\ge1\) equiprobable descendants, with \(M_i=1\) representing no prospective refinement. Then

\[
\boxed{
G_q
=
\frac{1}{1-q}
\log_2
\frac{
\displaystyle\sum_i p_i^qM_i^{1-q}
}{
\displaystyle\sum_i p_i^q
},
\qquad q\neq1.
}
\]

The Shannon limit is

\[
\boxed{
G_1
=
\sum_i p_i\log_2 M_i.
}
\]

Thus realized future information decomposes into occupancy-weighted local decoder capacities. The common-depth sparse-access model is recovered by setting

\[
M_i=
\begin{cases}
2^m,&i\in A,\\
1,&i\notin A.
\end{cases}
\]

## S6. Finite bounds

For the common-depth operator,

\[
\boxed{0\le G_q(m;A,P)\le m}
\]

for every finite \(q\ge0\). The lower bound is attained when no cell is accessible or \(m=0\); the upper bound is attained under complete access. Sparse access therefore cannot create more information than the decoder depth it exposes.

## S7. Ecological interpretation

The order \(q\) specifies which parts of the ecological state distribution receive weight. This is the same reason Rényi/Hill families are useful in ecological diversity measurement, but the object measured here is different: not species diversity, but the information gain produced by selectively accessible future refinement of semantic state cells.

- \(q=0\) treats every possible semantic cell equally and corresponds to **potential state diversity**. This is the quantity used by the main-text quotient count.
- \(q=1\) weights cells by occupancy and corresponds to **realized or experienced state information** along the declared ensemble.
- \(q>1\) increasingly emphasizes common semantic states and therefore measures access value for **dominant-state prediction**.

The three-regime theorem shows that one statement such as "one quarter of semantic cells are accessible" is insufficient once occupancy is nonuniform. A rare but structurally distinct set of accessible cells may preserve Hartley support while contributing little Shannon information; conversely, access targeted to highly occupied cells can produce substantially greater realized gain at the same \(k\).

## S8. Novelty boundary

The following are standard and are not claimed as new: Rényi entropy, Shannon entropy, Hartley entropy, Hill-number interpretation, and the fact that ordinary refinement increases information. The results claimed here concern the specific selective semantic-access refinement induced by CREST:

1. the exact finite \(G_q\) spectrum for selectively refined semantic cells;
2. recovery of the main-text \(\log_2(N/k)\) theorem as the \(q=0\) endpoint;
3. the \(q<1/q=1/q>1\) three-regime asymptotic law;
4. sharp fixed-\(k\) placement extrema under nonuniform occupancy; and
5. the heterogeneous local decoder-capacity extension.

These results remain finite-state statements. They do not establish stochastic-process convergence, continuous-time limits, or empirical occupancy distributions for any particular ecosystem.

## S9. Reproducibility

The formulas are implemented in `crest/renyi_access.py` and tested in `tests/test_renyi_access.py`. Tests include direct expansion of the refined distribution, exact recovery of the main-text \(N=4,k=1,m=10\) benchmark, numerical convergence to both asymptotic regimes, and brute-force enumeration of every fixed-\(k\) access set in a nonuniform example to verify the extremal theorem.

## Supplementary references

Jost, L. 2006. Entropy and diversity. *Oikos* 113:363–375.

Rényi, A. 1961. On measures of entropy and information. Pages 547–561 in *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics and Probability*, Volume 1. University of California Press, Berkeley.
