# CREST broad literature audit — 2026-08-21

> **Status:** broad cross-domain prior-art audit. This is substantially wider than the earlier targeted novelty screen, but it is **not a formal systematic review**: no Scopus/Web of Science export, PRISMA-style deduplication, exhaustive backward/forward citation screening, or preregistered inclusion criteria were performed. Negative search results therefore do not establish historical firstness.

## 1. Question

The audit asks whether the current CREST program, especially the Ecological State Adequacy Frontier and the derived concepts (Monitoring Adequacy Envelope, Counterfactual Obsolescence, State Shadow, Decision-Safe Ignorance, Monitoring Resolution Debt), duplicates established work.

Search strata covered:

1. ecological state, ecosystem identity, resilience, alternative stable states, State-and-Transition Models;
2. ecological model adequacy, coarse graining, state-variable selection;
3. model transferability and novel conditions;
4. conservation POMDPs, hidden state, state aggregation, adaptive management;
5. adaptive monitoring, monitoring redesign, value of information;
6. RL/AI state abstraction, bisimulation, causal abstraction, predictive-state compression;
7. representation learning and information-bottleneck phase transitions;
8. general philosophy of scientific representation and adequacy-for-purpose;
9. recent formal representation-adequacy, carrier, certification, obsolescence, and repair work;
10. exact phrase/near-phrase searches around monitoring adequacy, state shadow, information debt, counterfactual obsolescence, anticipatory state, and action-repertoire information burden.

## 2. Strong prior art — broad claims that CREST must not make

### 2.1 Ecological state and identity are established topics

- Delettre (2021), *Identity of ecological systems and the meaning of resilience*, explicitly treats state identity as an equivalence relation and separates local/global state identity from other forms of ecological identity.
- Boit & Spencer (2019), *Equivalence and dissimilarity of ecosystem states*, directly proposes an equivalence criterion for ecosystem states based on proportional population growth rates.
- State-and-Transition Model literature already treats ecological states through dynamics, thresholds, management-induced transitions, and intervention.

**Blocked claim:** CREST is the first theory to define ecological state equivalence or to make ecological states intervention-sensitive.

### 2.2 Purpose-relative adequacy is established

- Getz et al. (2018), *Making ecological models adequate*, explicitly links ecological model adequacy to state/control-variable choice, data determinacy, validation, sensitivity, coarse graining, prediction, and management.
- Parker (2020) and Bokulich & Parker (2021) establish adequacy-for-purpose and context-sensitive representation in philosophy of science.
- Parker et al. (2026), *An adequacy-for-purpose perspective for the environmental sciences*, explicitly imports this view into environmental science.

**Blocked claim:** CREST discovered that ecological representations are purpose- or context-relative.

### 2.3 Task-specific minimal states and management-relevant discretization are established

- Nicol & Chadès (2012), *Which States Matter?*, constructs a compact state discretization in conservation POMDPs by keeping states needed to preserve the management policy and explicitly studies the monitoring-versus-management tradeoff.
- RL/bisimulation/state-abstraction literature already develops minimal task-specific or action-preserving abstractions; Wang et al. (2024), *Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning*, is a recent explicit example.

**Blocked claim:** CREST is the first task-relevant minimal state abstraction or the first to connect management actions to state resolution.

### 2.4 Monitoring is already understood as adaptive to changing questions and management

- Ringold et al. (1996) and subsequent ecosystem-management literature explicitly argue for adaptive monitoring design.
- Lindenmayer & Likens (2009, 2011) make changing questions and new information central to adaptive monitoring; existing monitoring programs may be redesigned when policy/scientific questions change.
- Recent work continues to link monitoring types, critical uncertainty, adaptive management, and adjustment of monitoring investment.
- Value-of-information work in adaptive resource management already formalizes when additional information is worth acquiring for management.

**Blocked claim:** CREST is the first to say monitoring should change when scientific or management questions change.

### 2.5 Model transferability and novel conditions are established

- Yates et al. (2018), *Outstanding Challenges in the Transferability of Ecological Models*, reviews model transfer under novel conditions, nonstationarity, changed interactions, data bias, and uncertainty.
- Dumandan et al. (2024) empirically demonstrates loss of ecological forecast transferability under novel biotic conditions.

**Blocked claim:** CREST/MLTR discovered that an ecological state/model can fail when moved to new ecological conditions.

### 2.6 Representation phase transitions are established outside ecology

- Wu & Fischer (2020), *Phase Transitions for the Information Bottleneck in Representation Learning*, gives a formal theory of abrupt changes in representation as the compression/prediction objective changes.

**Blocked claim:** abrupt representational transitions per se are new.

## 3. Closest recent formal competitor: Swanson 2026

David T. Swanson, *Carriers and Adequacy for Purpose: A Formal Framework for Representation-Constrained Adequacy* (PhilArchive/PhilPapers manuscript, archived May 2026), is the closest item found in this broad audit.

It already formalizes:

- bounded operational representations called **carriers**;
- a refinement/post-processing preorder;
- purpose-relative adequacy via induced task loss;
- monotonicity of adequacy under refinement;
- minimal adequate carriers;
- task-indexed residue diagnostics;
- regime-dependent changes in adequacy/minimality;
- **representational obsolescence**;
- a revision/repair layer.

This materially lowers the safe novelty ceiling for the CREST philosophy paper.

**Consequences for current CREST vocabulary:**

- `Monitoring Adequacy Envelope` should be presented as a CREST/ecology specialization of monotone adequacy structure, not as a historically first adequacy region.
- `Counterfactual Obsolescence` cannot be sold as the first formal representational-obsolescence concept.
- `State Shadow` is mathematically a finite common refinement over contemplated states; the underlying construction is classical.
- `Monitoring Resolution Debt` is an exact CREST-derived resolution quantity, but the common-refinement/minimal-sufficiency substrate is not novel.

Swanson's carrier is a bounded rendering of histories, whereas CREST's J3/J6 carrier is a synchronized latent-world domain on which multiple ecological contracts can jointly live. The word `carrier` therefore names different mathematical objects, but the philosophical adequacy neighborhood is close.

## 4. What remains distinctive after the broader audit

The broad audit did **not** identify a published or preprint framework that matches the full current CREST architecture:

1. one coarse ecological state equivalence is constrained by four separately owned obligations — future sufficiency, inherited-semantic coherence, retained-mechanism robustness, and evidence/target licensing;
2. these obligations are synchronized only after an explicit **common-carrier existence gate** (J3/J6), with typed no-go certificates;
3. conditional on an admissible carrier, J1 gives a unique coarsest joint state;
4. mathematical state existence, evidence identification, and target reportability are explicitly separated;
5. structural repair and evidential licensing can have different optima (O1);
6. the management-enrichment witness jointly realizes
   \[
   \text{viability}\uparrow,\quad
   \text{required state resolution}\uparrow,\quad
   \text{full-state identifiability}\downarrow,
   \]
   while target-only reporting remains intact;
7. R1 gives the unique minimum evidence refinement `E ∨ J` needed to recover full-state identification and quantifies its finite resolution increase;
8. the CCOC extremal family then implies arbitrary finite-family growth of this exact monitoring-resolution debt from one newly relevant future action.

The strongest remaining contribution is therefore **not any one generic concept**. It is the ecology-specific coupling and cross-gate separation/interaction among representation, viable carrier, future/action responsibility, mechanism uncertainty, evidence, and target reporting.

## 5. Revised novelty hierarchy

### Tier 0 — established substrate; do not claim novelty

- purpose-relative adequacy;
- ecological state identity/equivalence;
- state-and-transition models;
- task-specific state abstraction;
- POMDP hidden-state management;
- adaptive monitoring;
- value of information;
- causal abstraction/bisimulation/predictive states;
- common refinement / partition joins;
- monotonicity under refinement;
- generic representational obsolescence;
- generic representation phase transitions.

### Tier 1 — exact CREST-derived concepts, useful but not priority claims

- Monitoring Adequacy Envelope;
- Counterfactual Obsolescence exact pair criterion;
- State Shadow / anticipatory common state;
- Decision-Safe Ignorance;
- Monitoring Resolution Debt.

These are valuable because they make the CREST architecture operational and testable, not because their order-theoretic mathematics is new.

### Tier 2 — strongest candidate scientific contribution

- the **four-contract ecological state-equivalence architecture**;
- explicit carrier-existence-before-state construction;
- state existence vs state identification vs target reportability separation;
- noncommutation between structural repair and evidential licensing;
- the management-enrichment cross-gate phenomenon and its exact state-debt/target-debt characterization;
- unbounded one-action monitoring-resolution debt inherited from the CCOC extremal family.

Historical firstness remains unproved.

## 6. Publication consequence

The manuscript should be written to survive the strongest prior-art reading:

> CREST is not a new general theory of adequacy, state abstraction, monitoring adaptation, or representational obsolescence. It is a theorem-grounded philosophy of **ecological state-equivalence adequacy** that couples four distinct obligations and exposes cross-gate phenomena that disappear when state representation, management viability, mechanism uncertainty, and evidence are treated separately.

The most defensible headline is therefore a **specific architecture + specific counterexample/theorem coupling**, not a new vocabulary claim.

## 7. What remains to call this a systematic review

A true systematic prior-art review would still require:

1. database-level searches in Web of Science/Scopus (and ideally PhilPapers/PhilArchive, Google Scholar, Crossref/Semantic Scholar);
2. fixed search strings and date ranges;
3. deduplication and inclusion/exclusion criteria;
4. backward and forward citation chasing from the closest anchors (especially Swanson 2026, Getz 2018, Nicol & Chadès 2012, Delettre 2021, Boit & Spencer 2019, Yates 2018, adaptive-monitoring reviews);
5. explicit screening of papers using state aggregation/lumpability/bisimulation in ecological decision models;
6. a final claim-by-claim evidence table.

Until that is done, the correct wording is **broad literature audit**, not exhaustive systematic review.
