# CREST manuscript and submission surfaces

## Current flagship

**Ecological State at a Temporal Cut: Sparse Semantic Access**  
Target: **The American Naturalist — Major Article**  
Canonical manuscript: `crest_flagship_amnat_v0.7_semantic_access.md`.

CREST treats the present as a zero-duration observational cut and defines ecological state as the least quotient induced on that cut by retrospective, transverse latent-present, and prospective distinguishability constraints.

The three companion responsibilities remain non-circular and non-identical:

- **MLTR / retrospective H:** primitive replacement histories first, complete carried-map equivalence second; left-of-cut structure.
- **MRM / transverse latent present Theta:** primitive candidate laws first, complete response-type equivalence second; hidden response structure within the observation fiber, without claiming full ontic mechanism identity.
- **CCOC / prospective F:** controlled law plus exogenously declared right-of-cut query grammar, response quotient afterward.

## v0.7 scientific center

The flagship distinguishes two structures controlling prospective refinement of the cut-state:

1. the minimum prerequisite set of retained interfaces needed before a future target is well formed; and
2. the semantic access relation describing on which retained history-mode x response-type combinations that target is actually addressable.

If `N` semantic pairs exist, `k` are addressable, and an addressable future query distinguishes `2^m` exterior signatures, then

\[
|Q_{H\Theta F}|=(N-k)+k2^m.
\]

When both H and Theta remain syntactic prerequisites,

\[
d_{H\Theta F}=\log_2\frac{(N-k)+k2^m}{N}
\]

and asymptotically

\[
d_{H\Theta F}=m-\log_2(N/k)+o(1).
\]

Prerequisite order determines **where** the burden appears; semantic coverage determines **how large** it is. The canonical witness has `N=4`, `k=1`; at `m=10` the grand coalition has 1027 classes / 10.00422 bits and the three-way dividend is 8.00422 bits. The earlier 4096-class / 12-bit / 10-bit-three-way result is retained only as the complete-access boundary `k=N=4`.

## Realizability no-go

The paper keeps three strict boundaries before the positive construction:

1. fixed precomputed partitions on a one-class baseline cannot generate positive interaction by common refinement alone;
2. a zero-debt post-cut audit preserving immutable MLTR history cannot later be activated by rewriting that history;
3. candidate-safe zero debt under one fixed MRM grammar implies a singleton response type.

These results prevent older abstract closure cascades from being overinterpreted as literal companion models.

## Supporting finite mathematics and novelty boundary

The finite partition/quotient/transport spine is **structural support, not a claim of new partition theory**. Common refinement, its unique-coarsest characterization, representation-equivalence of signature families, and the deterministic transport descent condition are treated as elementary finite-structure guarantees that make the cut-state construction well defined, representation safe, and composable when the declared evolution respects the quotient.

The flagship therefore does **not** claim mathematical novelty for Möbius/Harsanyi inversion, unanimity games, generic quotient-state abstraction, common-refinement lattice facts, or finite counting once an access relation is fixed.

The **paper-level theoretical contribution** is the separation of prerequisite order from semantic coverage at a temporal cut, together with the non-circular retrospective/transverse/prospective construction and strict realizability boundaries. The **quantitative headline** is the sparse-access degradation `log2(N/k)` relative to complete addressability.

The phrase `zero-duration cut` remains a finite idealization. The manuscript does not claim an epsilon-to-zero continuous-time limit theorem, continuous-time germ theorem, stochastic generality, approximate-state theorem, or infinite-state extension.

## Executable shallow-lake audit

The shallow-lake worked case is an ecological interpretation with an executable finite model, not empirical validation. Four worlds behind one coarse visible status cross two retrospective modes with two latent-response types. Target factorization and counterfactual substitution return:

- current status: `R = empty`;
- legacy-sensitive recovery: `R = {H}`;
- mechanism-specific intervention: `R = {Theta}`;
- composed restoration diagnostic: `R = {H,Theta}`.

The exact parity-style two-output map is a minimal formal witness of joint dependence rather than a biological law asserted by the restoration literature.

## AmNat submission metadata

Machine-readable metadata: `amnat_submission_metadata.json`  
Current pinned text word count: **4008**  
Short title: **Sparse Semantic Access**.

Generate the anonymous title-page metadata with:

```bash
python scripts/build_amnat_title_page.py
```

Default output: `dist/amnat_anonymous_title_page.md`.

The reported text word count is computed reproducibly from Introduction through Conclusion without subtracting display/inline mathematics or table rows. Literature Cited is outside the count.

## Current submission-readiness checklist

Use **`AMNAT_SUBMISSION_READINESS.md`** as the active blocker/readiness surface for the flagship. It separates repository-controlled checks from author-controlled fields and the literal-upload PDF gate.

The older `SUBMISSION_BLOCKERS_2026-08-24.md` is historical and belongs to the retained Biology & Philosophy submission surface; it is not the active AmNat checklist.

## Anonymous review-code package

Generate the deterministic whitelist-only review archive with:

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output: `dist/anonymous_review_code.zip`.

The v0.7 archive contains the minimal code needed for temporal-cut representation, strict companion-realizability checks, companion semantic quotients, sparse semantic access, semantic trace-equivalence quotient calculation, exact `N-k+k*2^m` benchmark checks, and the executable shallow-lake prerequisite/counterfactual-substitution audit.

## Remaining author-controlled fields

Author-controlled items are tracked in `AMNAT_SUBMISSION_READINESS.md`: final author metadata, affiliations/contact details, ORCIDs if used, acknowledgements, funding, conflicts, author contributions if requested, final Data and Code Accessibility wording, final generative-AI disclosure, and confirmation of author approval / no simultaneous consideration.

The final review PDF must be checked visually for double spacing, line numbering, page numbering, anonymity, equation rendering, and embedded math fonts. A cover letter is not treated as a blocker; necessary editor-facing notes belong in the submission system's author-comments field.

## Retained predecessor and historical surfaces

Noncanonical AmNat predecessors remain for provenance: `crest_flagship_amnat_v0.6_addressability.md`, `crest_flagship_amnat_v0.5_compositional.md`, `crest_flagship_amnat_v0.4_positioned.md`, `v0.3`, and `v0.2`.

The earlier Biology & Philosophy bundle is retained separately: `crest_biology_philosophy_blinded_submission.md`, `CREST_supplementary_information.md`, `biology_philosophy_title_page_TEMPLATE.md`, `SUBMISSION_BLOCKERS_2026-08-24.md`, and `crest_canonical_scope_2026-08-24.md`. The legacy verifier remains separate from the AmNat verifier.

## Current scientific spine

```text
raw ecological possibilities Omega
-> zero-duration observational cut O_t
-> visible-cut fibers O_t^{-1}(y)
-> retrospective / transverse / prospective pre-state structures
-> strict realizability no-go
-> prerequisite structure + semantic access relation A_f
-> legal prospective traces
-> least induced cut-state quotient Q_S
-> interaction accounting
-> ecological interpretation / evidence downstream
```

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/build_amnat_title_page.py
```

The test suite verifies the temporal-cut surface, definition firewall, strict realizability no-go, semantic-access quotient, shallow-lake prerequisite audit, AmNat manuscript compliance, submission metadata, generated anonymous title page, and anonymous review bundle.
