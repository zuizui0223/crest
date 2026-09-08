# CREST manuscript and submission surfaces

## Current flagship

The current CREST flagship is:

**What Must Survive the Present? Ecological State at a Temporal Cut and Interaction Across History, Latent Response, and Future**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.3_temporal_cut.md`.

The paper begins from an observational temporal cut

\[
O_t:\Omega\to Y_t,
\qquad
B_t=\ker O_t,
\]

and defines ecological state as the least information that must survive that cut under the declared scientific responsibilities.

The three temporal-position responsibilities developed in the current finite theory are:

- MLTR / history \(H\): retrospective inherited-semantic distinctions to the left of the cut;
- MRM / latent present \(\Theta\): response-relevant contemporaneous structure inside the fiber \(O_t^{-1}(y)\), transverse to the cut;
- CCOC / future \(F\): prospective or counterfactual response distinctions to the right of the cut.

The flagship quantitative results are:

\[
\boxed{m(H,F)=\log_2 n-1,}
\]

so past-by-future interaction is unbounded, and

\[
\boxed{m(H,\Theta,F)=b-\log_2 3,}
\]

so genuine history × latent-present × future interaction is also unbounded and satisfies

\[
\frac{m(H,\Theta,F)}{D_{H\Theta F}}
=1-\frac{\log_2 3}{b}\to1.
\]

At the canonical \(b=10\) endpoint, one visible present class yields 1024 adequate-state classes and 10 total bits; 9 bits are interaction-generated and 8.4150374993 bits (84.15% of the full state) are genuine three-way interaction.

The general CREST accounting quantity remains

\[
\Delta=D_{\rm joint}-\sum_iD_i,
\]

with the marked-cycle extremum

\[
\Delta=\log_2 n-1.
\]

Generic closure, fixed-point, partition-refinement, marked-cycle, Shapley, and Möbius/Harsanyi machinery are classical substrate. CREST's claim is the ecological state construction at a temporal cut and the interaction-generated information burden among declared responsibilities on one finite common lift.

## Retained predecessor manuscript

`crest_flagship_amnat_v0.2.md` is retained as the previous Δ-centered flagship draft. It is no longer canonical.

## Retained Biology & Philosophy bundle

The previous Biology & Philosophy submission surface remains intact for provenance and comparison:

**When Conservation Capacity Outgrows Conservation Knowledge: A Contract-Relative Theory of Ecological State**

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witnesses, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.
6. `../figures/crest_capacity_knowledge_paradox.svg` — Figure 1 source for that manuscript.

The legacy philosophy submission verifier intentionally continues to target `crest_biology_philosophy_blinded_submission.md`; it is not the verifier for the Am Nat flagship.

## Current scientific spine

```text
possible ecological worlds Ω
→ observational temporal cut O_t
→ visible baseline B_t = ker(O_t)
→ history H / latent-present Θ / future F responsibilities
→ least-information joint state J_t
→ coalition debts and Möbius interaction anatomy
→ unbounded H×F and H×Θ×F interaction
→ evidence licensing and reportability downstream
```

The companion programmes remain separate publication units:

- CCOC — future/composition obstruction;
- MLTR — inherited semantics/history obstruction;
- MRM — latent mechanism/response ambiguity and active resolution;
- CED — downstream evidence licensing.

CREST asks what information must survive the common present cut when these responsibilities interact.

## Claim firewall

The current finite paper does **not** claim:

- that history, latent present, and future exhaust every legitimate ecological state responsibility;
- a unique natural decomposition of all ecological systems into these coordinates;
- statistical confounding;
- a continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, or approximate generality;
- that the activation order must follow chronological order.

The present is a zero-width observational cut in the finite representation, not a proved metaphysical or continuous-time instantaneous state.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

The general pytest suite verifies the finite CREST theorem surface, including temporal-cut, temporal-interaction, joint-debt, and sharp-family regressions. `verify_crest_philosophy_submission.py` remains specific to the retained Biology & Philosophy manuscript. The flagship routing contract is pinned by `../docs/flagship_integration/flagship_integration_manifest.json` and its regression tests.
