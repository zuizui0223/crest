# CREST — Contract-Relative Ecological State Theory

CREST asks what information must be retained when an ecological system is observed at one temporal cut but scientific responsibilities reach into its history, hidden contemporaneous response structure, and future composition.

The trajectory-first question remains:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, mechanisms, and scientific observables depend on context?**

An ecological state is a **scientifically licensed compression of a temporally extended ecological world**. In the current finite formulation:

> **An ecological state is the least information that must survive an observational temporal cut under the declared scientific contract.**

At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible baseline

\[
B_t=\ker O_t.
\]

The present is this cut, not a finite-width temporal coordinate and not the state itself.

## Snapshot sufficiency at the cut

Snapshot sufficiency is a factorization question. For a required state map \(q_t:\Omega\to Q_t\), the visible present is sufficient exactly when

\[
O_t(\omega)=O_t(\omega')
\Longrightarrow
q_t(\omega)=q_t(\omega').
\]

A same-cut pair separated by the adequate state is therefore a finite witness that the visible present is insufficient for the declared contract.

## Primitive responsibilities before state

- **history / MLTR:** root law and raw replacement path first; carried maps second; retained history is a quotient of immutable histories by carried-semantic relevance.
- **latent present / MRM:** primitive candidate laws first; response types derived from declared response tables.
- **future / CCOC:** controlled law plus legal right-of-cut query grammar first; response equivalence derived from legal traces.
- **CED:** downstream evidence licensing, not a fourth temporal-position responsibility.

For compatibility with the earlier CREST vocabulary:

- **future sufficiency** = CCOC prospective/open-composition responsibility;
- **semantic coherence** = MLTR inherited-semantic/history responsibility;
- **mechanism robustness** = MRM latent-response responsibility;
- **evidence licensing** = downstream CED identification/reportability.

The dependency direction is

\[
\text{primitive companion objects}
\longrightarrow
\text{responsibility equivalences / legal grammars}
\longrightarrow
J_t.
\]

The dependency DAG is regression-tested to be acyclic.

## Strict realizability boundary

Three no-go facts prevent overinterpreting arbitrary refinement cascades as literal temporal companions:

1. fixed precomputed responsibility partitions on a one-class baseline cannot generate positive interaction merely by common refinement;
2. a zero-debt post-cut audit preserving immutable MLTR history cannot later be activated by that history partition; and
3. under one fixed MRM grammar, candidate-safe zero debt implies a singleton response type.

The old marked-cycle result \(\Delta=\log_2 n-1\) and old fixed-closure three-way result \(b-\log_2 3\) remain exact **abstract fixed-closure extrema**, not the flagship companion-derived claim.

## Flagship theorem: interface prerequisites determine interaction order

The v0.6 flagship no longer defines coalition values directly.

Use the explicit carrier

\[
\Omega_m=P_H\times P_\Theta\times\{0,1\}^m,
\]

where \(P_H\) contains MLTR replacement-history primitives distinguished by complete carried maps and \(P_\Theta\) contains MRM primitive candidate laws distinguished by complete response tables.

For each coalition \(S\), the code:

1. generates the legal grammar;
2. evaluates every legal trace on every world;
3. groups worlds with equal trace profiles;
4. computes
   \[
   v_R(S)=\log_2|Q_S|.
   \]

A future decoder has a minimal prerequisite set

\[
R\subseteq\{H,\Theta\}.
\]

An exterior word exists exactly when

\[
F\in S
\quad\text{and}\quad
R\subseteq S.
\]

The induced quotient therefore satisfies

\[
\boxed{
|Q_S|=
2^{\mathbf 1_{H\in S}+\mathbf 1_{\Theta\in S}+m\mathbf 1_{F\in S,\ R\subseteq S}}.
}
\]

This formula is now a theorem about generated trace quotients rather than the implementation definition.

Its Möbius consequence is a complete classification:

- \(R=\varnothing\): the \(m\)-bit exterior burden is an **F main effect**;
- \(R=\{H\}\): it is pure **H × F pairwise interaction**;
- \(R=\{\Theta\}\): it is pure **Θ × F pairwise interaction**;
- \(R=\{H,\Theta\}\): it is pure **H × Θ × F three-way interaction**.

Thus the **minimal interface prerequisite set determines the interaction order of state addressability debt**.

Pure three-way interaction is therefore conditional, not automatic. If F is allowed to decode the exterior signature without both interfaces, the three-way dividend becomes zero.

## Numerical illustration

For \(m=10\) and \(R=\{H,\Theta\}\):

- visible cut: **1 class**;
- history interface: **2 classes / 1 bit**;
- mechanism interface: **2 classes / 1 bit**;
- history + mechanism: **4 classes / 2 bits**;
- full grammar: **4096 classes / 12 bits**;
- state-count amplification over history + mechanism: **1024×**;
- genuine three-way interaction: **10 bits**;
- three-way share of the full state: **83.33%**.

These numbers illustrate the two-interface-complete decoder case; they are not universal ecological constants.

## Ecological interpretation

The immediate implication concerns modular state design.

If every future query factors through component interfaces independently, state components can often be budgeted modularly. If a future query is only meaningful or executable when several retained interfaces are simultaneously available, the representational burden associated with that query belongs to a higher-order interaction term.

CREST therefore asks not only which past, latent, or future quantities matter separately, but **which combinations of interfaces are prerequisites for the questions the state must answer**.

## Retained smaller diagnostics

The six-world CCOC/MLTR/MRM-labeled obstruction comparison remains a compatibility witness. Its before/after change is

\[
\delta D_{\rm joint}=\delta\Delta=0.7369655942\text{ bit},
\]

with interaction-order decomposition

\[
0.7369655942
=
0.4150374993+0.3219280949.
\]

Its diagnosis remains **`interaction-only`** because standalone debts are unchanged while the joint burden changes. The compatibility diagnostic reports `active_interaction_orders = [2, 3]`, and the pairwise term is dominant in that retained six-world comparison. It is not the flagship realization theorem.

## Publication roles

- **CREST flagship:** state at a temporal cut, realizability no-go, and decoder-prerequisite interaction-order characterization.
- **CCOC:** law-fixed future grammar, addressability, and open-composition response-interface lower bounds.
- **MLTR:** source-relative carried semantics, route coherence, and minimum historical completion.
- **MRM:** primitive candidate laws, response-type quotients, candidate-safe state, and active discrimination.
- **CED:** downstream evidence licensing and monitoring/reportability.

## Current flagship manuscript

Canonical manuscript:

`manuscript/crest_flagship_amnat_v0.6_addressability.md`

Title:

**Ecological State at a Temporal Cut: Interface-Dependent Interaction**

Target: **The American Naturalist — Major Article**.

The previous `crest_flagship_amnat_v0.5_compositional.md` is retained as the pre-characterization draft. v0.4, v0.3, and v0.2 remain provenance manuscripts.

## Canonical reading paths

- `docs/contract_relative_ecological_state_theory.md` — world-before-state and Snapshot sufficiency framing.
- `docs/crest_mathematical_spine.md` — carrier/state/evidence theorem chain and supporting finite bounds.
- `docs/crest_ecological_projection.md` — ecology-facing quotient interpretation and representational stability.
- `docs/crest_sharp_sequential_state_debt_law_2026-09-06.md` — sharp sequential response-capacity law.
- `docs/crest_temporal_companion_definition_firewall_2026-09-08.md` — non-circular companion dependency order.
- `docs/crest_companion_realizability_no_go_2026-09-08.md` — strict realizability boundary.
- `docs/crest_explicit_grammar_addressability_theorem_2026-09-08.md` — explicit grammar and interaction-order characterization.

## Proof and implementation map

- `crest/temporal_cut.py` — observational cut and fiber representation.
- `crest/companion_realizability.py` — strict no-go checks.
- `crest/explicit_temporal_grammar.py` — companion primitives, grammar generation, traces, quotients, and Möbius calculation.
- `tests/test_explicit_temporal_grammar.py` — all 8 coalition quotients plus counterfactual decoder rules.
- `artifacts/crest_explicit_grammar_benchmarks_2026-09-08.json` — canonical v0.6 benchmark.
- `crest/compositional_temporal_game.py` — retained pre-characterization direct-value implementation for provenance/regression only.
- `crest/temporal_interaction.py` — retained abstract fixed-closure extrema.

## Scope firewall

The current result is finite, exact, and conditional on declared companion primitives and legal grammar structure. CREST does **not** claim:

- that history, latent response, and future exhaust every ecological state responsibility;
- a unique natural decomposition of every ecological system into these roles;
- that every future decoder requires both companion interfaces;
- that pure three-way interaction is automatic;
- that decoder prerequisites can be inferred from state accounting alone;
- statistical confounding;
- a general continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, delayed-observation, or approximate generality.

The present is a zero-width **observational cut in the finite representation**, not a metaphysical theorem about physical instants.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
```

The finite theorem surface, non-circularity firewall, realizability boundary, explicit grammar quotient, manuscript routing, and submission packaging are regression-tested.
