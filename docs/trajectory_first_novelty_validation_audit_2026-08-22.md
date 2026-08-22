# CREST trajectory-first novelty and validation audit — 2026-08-22

> **Status:** current novelty/validation control after the trajectory-first reorganization, connected capability–resolution divergence theorem, and Biology & Philosophy manuscript integration. This is **not** a historical-firstness claim and **not** a database-complete systematic review.

## 1. Bottom-line verdict

CREST has a defensible mathematical/philosophical contribution, but most broad philosophical vocabulary is prior-art-adjacent and should not carry novelty by itself.

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

Konidaris (2019), *On the necessity of abstraction* (*Current Opinion in Behavioral Sciences* 29:1–7, doi:10.1016/j.cobeha.2018.11.005), explicitly treats state abstraction and action abstraction as coupled problems and discusses the direction in which action abstraction drives the state abstraction needed to support those actions.

**Blocked claim:** it is new in general that changing/adding actions can change which state distinctions a task representation needs.

CREST must therefore locate novelty in the **carrier/state/evidence/target conjunction and its quantitative scaling**, not in the qualitative statement “more actions can require a different state abstraction.”

### 2.6 Adequacy-for-purpose / representation repair

Purpose-relative adequacy and representation repair/obsolescence have strong philosophical and formal precedents.

**Blocked claim:** contract-relativity, minimal adequate representation, or representational obsolescence is itself new.

### 2.7 Adaptive monitoring / target-oriented design

Adaptive monitoring, value of information, partial identification, and target/goal-oriented experimental design already formalize question-specific evidence acquisition.

**Blocked claim:** CED is the first target-relevant monitoring framework or the first to prefer target reportability over full latent-state learning.

### 2.8 Bisimulation, observer extension, and viability–observability links

The capability–resolution theorem sits near several additional formal-methods traditions that must be kept explicit.

**Bisimulation partition refinement.** Groote, Martens & de Vink (2023), *Lowerbounds for Bisimulation by Partition Refinement* (*Logical Methods in Computer Science* 19(2), doi:10.46298/lmcs-19(2:10)2023), gives lower bounds for algorithms computing bisimulation on labelled transition systems, including deterministic families with small action alphabets. This is close to the finite refinement machinery used inside the CREST witness.

**Blocked claim:** small action alphabets, refinement cascades, or difficult/large bisimulation computations are new.

The CREST theorem is not an algorithmic lower bound for computing a quotient. Its quantity is the **change in the required quotient itself** relative to a simultaneous controlled-carrier change and fixed evidence/target contract.

**Observer/alphabet extension in supervisory control.** Natural-observer and hierarchical/decentralized supervisory-control work studies extending event/projection alphabets so an abstraction regains observer/nonblocking/control-consistency properties; Schmidt & Breindl (2011), *Maximally Permissive Hierarchical Control of Decentralized Discrete Event Systems* (*IEEE Transactions on Automatic Control* 56(4):723–737, doi:10.1109/TAC.2010.2067250), is a close neighbour. These results establish that control, observability, event alphabets, and abstractions must be coordinated.

**Blocked claim:** CREST is the first formalism to connect control-relevant event sets, observability, and valid abstraction.

The direction of the CREST scaling theorem differs: it fixes the evidence, enlarges what can be done by one action, and quantifies how much finer the **required state** can become while viability improves only marginally.

**Viability and observability.** Kassara's viability-kernel observability work links observability to a viability construction in continuous/set-valued control settings.

**Blocked claim:** viability and observability have never been studied jointly.

CREST's candidate contribution therefore cannot be “viability + observability”. It is the particular four-way scaling statement across **carrier gain, required-state complexity, evidence adequacy, and target reportability**.

### 2.9 Targeted no-bound nearest-neighbour scan — result

A targeted 2026-08-22 search explicitly covered:

- state/action abstraction coupling;
- labelled-transition-system bisimulation and partition-refinement lower bounds;
- alphabet/event extension and natural-observer synthesis in discrete-event control;
- viability–observability links;
- POMDP/predictive-state/state-reduction families already audited above.

This scan found strong matches to every **ingredient**, but did **not** identify a direct statement matching the full CREST conjunction

\[
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}\text{ arbitrary},
\qquad
\text{fixed evidence loses full-state adequacy},
\qquad
\text{coarse target remains reportable}.
\]

That negative result is **not evidence of historical firstness**. It is sufficient only for the current conservative manuscript wording: “we prove within CREST” / “candidate CREST-level contribution,” not “first theorem of its kind.”

## 3. What remains strongest

### A. Conditional finite state existence/minimality — foundational, not the main novelty claim

On a declared finite carrier, CREST-J1 gives

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

as the unique coarsest common fixed point above the baseline.

This answers **what the finite CREST state is**, but closure-operator/fixed-point theory is classical. J1 is the existence/minimality backbone, not the strongest originality claim.

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

## 5. Validation status for the current submission

### Closed

1. **Trajectory-first hierarchy** is integrated across README, mathematical spine, and manuscript.
2. **PSR/POMDP boundary** is explicit; no non-embeddability claim is made.
3. **Snapshot sufficiency** is explicitly a factorization criterion, not a novelty theorem.
4. **State/action abstraction boundary** is explicit through Konidaris (2019).
5. **Connected capability–resolution theorem** is analytically stated for arbitrary \(m\), with one connected transition system rather than a direct-sum witness.
6. **Regression/oracle consistency:** multi-Python CI verifies the finite witness surface; the Biology & Philosophy manuscript integration run passed **93 tests** on Python 3.10/3.11/3.12 and all submission-control checks after report synchronization.
7. **Manuscript theorem hierarchy:** J1 = conditional state backbone; qualitative action expansion = direction; capability–resolution divergence = scale/no-bound headline.
8. **Targeted nearest-neighbour scan for the no-bound conjunction** completed at the conservative, non-firstness level described above.
9. **Empirical data requirement removed:** real-data cases are optional illustrations, not theorem-validation conditions.

### P1 only if the novelty claim is strengthened later

A database-complete literature review is required before any wording such as “first,” “unprecedented,” or “no previous framework/theorem.” The current manuscript does not require such wording.

### P2 — optional future mathematics

Not current blockers:

- stochastic/continuous/infinite-state analogues that genuinely use CREST-specific multi-gate coupling;
- a general representational-stability metric/radius;
- a general observation-symmetry theorem;
- structural conditions that upper-bound the capability–resolution divergence in restricted ecological model classes.

The last item is now the most natural mathematical sequel: the theorem proves that no carrier-gain-only bound exists **without additional assumptions**, so future work can ask which locality, bounded-depth, bounded-response-rank, or blanket assumptions restore a finite bound.

## 6. Empirical status

Real-data or worked ecological applications are **optional illustrations**, not validation requirements for the finite theorem.

The mathematical claims stand or fall on definitions, proofs, counterexamples, and finite regression/oracle checks. Do not reopen empirical-data collection as a submission blocker unless the paper is deliberately changed into an empirical-methods paper.

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
- viability and observability are jointly studied for the first time;
- adequate state is purpose/contract-relative;
- monitoring should change when management changes;
- representational obsolescence is a new general concept;
- the no-bound theorem is historically first.

## 8. Development rule

**Stop theorem proliferation for the current paper.**

The current finite manuscript has its spine:

\[
\text{carrier existence}
\to
\text{least state }J
\to
\text{evidence licensing}
\to
\text{qualitative action expansion}
\to
\text{capability–resolution no-bound theorem}.
\]

A new result should enter only if it strengthens this exact chain through a necessary-and-sufficient boundary, a sharp bound under explicit additional assumptions, or a genuinely new cross-gate impossibility. Otherwise record it as future work rather than expanding the headline surface.
