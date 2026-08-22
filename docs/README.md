# CREST documentation map

This directory contains more proof and development material than the main scientific narrative needs. Use this map to keep the repository readable.

## Canonical scientific spine

Read these first, in order.

1. [`trajectory_first_program_architecture_2026-08-22.md`](trajectory_first_program_architecture_2026-08-22.md)  
   Canonical program hierarchy: temporally extended worlds → snapshot sufficiency → structural obstructions → finite state → evidence licensing.

2. [`contract_relative_ecological_state_theory.md`](contract_relative_ecological_state_theory.md)  
   Canonical philosophical statement of ecological state as scientifically licensed compression of a temporally extended ecological world.

3. [`crest_mathematical_spine.md`](crest_mathematical_spine.md)  
   Minimal proved finite chain: carrier → joint state → evidence → cross-gate consequence.

4. [`crest_ecological_projection.md`](crest_ecological_projection.md)  
   Projection to open ecosystems, history, latent mechanisms, observation, quotient laws, monitoring, and representational stability.

5. [`../manuscript/crest_philosophy_biology_philosophy.md`](../manuscript/crest_philosophy_biology_philosophy.md)  
   Current trajectory-first Biology & Philosophy manuscript.

## Headline proof documents

These support the mathematical spine directly.

- [`crest_joint_state_theorem_2026-08-17.md`](crest_joint_state_theorem_2026-08-17.md) — J1 joint minimality and evidence gate.
- [`crest_action_expansion_cross_gate_theorem_2026-08-22.md`](crest_action_expansion_cross_gate_theorem_2026-08-22.md) — opposed carrier/state/evidence effects under action expansion.
- [`crest_monitoring_resolution_debt_2026-08-21.md`](crest_monitoring_resolution_debt_2026-08-21.md) — minimum evidence refinement and finite monitoring debt.
- `crest_maximal_common_lift_theorem_2026-08-17.md` — J3 universal carrier.
- [`crest_controlled_common_lift_theorem_2026-08-18.md`](crest_controlled_common_lift_theorem_2026-08-18.md) — J6 controlled carrier.
- [`crest_synthesis_proof_ledger_2026-08-17.md`](crest_synthesis_proof_ledger_2026-08-17.md) — complete theorem/proof ownership ledger.

The trajectory-first framing does not change the proof status of these finite results.

## Supporting mathematics

These remain active proofs but are not separate philosophical headlines.

### Lift comparison

- `crest_lift_invariance_theorem_2026-08-17.md` — J2 faithful-lift invariance.
- `crest_lax_lift_bounds_theorem_2026-08-18.md` — J5 one-sided lift bounds.

### Carrier repair and complexity

- `crest_minimum_common_lift_relaxation_theorem_2026-08-17.md` — J4 universal repair.
- `crest_minimum_controlled_lift_relaxation_theorem_2026-08-18.md` — J7 controlled repair.
- `crest_repair_complexity_boundary_2026-08-18.md` — NP-completeness boundary.
- `crest_repair_evidence_noncommutation_2026-08-18.md` — O1 structural-vs-licensed repair obstruction.

Their role is technical: protect the carrier/state/evidence separation and characterize repair when Gate A fails.

## Derived concepts — retained, not promoted

The following documents record useful derived terminology and finite corollaries. They are **not** separate main theorem families.

- [`crest_candidate_concepts_provability_map_2026-08-21.md`](crest_candidate_concepts_provability_map_2026-08-21.md)
- [`crest_ecological_state_adequacy_frontier_2026-08-21.md`](crest_ecological_state_adequacy_frontier_2026-08-21.md)

This layer includes:

- Monitoring Adequacy Envelope;
- Counterfactual Obsolescence;
- Ecological State Shadow;
- Decision-Safe Ignorance;
- frontier/regime bookkeeping.

Use these concepts when they clarify a result; do not let them replace the trajectory-first narrative.

## Literature and novelty audits

These establish claim boundaries rather than the scientific theory itself.

- [`trajectory_first_novelty_validation_audit_2026-08-22.md`](trajectory_first_novelty_validation_audit_2026-08-22.md) — **current novelty and remaining-validation authority after the trajectory-first reframe**.
- `crest_prior_art_review_protocol_and_evidence_matrix_2026-08-21.md`
- [`crest_broad_literature_audit_2026-08-21.md`](crest_broad_literature_audit_2026-08-21.md) — broad pre-reframe evidence base.
- [`crest_adequacy_frontier_prior_art_audit_2026-08-21.md`](crest_adequacy_frontier_prior_art_audit_2026-08-21.md)

Current safe positioning:

- dynamic/trajectory-sensitive ecosystem identity is not new;
- causal-state and predictive-state compression of history/futures is not new;
- purpose-relative adequacy is not new;
- task-specific state abstraction and partial observability are not new;
- adaptive monitoring and target-oriented experimental design are not new;
- generic representational obsolescence is not new;
- the candidate CREST contribution is the ecology-specific coupling of trajectory-level state responsibility, three structural insufficiency layers, carrier/state minimality, downstream evidence licensing, and strict cross-gate consequences.

## Validation status

The **finite theorem surface** is already strongly validated by analytic proofs, independent exhaustive oracles on small finite systems, multi-Python CI, and end-to-end carrier → repair → J1 → evidence tests. See [`crest_post_state_validation_2026-08-21.md`](crest_post_state_validation_2026-08-21.md).

The main remaining validation work is now **novelty and ecological grounding**, not another round of finite theorem enumeration:

1. close the PSR / causal-state / controlled-abstraction prior-art boundary;
2. refresh the claim-by-claim literature matrix under the trajectory-first framing;
3. decide whether snapshot sufficiency remains a criterion or receives a genuinely stronger theorem;
4. add at least one end-to-end ecology-grounded worked case;
5. only then consider a CREST-specific stochastic/trajectory extension.

Dated pre-J1 and pre-trajectory validation notes remain provenance, not current authority.

## Submission-control and historical development records

These are provenance/audit material, not entry points for the theory.

Examples include:

- submission audits and validation reports;
- pre-/post-J1 claim ledgers;
- state-hypothesis recovery notes;
- publication sequence decisions;
- earlier development/novelty-gate documents.

Keep them for traceability, but do not cite them as the canonical definition of CREST when a canonical spine document exists.

## Code ownership map

```text
crest/
  carrier.py             Gate A: universal carrier
  controlled_carrier.py  Gate A: controlled carrier
  joint_state.py          Gate B/C: joint state + evidence
  carrier_repair.py       supporting J4 repair
  controlled_repair.py    supporting J7 repair
  lift_invariance.py      supporting J2 comparison
  lift_bounds.py          supporting J5 comparison
```

The package should remain small. Single-axis CCOC/MLTR/MRM/CED algorithms belong in their companion repositories rather than being copied into CREST.

## Test ownership map

Headline regression tests should be read as executable witnesses, not substitutes for analytic proofs.

Core test groups:

- `test_crest_joint_state*.py` — J1 and finite oracle;
- `test_crest_common_lift.py`, `test_crest_controlled_lift.py`, `test_crest_carrier_oracles.py` — Gate A;
- `test_crest_action_expansion_cross_gate.py`, `test_crest_adequacy_frontier.py` — cross-gate witness;
- `test_crest_microdonta_channel_bridge.py` — ecological channel-identifiability witness;
- `test_crest_derived_frontier_concepts.py` — derived regime mathematics.

Repair/lift tests are supporting regression suites.

## Development stop rule

A new named result enters the canonical spine only if it does at least one of the following:

1. proves a new necessary-and-sufficient condition for ecological state adequacy beyond a definitional factorization;
2. proves a genuinely cross-gate impossibility/noncommutation;
3. proves a sharp lower/upper bound that depends essentially on the CREST contract architecture;
4. produces an empirical discrimination that cannot be reduced to ordinary adaptive monitoring, POMDP, PSR, or generic state abstraction.

Otherwise, extend an existing theorem, add a witness, or record the idea under future research rather than creating another headline concept.
