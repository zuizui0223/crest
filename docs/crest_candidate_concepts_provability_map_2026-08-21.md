# CREST candidate concepts — provability map

> **Status:** derived-corollary development note, 2026-08-21. This document introduces no fifth audit and no J8 theorem family. It asks which higher-level concepts suggested by the adequacy-frontier work are already mathematically forced by J1/J5/CED-style partition order, and which remain only interpretations.

## 0. Verdict

Four candidate concepts were screened.

| Candidate | Mathematical status | Safe interpretation |
|---|---|---|
| **Monitoring Adequacy Envelope** | **proved derived theorem** | for fixed evidence and an order-compatible contract family, the contracts whose full states remain identifiable form a lower set |
| **Counterfactual Obsolescence** | **proved exact criterion** | monitoring can become inadequate with unchanged evidence exactly when contract strengthening activates a state split inside an evidence class |
| **Ecological State Shadow** | **proved finite anticipatory-state theorem** | a finite family of contemplated stronger contracts has a unique coarsest state that is sufficient for all of them; the extra splits relative to the current state are the exact dormant distinctions that may later activate |
| **Decision-Safe Ignorance** | **exact regime / corollary, not a new theorem family** | full state can remain unresolved while every evidence class is target-constant; the sharp state report is set-valued while the sharp target report is singleton-valued |

The first three are not merely names. They admit exact finite statements and proofs. Their mathematical substrate is classical partition order; the CREST content is the ecological interpretation and coupling to contract change, evidence, and management.

---

## 1. Setup

Fix one finite carrier

\[
U=\{u_1,\ldots,u_n\}
\]

and a fixed reliability-qualified evidence partition \(E\). For each admissible scientific contract \(c\) on this carrier, let \(J_c\) denote its unique coarsest CREST state partition supplied by J1.

Write

\[
c\le d
\]

for an **order-compatible strengthening** when the stronger contract cannot require fewer distinctions:

\[
J_d\text{ refines }J_c.
\]

This is the comparison regime already justified by J5-style one-sided refinement premises. No claim is made that every pair of real scientific purposes is globally orderable this way.

Evidence **licenses** a partition \(J\) when every evidence block lies inside one \(J\)-block. This is exactly the finite deterministic full-state reporting criterion implemented by `evidence_licenses`.

---

## 2. The Monitoring Adequacy Envelope

### Definition

For fixed evidence \(E\), define

\[
\boxed{
\mathfrak M(E)
=
\{c:\; c\text{ is admissible and }E\text{ licenses }J_c\}.
}
\]

This is the set of scientific contracts for which the unchanged monitoring system is sufficient to identify the full least-information state.

### Theorem M1 — envelope lower-set theorem

Let \((\mathfrak C,\le)\) be any finite or infinite family of admissible contracts on the same carrier with fixed evidence \(E\), and assume

\[
c\le d\Longrightarrow J_d\text{ refines }J_c.
\]

Then \(\mathfrak M(E)\) is a **lower set**:

\[
\boxed{
d\in\mathfrak M(E),\ c\le d
\Longrightarrow
c\in\mathfrak M(E).
}
\]

Equivalently, failure is upward closed:

\[
\boxed{
c\notin\mathfrak M(E),\ c\le d
\Longrightarrow
d\notin\mathfrak M(E).
}
\]

### Proof

Suppose \(d\in\mathfrak M(E)\). Every evidence block is therefore contained in one \(J_d\)-block. Because \(J_d\) refines \(J_c\), every \(J_d\)-block is contained in one \(J_c\)-block. Hence every evidence block is contained in one \(J_c\)-block, so \(E\) licenses \(J_c\). Therefore \(c\in\mathfrak M(E)\).

The upward-closed failure statement is the contrapositive. \(\square\)

### Consequence

Along an order-compatible strengthening path with fixed monitoring, **full-state identifiability can be lost but cannot later be recovered merely by requiring an even finer state**. Recovery requires changing evidence, changing the carrier/contract comparison, or leaving the order-compatible path.

This makes the phrase “monitoring adequacy envelope” literal: fixed monitoring supports a downward-closed region of the ordered contract family.

---

## 3. Counterfactual Obsolescence

### Definition

Consider \(c\le d\) on the same physical carrier, with the same evidence map \(E\). Monitoring undergoes **counterfactual obsolescence** from \(c\) to \(d\) when

\[
E\text{ licenses }J_c
\qquad\text{but}\qquad
E\text{ does not license }J_d.
\]

The word *counterfactual* means that the loss of adequacy is caused by a change in the future/intervention/semantic/mechanism responsibilities assigned to the state, not by a change in the current observation map itself.

### Theorem C1 — exact obsolescence criterion

Assume \(c\le d\) and fixed evidence \(E\), with \(E\) licensing \(J_c\). Then the following are equivalent:

1. monitoring is counterfactually obsolete under \(d\);
2. there exist \(u,v\in U\) such that
   \[
   E(u)=E(v),
   \qquad
   [u]_{J_c}=[v]_{J_c},
   \qquad
   [u]_{J_d}\ne[v]_{J_d};
   \]
3. at least one evidence block is split by the strengthened state partition \(J_d\).

### Proof

Because \(E\) licenses \(J_c\), two worlds in one evidence block must already lie in one \(J_c\)-block. Evidence fails to license \(J_d\) exactly when some evidence block contains two worlds with different \(J_d\) labels. This is precisely statements 2 and 3. \(\square\)

### Consequence

A monitoring programme can become inadequate even when:

- the physical carrier is unchanged;
- the observation map is unchanged;
- the realized evidence record is unchanged.

Only the **counterfactual responsibilities of the state** need change.

The existing management-enrichment witness is a constructive instance: adding `rescue` enlarges the viable carrier and activates a state distinction that the fixed monitoring record does not resolve.

---

## 4. Ecological State Shadow and the anticipatory state

The earlier informal “state shadow” idea can be made exact without asserting that the future is known.

### Definition — contemplated contract family

Fix a current contract \(c_0\) and a finite declared family of contemplated contracts

\[
\mathcal F=\{c_0,c_1,\ldots,c_m\}
\]

on the same carrier. Let their J1 states be

\[
J_0,J_1,\ldots,J_m.
\]

Define the **anticipatory partition**

\[
\boxed{
J^{\uparrow}_{\mathcal F}(u)
=
\bigl(J_0(u),J_1(u),\ldots,J_m(u)\bigr)
}
\]

up to canonical relabelling. Two worlds are merged by \(J^{\uparrow}_{\mathcal F}\) exactly when every contemplated contract allows them to remain merged.

### Theorem S1 — unique coarsest anticipatory state

\(J^{\uparrow}_{\mathcal F}\) is the unique coarsest partition sufficient for **every** contemplated contract:

1. \(J^{\uparrow}_{\mathcal F}\) refines each \(J_i\);
2. if a partition \(P\) refines every \(J_i\), then \(P\) refines \(J^{\uparrow}_{\mathcal F}\).

### Proof

If two worlds share one \(J^{\uparrow}_{\mathcal F}\)-block, their complete tuple of \(J_i\) labels is identical, so they share a block in every \(J_i\). Thus the anticipatory partition refines each \(J_i\).

Now let \(P\) refine every \(J_i\). If two worlds share one \(P\)-block, they share one block in every \(J_i\). Their label tuples are therefore identical, so they also share one \(J^{\uparrow}_{\mathcal F}\)-block. Hence \(P\) refines \(J^{\uparrow}_{\mathcal F}\). Uniqueness follows from mutual refinement of any two coarsest such partitions. \(\square\)

### Definition — ecological state shadow

Relative to the current state \(J_0\), define the **state shadow relation** as the set of currently merged pairs that the anticipatory state must split:

\[
\boxed{
\mathrm{Shadow}_{\mathcal F}(J_0)
=
\{(u,v):J_0(u)=J_0(v),\ J^{\uparrow}_{\mathcal F}(u)\ne J^{\uparrow}_{\mathcal F}(v)\}.
}
\]

These are not hidden “true states.” They are exactly the distinctions that are presently compressible under \(c_0\) but would matter under at least one explicitly contemplated contract.

### Corollary S1.1 — exact activation criterion

For a pair currently merged by \(J_0\),

\[
(u,v)\in\mathrm{Shadow}_{\mathcal F}(J_0)
\]

iff at least one contemplated contract \(c_i\) separates the pair.

Thus **dormant distinction activation** is not a separate primitive: it is the event that a pair in the current shadow becomes separated by the active contract.

### Corollary S1.2 — shadow burden

Define

\[
\Delta K_{\rm shadow}
=
\log_2|J^{\uparrow}_{\mathcal F}|-
\log_2|J_0|.
\]

Then

\[
\Delta K_{\rm shadow}\ge0.
\]

If the contemplated family is enlarged, \(J^{\uparrow}\) can only refine and \(\Delta K_{\rm shadow}\) cannot decrease.

Under a nested CCOC closed/open pair, \(J^{\uparrow}\) is the open exact interface. The existing one-action extremal family therefore gives

\[
\Delta K_{\rm shadow}=m
\]

for arbitrary \(m\). Hence finite ecological state shadows can carry an **unbounded anticipatory memory burden across a problem family**, even though each individual problem remains finite.

This is a corollary of the CCOC family, not a new lower-bound theorem.

---

## 5. Decision-Safe Ignorance

### Definition

For state partition \(J\), evidence \(E\), and declared target \(T\), call an evidence class **decision-safe ignorant** when it is compatible with more than one J-state but only one target value.

At the whole-contract level:

\[
\boxed{
\text{Decision-Safe Ignorance}
\iff
E\text{ licenses }T
\quad\text{and}\quad
E\text{ does not license }J.
}
\]

### Proposition D1 — exact reporting form

Decision-Safe Ignorance holds iff:

1. at least one sharp state report contains more than one J-block; and
2. every sharp target report is a singleton.

### Proof

`compatible_values_by_evidence` returns exactly the distinct state or target values represented inside each evidence block. Full-state licensing fails iff at least one evidence block contains more than one J label. Target licensing holds iff every evidence block contains exactly one target value. \(\square\)

### Interpretation

This is not ignorance in the sense of model failure. It is **target-safe unresolved state information**. The concept should not be promoted as a new mathematical theorem because the factorization criterion is already part of J1/CED. Its value is philosophical and decision-theoretic: it identifies which unresolved state distinctions need not be paid for when the declared target is already determined.

---

## 6. How the concepts fit together

The four concepts form one derived chain:

```text
current contract c0
    -> current least-information state J0
    -> contemplated stronger contracts
    -> unique coarsest anticipatory state J^up
    -> currently merged pairs split by J^up = State Shadow
    -> one such contract becomes active = dormant distinction activation
    -> if the fixed evidence no longer resolves the active J = Counterfactual Obsolescence
    -> all contracts still resolved by the fixed evidence = Monitoring Adequacy Envelope
    -> if full J is unresolved but target is constant = Decision-Safe Ignorance
```

The management-induced information-debt witness is a special cross-gate realization in which the same management enrichment expands viability while moving the active contract outside the old monitoring envelope.

---

## 7. Claim firewall

### Mathematically proved here as derived results

- Monitoring Adequacy Envelope lower-set property under an order-compatible contract family and fixed evidence.
- Exact pairwise criterion for Counterfactual Obsolescence.
- Unique coarsest anticipatory state for a finite declared family of contract-specific J partitions.
- Exact State Shadow / dormant activation characterization.
- Monotonic shadow burden under enlargement of the contemplated contract family.
- Exact Decision-Safe Ignorance reporting criterion.

### Not claimed

- that all real ecological contracts form one total or even globally useful partial order;
- that contemplated future contracts are objectively correct or exhaustive;
- that the state shadow is an intrinsic hidden ontology;
- that every management innovation causes counterfactual obsolescence;
- that every state-shadow distinction should be monitored in advance;
- that anticipatory state design is always normatively preferable to target-specific monitoring;
- historical firstness for partition joins, lower sets, quotient refinement, or factorization criteria.

The mathematical novelty question remains separate from provability. These propositions are valuable because they turn the new CREST vocabulary into exact, falsifiable objects, while their generic order-theoretic substrate remains classical.
