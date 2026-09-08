# CREST manuscript and submission surfaces

## Current flagship

The current CREST flagship is:

**Ecological State at a Temporal Cut: Interaction Across Time**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.4_positioned.md`.

The manuscript uses the observational temporal cut

\[
O_t:\Omega\to Y_t,
\qquad
B_t=\ker O_t,
\]

and defines ecological state as the least information that must survive that cut under declared scientific responsibilities.

The three temporal-position responsibilities are:

- MLTR / history \(H\): retrospective inherited-semantic distinctions to the left of the cut;
- MRM / latent present \(\Theta\): response-relevant contemporaneous structure inside the fiber \(O_t^{-1}(y)\), transverse to the cut;
- CCOC / future \(F\): prospective or counterfactual response distinctions to the right of the cut.

The flagship results are

\[
\boxed{m(H,F)=\log_2 n-1}
\]

and

\[
\boxed{m(H,\Theta,F)=b-\log_2 3,}
\]

with

\[
\frac{m(H,\Theta,F)}{D_{H\Theta F}}
=1-\frac{\log_2 3}{b}\to1.
\]

At \(b=10\), one visible present class yields 1024 adequate-state classes and 10 total bits; 9 bits are interaction-generated and 8.4150374993 bits (84.15% of the full state) are genuine three-way interaction.

## Why v0.4 replaces v0.3

v0.3 established the correct temporal-cut theorem but was not yet submission-positioned. v0.4 makes no new theorem claim. It fixes the manuscript-facing issues identified in the readiness audit:

- abstract reduced to **193 words** (Major Article limit: 200);
- keywords reduced to **6**;
- title reduced to **9 words**;
- Methods are explicitly placed before Results;
- Literature Cited is added;
- ecological memory, hysteresis, transient ecology, causal/predictive state, bisimulation, and state-abstraction prior art are cited in the manuscript rather than handled only by an internal novelty firewall.

The novelty boundary is now explicit: CREST does not claim that time matters, that histories can predict futures, or that task-preserving state abstraction is new. The CREST claim is that retrospective, latent-contemporaneous, and prospective responsibilities acting on one observational cut need not be separable; their interaction can be unbounded and can asymptotically dominate required state information.

## Retained predecessor manuscripts

- `crest_flagship_amnat_v0.3_temporal_cut.md` — theorem-correct predecessor without full literature positioning.
- `crest_flagship_amnat_v0.2.md` — earlier generic-Delta-centered flagship draft.

Both are retained for provenance and are no longer canonical.

## Retained Biology & Philosophy bundle

The previous Biology & Philosophy submission surface remains intact for provenance and comparison:

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witnesses, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.
6. `../figures/crest_capacity_knowledge_paradox.svg` — Figure 1 source for that manuscript.

The legacy philosophy submission verifier intentionally continues to target `crest_biology_philosophy_blinded_submission.md`; it is not the verifier for the Am Nat flagship.

## Current scientific spine

```text
possible ecological worlds Omega
-> observational temporal cut O_t
-> visible baseline B_t = ker(O_t)
-> history H / latent-present Theta / future F responsibilities
-> least-information joint state J_t
-> coalition debts and Mobius interaction anatomy
-> unbounded H x F and H x Theta x F interaction
-> evidence licensing and reportability downstream
```

The companion programmes remain separate publication units:

- CCOC — future/composition obstruction;
- MLTR — inherited semantics/history obstruction;
- MRM — latent mechanism/response ambiguity and active resolution;
- CED — downstream evidence licensing.

CREST asks what information must survive the common present cut when these responsibilities interact.

## Claim firewall

The finite flagship does **not** claim:

- that history, latent present, and future exhaust every legitimate ecological state responsibility;
- a unique natural decomposition of all ecological systems into these coordinates;
- statistical confounding;
- a continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, or approximate generality;
- that the activation order must follow chronological order.

The present is a zero-width observational cut in the finite representation, not a proved metaphysical or continuous-time instantaneous state.

## Anonymous review-code package

A deterministic whitelist-only review archive can now be generated locally:

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

The generated ZIP contains only the finite theorem implementation required for this paper, focused temporal-cut/interaction tests, the canonical numeric benchmark, a neutral README, and a SHA-256 manifest. It deliberately excludes `.git` history, provenance notes, empirical application material, public repository URLs, and submission metadata.

Regression tests verify that:

- the archive contains only the declared whitelist;
- the archive contains no repository-owner handle, GitHub URL, e-mail address, or ORCID token;
- repeated builds are byte-for-byte identical;
- every source file is hashed in the anonymous manifest; and
- after extraction, the focused temporal-cut theorem tests run successfully.

The upload location or anonymous repository/archive identifier remains author-controlled because it depends on the journal submission workflow.

## Submission blockers that remain author-controlled

1. **Anonymous code upload location.** The anonymous ZIP generator is complete; the remaining step is placing the generated archive on the journal-approved review surface without exposing author identity.
2. **Data and Code Accessibility Statement.** The journal requires a separate statement after Acknowledgments; final anonymous/archive identifiers must be inserted there and cited in Literature Cited.
3. **Generative-AI disclosure.** Current journal instructions require generative-AI use that contributed to content, analysis, code, or figures to be described transparently in the Methods section. The final wording must accurately describe the actual workflow used for the submitted version.
4. **Title page / author metadata.** Author names, affiliations, e-mails, ORCIDs, acknowledgments, funding, and contributions belong in the appropriate submission fields or title-page surface for double-anonymous review.
5. **PDF preparation.** Final review PDF needs double spacing, line numbers, page numbers, and embedded math fonts.

These are packaging/disclosure tasks, not missing mathematical results.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/verify_crest_philosophy_submission.py --write-report
```

The general pytest suite verifies the finite CREST theorem surface, including temporal-cut, temporal-interaction, joint-debt, sharp-family, AmNat manuscript-compliance, and anonymous-bundle regressions. `verify_crest_philosophy_submission.py` remains specific to the retained Biology & Philosophy manuscript. The flagship routing contract is pinned by `../docs/flagship_integration/flagship_integration_manifest.json` and its regression tests.
