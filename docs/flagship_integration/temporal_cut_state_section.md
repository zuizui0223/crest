# Manuscript-ready section — state at a temporal cut

## State is what must survive the cut

CREST does not need to define the present as a third temporal interval between a
past interval and a future interval.  Fix a time `t` and let

\[
O_t:\Omega\to Y_t
\]

be the declared observation available at that temporal cut.  The visible-present
baseline is the kernel partition

\[
B_t=\ker O_t,
\]

so two latent worlds are initially merged exactly when they return the same value
at the cut.  The word `present` therefore names the **cut itself and its
observational equivalence**, not an independently parameterized duration.

The two temporal sides of the cut are conceptually distinct.  Write
\(H^-_t\) for retrospective information carried from trajectories before `t`, and
\(F^+_t\) for prospective or counterfactual response structure relevant after
`t`.  Neither object is required to be fully retained.  They identify candidate
differences among latent worlds that may or may not matter to the scientific
contract.

A third source of distinction is not another direction along the time axis.
For one visible cut value \(y\), define the latent fiber

\[
L_t(y)=O_t^{-1}(y).
\]

Worlds inside the same fiber are observationally identical at the cut but can
carry different contemporaneous response structures \(\Theta_t\).  MRM occupies
this transverse direction: it asks whether differences inside a visible-present
fiber can safely remain unresolved when declared interventions or responses are
considered.

Thus the geometry is

```text
                     latent response fiber Theta_t
                               |
                               |  MRM
                               |
H^-_t  ------------------------*------------------------  F^+_t
history                      cut t                      future
MLTR                                                    CCOC
```

The finite theorem does not take an infinitesimal limit.  A continuous-time
extension could later replace the two sides by left and right trajectory germs,
but the proved finite theory requires only a declared observation cut and three
refinement responsibilities.

## Cut-state construction

On one finite carrier, let

\[
C_H,\qquad C_\Theta,\qquad C_F
\]

be the closures induced by retrospective history, latent contemporaneous response
structure, and prospective response responsibility.  The least-information state
that must survive at the cut is

\[
\boxed{
J_t=(C_H\vee C_\Theta\vee C_F)(B_t).
}
\]

The CREST state of latent world \(\omega\) at the cut is its block
\([\omega]_{J_t}\).  In this formulation a state is not the raw present snapshot.
It is the minimum information that cannot be forgotten at the cut once the
scientific responsibilities directed from the past, through the latent fiber,
and toward the future are enforced jointly.

This recovers the philosophical claim in the finite mathematics: a state is a
scientifically licensed compression of a temporally extended world, with the
present observation supplying the baseline rather than the answer.

## Past and future do not separate additively

For a coalition \(S\subseteq\{H,\Theta,F\}\), let

\[
v(S)=\log_2|J_S|-\log_2|B_t|.
\]

Even the two temporal sides of the cut need not contribute independently.  For
every integer \(n\ge2\), there exists a finite family for which all latent worlds
share one visible cut value and

\[
v(H)=1,\qquad v(F)=0,
\]

but

\[
v(HF)=\log_2n.
\]

Hence the past-by-future interaction is

\[
\boxed{
m(H,F)=\log_2n-1,
}
\]

which is unbounded.  The amount of history that an adequate state must retain
therefore cannot in general be determined independently of the future responses
that the state is required to support.

This is temporal **interaction or coupling**, not statistical confounding.  No
claim about omitted-variable bias or probabilistic common causes is intended.

## The latent fiber creates genuine three-way temporal interaction

The stronger result uses the same cut geometry.  For every integer \(m\ge2\), a
finite family exists with a single visible cut class and

\[
v(H)=1,\qquad v(\Theta)=v(F)=0,
\]

while

\[
|J_{H\Theta F}|=2^m,
\qquad
v(H\Theta F)=m\text{ bits}.
\]

Its complete coalition block counts are

| coalition | required blocks |
|---|---:|
| none | 1 |
| H | 2 |
| Theta | 1 |
| F | 1 |
| H + Theta | 3 |
| H + F | 2 |
| Theta + F | 1 |
| H + Theta + F | \(2^m\) |

Möbius inversion gives

\[
m(H,\Theta)=\log_2(3/2)
\]

and the genuine three-way interaction

\[
\boxed{
m(H,\Theta,F)=m-\log_2 3.
}
\]

Therefore

\[
m(H,\Theta,F)\to\infty
\]

and

\[
\boxed{
\frac{m(H,\Theta,F)}{v(H\Theta F)}
=1-\frac{\log_2 3}{m}
\to1.
}
\]

The mathematical consequence is stronger than generic non-additivity: required
state information can become asymptotically dominated by a distinction that
belongs to no single temporal position in isolation.  The past first creates a
distinction; that distinction makes a latent response difference operational;
that latent split then activates a prospective refinement cascade.

## Numerical closure

At \(m=10\), every latent world still has the same visible value at the temporal
cut, yet the adequate joint state requires

\[
2^{10}=1024
\]

classes and exactly **10 bits**.  The exact decomposition is

| contribution | bits | share of total state debt |
|---|---:|---:|
| history alone | 1.0000000000 | 10.00% |
| history x latent present | 0.5849625007 | 5.85% |
| history x future | 0 | 0% |
| latent present x future | 0 | 0% |
| **history x latent present x future** | **8.4150374993** | **84.15%** |
| **joint** | **10.0000000000** | **100%** |

Total interaction debt is 9 bits, or 90% of the joint burden.  Of those
interaction bits, 93.50% are in the genuine three-way dividend.

This gives a concrete endpoint for the state concept.  A single visible present
can correspond to a 1024-class scientifically adequate state not because the
present observation itself became richer, but because the information that must
survive the cut is generated jointly by historical, latent-contemporaneous, and
prospective responsibilities.

## Claim boundary

The theorem supports the following finite conditional claim:

> Given a declared observational cut and finite responsibility closures, the
> least-information state at the cut can be dominated by interaction among
> retrospective history, latent contemporaneous response structure, and
> prospective response responsibility.

It does **not** establish that these three responsibilities exhaust ecological
state, that nature provides a unique decomposition into them, or that every
latent mechanism is identifiable.  It also does not yet prove a continuous-time,
stochastic, infinite-state, delayed-observation, or infinitesimal-germ analogue.
