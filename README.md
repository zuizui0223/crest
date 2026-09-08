# CREST — Contract-Relative Ecological State Theory

CREST asks what information must be retained when an ecological system is observed at one temporal cut but scientific responsibilities reach into its history, hidden contemporaneous response structure, and future composition.

The trajectory-first question remains:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, mechanisms, and scientific observables depend on context?**

An ecological state is a **scientifically licensed compression of a temporally extended ecological world**. The current finite formulation locates that compression at an observational temporal cut:

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

The current companion-definition firewall makes the dependency order explicit.

- **history / MLTR:** a root law and raw replacement path are declared first; carried maps are derived; retained history is a quotient of immutable histories by carried-semantic relevance.
- **latent present / MRM:** primitive candidate laws are declared first; response types are derived from their declared response tables.
- **future / CCOC:** a controlled law is fixed and a legal right-of-cut future grammar is declared; response equivalence is derived from the traces that grammar can query.
- **CED:** downstream evidence licensing, not a fourth temporal-position responsibility.

Thus history, mechanism, and future are not assumed independent ontic coordinates. They are distinct pre-state responsibilities with different quantifier structures.

For compatibility with the earlier CREST vocabulary:

- **future sufficiency** = CCOC prospective/open-composition responsibility;
- **semantic coherence** = MLTR inherited-semantic/history responsibility;
- **mechanism robustness** = MRM latent-response responsibility;
- **evidence licensing** = downstream CED identification/reportability.

## Non-circular state construction

The dependency direction is

\[
\text{primitive companion objects}
\longrightarrow
\text{responsibility equivalences / contracts}
\longrightarrow
J_t.
\]

There is no reverse arrow from the final state \(J_t\) into the primitive history, candidate law, or future grammar. The machine-readable dependency DAG is regression-tested to be acyclic, with \(J_t\) as a sink.

## Strict realizability boundary

The earlier fixed-closure temporal cascades remain exact finite closure theorems, but they cannot simply be renamed as literal MLTR × MRM × CCOC models.

Three no-go facts matter:

1. fixed precomputed responsibility partitions on a one-class baseline cannot generate positive interaction merely by common refinement;
2. a zero-debt post-cut audit that preserves immutable MLTR history cannot later be activated by that history partition; and
3. under one fixed MRM grammar, if the visible partition is already candidate-safe, the response-type set is trivial.

Therefore the old marked-cycle result \(\Delta=\log_2 n-1\) and the old fixed-closure three-way result \(b-\log_2 3\) are retained as **abstract fixed-closure extrema**, not as the literal companion-derived headline.

## Literal pairwise bridges

The correct companion bridge conditions *relevance* on the declared future/intervention grammar without changing the raw past or primitive mechanism.

For an \(m\)-bit MLTR carried-map family, after \(k\) declared future queries,

\[
|H(k)|=2^k,
\qquad
K_H(k)=k.
\]

For the matching MRM candidate family under \(k\) declared probes,

\[
|R(k)|=2^k,
\qquad
K_\Theta(k)=k.
\]

At \(m=10\), both frontiers move from 1 relevant class / 0 bits to 1024 classes / 10 bits while the raw histories and primitive candidate laws remain unchanged.

## Flagship theorem: pure three-way compositional interaction

The literal cross-contract theorem uses CCOC's own closed-versus-jointly-open quantifier structure.

For \(S\subseteq\{H,\Theta,F\}\), define the exact coalition value

\[
\boxed{
v_m(S)
=
\mathbf 1_{H\in S}
+
\mathbf 1_{\Theta\in S}
+
m\,\mathbf 1_{\{H,\Theta,F\}\subseteq S}.
}
\]

Interpretation:

- MLTR supplies one binary history interface;
- MRM supplies one binary latent-response interface;
- an \(m\)-bit CCOC exterior/addressability coordinate becomes legally decodable only in the declared jointly open \(H+\Theta+F\) contract.

Therefore

\[
v(H)=1,
\quad v(\Theta)=1,
\quad v(F)=0,
\]

\[
v(H\Theta)=2,
\quad v(HF)=1,
\quad v(\Theta F)=1,
\]

while

\[
v(H\Theta F)=m+2.
\]

Every pairwise Möbius dividend is exactly zero, but

\[
\boxed{m(H,\Theta,F)=m.}
\]

Hence the genuine three-way interaction is unbounded and

\[
\frac{m(H,\Theta,F)}{D_{H\Theta F}}
=
\frac{m}{m+2}
\to1.
\]

This is the current literal MLTR × MRM × CCOC headline.

## Numeric endpoint

At \(m=10\):

- visible cut: **1 class**;
- history interface: **2 classes / 1 bit**;
- mechanism interface: **2 classes / 1 bit**;
- history + mechanism: **4 classes / 2 bits**;
- jointly open state: **4096 classes / 12 bits**;
- state-count amplification over history + mechanism: **1024×**;
- pairwise interaction: **0 bit**;
- genuine history × latent-response × future interaction: **10 bits**;
- three-way share of the full state: **83.33%**;
- three-way share of interaction debt: **100%**.

At \(m=18\), the pure three-way term is 90% of the full state information.

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

Its diagnosis remains **`interaction-only`** because standalone debts are unchanged while the joint burden changes. The compatibility diagnostic also reports `active_interaction_orders = [2, 3]`. It is no longer the flagship realization theorem.

## Publication roles

- **CREST flagship:** state at a temporal cut, strict companion-realizability boundaries, and literal conditioned compositional interaction.
- **CCOC:** law-fixed future grammar, addressability, and open-composition response-interface lower bounds.
- **MLTR:** source-relative carried semantics, route coherence, and minimum historical completion.
- **MRM:** primitive candidate laws, response-type quotients, candidate-safe state, and active discrimination.
- **CED:** downstream evidence licensing and monitoring/reportability.

## Current flagship manuscript

Canonical manuscript:

`manuscript/crest_flagship_amnat_v0.5_compositional.md`

Title:

**Ecological State at a Temporal Cut: Compositional Interaction Across Time**

Target: **The American Naturalist — Major Article**.

The previous `crest_flagship_amnat_v0.4_positioned.md` is retained as the pre-realizability-audit predecessor. v0.3 and v0.2 remain provenance manuscripts.

## Canonical reading paths

- `docs/contract_relative_ecological_state_theory.md` — world-before-state and Snapshot sufficiency framing.
- `docs/crest_mathematical_spine.md` — carrier/state/evidence theorem chain and supporting finite bounds.
- `docs/crest_ecological_projection.md` — ecology-facing quotient interpretation and representational stability.
- `docs/crest_sharp_sequential_state_debt_law_2026-09-06.md` — sharp sequential response-capacity law.
- `docs/crest_temporal_companion_definition_firewall_2026-09-08.md` — non-circular companion dependency order.
- `docs/crest_companion_realizability_no_go_2026-09-08.md` — strict fixed-closure/literal-companion boundary.
- `docs/crest_conditioned_temporal_bridges_2026-09-08.md` — future-conditioned history and grammar-conditioned mechanism frontiers.
- `docs/crest_compositional_temporal_three_way_theorem_2026-09-08.md` — literal pure three-way theorem.

## Proof and implementation map

- `crest/temporal_cut.py` — observational cut and fiber representation.
- `crest/companion_realizability.py` — strict realizability no-go checks.
- `crest/conditioned_temporal_bridges.py` — literal pairwise relevance frontiers.
- `crest/compositional_temporal_game.py` — literal cross-contract coalition game.
- `tests/test_companion_realizability.py` — no-go regressions.
- `tests/test_conditioned_temporal_bridges.py` — pairwise bridge regressions.
- `tests/test_compositional_temporal_game.py` — pure three-way regression.
- `artifacts/crest_compositional_temporal_benchmarks_2026-09-08.json` — canonical v0.5 numeric anchor.
- `crest/temporal_interaction.py` — retained abstract fixed-closure extrema.

## Scope firewall

The current result is finite, exact, and conditional on declared companion primitives and declared finite contracts. CREST does **not** claim:

- that history, latent response, and future exhaust every ecological state responsibility;
- a unique natural decomposition of every ecological system into these roles;
- statistical confounding;
- a general continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, delayed-observation, or approximate generality;
- that candidate mechanisms or replacement histories are inferred from the visible cut;
- that the abstract fixed-closure cascade is itself a literal simultaneous companion realization.

The present is a zero-width **observational cut in the finite representation**, not a metaphysical theorem about physical instants.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
```

The finite theorem surface, non-circularity firewall, realizability boundary, literal bridge, manuscript routing, and submission packaging are regression-tested.
