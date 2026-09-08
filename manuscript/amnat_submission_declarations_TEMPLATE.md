# The American Naturalist submission declarations — TEMPLATE

This file is a submission-preparation surface, not part of the blinded manuscript. Replace every bracketed field before submission. Do not upload author-identifying material inside the blinded review manuscript.

## 1. Data and Code Accessibility Statement

### Double-anonymous review version

> All code required to reproduce the finite mathematical results reported in this manuscript is provided in an anonymized review archive at **[ANONYMOUS REVIEW ARCHIVE OR JOURNAL FILE IDENTIFIER]**. The archive contains the minimal theorem implementation, focused regression tests, and the canonical numerical benchmark used in the manuscript. No empirical data are analyzed in this study. The review archive is generated deterministically from a whitelist-only source package and excludes repository history and author-identifying metadata.

### Publication / post-acceptance version

> All code required to reproduce the finite mathematical results reported in this manuscript is archived at **[PUBLIC REPOSITORY OR DOI]**. The archived release contains the theorem implementation, focused regression tests, and the canonical numerical benchmark. No empirical data are analyzed in this study. The archived software release is cited in the Literature Cited as **[SOFTWARE CITATION]**.

Do not substitute the public author-identifying repository URL into the blinded review version.

## 2. Generative-AI disclosure — author confirmation required

The journal's current instructions require transparent disclosure when generative-AI tools contributed to manuscript content, analysis, code, or figures. The final wording must describe the actual submitted workflow rather than a generic policy statement.

Working disclosure draft:

> Generative-AI tools were used during development of this work to assist with **[SELECT ALL THAT APPLY: mathematical exploration / code drafting / code review / literature-search assistance / manuscript drafting / language revision / figure preparation]**. All theorem statements, proofs, numerical claims, citations, code included in the review package, and final manuscript text were **[AUTHOR TO CONFIRM THE ACTUAL HUMAN VERIFICATION PROCESS]**. The authors take responsibility for the accuracy and integrity of the submitted work.

Before submission, replace the bracketed fields with an exact account of use. Do not state that an item was independently verified unless that verification was actually performed.

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

The final anonymous archive location is then inserted into Section 1 above.

## 7. Final submission checklist

- [ ] Canonical manuscript is `crest_flagship_amnat_v0.4_positioned.md`.
- [ ] Blinded manuscript contains no author names, affiliations, acknowledgments, repository-owner handles, or identifying URLs.
- [ ] Abstract remains at or below 200 words.
- [ ] Keywords remain at or below 6.
- [ ] Data and Code Accessibility Statement contains the correct anonymous review identifier.
- [ ] Generative-AI disclosure accurately describes the submitted workflow.
- [ ] Software/public archive citation is prepared for the nonblinded or accepted version as appropriate.
- [ ] Author contributions, funding, conflicts, and ORCID metadata are complete outside the blinded manuscript.
- [ ] Review PDF is double-spaced, line-numbered, page-numbered, and has embedded math fonts.
