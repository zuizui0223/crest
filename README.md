# CREST — Contract-Relative Ecological State Theory

CREST asks a more basic question than how to classify an ecosystem at one instant:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, mechanisms, and scientific observables depend on context?**

The working answer is:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

A present ecological snapshot is therefore not assumed to be the state. A CREST world may contain relevant history, present configuration, latent response structure, and counterfactual future responses. The state is the coarsest representation that may safely forget differences among those worlds under a declared scientific context.

```text
self-modifying ecological dynamics
        ↓
temporally extended possible worlds
        ↓
observation / intervention context
        ↓
scientific contract
        ↓
carrier feasibility
        ↓
least-information adequate state
        ↓
evidence licensing and reportability
```

The current proved mathematics is finite and exact. The trajectory-level framing is the organizing interpretation of that finite latent-world theory; CREST does **not** yet claim a general continuous or stochastic trajectory theorem.

## 1. World before state

Write a possible ecological world schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where:

- \(h_t\) is relevant ecological history;
- \(x_t\) is the present ecological configuration;
- \(\mathcal F_t\) is the declared future-response structure under relevant interactions or interventions.

For stochastic systems, \(\mathcal F_t\) may be a conditional distribution over future trajectories rather than one fixed future.

CREST does not require every coordinate of \(\omega\) to be retained. It asks which differences can be erased without invalidating the scientific work assigned to the state.

## 2. Scientific access and contract

Science does not observe the full world directly. An observation/intervention context \(V\) determines what distinctions are accessible, schematically

\[
O_V:\Omega\to Y_V.
\]

A scientific contract then declares which accessible or latent distinctions matter:

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where:

- \(\Gamma\): future interactions, operations, or interventions the state must survive;
- \(\mathcal H\): inherited meanings or history that must remain coherent;
- \(\Theta\): retained response mechanisms or causal alternatives;
- \(D\): experiment, observation, reliability, and evidence contract;
- \(T\): requested report or decision target.

State identity is therefore **context- and contract-relative but not arbitrary**. Scientists declare the task; dynamics, causal structure, and evidence can refute a proposed merge.

## 3. Snapshot sufficiency is a question, not an assumption

Let \(X(\omega)\) denote the present snapshot and \(q_{\mathcal C,V}(\omega)\) the adequate CREST state. A snapshot is sufficient exactly when it factors the required state:

\[
\boxed{
X(\omega)=X(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

This is a factorization criterion, not a novelty theorem. A pair of worlds with the same present snapshot but different required states is a witness that the present snapshot is insufficient for that scientific contract.

CREST currently studies three structural reasons this can happen and one separate evidential question.

## 4. Three structural obstructions to snapshot sufficiency

| structural obligation | companion | hidden difference that can become state-relevant |
|---|---|---|
| **future sufficiency** | [CCOC](https://github.com/zuizui0223/ccoc) | different future-accessible interactions, connections, or interventions |
| **semantic coherence** | [MLTR](https://github.com/zuizui0223/mltr) | different inherited meaning or replacement history after structural change |
| **mechanism robustness** | [MRM](https://github.com/zuizui0223/mrm) | different retained mechanisms that disagree on a required future response |

These are not rival definitions of state. They are three ways in which two worlds that look the same now can fail to be scientifically interchangeable.

### CCOC — future insufficiency

A currently erased distinction can become operationally necessary when the future grammar is enlarged. Present functional equivalence need not imply equivalence under colonization, reconnection, rewiring, or newly available intervention.

### MLTR — semantic / historical insufficiency

A category carried from a source system can cease to be exact after turnover or replacement. The old state label may remain verbally available while the inherited merge is no longer operationally safe.

### MRM — mechanistic insufficiency

Two worlds can share one visible state while retaining different response mechanisms. CREST preserves mechanism differences only when they can change a declared future response or target.

## 5. Evidence is a second-stage question — CED

[CED](https://github.com/zuizui0223/ced) is not another ontic reason that the present world differs. It asks whether the evidence can identify the state distinctions already required by the scientific contract.

Thus CREST separates

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}
}
\]

in general.

A required state can exist mathematically while the current record supports only a set of compatible states. Conversely, a requested target can remain reportable even when the full state is unresolved.

## 6. Finite mathematical spine

On one admissible finite common carrier \(U\), with baseline partition \(B\), the current finite theory represents the declared requirements by refinement closures

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}.
\]

CREST-J1 proves that

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the **unique coarsest / least-information** partition satisfying the declared finite requirements. The finite CREST state of latent world \(u\) is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

The lattice/fixed-point substrate is classical. J1 is the existence/minimality backbone, not the strongest novelty claim.

The finite theory is organized by three gates:

1. **carrier feasibility** — can the required descriptions be synchronized on one admissible world set?;
2. **representational adequacy** — what is the least-information state preserving the required distinctions?;
3. **evidential licensing** — does the observation contract identify which required state is occupied?

For evidence partition \(E\),

\[
\boxed{
\text{full deterministic state report exists}
\iff
J\preceq E.
}
\]

## 7. Main cross-gate theorem — capability–resolution divergence

The qualitative action-expansion result gives the direction: adding safe control options can enlarge the viable carrier, while strengthening the future responsibility can refine the least-information state and make fixed monitoring insufficient.

The stronger result is quantitative. For every integer \(m\ge1\), there is one connected finite deterministic CREST system in which adding a **single** controllable action `probe` gives

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m\text{ bits}.
}
\]

On the retained present slice \(U_0\):

- required state classes change from \(1\) to \(2^m\);
- fixed-monitoring resolution debt changes from \(0\) to exactly \(m\) bits;
- full-state identification changes from yes to no;
- a constant coarse target remains reportable.

The action alphabet changes only from `{hold}` to `{hold, probe}` and the output alphabet remains `{neutral, bit0, bit1, done}`. Repeated `probe` reads one latent coordinate at a time, and the readout paths terminate in the same `fragile` world that `probe` newly makes viable before reaching `safe`.

Therefore no universal finite function depending only on carrier-size gain can upper-bound required state complexity:

\[
\boxed{
\text{viability gain alone cannot upper-bound representational burden.}
}
\]

This is the main nontrivial mathematical headline beyond the conditional J1 state construction. CREST does **not** claim novelty for generic state/action abstraction coupling, automaton minimization, viability kernels, or predictive states separately.

## 8. Ecological rules as quotient laws

CREST treats a coarse ecological rule as an effective law on a declared state quotient. A rule is well-defined only while every world merged by that quotient agrees on the response the rule must provide.

Therefore a rule can be valid in one observational, structural, or intervention context and fail after the context changes without having been false in its original domain.

\[
\boxed{
\text{ecological rule}
=\text{ effective law on a scientifically adequate quotient}
\]

This is a non-relativist claim: the underlying dynamics do not change because the observer changes description. What changes is whether the distinctions erased by the old quotient remain irrelevant to the new task.

## 9. Representational stability and monitoring debt

CREST distinguishes at least:

- **dynamical stability** — whether the ecological system resists or recovers from perturbation;
- **evolutionary stability** — whether strategies or traits resist invasion under the relevant evolutionary model;
- **representational stability** — whether the same state quotient remains adequate when observation, intervention, future, mechanism, or reporting responsibility changes.

A newly available intervention can refine the state distinction before that intervention is executed. The connected scaling family shows that this representational change can be arbitrarily large in bits even while the controlled-carrier gain stays fixed at one world.

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to the contract.**

This is representational, not backward, causation.

For fixed evidence partition \(E\), the minimum refinement that preserves existing evidence distinctions and identifies \(J\) is

\[
E\vee J,
\]

with finite monitoring-resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

A channel-factorization witness further shows that some monitoring debt is structural: repeated measurement of one net output cannot necessarily break a causal symmetry; a new discriminating measurement channel may be required.

## 10. Prior-art firewall

The current headline is deliberately narrower than several established ideas.

CREST does not claim novelty for:

- dynamic or trajectory-sensitive ecosystem identity;
- predictive equivalence or causal states;
- Predictive State Representations based on future action-observation tests;
- purpose-relative or task-specific state abstraction;
- POMDP state reduction;
- the generic coupling of state and action abstraction, including the direction emphasized by Konidaris (2019) in which action abstraction can drive the state abstraction needed to support those actions;
- generic viability/observability mathematics;
- adaptive monitoring or target-oriented experimental design.

The candidate CREST-level contribution is the **carrier/state/evidence/target cross-gate conjunction and its scale separation**: a fixed-size capability expansion can add exactly one viable world while forcing arbitrarily many additional bits of least-state and monitoring resolution, with full-state licensing lost but a coarse target retained.

## 11. Canonical reading order

1. [`docs/contract_relative_ecological_state_theory.md`](docs/contract_relative_ecological_state_theory.md) — trajectory-first philosophical statement and state definition.
2. [`docs/crest_mathematical_spine.md`](docs/crest_mathematical_spine.md) — canonical finite theorem chain and scaling result.
3. [`docs/crest_capability_resolution_divergence_theorem_2026-08-22.md`](docs/crest_capability_resolution_divergence_theorem_2026-08-22.md) — analytic connected scaling construction and no-bound corollary.
4. [`docs/crest_ecological_projection.md`](docs/crest_ecological_projection.md) — ecology-facing interpretation, quotient laws, and stability.
5. [`manuscript/crest_biology_philosophy_blinded_submission.md`](manuscript/crest_biology_philosophy_blinded_submission.md) — Biology & Philosophy target manuscript.
6. [`docs/README.md`](docs/README.md) — supporting proofs, audits, optional applications, and archived development concepts.

## 12. Scope firewall

CREST does **not** currently claim:

- one intrinsic ecological partition independent of scientific context;
- that the historical companion programs exhaust every legitimate notion of ecological state;
- that every present snapshot is insufficient;
- a general theorem that all ecological dynamics are deterministic, chaotic, or globally fitness-maximizing;
- a general infinite, continuous, stochastic, approximate, or delayed-observation trajectory theorem;
- that generic partition refinement, state abstraction, action abstraction, purpose-relative modelling, causal states, or effective theories are new;
- that a one-world viability gain generically creates large state complexity in real ecosystems;
- that empirical data are required to establish the finite theorem;
- that finite state-memory bits equal financial or field sampling costs.

The trajectory-first framing organizes the finite theory; the connected scaling theorem is an exact finite existence result, not an empirical frequency claim.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

## Provenance

The independent repository was migrated from `zuizui0223/mrm` at audited source SHA `72550fa8335cbffb901785f8a171c647b3cf8cc6`. See `PROVENANCE.md` for migration provenance and `docs/crest_synthesis_proof_ledger_2026-08-17.md` for the full proof inventory.
