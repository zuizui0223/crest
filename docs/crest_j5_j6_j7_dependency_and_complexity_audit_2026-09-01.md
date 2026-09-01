# CREST J5/J6/J7 dependency and complexity audit — 2026-09-01

## Purpose

This note prevents an incorrect linearization of the mature CREST theorem program. J5, J6, and J7 are all proved results, but the valid dependency structure is not `J5 -> J6 -> J7`.

## Actual dependencies

### J5 — one-sided lift-refinement bounds

J5 compares already-declared joint CREST contracts under a one-sided source-to-target projection. With exact evidence/target pullback and commuting shared actions, a stronger source can only refine the pulled target state and a weaker source can only coarsen it. J2 is the equality case.

J5 is therefore a **comparison theorem**. It does not construct the controlled carrier used by J6 and is not a premise of the J7 repair characterization.

Executable evidence: `tests/test_crest_lax_lift.py` checks both directions, the faithful equality case, action-commutation failure, action-inclusion direction, and the evidence-pullback firewall.

### J6 — maximal controlled common carrier

J6 is the controlled carrier theorem. Its descending AND/OR viability operator returns the unique greatest compatible controlled-invariant carrier, a memoryless safe selector when nonempty, coverage status, and finite typed elimination certificates.

Executable evidence: `tests/test_crest_carrier_oracles.py` compares J6 against exhaustive subset enumeration over 128 small random finite problems, while `tests/test_crest_controlled_lift.py` checks theorem-facing witnesses and certificates.

### J7 — exact repair calculus for J6

J7 begins only after the J6 language has been declared. For each retained subset, the enabling, uncontrollable-edge cuts, fallback installations, and coverage waivers are forced; the global optimum is the minimum fixed-witness cost across repair-feasible nonempty subsets.

Thus the relevant structural chain is

```text
controlled synchronization contract
    -> J6 maximal controlled carrier / typed no-go
    -> J7 fixed-witness necessary-and-sufficient repair cost
    -> global subset selection
```

J5 can compare state contracts before or after this carrier layer when its projection assumptions are met, but it is a parallel comparison result rather than a predecessor of J6/J7.

## NP-completeness boundary

The J7-REPAIR decision problem is in NP because a retained subset plus its forced repair operations is a polynomial-size certificate whose cost and repaired controlled-carrier validity can be checked in polynomial time for the finite explicit input.

Weighted set cover reduces to J7-REPAIR using the restricted language already recorded in the analytic proof:

- no uncontrollable transitions;
- one controllable self-loop per world;
- no fallback installation;
- one binary coverage component per universe element;
- admitting world `i` has the corresponding set cost;
- coverage-waiver costs exceed the total cost of admitting all candidate sets.

Under this construction a repair of cost at most `B` exists exactly when the weighted set-cover instance has a cover of cost at most `B`. Hence J7-REPAIR is NP-hard; together with NP membership it is NP-complete.

The original regression `tests/test_crest_repair_set_cover_reduction.py` checks one explicit weighted-set-cover witness. `tests/test_crest_j7_set_cover_oracle_family.py` strengthens the executable layer by comparing the J7 solver with an independent brute-force weighted-set-cover oracle over a deterministic family of small coverable instances and by checking that the reduction remains inside the restricted theorem language.

## Claim boundary

This complexity result is not claimed as a new generic complexity theorem for set cover, model repair, or safety games. Its role is narrower: it identifies where CREST's declared carrier-repair optimization becomes computationally hard even after the J6 viability machinery has been reduced to trivial self-loops. The hardness is therefore attributable to global coverage selection, not to hidden safety-game complexity.

## Submission consequence

For the Biology & Philosophy manuscript, the J-series remains supporting formal infrastructure and should not displace the conservation-capacity / conservation-knowledge thesis. For a possible Philosophy of Science or technical companion treatment, the correct formal story is the branched dependency above, not a fictitious `J5 -> J6 -> J7` theorem chain.
