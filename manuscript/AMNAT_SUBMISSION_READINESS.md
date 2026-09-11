# The American Naturalist submission readiness

**Current target:** *The American Naturalist* — Major Article  
**Canonical manuscript:** `crest_flagship_amnat_v0.7_semantic_access.md`  
**Current text word count:** 4008  
**Purpose:** current submission-readiness surface for the AmNat flagship. The older `SUBMISSION_BLOCKERS_2026-08-24.md` is retained only as a historical Biology & Philosophy record.

## Repository-controlled status

- Canonical manuscript is fixed at `crest_flagship_amnat_v0.7_semantic_access.md`.
- The current scientific hierarchy is explicit: finite partition/quotient/transport results are supporting structural guarantees rather than independent mathematical novelty claims.
- The paper-level theoretical contribution is the separation of prerequisite order from semantic coverage at a temporal cut.
- The quantitative headline is the sparse-access degradation `log2(N/k)` relative to complete addressability.
- The zero-duration cut remains a finite idealization; no epsilon-to-zero continuous-time theorem is claimed.
- The shallow-lake model is presented as a worked ecological interpretation and executable formal witness, not empirical validation.
- The canonical manuscript remains well below the Major Article word ceiling at 4008 words by the repository's pinned counting method.
- Anonymous review-code bundle and anonymous title-page builders are implemented and covered by the reproducibility suite.

## Current AmNat review-format requirements tracked by the repository

Before literal upload, the review manuscript must be prepared with:

- double-anonymous review separation;
- abstract within 200 words;
- no more than six keywords/metadata entries as currently pinned;
- double spacing;
- continuous line numbering;
- page numbering;
- embedded math fonts in the final PDF;
- article type, short title, text word count, keywords, and manuscript elements supplied in the submission metadata/title-page workflow.

A cover letter is not treated as a blocker. Any necessary editor-facing note should be placed in the submission system's author-comments field.

## Remaining author-controlled fields

The repository cannot close these without author input or final approval:

1. final author list and order;
2. affiliations;
3. corresponding-author contact details;
4. ORCID identifiers, if used;
5. acknowledgements or an explicit none statement;
6. funding statement or an explicit no-funding statement;
7. competing-interests statement;
8. final author-contribution statement, if requested at submission;
9. final Data and Code Accessibility Statement identifying whether the anonymous review-code ZIP is uploaded directly or replaced by a reviewer-accessible anonymous repository identifier;
10. final generative-AI disclosure consistent with actual use and human verification;
11. confirmation that all authors approve submission and that the manuscript is not under consideration elsewhere.

## Machine-readable preflight

Run:

```bash
python scripts/check_amnat_submission_preflight.py
```

The report separates three states rather than collapsing them into one pass/fail flag:

- `repository_ready`: canonical manuscript, metadata, word count, abstract, keywords, short title, and builders are internally consistent;
- `author_fields_ready`: the supplied declarations file contains no unresolved bracketed author-controlled placeholders;
- `pdf_visual_and_font_gate_confirmed`: the final review PDF has been manually checked for spacing, line/page numbering, anonymity, equation rendering, and embedded fonts.

The default declarations input is the template, so `repository_ready=true` with `author_fields_ready=false` is the expected pre-submission state until the author supplies the final declarations. To test a completed nonblinded declarations file and explicitly confirm the PDF gate:

```bash
python scripts/check_amnat_submission_preflight.py \
  --declarations path/to/final_declarations.md \
  --pdf-verified
```

`literal_upload_ready` becomes true only when all three layers are closed. The CLI exits nonzero only for a repository-controlled failure; unresolved author fields are reported as blockers without making the reproducibility suite fail.

## Literal-upload gate

Repository-controlled work is complete only when all of the following succeed from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/build_amnat_title_page.py
python scripts/check_amnat_submission_preflight.py
```

The final review PDF must then be checked visually for double spacing, line numbering, page numbering, anonymity, equation rendering, and embedded fonts.

## Historical separation

`SUBMISSION_BLOCKERS_2026-08-24.md`, `crest_biology_philosophy_blinded_submission.md`, `CREST_supplementary_information.md`, `biology_philosophy_title_page_TEMPLATE.md`, and `crest_canonical_scope_2026-08-24.md` belong to the retained Biology & Philosophy submission surface. They are not current AmNat blockers and must not be used as the active submission checklist.
