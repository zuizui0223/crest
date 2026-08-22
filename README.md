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
minimal adequate state
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

A pair of worlds with the same present snapshot but different required states is therefore a witness that the present snapshot is insufficient for that scientific contract.

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

On one admissible finite common carrier \(U\), with baseline partition \(B\), the current finite theory represents the declared requirements by refinement closures. In the existing implementation these include

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}.
\]

CREST-J1 proves that their least common fixed refinement

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the **unique coarsest / least-information** partition satisfying the declared finite requirements. The finite CREST state of latent world \(u\) is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

The lattice/fixed-point substrate is classical. The CREST contribution is the ecological contract that determines which distinctions the joint state must preserve.

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

## 7. Ecological rules as quotient laws

CREST treats a coarse ecological rule as an effective law on a declared state quotient. A rule is well-defined only while every world merged by that quotient agrees on the response the rule must provide.

Therefore a rule can be valid in one observational, structural, or intervention context and fail after the context changes without having been false in its original domain.

\[
\boxed{
\text{ecological rule}
=\text{ effective law on a scientifically adequate quotient}
}
\]

This is a non-relativist claim: the underlying dynamics do not change because the observer changes description. What changes is whether the distinctions erased by the old quotient remain irrelevant to the new task.

## 8. Representational stability

CREST distinguishes at least:

- **dynamical stability** — whether the ecological system resists or recovers from perturbation;
- **evolutionary stability** — whether strategies or traits resist invasion under the relevant evolutionary model;
- **representational stability** — whether the same state quotient remains adequate when observation, intervention, future, mechanism, or reporting responsibility changes.

The existing action-expansion witness already realizes a strict case in which the ecosystem need not change physically before the adequate state changes. A newly available intervention can refine the state distinction before that intervention is executed.

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to the contract.**

This is representational, not backward, causation.

## 9. Cross-gate consequences retained from the finite theory

Under explicit one-sided assumptions, enlarging a management repertoire can

\[
|K^*|\uparrow,
\qquad
|J|\uparrow,
\qquad
\text{full-state identifiability}\downarrow,
\]

while target reportability remains unchanged.

For fixed evidence partition \(E\), the minimum refinement that preserves existing evidence distinctions and identifies \(J\) is

\[
E\vee J,
\]

with finite monitoring-resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

A microdonta-derived channel witness further shows that some monitoring debt is structural: repeated measurement of one net output cannot necessarily break a causal symmetry; a new discriminating measurement channel may be required.

## 10. Canonical reading order

1. [`docs/contract_relative_ecological_state_theory.md`](docs/contract_relative_ecological_state_theory.md) — trajectory-first philosophical statement and state definition.
2. [`docs/crest_ecological_projection.md`](docs/crest_ecological_projection.md) — ecology-facing interpretation, quotient laws, and stability.
3. [`docs/crest_mathematical_spine.md`](docs/crest_mathematical_spine.md) — minimal proved finite theorem chain.
4. [`manuscript/crest_philosophy_biology_philosophy.md`](manuscript/crest_philosophy_biology_philosophy.md) — Biology & Philosophy target manuscript.
5. [`docs/README.md`](docs/README.md) — supporting proofs, audits, and archived development concepts.

## 11. Scope firewall

CREST does **not** currently claim:

- one intrinsic ecological partition independent of scientific context;
- that the four historical companion programs exhaust every legitimate notion of ecological state;
- that every present snapshot is insufficient;
- a general theorem that all ecological dynamics are deterministic, chaotic, or globally fitness-maximizing;
- a general infinite, continuous, stochastic, approximate, or delayed-observation trajectory theorem;
- that generic partition refinement, state abstraction, purpose-relative modeling, causal states, or effective theories are new;
- that finite state-memory bits equal financial or field sampling costs.

The present trajectory-first framing reorganizes the existing finite theory; it does not silently upgrade philosophical interpretation into an unproved mathematical theorem.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

## Provenance

The independent repository was migrated from `zuizui0223/mrm` at audited source SHA `72550fa8335cbffb901785f8a171c647b3cf8cc6`. See `PROVENANCE.md` for migration provenance and `docs/crest_synthesis_proof_ledger_2026-08-17.md` for the full proof inventory.
