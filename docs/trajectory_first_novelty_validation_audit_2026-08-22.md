# CREST trajectory-first novelty and validation audit — 2026-08-22

> **Status:** current novelty/validation control after the trajectory-first reorganization and the capability–resolution divergence result. This is not a historical-firstness claim and not a database-complete systematic review.

## 1. Bottom-line verdict

CREST has a defensible mathematical/philosophical contribution, but most of the broad philosophical vocabulary is prior-art-adjacent and should not carry novelty by itself.

Not novelty-bearing on its own:

- ecological identity is dynamic rather than a static snapshot;
- ecological state can depend on history, trajectory, basin, or future response;
- histories can be compressed into predictive equivalence classes;
- controlled-system state can be represented by predictions of future action-observation tests;
- state abstraction can be task-specific;
- action abstraction and state abstraction can constrain one another;
- future actions/options can determine which state distinctions are useful for planning;
- adequacy is purpose/context-relative;
- monitoring can change with management questions;
- representational obsolescence under a changed task/regime;
- eco-evolutionary feedback makes response structure context dependent.

The strongest current CREST-level contribution is the **multi-gate ecological state architecture plus a sharp cross-gate scaling result**:

```text
temporally extended ecological worlds
    -> declared observation/intervention contract
    -> carrier feasibility
    -> least-information adequate state
    -> evidence licensing
    -> target-only / set-valued fallback
    -> capability expansion can move these gates at radically different scales
```

The central mathematical object is not “a predictive state” alone. It is a declared ecological-state contract that separates **viable carrier**, **required state**, **identified state**, and **reportable target**.

## 2. Closest prior-art families

### 2.1 Dynamic ecosystem identity

Collier & Cumming (2011) and Delettre (2021) already make ecological identity dynamic, process-sensitive, trajectory-sensitive, and/or basin-sensitive.

**Blocked claim:** CREST is the first theory in which ecological state is temporally extended or dynamical.

### 2.2 Computational mechanics / causal states

Causal-state constructions group histories by equality of conditional future distributions and provide minimal predictive sufficient statistics.

**Blocked claim:** CREST invents state as an equivalence class of histories according to future behavior.

### 2.3 Predictive State Representations

Littman, Sutton & Singh (2002) and Singh, James & Rudary (2004) represent controlled-system state using predictions of future action-observation tests.

**Blocked claim:** CREST is the first framework in which counterfactual future tests determine present predictive state.

### 2.4 Task-specific state abstraction / POMDPs

Bisimulation, MDP/POMDP state reduction, causal abstraction, and conservation decision theory already seek compact task-relevant states.

**Blocked claim:** CREST is the first minimum task-specific or management-relative state representation.

### 2.5 State–action abstraction coupling

Konidaris (2019), *On the necessity of abstraction* (Current Opinion in Behavioral Sciences, doi:10.1016/j.cobeha.2018.11.005), explicitly treats state abstraction and action abstraction as coupled problems and notes the less-explored direction in which action abstraction drives the state abstraction needed to support those actions.

This is a material nearest neighbour for the CREST action-expansion narrative.

**Blocked claim:** it is new in general that changing/adding actions can change which state distinctions a task representation needs.

CREST must therefore locate novelty in the **carrier/state/evidence/target conjunction and its quantitative scaling**, not in the qualitative statement “more actions can require a different state abstraction.”

### 2.6 Adequacy-for-purpose / representation repair

Purpose-relative adequacy and representation repair/obsolescence already have strong philosophical and formal precedents, including the Swanson 2026 manuscript used in the prior audit.

**Blocked claim:** contract-relativity, minimal adequate representation, or representational obsolescence is itself new.

### 2.7 Adaptive monitoring / target-oriented design

Adaptive monitoring, value of information, partial identification, and target/goal-oriented experimental design already formalize question-specific evidence acquisition.

**Blocked claim:** CED is the first target-relevant monitoring framework or the first to prefer target reportability over full latent-state learning.

## 3. What remains strongest

### A. Conditional finite state existence/minimality — foundational, not the main novelty claim

On a declared finite carrier, CREST-J1 gives

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

as the unique coarsest common fixed point above the baseline.

This is essential because it answers **what the finite CREST state is**. But closure-operator/fixed-point theory is classical, so J1 should be presented as the formal existence/minimality backbone rather than as the strongest originality claim.

### B. Required state vs evidence vs target

CREST explicitly separates

\[
\text{required state},\qquad
\text{identified state},\qquad
\text{reportable target}.
\]

Full-state licensing is

\[
J\preceq E,
\]

while a target can still factor through \(E\) when the full state does not.

The ingredients are not individually unprecedented; the defensible point is their explicit placement downstream of carrier/state adequacy rather than collapse into one belief-state or decision object.

### C. Capability–resolution divergence — strongest current mathematical headline

For every \(m\ge1\), the connected deterministic witness uses one newly admitted action `probe` and a bounded four-symbol output alphabet to realize

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m.
}
\]

On the same retained present slice:

- required state: \(1\to 2^m\) classes;
- fixed-monitoring debt: \(0\to m\) bits;
- full-state licensing: yes \(\to\) no;
- coarse target reportability: yes \(\to\) yes.

Every address-readout trajectory enters the same newly rescued `fragile` world, so the result is not a disjoint union of independent readout and rescue gadgets.

The no-bound corollary is

\[
\boxed{
\text{there is no finite }f(\Delta|K^*|)
\text{ that universally upper-bounds }\Delta K_{U_0}.
}
\]

This is stronger than the qualitative observation that actions and state abstractions interact. It asserts an **unbounded scale separation across CREST gates while capability gain is fixed at one world**.

### D. Repair/evidence noncommutation

O1 shows that a cheapest structural carrier repair need not be a cheapest fully evidence-licensed repair. This remains useful because it prevents Gate A repair and Gate C licensing from being collapsed into one optimization objective.

## 4. Companion-program claim ceilings

- **CCOC:** candidate novelty is the constrained same-system closed/open interface separation and bounded-local sharpness realization, not generic future-sensitive minimization.
- **MLTR:** candidate novelty is source-relative exact repair constrained to preserve inherited labels/meaning, not generic partition refinement.
- **MRM:** many standalone pieces are close to standard robust/model-uncertain prediction; its strongest role is as a mechanism-response constraint inside CREST.
- **CED:** strongest as the downstream evidence/licensing layer; target-oriented OED/VOI/partial identification are not novel individually.

## 5. Validation still required before submission

### P0 — integrate the scaling theorem into the manuscript

The Biology & Philosophy manuscript still describes the older qualitative `rescue` witness as the main action-expansion result.

**Pass condition:** the manuscript distinguishes:

1. J1 = conditional least-state existence/minimality backbone;
2. qualitative action expansion = monotone direction;
3. capability–resolution divergence = arbitrary cross-gate scale separation/no-bound theorem.

### P0 — add the state/action-abstraction prior-art boundary

The manuscript already contains the PSR/POMDP boundary but should also cite Konidaris (2019) or equivalent state/action abstraction work.

**Pass condition:** it explicitly concedes that action choice/action abstraction can shape required state abstraction, and locates the CREST claim in the carrier/state/evidence/target scaling conjunction.

### P0 — theorem proof/test consistency

The connected witness must remain analytically described and executable from the same transition system.

**Pass condition:** multi-Python CI verifies for a finite range of \(m\) that:

- carrier gain is exactly one;
- present-state class count is \(1\to2^m\);
- monitoring debt is exactly \(m\) bits;
- full-state evidence fails after expansion;
- coarse target remains reportable;
- readout paths terminate in the same rescued world.

The analytic proof supplies arbitrary \(m\); finite tests are regression witnesses, not the proof.

### P1 — nearest-neighbour search for the no-bound conjunction

The web/secondary search to date confirms strong prior art for automata state complexity, task-specific abstraction, action/state abstraction coupling, viability, observability, and partial observability. It has not produced a direct match to the full conjunction

\[
\Delta|K^*|=1,\quad
\Delta K\text{ arbitrary},\quad
\text{evidence adequacy lost},\quad
\text{target reportability retained}.
\]

That absence is not proof of historical firstness.

**Pass condition for current paper:** claim only a `candidate CREST-level contribution` / `we prove within this framework`, not “first ever,” unless a database-complete review is later performed.

### P2 — optional future mathematics

Not current blockers:

- stochastic/continuous/infinite-state analogues that genuinely use the CREST multi-gate coupling;
- a general representational-stability metric/radius;
- a general observation-symmetry theorem.

## 6. Empirical status

Real-data or worked ecological applications are **optional illustrations**, not validation requirements for the finite theorem.

The mathematical claims stand or fall on definitions, proofs, counterexamples, and finite regression/oracle checks. Do not reopen empirical-data collection as a submission blocker unless the paper is deliberately changed from a mathematical/philosophical paper into an empirical-methods paper.

## 7. Current safe positioning

Safe:

> CREST provides a finite contract architecture that separates carrier feasibility, least-information state, evidence identification, and target reportability, and proves that one fixed-size capability expansion can add only one viable world while forcing arbitrarily many bits of additional state and monitoring resolution.

Also safe:

> The future repertoire can change the adequate present representation before the physical ecosystem changes; the novelty claim is not that actions can affect state abstraction in general, but that the effects on viability, required state, evidence adequacy, and target reportability can diverge without any carrier-gain-only bound.

Not safe as novelty claims:

- ecological state is a trajectory;
- state is a compression of history/future;
- future tests can define present predictive state;
- actions can affect state abstraction;
- adequate state is purpose/contract-relative;
- monitoring should change when management changes;
- representational obsolescence is a new general concept.

## 8. Development rule

Do not add another theorem family now.

Current order:

1. validate and merge the connected capability–resolution theorem;
2. integrate it into the mathematical spine and manuscript;
3. add the Konidaris/action–state abstraction boundary;
4. re-run submission controls and theorem CI;
5. stop mathematical proliferation unless a new result strengthens the same carrier/state/evidence/target chain.
