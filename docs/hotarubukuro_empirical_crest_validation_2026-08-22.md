# Hotarubukuro empirical CREST validation — 2026-08-22

> **Status:** cross-repository empirical replay on locked results from `zuizui0223/hotarubukuro` main SHA `661321107ed47468a48e3be32a3461ebb5ca99a5`. This is a CREST application to real observations and fitted ecological surfaces. It is **not** a re-estimation of the original models from raw data and does not create new causal claims.

## 1. Validation question

Can the current binary flower-colour snapshot

\[
X \in \{\text{white},\text{pigmented}\}
\]

serve as one adequate ecological state across the scientific responsibilities already present in the *Campanula punctata* analysis?

The source paper already separates three empirical tasks:

1. broad environmental differentiation of pigmentation state;
2. a local Bombus-facing mechanism hypothesis at sharp colour transitions;
3. a continuous isolation / human-context question within the geographical colour pattern.

CREST asks whether the same state compression is adequate for all three, and whether a distinction required by a target is actually identified by the available evidence.

The replay uses only locked source results:

- `reproducibility/broad_environment_spatial_final_2026-08-19.md`;
- `reproducibility/bombus_local_sharp_transition_current_results_2026-08-09.md`;
- `reproducibility/continuous_colour_isolation_human_context_result_2026-08-18.md`.

The machine-readable replay is `artifacts/hotarubukuro_empirical_crest_replay_2026-08-22.json`.

## 2. Present snapshot

The retained 1-km colour-cell geometry contains **1,305 cells**, of which **674 are pigmented and 631 white**. The snapshot state is deliberately minimal: whether a cell contains any pigmented record.

This binary state is scientifically useful. CREST does not begin by declaring the snapshot inadequate. It asks which declared tasks it can support without hiding a relevant distinction.

## 3. Contract A — broad environmental differentiation

The locked Broad analysis treats pigmentation state and conditional visible intensity as related but non-interchangeable responses.

For pigmentation state, the held-out environmental divergence associated with supported terms exceeded the cross-fitted space-only expectation:

\[
0.100608 - 0.048475 = 0.052133,
\qquad P=0.00998.
\]

For conditional intensity, the corresponding supported-term excess was not detected (`P = 0.26347`).

### CREST decision

For the broad question

> does pigmentation-state differentiation align with supported environmental differences beyond geographic continuity?

the binary pigmentation state is a meaningful scientific compression. The result also demonstrates why state and intensity cannot be silently merged into one universal colour coordinate: the two responses carry different broad-scale structure.

**Outcome:** the binary snapshot is **adequate/useful for this declared target**. CREST does not force additional state merely because more variables exist.

## 4. Contract B — local Bombus mechanism

At the strict 5-km pure-transition comparison, the locked source result found:

- 67 non-overlapping pairs;
- mean pigmented-minus-white focal Bombus support `+0.03590`;
- median `-0.00277`;
- proportion positive `0.493`;
- one-sided sign-flip `P = 0.02716`;
- BH `q = 0.08148` across the primary 5/10/25-km family.

The raw-support sensitivity was null at 5 km (`P = 0.26715`), and the signal attenuated at broader windows. The source interpretation therefore already treats this as weak local consistency rather than proof of pollinator-mediated selection.

### CREST decision

For the target

> is the present colour transition licensed to carry a deterministic pollinator-mediated mechanism label?

the answer is **no**.

The observed colour snapshot is compatible with more than one mechanism-level explanation, and the retained evidence does not collapse those alternatives to a unique response mechanism. CREST therefore routes this through MRM/CED as an ambiguity-explicit state rather than upgrading the binary colour state into a causal pollinator state.

**Outcome:** a pollinator-mediated selection state is **not identified**. Direct visitation, stigma contact, pollen transfer and fitness measurements are the missing discriminating channels named by the source analysis.

## 5. Contract C — human context within pigmented occurrences

The continuous-isolation analysis uses all 1,305 colour cells and avoids threshold-defined candidate events. After correcting same-colour isolation by local flower-cell spacing, the 5-km population relationships were:

\[
\rho_{pigmented}=0.285498,
\qquad
\rho_{white}=0.078506.
\]

For pigmented cells, the relative-isolation association exceeded the fitted natural-map expectation:

- all natural maps: upper-tail `P = 0.000900`;
- count-conditioned maps: upper-tail `P = 0.003996`.

By contrast, the direct relative pigmented-minus-white contrast did **not** clearly exceed natural geography (`P = 0.158584`). The locked source conclusion is therefore not a reciprocal colour displacement. It is a narrower **pigmented-specific human-context overlay**.

### CREST decision

For the target

> is the binary pigmentation snapshot sufficient to represent the human-context structure relevant to provenance follow-up?

the answer is **no**.

Within the single snapshot block `pigmented`, isolation relative to other pigmented cells carries additional, reproducible human-context structure beyond the fitted natural geography. The scientific representation for this target therefore needs at least a within-pigmented context axis; treating all pigmented cells as one interchangeable state would erase target-relevant variation.

This is a real-data failure of **universal** snapshot adequacy, but it does not imply that a new discrete provenance class has been discovered.

## 6. Evidence gate — required distinction is not identified provenance

The same source result explicitly limits the causal interpretation. It does **not** establish:

- horticultural origin;
- planting or escape;
- establishment mechanism;
- phenotypic plasticity;
- pollen movement or gene flow;
- causation by people.

CREST therefore separates two outputs:

\[
\boxed{
\text{within-pigmented context distinction is required for the target}
}
\]

from

\[
\boxed{
\text{human/provenance causal state is identified}
}
\]

which is false under the current evidence.

The narrower target remains reportable: pigmented occurrences show an excess positive isolation–population relationship relative to the fitted natural colour geography, including after local sampling-density correction.

This is exactly the CREST separation

\[
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}.
\]

## 7. What changed scientifically after the CREST audit

A snapshot-only interpretation could easily overcompress the system into `white` versus `pigmented` and then seek one explanatory rule for that binary variable. The empirical CREST audit returns a different object:

| Scientific responsibility | Is binary colour state adequate? | Licensed output |
|---|---|---|
| broad environment-vs-space differentiation | **yes, for the stated target** | pigmentation-state differentiation contains supported environmental structure beyond space |
| local Bombus mechanism | **not as a deterministic causal state** | weak local consistency; mechanism remains unresolved |
| human-context / provenance-facing structure | **no** | retain a within-pigmented isolation/context distinction, but report only a human-context overlay |

The gain is therefore not a better classifier score. It is a stricter allocation of scientific claims to the state representation that can support them.

## 8. Validation verdict

This real-data application supports three CREST claims without adding a new theorem:

1. **State adequacy is target-relative in a nontrivial ecological analysis.** The same binary snapshot is adequate for one paper-level question and insufficient for another.
2. **Mechanism uncertainty and representational refinement are different problems.** The human-context result requires additional within-state structure while the Bombus mechanism remains unresolved.
3. **Required representation and licensed causal interpretation separate empirically.** The data justify a human-context overlay but not a provenance/causal state.

The result therefore advances CREST beyond a purely toy or relabelled application: one real ecological dataset already contains a case where a useful snapshot state survives one contract, fails another, and cannot be promoted to a deterministic mechanism state under the current evidence.

## 9. Claim ceiling

This document is a replay of frozen source conclusions, not a new causal analysis. It must not be used to claim that CREST has been benchmarked against alternative state-learning algorithms, that a discrete natural-versus-human provenance state has been inferred, or that pollinator-mediated selection has been demonstrated.

The next empirical escalation, if needed, is not another abstract theorem. It is a discriminating observation layer: provenance/genetic evidence for the human-context branch and direct pollination/fitness evidence for the Bombus branch.
