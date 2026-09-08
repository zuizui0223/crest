# CREST — Contract-Relative Ecological State Theory

CREST asks what information must be retained when an ecological system is observed at one temporal cut but scientific responsibilities reach into its history, hidden contemporaneous response structure, and future.

The underlying trajectory-first question remains:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, mechanisms, and scientific observables depend on context?**

The earlier formulation remains valid: an ecological state is a **scientifically licensed compression of a temporally extended ecological world**. The current finite theorem sharpens that statement by locating the compression at an observational temporal cut:

> **An ecological state is the least information that must survive an observational temporal cut under the declared scientific responsibilities.**

The current finite theory does not identify the present with a finite-width interval or with the state itself. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible-present baseline

\[
B_t=\ker O_t.
\]

Worlds in one block of \(B_t\) look the same at the cut. CREST asks which distinctions among those worlds may safely be erased.

The three temporal-position responsibilities developed here are:

- **history / MLTR:** retrospective inherited-semantic distinctions to the left of the cut;
- **latent present / MRM:** response-relevant contemporaneous structure inside the fiber \(O_t^{-1}(y)\), transverse to the cut;
- **future / CCOC:** prospective or counterfactual response distinctions to the right of the cut.

CED remains downstream evidence licensing rather than a fourth temporal-position axis.

## Canonical state construction

On one declared finite common carrier, let

\[
C_H,\qquad C_\Theta,\qquad C_F
\]

be the history, latent-present, and future refinement closures acting above \(B_t\). The least-information adequate state is

\[
\boxed{
J_t=(C_H\vee C_\Theta\vee C_F)(B_t).
}
\]

For a coalition \(S\subseteq\{H,\Theta,F\}\), let

\[
v(S)=\log_2|J_S|-\log_2|B_t|.
\]

The general joint-debt accounting quantity is

\[
\boxed{
\Delta=D_{\rm joint}-\sum_iD_i.
}
\]

## Headline temporal interaction results

### Past × future

For every \(n\ge2\), there is a finite family with one visible present class such that

\[
D_H=1,\qquad D_F=0,\qquad D_{HF}=\log_2n,
\]

so

\[
\boxed{m(H,F)=\log_2n-1}
\]

is unbounded.

Thus how much of the past must be retained at the cut cannot in general be computed independently of what future the state must support.

### History × latent present × future

For every integer \(b\ge2\), there is a finite family with

\[
D_H=1,\qquad D_\Theta=D_F=0,
\]

but

\[
D_{H\Theta F}=b\text{ bits}
\]

and genuine three-way interaction

\[
\boxed{m(H,\Theta,F)=b-\log_2 3.}
\]

Therefore

\[
\frac{m(H,\Theta,F)}{D_{H\Theta F}}
=1-\frac{\log_2 3}{b}\to1.
\]

The required state can therefore be asymptotically dominated by information generated only through coupling among history, latent contemporaneous response structure, and future.

## Numeric endpoint

At \(b=10\):

- visible present: **1 class**;
- adequate state: **1024 classes**;
- joint debt: **10 bits**;
- total interaction debt: **9 bits (90%)**;
- genuine history × latent-present × future interaction: **8.4150374993 bits (84.15% of the full state)**.

This is the current flagship numerical closure.

## Retained obstruction-change diagnostics

The earlier six-world CCOC/MLTR/MRM obstruction-spectrum comparison remains part of the mainline regression surface. Turning on the activation cascade changes the required joint state from 3 to 5 classes while all standalone debts stay fixed. The joint-debt change is

\[
\delta D_{\rm joint}=\delta\Delta=0.7369655942\text{ bit},
\]

with exact interaction-order decomposition

\[
0.7369655942
=
0.4150374993
+
0.3219280949
\quad\text{bits}.
\]

Its change diagnosis is **`interaction-only`** because every standalone debt is unchanged while the joint burden changes. The before/after diagnostic reports `active_interaction_orders = [2, 3]`, with the pairwise term dominant in that six-world comparison. These values are retained as a smaller compatibility witness; the temporal-cut \(b=10\) theorem is now the flagship endpoint.

## Publication roles

- **CREST flagship:** state at a temporal cut and interaction-generated state information.
- **CCOC:** future/composition obstruction and open-future response-interface lower bounds.
- **MLTR:** carried semantics, route coherence, and minimum historical completion after structural replacement.
- **MRM:** latent mechanism/response ambiguity, candidate-safe state, and active-discrimination frontier.
- **CED:** downstream evidence licensing and monitoring/reportability.

The companion theories remain separate. CREST uses their responsibilities on a common cut and studies the joint state they require.

## Current flagship manuscript

Canonical manuscript:

`manuscript/crest_flagship_amnat_v0.3_temporal_cut.md`

Title:

**What Must Survive the Present? Ecological State at a Temporal Cut and Interaction Across History, Latent Response, and Future**

Target: **The American Naturalist — Major Article**.

The previous Δ-centered `crest_flagship_amnat_v0.2.md` remains in the repository as provenance but is no longer canonical.

## Proof and implementation map

- `crest/temporal_cut.py` — temporal-cut contract and fiber representation.
- `crest/temporal_interaction.py` — exact past/future and three-way sharp families.
- `tests/test_crest_temporal_cut.py` — cut/fiber regression tests.
- `tests/test_crest_temporal_interaction.py` — pairwise and three-way interaction regressions.
- `docs/crest_temporal_state_interaction_theorem_2026-09-08.md` — analytic theorem statement and proof.
- `docs/flagship_integration/temporal_cut_state_section.md` — manuscript-ready theorem section.
- `artifacts/crest_temporal_cut_numeric_benchmarks_2026-09-08.json` — reproducible numeric anchors.
- `crest/joint_debt.py` — generic joint-debt accounting.
- `crest/obstruction_spectrum.py` — coalition, Shapley, and Möbius/Harsanyi decomposition.
- `crest/obstruction_compare.py` — before/after change diagnosis and active interaction orders.

## Scope firewall

The current result is finite, exact, and conditional on a declared common carrier and responsibility closures. CREST does **not** currently claim:

- that history, latent present, and future exhaust every legitimate ecological state responsibility;
- a unique natural decomposition of every ecological system into these axes;
- statistical confounding;
- a general continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, delayed-observation, or approximate generality;
- that latent response structure is identifiable from the visible cut;
- that activation order must follow chronological order.

The present is a zero-width **observational cut in the finite representation**, not a proved metaphysical claim about physical instants.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
```

The finite theorem surface and flagship routing are regression-tested.
