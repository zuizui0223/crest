# CREST state-hypothesis recovery — 2026-08-21

> **Status:** post-J1/J3/J6 recovery synchronization. This document does not add a new theorem. It records what the CREST program now actually proves about “one ecological state,” what earlier formulations were too broad, and what remains open.

## 1. Recovery verdict

The central state question is now recovered far enough to state a precise answer.

The unrestricted hypothesis

> there is one nature-given, globally unique ecological state partition that simultaneously satisfies every CREST requirement

is **rejected as too broad**. The companion theories do not automatically share one carrier, one action semantics, one inherited-label structure, one mechanism family, one evidence relation, or one target.

The corrected conditional hypothesis is **proved**:

> On a declared finite common latent-world carrier, if the four CREST audits induce monotone inflationary idempotent refinement closures on the same partition lattice, then there is a unique coarsest partition satisfying all four obligations.

That partition is CREST-J1.

## 2. What the CREST state is

Fix a declared scientific contract

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T)
\]

and an admissible finite common carrier \(U\). Let \(B\) be the baseline partition containing distinctions that must already be preserved, and let

\[
C_\Gamma,\quad C_\mathcal H,\quad C_\Theta,\quad C_{D,T}
\]

be the four audit closures on \(\Pi(U)\).

Define

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

J1 proves that \(J\) is the **unique coarsest / least-information common fixed point above \(B\)**.

For one latent ecological world \(u\in U\), the CREST state is therefore

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

In words:

> **The CREST state of a configuration is the equivalence class that preserves every distinction required by the declared future, inherited-semantic, mechanism, and target-resolution contracts while discarding every distinction that none of those obligations forces us to keep.**

This is a state-representation result, not a claim that nature contains one privileged partition independently of the scientific contract.

## 3. Recovered hypothesis table

| Recovery item | Earlier/broad question | Current verdict | Formal anchor |
|---|---|---|---|
| STATE-H0 | Is there one unconditional “true” CREST state across all contracts and carriers? | **REJECT / NOT CLAIMED.** Different carriers/contracts/targets may yield different partitions. | J1 boundaries |
| STATE-H1 | Do the four companion contracts automatically share one common world set? | **NO.** A common carrier must first be declared/constructed and may fail to exist. | J3 / J6 |
| STATE-H2 | On an admissible common carrier, is there one least-information state satisfying all four audits? | **PROVED.** Unique coarsest common fixed point \(J\). | J1 |
| STATE-H3 | Is one pass through four separately minimized audits enough? | **REFUTED.** The seven-world cascade witness requires repeated fair refinement. | J1 one-pass obstruction |
| STATE-H4 | Must the audit operators commute pairwise in order for one joint state to exist? | **NO.** Pairwise commutation is unnecessary; fair finite iteration reaches the same least common fixed point. | J1 |
| STATE-H5 | If the required joint state exists, is it automatically identified by the data? | **REFUTED.** Full deterministic state reporting exists iff \(J\preceq E_D\). | J1 evidence gate / CED |
| STATE-H6 | If the full joint state is not identified, must every ecological target remain ambiguous? | **NO.** A target may still factor through the evidence partition even when \(J\not\preceq E_D\). | J1 target corollary |
| STATE-H7 | Can scientifically invisible latent duplication change the CREST state? | **NO under faithful lift.** The joint state pulls back exactly. | J2 |
| STATE-H8 | What happens under one-sided strengthening/weakening of lift obligations? | **PROVED one-sided refinement bounds.** | J5 |
| STATE-H9 | Is the cheapest structurally valid repair also the cheapest fully evidence-licensed repair? | **REFUTED by witness:** \(R^*_{\rm structural}=1<R^*_{\rm licensed}=2\). | O1 |
| STATE-H10 | If no admissible common carrier exists, can the failure be repaired inside a declared finite repair language? | **CHARACTERIZED conditionally.** J4/J7 give exact fixed-witness repair costs and global finite optima; feasibility can fail. | J4 / J7 |

## 4. Three gates that must not be collapsed

The recovered program now has a clean three-gate state logic.

### Gate A — carrier existence

Before asking for one state, the companion contracts must be synchronizable.

- universal-action contract: J3 returns the greatest transition-closed carrier \(U^*\);
- controlled contract: J6 returns the greatest robustly controlled-invariant carrier \(K^*\).

If the required carrier is empty or coverage-incomplete, there is no fully adequate joint state under that declared synchronization. The appropriate response is to change/repair the contract, not merely refine a partition.

### Gate B — state construction

On an admissible carrier, J1 returns the unique coarsest required joint partition \(J\).

This is the answer to **what state must the representation distinguish?**

### Gate C — evidential licensing

Let \(E_D\) be the reliability-qualified evidence partition. A deterministic report of the full CREST state exists exactly when

\[
\boxed{J\preceq E_D.}
\]

If this fails, the state requirement still exists mathematically, but the current evidence does not identify which \(J\)-block is occupied. The sharp report is the set of compatible \(J\)-blocks, not an invented finer observation.

Thus

\[
\boxed{
\text{required state}\neq\text{identified state}\neq\text{target report}
}
\]

in general.

## 5. What the four companion repositories contribute

The four companion programs should no longer be described as four candidate definitions of ecological state.

They supply four classes of **constraints on one proposed state equivalence**:

- **CCOC:** distinctions required by the declared future repertoire;
- **MLTR:** distinctions required to preserve inherited operational meaning;
- **MRM:** distinctions required for candidate-safe deterministic prediction, or explicit ambiguity when no such deterministic collapse exists;
- **CED:** distinctions required for target-safe tracking and the separate evidence condition for whether those distinctions are earned by observation.

J1 is the synthesis step that converts these constraints, once placed on one carrier, into one least-information partition.

## 6. Noncommutation is supporting structure, not the definition of state

The seven-world J1 witness shows that a one-pass composition of separately minimized audits can miss distinctions induced by later refinements. This matters because it rules out a naive “solve four problems independently and intersect once” strategy.

However, CREST should not be reframed primarily as a theory of noncommutation. The philosophical object remains the joint ecological state \([u]_J\). Noncommutation explains why constructing that state can require coupled iteration.

O1 adds a different ordering obstruction: the cheapest carrier repair need not be the cheapest repair whose downstream joint state is fully licensed by evidence. Again, this is a diagnostic boundary around the state concept, not the state definition itself.

## 7. Hypotheses still open or intentionally unclaimed

The recovery does **not** establish:

1. a canonical common carrier \(U\) forced by nature;
2. uniqueness of \(J\) across different choices of carrier, future grammar, inherited semantics, retained mechanisms, evidence contract, or target;
3. philosophical exhaustiveness of the four audit families;
4. one additive scalar combining CCOC memory, MLTR defect, MRM ambiguity, and CED evidence/risk quantities;
5. stochastic, approximate, continuous, infinite-state, delayed-control, or partial-observation analogues without new assumptions;
6. that every real ecological system has a coverage-complete admissible carrier;
7. that a structurally or evidentially more expensive repair is normatively or ecologically preferable.

These are boundaries, not missing pieces of the current finite theorem.

## 8. Manuscript synchronization required

The current Biology & Philosophy manuscript was drafted before the J1/J3/J6 synthesis had been fully propagated into the philosophy claim controls. It therefore still contains pre-J1 language denying or leaving open “joint minimality” without the needed qualifier.

That wording must be replaced by the following distinction:

- **forbidden:** “CREST finds one globally minimal ecological state independent of scientific contract”;
- **allowed/formal:** “on a declared admissible finite common carrier, CREST-J1 yields the unique coarsest state partition satisfying the four declared representational obligations”;
- **required boundary:** evidence may fail to identify that required state, and different contracts/carriers may yield different states.

Until this synchronization reaches the review manuscript and submission verifier, the philosophy manuscript should not be treated as final-submission ready.

## 9. Canonical one-sentence answer

> **A CREST ecological state is not an intrinsic label attached to nature; it is the block \([u]_J\) of the unique coarsest joint partition required by a declared admissible scientific contract, with a separate evidence gate determining whether that state can actually be reported.**
