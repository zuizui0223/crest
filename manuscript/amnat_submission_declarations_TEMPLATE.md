# The American Naturalist submission declarations — TEMPLATE

This file is a submission-preparation surface, not part of the blinded manuscript. Replace the remaining bracketed author/publication fields before submission. Do not upload author-identifying material inside the blinded review manuscript.

## 1. Data and Code Accessibility Statement

### Double-anonymous review version

> All code required to reproduce the finite mathematical and modeling results reported in this manuscript is supplied as an anonymized review ZIP uploaded directly with the Editorial Manager submission. The archive contains the temporal-cut implementation, strict companion-realizability audit, companion semantic quotients, sparse semantic-access state quotient, focused regression tests, and the executable shallow-lake prerequisite audit, together with a README describing reproduction steps. The shallow-lake component is a literature-grounded finite decision model rather than an empirical data analysis. The review archive is generated deterministically from a whitelist-only source package and excludes repository history and author-identifying metadata.

### Publication / post-acceptance version

> All code required to reproduce the finite mathematical and modeling results reported in this manuscript is archived at **[PUBLIC REPOSITORY OR DOI]**. The archived release contains the theorem implementation, semantic-access quotient, shallow-lake prerequisite audit, focused regression tests, and canonical numerical benchmarks. The archived software release is cited in the Literature Cited as **[SOFTWARE CITATION]**.

Do not substitute a public author-identifying repository URL into the blinded review version.

## 2. Generative-AI disclosure

The review manuscript is assembled with the canonical disclosure stored at `docs/amnat_ai_disclosure_2026-09-09.md` and inserted as Section 11.1, **Reproducibility methods and AI-assisted development**.

Canonical disclosure:

> Generative AI tools were used during mathematical exploration, code drafting and troubleshooting, literature-search assistance, and manuscript drafting and language revision. AI outputs were treated as provisional and were accepted only after human review. Human verification included direct review and editing of the submitted manuscript and code, execution of the full automated test suite across supported Python versions, and independent recomputation of key finite-state numerical claims, including the sparse-access benchmarks and broader parameter sweeps. The submitting authorship retains full responsibility for all content.

This wording reflects the documented submitted workflow. Do not weaken the human-verification language or add uses such as figure generation unless they actually occurred.

## 3. Author contribution statement — nonblinded submission metadata

Use the journal's required taxonomy or contribution format if the submission system specifies one.

- Conceptualization: **[NAME(S)]**
- Formal analysis: **[NAME(S)]**
- Methodology: **[NAME(S)]**
- Software: **[NAME(S)]**
- Validation: **[NAME(S)]**
- Visualization: **[NAME(S)]**
- Writing — original draft: **[NAME(S)]**
- Writing — review and editing: **[NAME(S)]**
- Supervision: **[NAME(S), IF APPLICABLE]**
- Funding acquisition: **[NAME(S), IF APPLICABLE]**

## 4. Author and affiliation metadata — nonblinded surface

- Corresponding author: **[NAME]**
- Affiliation(s): **[AFFILIATION(S)]**
- E-mail: **[EMAIL]**
- ORCID: **[ORCID]**
- Current address, if required: **[ADDRESS]**

Keep these fields out of the blinded review manuscript and anonymous code archive.

## 5. Acknowledgments and funding

Acknowledgments:

> **[ACKNOWLEDGMENTS OR `None` IF PERMITTED]**

Funding:

> **[FUNDER / GRANT NUMBER / `No external funding` AS ACCURATE]**

Conflicts of interest:

> **[DECLARATION]**

## 6. Review-code and review-manuscript handoff

Generate the anonymous code archive from a clean checkout with:

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

Generate the exact review manuscript, including the AI disclosure, with:

```bash
python scripts/build_amnat_review_manuscript.py
python scripts/build_amnat_title_page.py
```

Before uploading, verify the full test suite and anonymous bundle checks pass. The anonymous code ZIP can be uploaded directly to Editorial Manager; an external anonymous repository link is optional for review.

## 7. Final submission checklist

- [ ] Scientific source manuscript is `crest_flagship_amnat_v0.7_semantic_access.md`.
- [ ] Review manuscript is generated with `scripts/build_amnat_review_manuscript.py` and contains Section 11.1 AI disclosure.
- [ ] Blinded manuscript contains no author names, affiliations, acknowledgments, repository-owner handles, or identifying URLs.
- [ ] Abstract remains at or below 200 words.
- [ ] Keywords remain at or below 6.
- [ ] Review title-page word count matches `amnat_submission_metadata.json`.
- [ ] Anonymous review-code ZIP is attached in Editorial Manager or an equivalent reviewer-accessible anonymous link is supplied.
- [ ] Software/public archive citation is prepared for the nonblinded or accepted version as appropriate.
- [ ] Author contributions, funding, conflicts, and ORCID metadata are complete outside the blinded manuscript.
- [ ] Review PDF is double-spaced, line-numbered, page-numbered, and has embedded math fonts.
