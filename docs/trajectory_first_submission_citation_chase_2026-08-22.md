# CREST trajectory-first submission citation chase — 2026-08-22

> **Status:** final conservative nearest-neighbour chase for the trajectory-first manuscript. This is not a database-complete systematic review and does not establish historical firstness. It records the closest primary/authoritative sources that materially constrain manuscript claims.

## 1. Predictive state — direct boundary

### Littman, Sutton & Singh (NIPS 2001 / NIPS 14)

Primary proceedings abstract states that dynamical-system states can be represented by **multi-step, action-conditional predictions of future observations** and compares this representation directly with POMDP states.

**CREST consequence:** future actions/tests defining predictive state is prior art. No novelty claim is allowed for that principle.

### Singh, James & Rudary (UAI 2004)

PSR theory represents state by predictions of observable outcomes of experiments/tests that can be performed on the system and formalizes histories × future tests through the system-dynamics matrix.

**CREST consequence:** the trajectory-first `history + future-response` language must be positioned as continuous with PSR, not as a new state ontology.

### Computational mechanics

Shalizi & Crutchfield show that causal-state representations based on predictive equivalence are minimal representations consistent with accurate prediction.

**CREST consequence:** state as a predictive equivalence class / minimal sufficient predictive compression is not novel.

## 2. Task-specific and management-specific state

### Nicol & Chadès (2012)

The conservation POMDP example discretizes a continuous state space using only states necessary to maintain an optimal management policy and explicitly analyzes monitoring versus management allocation.

**CREST consequence:** “which states matter for management?” and management-relative compression are established ecological decision-theory ideas.

### Reward-predictive state abstractions

Later reinforcement-learning work shows state abstractions chosen to predict future reward sequences and studies their reuse across tasks with changing transition and reward functions.

**CREST/MLTR consequence:** portability/generalization of predictive abstractions across changed tasks is also prior art. MLTR must retain its narrower claim: one inherited classification is fixed, transported through a declared source–target relation, and any repair is constrained to preserve carried source semantics.

### Walsh, Li & Littman (2006)

This work explicitly treats **transferring state abstractions between MDPs**.

**CREST/MLTR consequence:** abstraction transfer itself is not novel; source-relative carried-label exact repair/history constraints remain the defensible MLTR boundary.

## 3. Structural + observational uncertainty

Ecological adaptive-management/POMDP work already combines structural uncertainty over alternative process models with observational uncertainty about current state. Fackler & Pacifici (2014) is an especially close ecology-facing anchor.

**CREST/MRM/CED consequence:** merely combining mechanism/model uncertainty with partial observation is not novel. CREST's safe claim is the explicit decomposition into response-relevant mechanism requirement and a separate evidence-licensing gate, plus the finite cross-gate witness.

## 4. Target-oriented evidence design

Goal-/prediction-oriented OED literature explicitly chooses experiments to reduce uncertainty in a prediction or quantity of interest rather than in the full parameter/state vector.

**CREST/CED consequence:** target-specific monitoring or “learn only what matters for the target” is not novel. CED's contribution must remain the combined finite reportability interface: evidence classes, sharp ambiguity, target/action-stable required resolution, failure-aware licensing, and false-resolution/risk-limited reporting.

## 5. Adequacy and representation change

Existing adequacy-for-purpose work already makes representation/model adequacy purpose-relative. Swanson (2026) further formalizes minimal adequate carriers, regime-sensitive adequacy, representational obsolescence, and repair.

**CREST consequence:** contract relativity, minimal adequate representation, and obsolescence are not headline novelties.

## 6. Claims that survive this chase

The chase does not identify one nearest neighbour that already packages the current CREST structure as the same scientific object:

1. typed future/composition insufficiency (CCOC);
2. inherited-semantic/history portability constraint (MLTR);
3. response-relevant retained-mechanism insufficiency (MRM);
4. explicit common-carrier feasibility/no-go before joint state construction;
5. finite conditional joint minimality on that carrier;
6. downstream evidence licensing (CED);
7. explicit required-state vs identified-state vs reportable-target separation;
8. strict action-expansion witness with carrier ↑, required resolution ↑, full-state identifiability ↓, target reportability preserved;
9. repair/evidence noncommutation O1.

This is **not evidence of historical firstness**. It is the residual claim set that survived the nearest-neighbour review.

## 7. Submission-safe wording

> Predictive states, action-conditioned future-test representations, task-specific abstraction, abstraction transfer, structural/observational uncertainty, target-oriented experiment design, and adequacy-for-purpose are all established. CREST contributes an ecology-specific state-adequacy architecture that makes future/composition, inherited semantics, retained mechanisms, carrier feasibility, evidence identification, and reportability separately auditable and derives finite cross-gate consequences from their coupling.

## 8. Final literature stop rule

For the current Biology & Philosophy submission, additional broad keyword searching should not trigger theorem expansion. Further literature work is justified only when:

- a reviewer-visible headline lacks a direct nearest-neighbour citation;
- backward/forward chasing uncovers a source that already proves the same cross-gate coupling; or
- a cited source changes the safe wording above.

Otherwise the active risk has shifted from conceptual prior-art discovery to final source verification, prose accuracy, and ecological generality.