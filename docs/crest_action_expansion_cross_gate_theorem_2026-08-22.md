# CREST action-expansion cross-gate theorem — 2026-08-22

> **Status:** derived cross-gate proposition. This is not J8 and adds no fifth audit. The component monotonicities are classical; the CREST contribution is their explicit coupling across the controlled-carrier, state-resolution, and evidence gates.

## 1. Why this result matters

The strongest non-obvious CREST perspective is not that ecological state representations are purpose-relative. It is that the **same expansion of management capability can move different adequacy gates in opposite practical directions**.

Adding a controllable action can:

1. enlarge the set of ecological worlds that can be kept viable;
2. make previously mergeable worlds future-distinct and therefore require a finer state;
3. cause unchanged monitoring to cease identifying that required state; while
4. leaving a declared target reportable.

In short:

\[
\boxed{
\text{more control can mean a larger viable domain but a smaller equivalence relation.}
}
\]

The intervention need not be executed. Merely adding it to the declared admissible future/action repertoire can change what must count as the same state.

## 2. Setup

Fix a finite ambient world set \(W\), compatibility set \(W_0\), uncontrollable action set \(A_u\), and two controllable repertoires

\[
A_c\subseteq A_c'.
\]

Assume that all old transitions and uncontrollable transitions are unchanged when passing from \(A_c\) to \(A_c'\).

Let \(K^*(A_c)\) and \(K^*(A_c')\) be the J6 greatest robustly controlled-invariant carriers.

On a fixed common retained carrier \(U\), let \(J_\Gamma\) be the required CREST state under future grammar/action repertoire \(\Gamma\), and let \(J_{\Gamma'}\) be the state after an order-compatible strengthening \(\Gamma\subseteq\Gamma'\), with the other audit obligations unchanged. Order-compatible means that every partition adequate for \(\Gamma'\) is also adequate for \(\Gamma\).

Let \(E\) be a fixed evidence partition.

## 3. Proposition A — control expansion is carrier-monotone

\[
\boxed{K^*(A_c)\subseteq K^*(A_c').}
\]

### Proof

For a candidate set \(S\subseteq W_0\), define the J6 predecessor operator

\[
G_{A_c}(S)=\{w\in S:\text{all uncontrollable successors remain in }S\text{ and at least one }a\in A_c\text{ has a successor in }S\}.
\]

Because \(A_c\subseteq A_c'\), every witness control available under \(A_c\) remains available under \(A_c'\). Hence

\[
G_{A_c}(S)\subseteq G_{A_c'}(S)
\]

for every \(S\). Starting both descending iterations from the same \(W_0\), induction gives inclusion at every iterate, and therefore at the greatest fixed points:

\[
K^*(A_c)\subseteq K^*(A_c').
\]

Thus adding controllable options cannot remove a world solely from the J6 viable carrier when old dynamics and uncontrollable obligations are preserved. \(\square\)

## 4. Proposition B — future-responsibility expansion is state-refinement monotone

On a fixed common carrier \(U\), if \(\Gamma'\) is an order-compatible strengthening of \(\Gamma\), then

\[
\boxed{J_\Gamma\preceq J_{\Gamma'}.}
\]

### Proof

Every state partition satisfying the stronger future obligation also satisfies the weaker one. Therefore the feasible common-fixed-point set under \(\Gamma'\) is a subset of the feasible set under \(\Gamma\). Since J1 chooses the unique coarsest feasible partition in each set, the stronger-contract minimum cannot be coarser:

\[
J_\Gamma\preceq J_{\Gamma'}.
\]

Equivalently, adding future/action responsibilities can preserve or split old state blocks, but cannot force previously required distinctions to disappear under this one-sided comparison. \(\square\)

## 5. Proposition C — fixed-evidence identifiability is antitone in required state refinement

If

\[
J_\Gamma\preceq J_{\Gamma'}
\]

and fixed evidence \(E\) fails to identify \(J_\Gamma\), then it also fails to identify \(J_{\Gamma'}\):

\[
\boxed{
J_\Gamma\not\preceq E
\Longrightarrow
J_{\Gamma'}\not\preceq E.
}
\]

Equivalently,

\[
J_{\Gamma'}\preceq E\Longrightarrow J_\Gamma\preceq E.
\]

### Proof

If every evidence block lies inside a finer \(J_{\Gamma'}\)-block, it necessarily lies inside the containing coarser \(J_\Gamma\)-block. The contrapositive gives the failure statement. \(\square\)

This is the order-theoretic reason fixed monitoring can lose full-state adequacy along contract strengthening but cannot regain it merely because the required state is refined further.

## 6. Cross-gate consequence — opposed monotonicities

Under aligned management/future expansion, the same scientific change can therefore have two different monotone effects:

\[
\boxed{
A_c\uparrow
\Rightarrow
K^*\uparrow
\qquad\text{while}\qquad
\Gamma\uparrow
\Rightarrow
J\text{ refines}.
}
\]

The first effect is permissive: more worlds can become safely manageable.

The second is demanding: fewer worlds may be scientifically interchangeable.

These are not contradictory because they live on different gates. Their conjunction is the key CREST perspective:

> **Management capability can expand the domain on which a state must work while simultaneously increasing the information that the state must retain.**

## 7. Strict simultaneous witness

The existing four-world `rescue` construction makes all relevant inequalities strict.

Worlds:

\[
\{a,b,c,\mathrm{bad}\}.
\]

Before enrichment, only `hold` is available. `a` and `c` are viable; `b` exits to `bad`, so

\[
K^*_{\rm before}=\{a,c\}.
\]

After adding one controllable action `rescue`, `b` can remain viable, so

\[
K^*_{\rm after}=\{a,b,c\}.
\]

But `rescue` also distinguishes `a` from `b`:

\[
a\xrightarrow{\rm rescue}c,
\qquad
b\xrightarrow{\rm rescue}b.
\]

Hence the least-information required state splits them. Fixed monitoring still merges them in one `live` evidence class, so full-state identification is lost. The declared target `survives` remains constant across `a,b`, so target reporting survives.

Thus one added action realizes

\[
\boxed{
|K^*|\uparrow,
\quad |J|\uparrow,
\quad \text{full-state identifiability}\downarrow,
\quad \text{target reportability unchanged}.
}
\]

## 8. Quantitative corollary

For fixed evidence \(E\), the minimum monitoring refinement needed to identify \(J\) is

\[
E\vee J,
\]

with resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

State-refinement monotonicity gives

\[
J_\Gamma\preceq J_{\Gamma'}
\Longrightarrow
D_E(J_\Gamma)\le D_E(J_{\Gamma'}).
\]

The `rescue` witness changes debt from zero to

\[
\log_2(3/2)>0
\]

while target debt stays zero.

The existing CCOC extremal family strengthens this: one newly relevant future action can create exactly \(m\) bits of monitoring-resolution debt for arbitrary finite \(m\) across the family.

## 9. Philosophical reading

The result suggests a sharper formulation of CREST than generic purpose-relativity:

> **An ecological intervention does not merely act on a pre-existing state space. By entering the admissible future repertoire, it can change which ecological differences must count as state differences before that intervention is ever executed.**

This separates the result from ordinary dual-control language. Dual control concerns how executing an action can change future information and control. The CREST effect occurs already at the level of **action availability and representational obligation**.

## 10. Novelty firewall

Not claimed as new:

- viability kernels or their monotonicity with available controls;
- observability or partial observability;
- links between viability and observability;
- state abstraction, bisimulation, or future-sensitive equivalence;
- adaptive monitoring when management questions change;
- the partition-order arguments used above.

The candidate contribution is the **cross-gate conjunction**: the same management-repertoire expansion can enlarge the controlled carrier while tightening the least-information ecological state and defeating unchanged full-state monitoring, with target reporting optionally preserved. The current broad prior-art audit found close ingredients but no direct match to that full conjunction; this is not a historical-firstness claim.
