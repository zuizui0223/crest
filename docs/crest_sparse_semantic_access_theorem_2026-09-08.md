# Sparse semantic access at a temporal cut

**Status:** exact finite CREST result derived from the v0.7 semantic-access quotient.  This document does **not** claim novelty for Möbius inversion itself.  The substantive modeling object is the coverage of the semantic history-mode × response-type interface on which a future decoder is legal.

## 1. Setup

Let the retained MLTR history quotient contain `r` semantic modes and the retained MRM candidate-safe quotient contain `s` response types.  Write

\[
N=rs
\]

for the number of semantic interface pairs.  Let

\[
A\subseteq H_{\min}\times\Theta,
\qquad |A|=k,
\]

be the semantic access relation for a future decoder carrying an exterior signature

\[
a\in\{0,1\}^m.
\]

Assume every semantic pair occurs in the finite carrier.  H and Theta expose their derived semantic interfaces.  The exterior decoder is syntactically a joint H–Theta–F query, but it returns the m-bit exterior signature only on pairs in A.  On pairs outside A, all exterior signatures are merged into one inaccessible trace class.

This setup distinguishes **interface order** from **semantic coverage**.  Requiring both H and Theta fixes the interaction order; the density of A controls how much of the exterior information is actually addressable.

## 2. Exact grand-coalition quotient

Each inaccessible semantic pair contributes exactly one state class.  Each addressable semantic pair contributes one class for each exterior signature, hence `2^m` classes.  Therefore

\[
\boxed{
|Q_{H\Theta F}|=(N-k)+k2^m.
}
\]

The proper-coalition quotient sizes are

\[
|Q_H|=r,
\qquad
|Q_\Theta|=s,
\qquad
|Q_F|=1,
\]

\[
|Q_{H\Theta}|=N,
\qquad
|Q_{HF}|=r,
\qquad
|Q_{\Theta F}|=s,
\]

because the joint decoder requires both semantic interfaces.

## 3. Exact three-way dividend

Using base-2 state information

\[
v(S)=\log_2|Q_S|,
\]

the three-way Möbius/Harsanyi dividend is

\[
d_{H\Theta F}
=
v(H\Theta F)-v(H\Theta)-v(HF)-v(\Theta F)
+v(H)+v(\Theta)+v(F)-v(\varnothing).
\]

The proper-coalition terms cancel, leaving

\[
\boxed{
d_{H\Theta F}
=
\log_2\frac{(N-k)+k2^m}{N}.
}
\]

This is generally non-integer.  The v0.6 complete-addressability formula is the boundary case `k=N`, for which

\[
d_{H\Theta F}=m.
\]

If `k=0`, the future decoder is nowhere semantically addressable and the three-way dividend is zero.

## 4. Sparsity penalty

For fixed `N` and `k>0`, as `m -> infinity`,

\[
(N-k)+k2^m
=
k2^m\left(1+\frac{N-k}{k2^m}\right),
\]

so

\[
\boxed{
d_{H\Theta F}
=
m+\log_2(k/N)+o(1)
=
m-\log_2(N/k)+o(1).
}
\]

Hence the loss relative to complete addressability tends to

\[
\boxed{
\log_2(N/k)
}
\]

bits.  This is the **semantic sparsity penalty**.

The result should not be phrased as a continuous change in interaction *order*: while both H and Theta remain syntactic prerequisites, the exterior burden remains a three-way term.  What semantic sparsity changes continuously (through the logarithm of coverage) is its magnitude.

## 5. Canonical v0.7 witness

The current nontrivial companion model has

\[
r=s=2,
\qquad N=4,
\qquad k=1.
\]

Therefore

\[
|Q_{H\Theta F}|=3+2^m
\]

and

\[
\boxed{
d_{H\Theta F}=\log_2((3+2^m)/4).}
\]

Numerically:

| m | grand classes | grand bits | three-way dividend |
|---:|---:|---:|---:|
| 4 | 19 | 4.247927513 | 2.247927513 |
| 8 | 259 | 8.016808288 | 6.016808288 |
| 10 | 1027 | 10.004220466 | 8.004220466 |

The deficit from the v0.6 complete-access value tends to two bits because

\[
\log_2(N/k)=\log_2 4=2.
\]

## 6. Modeling interpretation

The prerequisite set and the access relation answer different questions.

- The prerequisite set asks **which retained interfaces must be present at all** for the future query to be well formed.
- The access relation asks **on which semantic combinations of those interfaces the query is actually licensed or meaningful**.

The earlier v0.6 theorem used the complete relation

\[
A=H_{\min}\times\Theta.
\]

That case is exact but special.  The sparse theorem shows that companion semantics can reduce addressability without changing the syntactic interaction order.

For ecological applications this prevents a misleading inference: identifying a target as requiring both history and latent response does not imply that every history–response combination supports the same future decoder.  Coverage of the semantic product is an additional model object that must be justified.

## 7. Reproducibility

The executable derivation is in

- `crest/semantic_access.py` — derived history modes, response types, and semantic access relation;
- `crest/semantic_temporal_quotient.py` — raw-world enumeration, semantic trace profiles, induced quotients, and dividends;
- `tests/test_semantic_temporal_quotient.py` — exact checks for `k=0,...,N`, including the canonical `19`, `259`, and `1027` grand-coalition class counts.

No coalition value is assigned directly in this pipeline.
