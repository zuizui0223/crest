# CREST Biology & Philosophy submission bundle

## Canonical submission spine

Only these five files are first-class manuscript-facing artifacts:

1. `crest_biology_philosophy_blinded_submission.md` — blinded review manuscript.
2. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page.
3. `SUBMISSION_README.md` — this bundle map.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — philosophy → finite mathematics → ecological projection scope contract.

Superseded manuscripts, handoffs, title pages, and integrated inserts are preserved under
`../archive/graphify-cleanup-2026-08-24/manuscript/`.

## Scientific spine

```text
PHILOSOPHY
temporally extended ecological worlds
→ contract-relative state sameness
→ quotient-level ecological laws

MATHEMATICS
finite carrier
→ least-information required state
→ evidence licensing
→ capability–resolution divergence

ECOLOGY
state variables are conditional compressions
→ functional equivalence is future-relative
→ history and mechanism matter only when response-relevant
→ monitoring success need not identify full state
→ representational stability differs from dynamical stability
```

The theorem-level headline is

\[
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m
\]

for arbitrary finite \(m\), with full-state licensing lost under fixed evidence while a coarse target remains reportable.

## Verified submission state

- Abstract: 216 words
- Main text before References: 5,810 words
- Keywords: 6
- Double-blind identifier hits: 0
- Automated blockers: 0
- Full regression suite at cleanup: 133 tests passed

Run:

```bash
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

The deterministic verifier record is `../artifacts/crest_philosophy_submission_report.json`.
