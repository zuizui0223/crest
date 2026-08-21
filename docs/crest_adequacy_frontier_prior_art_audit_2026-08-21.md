# CREST adequacy-frontier prior-art audit — 2026-08-21

> **Status:** targeted novelty audit for the Ecological State Adequacy Frontier (ESAF) and the management-induced information-debt witness. This is not a systematic review and does not authorize historical-firstness language.

## 1. Candidate claim under review

The claim being tested is not merely that ecological states are purpose-relative, partially observed, or task-specific.

The stronger CREST candidate is:

> **Changing a declared ecological action/future contract can move a system across distinct state-adequacy regimes: it can change the maximal viable carrier, the least-information state required for the scientific task, and whether fixed evidence can identify that state. In particular, one added controllable management action can enlarge the viable carrier while increasing the required state resolution beyond existing monitoring, even though a declared target remains reportable.**

This is the proposed ecological state-adequacy frontier / management-induced information-debt claim.

---

## 2. Existing ideas that block broader novelty claims

### 2.1 Adequacy-for-purpose is established

Parker's adequacy-for-purpose account evaluates scientific models relative to purpose and context. Parker, Carey, Olsson & Thomas (2026) explicitly carry this perspective into environmental science.

**Consequence for CREST:** do not claim novelty for `ecological state is purpose-relative` or `model adequacy depends on context`.

### 2.2 Task-specific minimal state abstraction is established

Reinforcement-learning and causal-abstraction work derives minimal/task-specific abstractions that preserve reward, value, dynamics, or planning-relevant information; Wang et al. (2024) is a recent explicit example.

**Consequence for CREST:** do not claim novelty for existence of minimal sufficient task abstractions or partition refinement itself.

### 2.3 Representation phase transitions are established

Information-bottleneck theory explicitly studies abrupt changes in representation complexity as the compression/prediction objective varies (e.g. Wu & Fischer 2020).

**Consequence for CREST:** `representational tipping point` can be ecological interpretive language, but not a generic mathematical priority claim.

### 2.4 Local-to-global coherence and ecological sheaves are no longer empty territory

Sheaf theory is a standard language for locally consistent assignments that may fail to admit a global section. Recent 2026 work applies this idea directly to microbial ecological communities and global metabolic coherence.

**Consequence for CREST:** do not lead with `ecological contextuality` or `local states fail to glue globally` as a firstness claim.

### 2.5 Partial observability and control-information coupling are established

POMDPs, active sensing, and dual control distinguish hidden state from belief/observation and allow actions to affect information acquisition or future estimation quality.

**Consequence for CREST:** do not claim novelty for hidden ecological state, belief-state reasoning, or the idea that management and learning can interact.

---

## 3. Ecology already recognizes management-dependent monitoring, but usually operationally

Ecological adaptive-management and monitoring literature explicitly links monitoring design to management objectives and available interventions.

Examples found in this pass include:

- monitoring frameworks that revise design when new management options become available;
- state-and-transition models in restoration, where the appropriate level of state detail depends on model purpose and available resources;
- targeted monitoring that selects a small set of variables sufficient to distinguish management-relevant vegetation states;
- ecosystem-based management frameworks in which management objectives, indicators, monitoring strategy, and action rules are co-designed.

These works strongly motivate the CREST problem but do not, in the sources reviewed here, supply the same exact order-theoretic decomposition into:

1. maximal admissible carrier;
2. unique coarsest required state;
3. evidence-compatible state set / target report;
4. action-repertoire changes that can move the system across those gates.

---

## 4. What appears to survive the targeted search

### 4.1 The three-object frontier

The combination

\[
\mathcal C\mapsto
\bigl(U^*_{\mathcal C}\text{ or }K^*_{\mathcal C},\;J_{\mathcal C},\;\mathcal S_{\mathcal C}(e)\bigr)
\]

has a different target from standard task abstraction, model adequacy, or state estimation.

It asks simultaneously:

- which worlds can coherently remain in the declared scientific problem;
- what is the least-information state required on those worlds;
- what subset of those states is still compatible with the evidence.

The safe contribution claim is the **coupling and separation of these three gates**, not any one underlying algorithm.

### 4.2 One-way epistemic frontier under fixed evidence

Along an order-compatible chain in which required state partitions become finer while evidence is held fixed, once full-state identification fails it cannot be restored by further state refinement alone.

This is mathematically elementary, but it gives an ecological boundary that differs from generic `more data / less data` language: **scientific requirements can outrun a fixed monitoring programme even without deterioration in the data themselves**.

### 4.3 Atomic future-contract sensitivity

CCOC already proves an exact family where opening one primitive action increases the required exact state memory by an arbitrary \(m\) bits.

The novelty-safe interpretation is not `representations can have phase transitions`, but:

> **one small edit to the ecological future/action contract can make a previously adequate state variable arbitrarily under-resolved across a finite family.**

### 4.4 Management-induced information debt — strongest current candidate

The new CREST finite witness adds one controllable action and verifies all of the following simultaneously:

1. the J6 maximal viable carrier expands;
2. the J1 required state count increases;
3. the previously adequate fixed evidence no longer identifies the full state;
4. the declared target remains reportable.

This differs from classical dual control in logical direction. Dual control asks how **executing** an action can change future information. The CREST witness asks how **making an action available as part of the scientific/management contract** changes what state information is required before that action is used.

No directly matching result was found in the targeted searches across state abstraction, dual control/POMDP, ecological monitoring, and adaptive management.

**Safe wording:** `CREST formalizes a management-induced information-debt phenomenon.`

**Unsafe wording without a systematic review:** `CREST is the first theory to discover management-induced information debt.`

---

## 5. Strong ecological implication

The most distinctive applied implication is:

> **Monitoring can become scientifically obsolete before the ecosystem changes physically.**

A monitoring programme may have fully identified the old adequate state. If management capability, connectivity, colonization opportunity, invasion possibility, or another future-facing contract expands, the new least-information state can require distinctions that the old observations never separated.

Thus an apparent monitoring failure can arise from **expanded counterfactual responsibility** rather than degraded sensor quality or an already-realized ecological regime shift.

This provides a concrete bridge to restoration and adaptive management: expanding what managers can do can expand what they must know.

---

## 6. Recommended manuscript novelty boundary

### Lead

- ecological state adequacy as a **frontier across carrier feasibility, required state resolution, and evidence resolution**;
- the management-induced information-debt witness;
- monitoring obsolescence under expanded future/action contracts;
- target-only reportability as a regime distinct from full-state identification.

### Cite as ancestry, not novelty

- adequacy-for-purpose;
- task-specific state abstraction / bisimulation;
- information-bottleneck representation phase transitions;
- POMDP / active sensing / dual control;
- ecological state-and-transition monitoring;
- sheaf/global-section contextuality.

### Do not claim yet

- historical firstness;
- universal compression–portability–observability trilemma;
- generic ecological contextuality;
- a universal theorem that more control always increases information demand.

---

## 7. Literature checked in this pass

Representative sources include:

- Parker, W. S. (2020). *Model Evaluation: An Adequacy-for-Purpose View*. Philosophy of Science.
- Bokulich, A. & Parker, W. S. (2021). *Data models, representation and adequacy-for-purpose*. European Journal for Philosophy of Science.
- Parker, W. S., Carey, C. C., Olsson, F. & Thomas, Q. (2026). *An adequacy-for-purpose perspective for the environmental sciences*. Frontiers in Ecology and the Environment. DOI: 10.1002/fee.70058.
- Wang, Z. et al. (2024). *Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning*. AAAI.
- Wu, T. & Fischer, I. (2020). *Phase Transitions for the Information Bottleneck in Representation Learning*. ICLR.
- Rumpff et al. / adaptive-management state-and-transition modelling literature on uncertainty, monitoring and management actions.
- Jones et al. (2023). *What state of the world are we in? Targeted monitoring to detect transitions in vegetation restoration projects*. Ecological Applications.
- Luxton et al. (2025/2026). *State-and-transition models as a contextual framework for leading indicators of restoration trajectories*. Methods in Ecology and Evolution.
- adaptive-management monitoring road-map literature noting that new management options can trigger redesign of monitoring/set-up assumptions.
- classical dual-control and active-sensing literature in which control actions affect information acquisition or state estimation.
- 2026 sheaf-theoretic work on global metabolic coherence in microbial communities.

The search was targeted rather than systematic. Before any `first`, `novel`, or historical-priority sentence enters the manuscript, a dedicated database-level review is still required.
