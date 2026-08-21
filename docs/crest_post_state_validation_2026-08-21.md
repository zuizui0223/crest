# CREST post-state validation — 2026-08-21

> **Status:** validation/consolidation note. No new theorem. This note checks what remains after the state-existence trichotomy was fixed and distinguishes already-validated consequences from genuine open boundaries.

## 1. Validation target

The state-existence result is useful only if the resulting state is not an artefact of an arbitrary latent description, if contract strengthening behaves in the expected direction, and if carrier repair really reconnects the existence gate to the J1 state/evidence gates.

The post-state checks are therefore:

1. **representation invariance:** scientifically invisible latent duplication must not change the CREST quotient or licensing;
2. **contract monotonicity:** stronger declared obligations may refine the state, weaker obligations may coarsen it, but evidence changes must not be silently attributed to audit strength;
3. **repair-to-state closure:** a J4/J7 repair that restores an admissible carrier must actually feed a valid carrier into J1;
4. **repair does not imply observation:** restoring carrier/state existence must remain logically distinct from evidential licensing.

## 2. J2 — faithful representation invariance

Existing `test_crest_lift_invariance.py` already validates the strongest finite faithful-lift reading needed by the philosophy manuscript:

- every audit closure commutes with faithful pullback over all target partitions in the witness;
- redundant latent duplication preserves the joint quotient up to block isomorphism;
- two different faithful latent duplications reduce to the same joint state;
- full-state and target-only licensing are preserved;
- audit-visible duplication is rejected as non-faithful and can legitimately refine the state.

Therefore CREST does **not** identify state with the number of latent variables or worlds in a chosen representation. Under the J2 faithfulness premises, scientifically invisible descriptive duplication cannot create a new ecological state distinction.

Boundary: J2 does not prove invariance under arbitrary non-faithful redescriptions. If the added detail changes an audit-visible label, legal action, successor, evidence class, or target, refinement can be scientifically real.

## 3. J5 — one-sided contract changes

Existing `test_crest_lax_lift.py` validates the one-sided comparison boundary:

- a source with strictly stronger audit obligations can only refine the pulled-back target state;
- a weaker source can only coarsen it;
- faithful equality is recovered as the equality case of both bounds;
- target-only licensing is preserved under the exact evidence/target pullback premise;
- full-state licensing has only the theorem's corresponding one-sided implication;
- altered evidence is rejected rather than being misreported as an effect of audit strength.

Thus CREST's contract-relativity has a controlled order structure: changing the declared scientific burden in a known direction constrains how the required state can move. It does not permit arbitrary state changes under fixed comparison premises.

Boundary: J5 is not a theorem that every real change of scientific purpose can be globally ordered as stronger/weaker. It applies only when the declared one-sided projection premises hold.

## 4. J4/J7 repair-to-state closure

The carrier tests already proved that J4 and J7 repairs yield verified admissible kernels under their declared repair languages. The missing end-to-end check was whether the repaired J4 carrier can then be used as an actual J1 carrier rather than merely passing a local repair predicate.

`tests/test_crest_repair_to_joint_state.py` closes that validation gap for the universal J4 path:

- the unrepaired maximal J3 kernel is nonempty but coverage-incomplete, so no fully adequate state exists under the original full contract;
- the unique minimum J4 repair cuts one transition at cost 1 and restores an admissible coverage-complete carrier;
- J1 then constructs the required joint state on that repaired carrier;
- fine evidence licenses the full repaired state;
- coarse evidence leaves that same required state unresolved while the constant target remains reportable.

The controlled J7 path was already connected to J1/CED by `test_crest_repair_evidence_noncommutation.py` (O1): the cheapest structural repair can produce a valid J1 state that remains evidentially unresolved, while a more expensive repair is fully licensed.

Therefore the finite workflow is now validated in both universal and controlled forms:

```text
carrier no-go
  -> declared J4/J7 repair
  -> verified admissible carrier
  -> J1 required joint state
  -> independent evidence/target licensing gate
```

Repair restores a contract **only within the declared repair language**. It does not show that the repair is normatively best, ecologically true, or empirically identifiable.

## 5. What is now closed enough for the manuscript

The following manuscript-level interpretations are supported by analytic theorems plus executable regression checks:

- a fully adequate state may fail to exist under a declared synchronization/action/coverage contract;
- when an admissible common carrier exists, J1 gives the unique coarsest required joint state under its closure premises;
- faithful representational duplication does not change that state or its licensing status;
- one-sided strengthening/weakening constrains state refinement in the expected direction;
- a declared carrier repair can restore state existence;
- repaired state existence still does not imply evidential identification;
- target-only reporting can remain possible when the full state is unresolved.

These are finite, exact, contract-relative claims. None licenses a nature-given ontology or a universal empirical state variable.

## 6. Remaining genuine boundaries

Further theorem development is **not required for the current Biology & Philosophy submission**, but the following remain genuine research boundaries rather than validation defects:

- no theorem selects a nature-given common carrier, audit family, action-role assignment, target, evidence model, fallback, or repair cost scale;
- no invariance theorem covers arbitrary non-faithful changes of representation;
- no total ordering exists for arbitrary changes of scientific contract;
- J4/J7 repair languages are not proved exhaustive over every scientifically conceivable repair;
- no stochastic, continuous, infinite-state, approximate, partial-observation, or delayed-control generalization is established by the current finite results;
- the four audit axes are not proved philosophically exhaustive;
- empirical validity of any declared ecological contract remains application-specific.

The next manuscript action should therefore be **claim and presentation validation**, not new theorem proliferation.
