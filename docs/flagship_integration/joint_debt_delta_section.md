# Flagship section — joint debt is not additive

> **Role in PR #66:** this section replaces the matched carrier-gain theorem pair as the quantitative headline of the integrated CREST manuscript. The carrier no-bound result and the sharp sequential law \(H\log_2 r\) remain supporting results. The fixed-point and marked-cycle mathematics used below are classical finite-state substrate; the CREST claim is the accounting interpretation of their interaction across separately declared ecological responsibilities.

## Joint responsibility can cost more than the sum of its parts

CREST begins with a baseline ecological state partition \(B\) on one declared finite common carrier. Each scientific responsibility—future response, inherited semantics, retained mechanism, evidence/target discipline, or another explicitly declared audit—acts as a refinement closure \(C_i\). If responsibility \(i\) were considered alone, the extra state information it demands would be

\[
D_i
=
\log_2|C_i(B)|-
\log_2|B|.
\]

A natural accounting rule would therefore assign a monitoring or representation budget to each responsibility separately and add them. That rule assumes that the distinctions required by one responsibility do not change what another responsibility can distinguish.

CREST does not have that independence in general. The state needed when all responsibilities are imposed together is the least common fixed point

\[
J
=
(C_1\vee\cdots\vee C_k)(B),
\]

obtained by fair iteration of the closures. Its joint debt is

\[
D_{\mathrm{joint}}
=
\log_2|J|-
\log_2|B|.
\]

We therefore define the **joint-debt excess**

\[
\boxed{
\Delta
=
D_{\mathrm{joint}}
-
\sum_{i=1}^{k}D_i.
}
\]

The quantity is deliberately an accounting diagnostic rather than a claim that subtraction has discovered a new class of finite-state theorem. Its ecological content is operational: \(\Delta>0\) means that separately budgeting the state or monitoring resolution demanded by each responsibility understates the burden of satisfying them simultaneously. One audit can create a distinction that makes another audit newly informative, which can create another distinction in turn. The scientific responsibilities interact through the state they jointly refine.

This distinction matters for the integrated CREST programme because the companion theories do not merely contribute independent checkboxes. CCOC can require a future-facing distinction, MLTR can require inherited semantic coherence, and MRM can require a retained mechanism distinction. Once placed on one declared common lift, a split introduced for one reason can expose a successor, history, or response difference that another audit could not detect from the original baseline. The combined state is therefore not, in general, recoverable by computing each module once against the untouched baseline and summing the resulting bit counts.

### A sharp cyclic family

The interaction can be arbitrarily large even with only two audit closures. Consider \(n\ge2\) worlds arranged on a directed cycle and start from the indiscrete baseline partition \(B\), containing one state. The first audit marks one world and otherwise treats all worlds alike. Acting alone it creates exactly two classes, so

\[
D_1=1\text{ bit}.
\]

The second audit has no static mark. It requires only that states merged in the same class have successors in the same class under one deterministic cycle step. Against the indiscrete baseline, every successor still lies in the same single block, so the audit changes nothing:

\[
D_2=0.
\]

If the audits are applied jointly, however, the one marked state changes the successor signature of its predecessor. That predecessor must split. Its newly distinct block changes the successor signature of the preceding world, forcing another split, and so on around the cycle. At the common fixed point every world is distinct. Hence

\[
D_{\mathrm{joint}}=\log_2 n
\]

and therefore

\[
\boxed{
\Delta=\log_2 n-1.
}
\]

Because \(n\) is arbitrary, the positive joint-debt excess is unbounded. Yet neither responsibility considered alone signals the final burden: their separate debts always sum to one bit. The family is intentionally minimal. Mathematically, it is the familiar phenomenon that a seed distinction propagated through deterministic successor stability can make the coarsest stable partition discrete. CREST does not claim that phenomenon itself as novel. What the example establishes for the present framework is the failure of **responsibility-wise additive accounting**.

### What cannot happen

There is also a useful zero case. If every responsibility has zero individual debt,

\[
D_i=0\quad\text{for all }i,
\]

then every closure already fixes the baseline \(B\). The baseline is therefore a common fixed point, so fair joint iteration cannot refine it. Consequently

\[
\boxed{
D_i=0\ \forall i
\Longrightarrow
D_{\mathrm{joint}}=0
\Longrightarrow
\Delta=0.
}
\]

Thus positive synergy cannot arise from a collection of audits that each literally leave the baseline unchanged. At least one responsibility must first create a distinction; the excess appears when that distinction activates additional refinements under other responsibilities.

## Ecological interpretation

The practical implication is a warning against allocating monitoring effort one responsibility at a time. Suppose managers separately ask whether a community is future-sufficient for a reconnection plan, whether an inherited functional category remains meaningful after turnover, and whether retained mechanisms agree on intervention response. Running each audit against the same coarse baseline can make the total look modest. But once a future-facing measurement separates two worlds, that split may expose a history-dependent transition; once history is retained, it may expose a mechanism-specific response. The integrated requirement can therefore demand substantially finer resolution than the sum of the first-pass module budgets.

This is the sense in which \(\Delta\) is an **integration-only quantity**. CCOC, MLTR, or MRM alone can define their own repair burden, but none of them can define \(D_{\mathrm{joint}}\) for a common contract spanning all responsibilities. The quantity belongs to CREST precisely because it measures what becomes visible only after the responsibilities are composed.

The earlier carrier-gain no-bound result remains useful but is no longer the headline: it shows that a small increase in feasible management capacity need not imply a small state burden. The sequential response-depth law also remains useful as a supporting upper bound when one response channel is isolated. The new hierarchy is therefore:

\[
\boxed{
\text{joint non-additivity }\Delta
\quad\text{(headline accounting result)}
}
\]

\[
\text{carrier-gain no-bound}
\quad+\quad
\text{sharp }H\log_2 r\text{ response bound}
\quad\text{(supporting structural results).}
\]

For an ecological journal, the claim is not that a marked cycle is a new mathematical object. It is that a state theory assembled from multiple scientifically necessary responsibilities requires a **joint budget**, because the cost of their intersection can be generated by cascade rather than by independent addition.
