# CREST manuscript and submission surfaces

## Current flagship

**Ecological State at a Temporal Cut: Sparse Semantic Access**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.7_semantic_access.md`.

The paper defines ecological state as the least information that must survive an observational temporal cut under a declared scientific contract.

The three motivating companion responsibilities remain non-circular and non-identical:

- **MLTR / history H:** primitive replacement histories first, complete carried-map equivalence second;
- **MRM / latent response Theta:** primitive candidate laws first, complete response-type equivalence second;
- **CCOC / future F:** controlled law plus exogenously declared legal query grammar, response quotient afterward.

## v0.7 scientific center

The flagship no longer treats full interface addressability as implicit.

It distinguishes two modeling objects:

1. the minimum prerequisite set of retained interfaces needed before a future target is well formed; and
2. the semantic access relation describing on which retained history-mode x response-type combinations the target is actually addressable.

If `N` semantic pairs exist, `k` are addressable, and an addressable future query distinguishes `2^m` exterior signatures, then the exact grand-coalition quotient is

\[
|Q_{H\Theta F}|=(N-k)+k2^m.
\]

When both H and Theta remain syntactic prerequisites, the three-way state dividend is

\[
d_{H\Theta F}=\log_2\frac{(N-k)+k2^m}{N}
\]

and approaches

\[
m-\log_2(N/k).
\]

Thus prerequisite order determines **where** the burden appears, while semantic coverage determines **how large** that burden is.

The canonical semantic witness has `N=4`, `k=1`. At `m=10` it gives:

- history + mechanism: 4 classes / 2 bits;
- grand coalition: **1027 classes / 10.00422 bits**;
- three-way dividend: **8.00422 bits**;
- asymptotic sparsity penalty relative to full access: **2 bits**.

The older 4096-class / 12-bit / 10-bit-three-way result is retained only as the complete-access boundary `k=N=4`.

## Realizability no-go remains a main result

The paper keeps three strict boundaries before the positive construction:

1. fixed precomputed partitions on a one-class baseline cannot generate positive interaction by common refinement alone;
2. a zero-debt post-cut audit preserving immutable MLTR history cannot later be activated by rewriting that history;
3. candidate-safe zero debt under one fixed MRM grammar implies a singleton response type.

These results prevent older abstract closure cascades from being overinterpreted as literal companion models.

## Executable shallow-lake prerequisite audit

The shallow-lake worked case is now an executable finite decision model rather than a markdown-only target table. Four worlds behind one coarse visible status cross two retrospective modes with two latent-response types. The code tests target factorization and counterfactual substitution of each interface.

It returns:

- current status: `R = empty`;
- legacy-sensitive recovery: `R = {H}`;
- mechanism-specific intervention: `R = {Theta}`;
- composed restoration policy: `R = {H,Theta}`.

This is **literature-grounded conceptual modeling, not empirical validation** and not a universal claim about shallow lakes.

## Novelty boundary

The flagship does **not** claim mathematical novelty for:

- Möbius/Harsanyi inversion;
- unanimity games;
- quotient state abstraction;
- finite counting after an access relation is fixed.

The contribution is the modeling architecture: non-circular companion semantics, strict realizability boundaries, target-relative interface-prerequisite identification, explicit semantic access coverage, and propagation of both objects into one exact temporal-cut state quotient.

## Retained predecessor manuscripts

- `crest_flagship_amnat_v0.6_addressability.md` — complete-addressability predecessor;
- `crest_flagship_amnat_v0.5_compositional.md` — pre-characterization draft;
- `crest_flagship_amnat_v0.4_positioned.md`, `v0.3`, `v0.2` — provenance drafts.

All remain noncanonical.

## Retained Biology & Philosophy bundle

The earlier philosophy-facing submission surface remains intact for provenance and comparison and is deliberately separate from the AmNat flagship:

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — retained supplementary definitions and worked-case material.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — historical author-controlled blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.

The legacy verifier continues to target `crest_biology_philosophy_blinded_submission.md`; it is not the AmNat verifier.

## Current scientific spine

```text
possible ecological worlds Omega
-> observational temporal cut O_t
-> companion semantic outputs
-> strict realizability no-go
-> target prerequisite identification
-> semantic access relation A_f
-> legal semantic traces
-> induced quotient Q_S
-> interaction accounting
-> evidence licensing downstream
```

## Claim firewall

The flagship does **not** claim:

- that history, latent response, and future are independent ontic coordinates;
- that they exhaust every ecological state responsibility;
- that all legal future grammars require both companion interfaces;
- that semantic access is complete across the interface product;
- that prerequisite sets or access relations can be inferred from state accounting alone;
- that the shallow-lake decision model is empirical validation;
- statistical confounding;
- continuous-time, stochastic, infinite-state, or approximate generality.

## Anonymous review-code package

Generate the deterministic whitelist-only review archive with

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

The v0.7 archive contains the minimal code needed for:

- temporal-cut representation;
- strict companion-realizability checks;
- companion semantic quotients;
- sparse semantic access;
- semantic trace-equivalence quotient calculation;
- exact `N-k+k*2^m` benchmark checks;
- executable shallow-lake prerequisite and counterfactual-substitution audit.

## Submission blockers that remain author-controlled

1. **Anonymous code upload location.** The generator is complete; the review-safe upload surface depends on the journal workflow.
2. **Data and Code Accessibility Statement.** Insert the final anonymous/archive identifier in `amnat_submission_declarations_TEMPLATE.md`.
3. **Generative-AI disclosure.** Confirm actual uses and human verification.
4. **Title page / author metadata.** Names, affiliations, e-mails, ORCIDs, acknowledgments, funding, contributions, and conflicts stay outside the blinded manuscript.
5. **PDF preparation.** Final review PDF needs journal-required spacing, line/page numbering, and embedded math fonts.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
```

The general pytest suite verifies the temporal-cut surface, definition firewall, strict realizability no-go, semantic-access quotient, shallow-lake prerequisite audit, AmNat manuscript compliance, and anonymous review bundle.
