# CREST signature-family invariance theorem

## Purpose

The least temporal-cut quotient should not depend on arbitrary representation choices such as signature names, codomain labels, coordinate order, duplicated signatures, or whether the same joint information is written as one packed signature or several coordinates.

This note states the exact finite condition under which two different pre-state signature families represent the same state information.

## Setup

Fix a finite carrier \(\Omega\) and one observational cut

\[
O_t:\Omega\to Y_t.
\]

Let

\[
\mathcal G=(g_1,\ldots,g_r),\qquad
\mathcal H=(h_1,\ldots,h_s)
\]

be two finite families of pre-state signatures, each defined independently of the final cut-state.

Write

\[
Q_{\mathcal G}=Q(O_t,\mathcal G),\qquad
Q_{\mathcal H}=Q(O_t,\mathcal H)
\]

for the unique coarsest cut-state quotients preserving the cut and the respective signature families.

## Theorem — representation invariance

The following are equivalent:

1. \(Q_{\mathcal G}\) and \(Q_{\mathcal H}\) have exactly the same blocks, up to relabeling of quotient classes;
2. every \(g_i\) factors through \(Q_{\mathcal H}\), and every \(h_j\) factors through \(Q_{\mathcal G}\).

Equivalently, the two families generate the same equivalence relation on \(\Omega\) after the fixed cut observation is included.

### Proof

If the two induced quotients have the same blocks, every signature in either family is constant on those blocks because its own induced quotient preserves it. Thus mutual factorization holds.

Conversely, suppose every \(g_i\) factors through \(Q_{\mathcal H}\). Then \(Q_{\mathcal H}\) preserves the cut and every member of \(\mathcal G\). By the least-cut universal property, \(Q_{\mathcal H}\) refines \(Q_{\mathcal G}\). The symmetric assumption gives the reverse refinement. Two finite partitions refining one another have identical blocks up to relabeling. Therefore

\[
Q_{\mathcal G}=Q_{\mathcal H}
\]

as quotient partitions.

## Corollary — redundant-extension invariance

Let \(\mathcal A\) be an additional family. Then

\[
Q(O_t,\mathcal G\cup\mathcal A)=Q(O_t,\mathcal G)
\]

if and only if every member of \(\mathcal A\) already factors through \(Q_{\mathcal G}\).

Therefore duplicate coordinates, deterministic recodings, signature relabelings, and any other functions of the existing cut-state cannot inflate the state merely by being listed again.

## What this removes

The final state does **not** depend on:

- signature names;
- codomain labels;
- order of coordinates;
- duplicated coordinates;
- splitting one joint signature into several mutually equivalent coordinates;
- packing several coordinates into one signature;
- adding any signature already determined by the current induced state.

What remains scientifically substantive is the generated distinguishability relation itself. Different signature families that generate genuinely different equivalence relations are different theoretical assumptions, not harmless reparameterizations.

## Boundary of the theorem

This theorem does not say that every ecological choice of pre-state signatures is scientifically valid. It says something narrower and exact:

> once a scientific problem has been represented by a family of pre-state distinctions, only the equivalence relation generated jointly with the temporal cut matters for the induced state.

Thus the remaining modeling freedom lies in which distinctions are admitted as scientifically meaningful, not in how those distinctions are encoded.

## Relation to sparse semantic access

MLTR carried semantics, MRM candidate-safe response types, and CCOC prospective traces provide one structured family of pre-state signatures. Any alternative representation of those same distinctions that mutually factors through the canonical induced state produces exactly the same CREST cut-state quotient and therefore the same quotient cardinality and sparse-access accounting.
