# CREST post-state validation — 2026-08-21

> **Status:** validation/consolidation complete for the current finite theorem surface. No new theorem. This note distinguishes validated manuscript claims from genuine research boundaries that are intentionally left open.

## 1. Validation target

The state-existence result is useful only if the resulting state is not an artefact of an arbitrary latent description, if contract strengthening behaves in the expected direction, if the carrier gates really return greatest admissible kernels, and if carrier repair reconnects the existence gate to the J1 state/evidence gates without silently granting observational knowledge.

The post-state checks are therefore:

1. **representation invariance:** scientifically invisible latent duplication must not change the CREST quotient or licensing;
2. **contract monotonicity:** stronger declared obligations may refine the state, weaker obligations may coarsen it, but evidence changes must not be silently attributed to audit strength;
3. **carrier oracle:** J3/J6 must agree with independent exhaustive subset search on small finite problems;
4. **joint-state oracle:** J1 must agree with an independent exhaustive partition search on small finite contracts;
5. **repair-to-state closure:** a J4/J7 repair that restores an admissible carrier must feed a valid carrier into J1;
6. **repair does not imply observation:** restoring carrier/state existence must remain logically distinct from evidential licensing;
7. **manuscript boundary:** Abstract, joint-state section, Limits, and Conclusion must state conditional rather than intrinsic/global state claims.

## 2. J2 — faithful representation invariance

`test_crest_lift_invariance.py` validates the finite faithful-lift reading needed by the philosophy manuscript:

- every audit closure commutes with faithful pullback over all target partitions in the witness;
- redundant latent duplication preserves the joint quotient up to block isomorphism;
- two different faithful latent duplications reduce to the same joint state;
- full-state and target-only licensing are preserved;
- audit-visible duplication is rejected as non-faithful and can legitimately refine the state.

Therefore CREST does **not** identify state with the number of latent variables or worlds in a chosen representation. Under the J2 faithfulness premises, scientifically invisible descriptive duplication cannot create a new ecological state distinction.

Boundary: J2 does not prove invariance under arbitrary non-faithful redescriptions. If added detail changes an audit-visible label, legal action, successor, evidence class, or target, refinement can be scientifically real.

## 3. J5 — one-sided contract changes

`test_crest_lax_lift.py` validates the one-sided comparison boundary:

- a source with strictly stronger audit obligations can only refine the pulled-back target state;
- a weaker source can only coarsen it;
- faithful equality is recovered as the equality case of both bounds;
- target-only licensing is preserved under the exact evidence/target pullback premise;
- full-state licensing has only the theorem's corresponding one-sided implication;
- altered evidence is rejected rather than being misreported as an effect of audit strength.

Thus CREST's contract-relativity has a controlled order structure: changing the declared scientific burden in a known direction constrains how the required state can move. It does not permit arbitrary state changes under fixed comparison premises.

Boundary: J5 is not a theorem that every real change of scientific purpose can be globally ordered as stronger/weaker. It applies only when the declared one-sided projection premises hold.

## 4. Independent Gate-A oracle — J3/J6

PR #10 adds `tests/test_crest_carrier_oracles.py`.

For **128 deterministic small problems per gate** (1–4 worlds), the test enumerates every ambient subset and independently checks:

- universal compatible transition closure for J3;
- robust controlled invariance for J6;
- the greatest kernel obtained as the union of all valid subsets;
- existence, coverage completeness, and admissibility;
- J3 finite elimination chains;
- J6 safe policy containment and finite no-go certificates.

The oracle carriers agree with `maximal_common_lift` and `maximal_controlled_common_lift` across the tested cases. The full CREST matrix passed on Python 3.10, 3.11, and 3.12.

This broadens the executable support for the statement that Gate A is an actual greatest-carrier/no-go test, not merely a property of one hand-built witness.

## 5. Independent J1 oracle

PR #9 adds `tests/test_crest_joint_state_oracle.py`.

For **96 deterministic small contracts** (1–4 worlds), the test:

- generates four audit contracts with varying static distinctions, legal-action rows, and successors;
- enumerates every partition of the carrier;
- evaluates audit fixed-point validity directly from labels, legality, and successor blocks without calling `AuditRefinement.close`;
- independently selects the unique coarsest common fixed point above the baseline;
- compares the oracle partition with `solve_joint_crest_state`;
- repeats with reversed audit order;
- independently checks full-state and target-only evidence licensing.

All tested contracts matched the J1 solver and the full Python matrix passed. This is regression support for the implementation; the quantified existence/minimality result remains the analytic J1 proof.

## 6. J4/J7 repair-to-state closure

The carrier tests already prove that J4 and J7 repairs yield verified admissible kernels under their declared repair languages. PR #8 adds the previously missing universal end-to-end check `tests/test_crest_repair_to_joint_state.py`:

- the unrepaired maximal J3 kernel is nonempty but coverage-incomplete, so no fully adequate state exists under the original full contract;
- the unique minimum J4 repair cuts one transition at cost 1 and restores an admissible coverage-complete carrier;
- J1 then constructs the required joint state on that repaired carrier;
- fine evidence licenses the full repaired state;
- coarse evidence leaves the same required state unresolved while the constant target remains reportable.

The controlled J7 path was already connected to J1/CED by `test_crest_repair_evidence_noncommutation.py` (O1): the cheapest structural repair can produce a valid J1 state that remains evidentially unresolved, while a more expensive repair is fully licensed.

Therefore the finite workflow is validated in both universal and controlled forms:

```text
carrier no-go
  -> declared J4/J7 repair
  -> verified admissible carrier
  -> J1 required joint state
  -> independent evidence/target licensing gate
```

Repair restores a contract **only within the declared repair language**. It does not show that the repair is normatively best, ecologically true, or empirically identifiable.

## 7. Manuscript claim/presentation audit

The current Biology & Philosophy manuscript was checked against the recovered theorem boundaries after the oracle and repair validations.

The manuscript now consistently states that:

- the four audits are constraints on one proposed state, not four rival state definitions;
- J1 supplies conditional unique coarseness only after an admissible finite common carrier is fixed;
- J3/J6 carrier failure means no **fully adequate state under the declared contract**, not that no mathematical partition can be written at all;
- `State_C(u) = [u]_J` is a required representational state, not automatically an observation;
- full-state reporting is separately licensed by the evidence gate;
- different carriers/contracts/targets may yield different states;
- carrier repair is contract-relative and not a claim of normative or ecological optimality;
- the framework does not claim exhaustiveness, an intrinsic state of nature, or a universal stochastic/continuous theory.

The automated submission verifier remains green and rejects the stale pre-J1 blanket wording that treated conditional joint minimality as wholly open.

## 8. What is now closed enough for the manuscript

The following interpretations are supported by analytic theorems plus executable regression checks:

- a fully adequate state may fail to exist under a declared synchronization/action/coverage contract;
- the carrier/no-go decision is backed by greatest-kernel proofs and independent finite subset oracles;
- when an admissible common carrier exists, J1 gives the unique coarsest required joint state under its closure premises;
- the J1 solver agrees with independent exhaustive partition oracles on the tested small contracts;
- faithful representational duplication does not change that state or its licensing status;
- one-sided strengthening/weakening constrains state refinement in the expected direction;
- a declared carrier repair can restore state existence;
- repaired state existence still does not imply evidential identification;
- target-only reporting can remain possible when the full state is unresolved.

These are finite, exact, contract-relative claims. None licenses a nature-given ontology or a universal empirical state variable.

## 9. Remaining genuine boundaries — not submission blockers

The following are intentionally **not** converted into new theorem work for the current manuscript:

- no theorem selects a nature-given common carrier, audit family, action-role assignment, target, evidence model, fallback, or repair cost scale;
- no invariance theorem covers arbitrary non-faithful changes of representation;
- no total ordering exists for arbitrary changes of scientific contract;
- J4/J7 repair languages are not proved exhaustive over every scientifically conceivable repair;
- no stochastic, continuous, infinite-state, approximate, partial-observation, or delayed-control generalization is established by the current finite results;
- the four audit axes are not proved philosophically exhaustive;
- empirical validity of any declared ecological contract remains application-specific.

These are **future research boundaries, not unresolved validation defects** in the finite claims used by the Biology & Philosophy manuscript.

## 10. Validation stop rule

No further theorem-family or synthetic-witness expansion is justified for submission readiness. The remaining work is journal presentation and human responsibility review: final Table 1/typesetting, author metadata/declarations, source-and-claim read-through, AI-disclosure approval after that review, policy recheck, and one immutable replay on the exact upload candidate.
