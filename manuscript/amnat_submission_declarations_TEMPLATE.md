# The American Naturalist submission declarations — TEMPLATE

This file is a submission-preparation surface, not part of the blinded manuscript. Replace every bracketed author-controlled field before submission. Do not upload author-identifying material inside the blinded review manuscript.

## 1. Data and Code Accessibility Statement

### Double-anonymous review version

> All code required to reproduce the finite mathematical and modeling results reported in this manuscript is supplied as an anonymized review-code ZIP uploaded directly with the submission in Editorial Manager. The archive contains the temporal-cut implementation, strict companion-realizability audit, companion semantic quotients, sparse semantic-access state quotient, focused regression tests, and the executable shallow-lake prerequisite audit. The shallow-lake component is a literature-grounded finite decision model rather than an empirical data analysis. The review archive is generated deterministically from a whitelist-only source package and excludes repository history and author-identifying metadata.

This direct-upload route is allowed by the journal's review policy and does not require a public author-identifying URL during double-anonymous review.

### Publication / post-acceptance version

> All code required to reproduce the finite mathematical and modeling results reported in this manuscript is archived at **[PUBLIC REPOSITORY OR DOI]**. The archived release contains the theorem implementation, semantic-access quotient, shallow-lake prerequisite audit, focused regression tests, and canonical numerical benchmarks. The archived software release is cited in the Literature Cited as **[SOFTWARE CITATION]**.

Do not substitute the public author-identifying repository URL into the blinded review version.

## 2. Generative-AI disclosure — author confirmation required

The final wording must describe the actual submitted workflow rather than a generic policy statement. The working draft below reflects the documented development workflow in this repository and conversation history; the author must confirm the verification clause before submission.

Working disclosure draft:

> Generative-AI tools were used during development of this work to assist with mathematical exploration, code drafting and review, literature-search assistance, manuscript drafting, and language revision. All theorem statements, proofs, numerical claims, citations, code included in the review package, and final manuscript text were **[AUTHOR TO CONFIRM THE ACTUAL HUMAN VERIFICATION PROCESS]**. The authors take responsibility for the accuracy and integrity of the submitted work.

Before submission, replace the remaining bracketed verification field with an exact account of human review. Do not state that an item was independently verified unless that verification was actually performed.

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

## 6. Review-code handoff

Generate the anonymous archive from a clean checkout with:

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

Before uploading, verify that the generated archive passes:

```bash
pytest tests/test_amnat_anonymous_bundle.py
```

Upload that ZIP directly to Editorial Manager for double-anonymous review. A public repository/DOI is a post-acceptance requirement, not an initial-submission blocker when the anonymous ZIP is supplied directly for review.

## 7. Final submission checklist

- [ ] Canonical manuscript is `crest_flagship_amnat_v0.7_semantic_access.md`.
- [ ] Blinded manuscript contains no author names, affiliations, acknowledgments, repository-owner handles, or identifying URLs.
- [ ] Abstract remains at or below 200 words.
- [ ] Keywords remain at or below 6.
- [ ] Anonymous review-code ZIP is uploaded directly with the submission.
- [ ] Generative-AI disclosure accurately describes the submitted workflow and human verification.
- [ ] Software/public archive citation is prepared for the nonblinded or accepted version as appropriate.
- [ ] Author contributions, funding, conflicts, and ORCID metadata are complete outside the blinded manuscript.
- [ ] Review PDF is double-spaced, line-numbered, page-numbered, and has embedded math fonts.
