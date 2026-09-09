# CREST temporal-cut / latent-present reframing — 2026-09-09

## Decision

The flagship should be read as a finite theory of state **at a temporal boundary**, not as a design manual.

The present is treated as a zero-width temporal cut in the idealized representation. The finite theory does not require a continuous-time limit theorem; the phrase `zero-width` is interpretive shorthand for the fact that the present is represented by a cut map at one indexed time rather than by a finite-duration interval.

The three companion roles are therefore:

- **MLTR / retrospective side**: distinctions inherited from the left of the cut;
- **MRM / latent-present fiber**: distinctions transverse to the visible cut, hidden behind the same present observation but represented by different candidate-safe response types;
- **CCOC / prospective side**: distinctions exposed by legal right-of-cut queries.

The state is not caused by these three roles. They induce distinguishability constraints on the cut. The CREST state is the least quotient/refinement on the cut compatible with all retained constraints.

## Finite formalization

Let

\[
O_t:\Omega\to Y_t
\]

be the observation map at cut time `t`, with baseline equivalence

\[
B_t=\ker O_t.
\]

For one observed value `y`, the fiber

\[
L_t(y)=O_t^{-1}(y)
\]

is the set of raw worlds hidden behind that visible cut value. The phrase **latent present** refers to structure within this fiber that remains invisible to `O_t` but is separated by MRM response equivalence.

MLTR supplies a retrospective semantic map `H_t`; MRM supplies a transverse latent-response map `Theta_t`; CCOC supplies prospective response constraints indexed by a legal query grammar. None is defined from the final CREST state.

The adequate cut-state is the least quotient of `Omega` refining `B_t` enough to preserve the declared left, transverse, and right distinctions. In closure notation,

\[
J_t=(C_H\vee C_\Theta\vee C_F)(B_t),
\]

with sparse semantic access modifying which prospective distinctions are actually active inside the `H x Theta` product.

## Important boundary

CREST has **not** proved a continuous-time theorem in which an interval `[t-epsilon,t+epsilon]` converges as `epsilon -> 0` to the finite cut construction. Therefore the manuscript should not write such a limit as a theorem. It may say that the finite model idealizes the present as a zero-duration boundary rather than a finite observation window.

Likewise, `Theta` is not a complete ontic mechanism coordinate. It is a candidate-safe latent response structure inside the present observation fiber. Calling it a `latent-present fiber` is an interpretation of its geometric role at the cut, not a claim that MRM recovers every hidden causal mechanism.

## Pure-theory reading

The central question becomes:

> Given an observational cut and retrospective, transverse, and prospective equivalence/access structures, what is the minimal state quotient induced on the cut, and how does its complexity change under partial prospective access?

The sparse-access theorem then studies the cardinality of that induced quotient. The shallow-lake model is an interpretation/witness of the abstract structure, not the source of the theory and not a state-design prescription.
