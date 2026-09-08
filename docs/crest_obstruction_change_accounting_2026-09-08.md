# CREST obstruction-change accounting

## Status

Finite exact accounting result on two declared CREST obstruction spectra with the same named responsibility set. The identities are Möbius/cooperative-game substrate; the CREST contribution is the contract-relative ecological-state diagnostic built from them.

## Setup

Let two declared finite contracts, `before` and `after`, use the same responsibility names `N`. For every coalition `S subseteq N`, let

\[
v^-(S),\qquad v^+(S)
\]

be the obstruction state debt of the coalition relative to its declared baseline. Let `m^-(S)` and `m^+(S)` be the Möbius/Harsanyi dividends, so

\[
v^\pm(N)=\sum_{\varnothing\ne S\subseteq N}m^\pm(S).
\]

Define

\[
\delta m(S)=m^+(S)-m^-(S).
\]

Singleton dividends are the standalone debts:

\[
m(\{i\})=D_i.
\]

## Proposition 1 — exact change decomposition

The change in joint state debt satisfies

\[
\boxed{
\delta D_{\rm joint}
=
\sum_{\varnothing\ne S\subseteq N}\delta m(S)
=
\sum_i\delta D_i+\delta\Delta.
}
\]

Moreover,

\[
\boxed{
\delta\Delta
=
\sum_{|S|\ge2}\delta m(S).
}
\]

Thus every before/after change in joint burden is exactly decomposed into direct singleton changes plus interaction changes.

### Proof

Subtract the two Möbius reconstructions of `v(N)`. Split the resulting sum into singleton and order-at-least-two coalitions. Since singleton dividends equal standalone debts and `Delta = D_joint - sum_i D_i`, the displayed identities follow. ∎

## Corollary 1 — interaction-only change

If every standalone debt is unchanged,

\[
\delta D_i=0\quad\forall i,
\]

then

\[
\boxed{
\delta D_{\rm joint}=\delta\Delta
=
\sum_{|S|\ge2}\delta m(S).
}
\]

Therefore any nonzero joint-burden change is entirely interaction-generated.

Conversely, under the implemented diagnostic definition, a comparison is `interaction-only` exactly when all standalone changes vanish and `delta Delta` is nonzero.

The sign gives the direction:

- `delta D_joint > 0`: interaction-only burden increase;
- `delta D_joint < 0`: interaction-only burden decrease;
- `delta D_joint = 0`: no net joint-burden change at the declared tolerance.

## Proposition 2 — interaction-order anatomy

For order `k`, define

\[
M_k=\sum_{|S|=k}\delta m(S).
\]

Then

\[
\boxed{
\delta D_{\rm joint}=\sum_{k\ge1}M_k,
\qquad
M_1=\sum_i\delta D_i,
\qquad
\delta\Delta=\sum_{k\ge2}M_k.
}
\]

This partitions the net representational change by coalition order. The implementation calls an order `k >= 2` active when `|M_k|` exceeds tolerance and reports the active order with greatest `|M_k|` as the dominant interaction order, breaking exact ties toward the lower order.

The dominant-order label is a diagnostic summary, not a theorem that one coalition order is causally primary.

## Canonical CCOC/MLTR/MRM change

The six-world comparison keeps all standalone debts unchanged while switching on the CCOC -> MLTR -> MRM activation cascade.

Before:

\[
D_{\rm joint}^-=0.5849625007211561\ \mathrm{bit},
\qquad |J^-|=3.
\]

After:

\[
D_{\rm joint}^+=1.3219280948873622\ \mathrm{bit},
\qquad |J^+|=5.
\]

Therefore

\[
\delta D_{\rm joint}=+0.7369655941662061\ \mathrm{bit}.
\]

All singleton changes are zero. The nonzero higher-order changes are

\[
M_2=+0.4150374992788439\ \mathrm{bit},
\]

from `CCOC x MLTR`, and

\[
M_3=+0.3219280948873622\ \mathrm{bit},
\]

from `CCOC x MLTR x MRM`.

Hence

\[
0.7369655941662061
=
0.4150374992788439
+
0.3219280948873622.
\]

The machine-readable diagnosis is therefore

```text
change_class             interaction-only
joint_debt_direction     increase
direct_direction         unchanged
interaction_direction    increase
active_interaction_orders [2, 3]
dominant_interaction_order 2
```

The reverse comparison has the same source class and active orders but `joint_debt_direction=decrease`; all nonzero order contributions reverse sign.

## What this adds to CREST

A static obstruction spectrum answers how much state resolution a declared contract requires and how that burden is distributed across direct and interaction terms. The change accounting answers a different question:

> When the contract or system representation changes, did required state burden move because one responsibility became more demanding, because responsibilities became more strongly coupled, or both?

This makes representational stability numerically diagnosable in finite declared models rather than only qualitatively described.

## Scope firewall

The result does not infer ecological contracts, carriers, mechanisms, replacement histories, or observation relations from data. It does not claim novelty for Möbius inversion, Harsanyi dividends, or arithmetic differencing. It is an exact finite accounting layer conditional on the CREST obstruction game supplied by the declared model.
