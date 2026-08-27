# CREST Biology & Philosophy submission bundle

## Manuscript identity

**When Conservation Capacity Outgrows Conservation Knowledge: A Contract-Relative Theory of Ecological State**

The paper asks when different ecological worlds should count as the same state and uses the capability–resolution theorem to formalize the conservation asymmetry that a new management capability can make an old state description inadequate before the intervention is executed.

## Submission-facing files

1. `crest_biology_philosophy_blinded_submission.md` — blinded main manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witness, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — manuscript-scope contract.
6. `../figures/crest_capacity_knowledge_paradox.svg` — Figure 1 source.

Superseded drafts and development inserts remain preserved outside the active submission surface.

## Scientific spine

```text
CONSERVATION PARADOX
new management capability
→ previously irrelevant ecological differences can become response-relevant
→ old state description can lose adequacy

ECOLOGICAL STATE
possible ecological worlds
→ well-posed scientific responsibility
→ justified state equivalence
→ quotient-level ecological law

WORKED ECOLOGY
shallow-lake restoration
→ same current turbid status
→ sediment legacy vs food-web feedback
→ mechanism-specific actions force a state split
→ routine evidence can remain too coarse

FINITE THEORY
carrier feasibility
→ least-information required state
→ evidence licensing
→ capability–resolution divergence

CONCLUSION
conservation capacity can outgrow conservation knowledge
```

The theorem-level headline remains

\[
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m
\]

for arbitrary finite \(m\), with full-state licensing lost under fixed evidence while a coarse target remains reportable.

## Novelty position

CREST does not claim novelty for purpose-relative adequacy, predictive equivalence, POMDP/PSR expressivity, state/action abstraction coupling, ecological history dependence, multiple realization, or generic partition refinement.

The defended contribution is:

1. an ecology-specific separation of admissible worlds, task-required state, evidence-identified state, reportable target, and quotient-law validity;
2. explicit well-posedness conditions preventing contract-relativity from becoming arbitrary relabelling;
3. one connected finite no-bound construction across carrier, state, evidence, and target layers;
4. the conservation consequence that capability gain can increase state-information requirements before ecological intervention occurs.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

The automated suite verifies the finite theorem constructions and the submission verifier checks abstract length, keyword count, blinded identifiers, canonical manuscript sections, philosophical positioning, and theorem headline.

The deterministic verifier record is `../artifacts/crest_philosophy_submission_report.json`.
