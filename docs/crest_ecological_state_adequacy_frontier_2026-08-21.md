# Ecological State Adequacy Frontier — theory development and novelty gate

> **Status:** theory-development note, 2026-08-21. This note does not add J8 or a fifth audit. It asks which higher-level theoretical consequence actually survives comparison with neighboring ideas after J1–J7/O1 and the four companion theorem families are taken as established inputs.

## 1. Why the old headline still feels obvious

The sentence

> ecological state is relative to scientific purpose

is too weak to carry the novelty of CREST by itself.

Purpose-relative model adequacy is already an established philosophy-of-science position, including recent explicit applications to environmental science. Minimal task-specific state abstractions are also standard objects in reinforcement learning and causal/bisimulation abstraction. Representation-learning theory already contains phase transitions in compression/prediction trade-offs. Sheaf theory already formalizes local compatibility without global coherence, including recent ecological applications.

Therefore CREST should **not** claim novelty for any of the following slogans alone:

- state is purpose-relative;
- minimal sufficient representations exist for tasks;
- representations can change abruptly as an objective changes;
- local ecological descriptions need not glue into a global description;
- hidden state can remain partially observable.

The stronger CREST question is whether its already-proved cross-contract structure yields a distinctive ecological theory that couples **viability, representation, and evidence**.

---

## 2. Candidate that survives the first novelty screen

### Ecological State Adequacy Frontier (ESAF)

The proposed theory object is not one state partition. It is the response of the required ecological state to changes in the declared scientific contract and evidence.

Let a finite scientific contract be denoted by \(\mathcal C\). Where the relevant common carrier is admissible, define

\[
J_{\mathcal C}
\]

as the J1 unique coarsest joint state partition. Let

\[
K(\mathcal C)=\log_2 |J_{\mathcal C}|
\]

be the exact state-information burden. For evidence record \(e\), let

\[
\mathcal S_{\mathcal C}(e)
=
\{[u]_{J_{\mathcal C}}:u\text{ is compatible with }e\}
\]

and define the residual full-state ambiguity

\[
A(\mathcal C,e)=\log_2 |\mathcal S_{\mathcal C}(e)|.
\]

For a declared target \(T\), define analogously

\[
\mathcal T_{\mathcal C}(e)
=
\{T(u):u\text{ is compatible with }e\}.
\]

The full finite state profile is therefore

\[
\Phi(\mathcal C,e)
=
\bigl(
\operatorname{Adm}(\mathcal C),
K(\mathcal C),
A(\mathcal C,e),
|\mathcal T_{\mathcal C}(e)|
\bigr),
\]

where \(\operatorname{Adm}=1\) means the declared carrier/coverage gate passes.

The **adequacy frontier** is the set of contract/evidence changes at which one of these components changes regime: required state resolution increases, full-state identification is lost, target-only reportability changes, or the fully adequate joint state ceases to exist.

This is more specific than generic adequacy-for-purpose: it describes the **ordered response of the ecological state itself** to additional scientific obligations.

---

## 3. Four regimes, not one yes/no notion of state

The finite CREST results distinguish at least four scientifically different regimes.

### Regime I — full state identified

The carrier is admissible and every evidence class lies inside one J1 state block.

\[
\operatorname{Adm}=1,
\qquad
|\mathcal S(e)|=1.
\]

### Regime II — state unresolved, target still resolved

The required J1 state exists, but the evidence class intersects multiple state blocks while the requested target remains constant.

\[
\operatorname{Adm}=1,
\qquad
|\mathcal S(e)|>1,
\qquad
|\mathcal T(e)|=1.
\]

This is a genuinely useful ecological regime: management-relevant prediction can remain justified without full ecological-state identification.

### Regime III — state and target unresolved

The state exists but the evidence is insufficient even for the requested target.

\[
\operatorname{Adm}=1,
\qquad
|\mathcal T(e)|>1.
\]

### Regime IV — no fully adequate state under the contract

The maximal carrier is empty or coverage-incomplete.

\[
\operatorname{Adm}=0.
\]

This is not an observation problem. Refining the state partition cannot repair an incoherent carrier contract.

---

## 4. Derived order structure: an epistemic frontier

J5 already gives one-sided refinement bounds when two contracts admit the required exact comparison. Along a chain of contract strengthening for which

\[
J_{\mathcal C_0}
\preceq
J_{\mathcal C_1}
\preceq
\cdots
\]

in the sense that later contracts require at least as many state distinctions, the exact state burden \(K(\mathcal C_i)\) cannot decrease.

Now hold the evidence partition fixed. A basic factorization consequence is:

> if fixed evidence fails to identify a coarser required state, it cannot identify any later refinement of that state.

Equivalently, along an order-compatible strengthening chain, full-state licensing can change from `identified` to `unresolved`, but cannot recover without either changing the evidence contract or coarsening the required state.

This creates an **epistemic frontier** in contract space.

The result is elementary once the partition order is explicit; the contribution is not the lattice fact by itself. The CREST-level point is that scientific ambition can move a project across an evidence boundary even when the physical observations have not changed.

`tests/test_crest_adequacy_frontier.py` exhausts a small partition family to lock this direction into regression tests.

---

## 5. Atomic contract changes need not cause small state changes

A smooth-frontier intuition is false in the current theorem program.

CCOC supplies a fixed-regular family in which the physical controlled network and primitive alphabet remain fixed and opening one previously illegal primitive action changes the exact response interface from

\[
|J_{\rm closed}|=2
\]

to

\[
|J_{\rm open}|=2^{m+1},
\]

so

\[
K_{\rm open}-K_{\rm closed}=m.
\]

Because \(m\) is arbitrary, one atomic future-grammar extension can create an arbitrarily large exact state-information surcharge across the family.

This should **not** be sold as the first mathematical phase transition in representation learning; information-bottleneck and abstraction literatures already contain abrupt representation changes. The ecology-facing consequence is narrower:

> a small change in what futures or interventions must be supported can invalidate a previously adequate ecological classification by an arbitrarily large amount, even before the underlying physical configuration has changed.

`representational tipping point` is useful interpretive language for this phenomenon, but not a historical-priority claim.

---

## 6. New cross-gate witness: management-induced information debt

The strongest new synthesis found in this pass is a finite witness coupling J6, J1, and the evidence gate.

`tests/test_crest_adequacy_frontier.py` constructs a controlled contract with worlds

\[
\{a,b,c,\mathrm{bad}\}.
\]

Initially the only controllable action is `hold`.

- \(a\) can safely hold itself;
- \(c\) can safely hold itself;
- \(b\) is driven to the incompatible world by `hold`.

The maximal controlled carrier is therefore

\[
K^*_{\rm before}=\{a,c\}.
\]

The fixed evidence distinguishes `candidate` from `anchor`, so the two-state required representation is fully identified.

Now add exactly one controllable action, `rescue`.

- `rescue` makes \(b\) viable;
- `rescue` sends \(a\) toward the anchor class but keeps \(b\) in the candidate class.

The maximal controlled carrier strictly expands:

\[
K^*_{\rm after}=\{a,b,c\}.
\]

But the new action also makes \(a\) and \(b\) scientifically distinguishable in the J1 future audit. The required state count increases from two to three while the old evidence still merges \(a\) and \(b\).

Therefore:

\[
\boxed{
\text{more control}
\quad\Rightarrow\quad
\text{larger viable carrier}
\quad\text{and simultaneously}\quad
\text{greater state-information burden}
}
\]

in this finite witness.

Full-state licensing is lost, but the target `survives` remains constant across the observationally merged \(a,b\) class, so target-only reporting remains licensed.

This is **not** a universal theorem that every new management action increases information demand. It is an existence result showing that management enrichment can have this counter-directional effect.

### Ecological interpretation

A new restoration or management option can make more ecological configurations manageable while simultaneously making the old monitoring state variable inadequate for deciding how the new option behaves.

Call this phenomenon **management-induced information debt**:

> expanding the action repertoire can create new viable futures whose safe use requires distinctions that the pre-existing monitoring programme was never designed to observe.

This differs from classical dual control. Dual control studies how chosen control actions can also generate information about an uncertain system. The CREST witness instead changes the **available action repertoire** and shows that doing so can change what counts as a sufficient ecological state before any information-gathering action is executed.

---

## 7. A stronger ecological prediction: monitoring can become obsolete before nature changes

Combine the CCOC open-future effect with the J1 evidence gate.

Suppose a monitoring system \(E_D\) was adequate for an old contract \(\mathcal C_0\):

\[
E_D\text{ identifies }J_{\mathcal C_0}.
\]

A management, connectivity, invasion, recolonization, or intervention change can strengthen the future contract to \(\mathcal C_1\) without changing the currently observed physical configuration.

If

\[
J_{\mathcal C_1}
\]

strictly refines the old state beyond what \(E_D\) distinguishes, then the monitoring system becomes insufficient immediately:

\[
E_D\text{ no longer identifies }J_{\mathcal C_1}.
\]

Thus monitoring adequacy can fail because the **space of scientifically relevant futures changed**, not because the ecosystem has already crossed a physical regime shift.

This is a distinct ecological warning from conventional early-warning theory: the failure occurs in the representation/measurement contract before an ecological state transition need occur.

---

## 8. O1 makes the frontier multi-objective

O1 proves

\[
R^*_{\rm structural}=1<R^*_{\rm licensed}=2.
\]

So the cheapest repair that restores structural state existence need not be the cheapest repair whose resulting full state is evidentially identifiable.

The adequacy frontier is therefore not generally reducible to a single scalar notion of `better state`.

At minimum, one must distinguish:

- carrier feasibility;
- required representation complexity;
- full-state evidential resolution;
- target resolution;
- repair or monitoring cost.

This is where CREST differs most sharply from a single compression objective or a generic adequacy score.

---

## 9. What not to lead with after the novelty search

### 9.1 Generic adequacy-for-purpose

Parker's adequacy-for-purpose view and its 2026 environmental-science application already make purpose/context dependence explicit. CREST should cite this as philosophical ancestry, not compete with it.

### 9.2 Minimal task-specific abstraction

Task-specific minimal causal/bisimulation abstractions are established in reinforcement learning. CREST's stronger target is the coupling of several ecological obligations plus carrier/evidence gates, not minimality alone.

### 9.3 Generic representation phase transitions

Information-bottleneck theory already studies phase transitions as compression/prediction trade-offs change. The safe CREST claim is the exact **atomic future-contract sensitivity** supplied by CCOC and its ecological monitoring consequence.

### 9.4 Generic local-to-global contextuality

Sheaf theory already treats local compatibility without global sections, and 2026 work explicitly applies global-section/cohomological coherence ideas to microbial ecological communities. CREST should therefore not claim firstness for `ecological contextuality` in general.

A future **contract-contextuality** theory might still be distinct if it formalizes incompatibility among future, semantic, mechanism, and evidence contracts specifically, but this requires a dedicated prior-art and theorem pass before promotion.

---

## 10. Recommended theoretical hierarchy

### Current CREST manuscript — promote

1. **Ecological State Adequacy Frontier** as the higher-level conceptual synthesis.
2. The three gates: carrier existence -> least-information required state -> evidence/target licensing.
3. **Management-induced information debt** as the counterintuitive finite cross-gate witness.
4. **Atomic future-contract sensitivity** / representational tipping as the CCOC-derived sharp example.
5. Monitoring obsolescence without prior physical regime change as the main ecological implication.

### Keep as supporting mathematics

- J2/J5 invariance and contract-order results;
- J4/J7 repair optimization;
- O1 structural-vs-licensed repair separation;
- four companion theorem families.

### Later, only after a new novelty gate

- sheaf-style contract contextuality;
- stochastic/continuous adequacy frontiers;
- a scalable theorem family coupling control expansion, state inflation, and evidence collapse;
- empirical application to restoration or island/ecological-network monitoring.

---

## 11. Stronger paper-level thesis

The paper should no longer stop at:

> ecological states are contract-relative.

A stronger thesis supported by the current program is:

> **Ecological state adequacy has a structured frontier. As scientific obligations and available actions change, the largest coherent world set, the least-information adequate state, and the evidence-compatible state set can move in different directions. More management capability can enlarge what is viable while increasing what must be known, and a monitoring system can therefore become inadequate before the ecosystem itself changes state.**

The mathematical content behind this thesis is already distributed across CCOC, J1/J5/J6, the evidence gate, O1, and the new finite management-enrichment witness. The novelty claim should be placed on this coupling, not on generic minimality, phase transitions, contextuality, or adequacy-for-purpose.

## 12. Literature boundary used in this novelty pass

Neighboring concepts reviewed in this pass include:

- Parker, Carey, Olsson & Thomas (2026), *An adequacy-for-purpose perspective for the environmental sciences*, Frontiers in Ecology and the Environment, DOI 10.1002/fee.70058;
- Parker (2020), *Model Evaluation: An Adequacy-for-Purpose View*, Philosophy of Science;
- Bokulich & Parker (2021), *Data models, representation and adequacy-for-purpose*, European Journal for Philosophy of Science;
- Wang et al. (2024), *Building Minimal and Reusable Causal State Abstractions for Reinforcement Learning*, AAAI;
- Wu & Fischer (2020), *Phase Transitions for the Information Bottleneck in Representation Learning*, ICLR;
- Luxton et al. (2025/2026), *State-and-transition models as a contextual framework for leading indicators of restoration trajectories*, Methods in Ecology and Evolution;
- Jones et al. (2023), *What state of the world are we in? Targeted monitoring to detect transitions in vegetation restoration projects*, Ecological Applications;
- recent 2026 sheaf-theoretic ecological work on global metabolic coherence in microbial communities;
- classical dual-control / POMDP work in which actions affect information acquisition or state estimation.

This is a targeted novelty screen, not yet a systematic review. Historical-priority language should remain off until a dedicated search is complete.
