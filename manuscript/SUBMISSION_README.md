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
ECOLOGICAL-STATE PROBLEM
when should different ecological worlds count as the same state?
→ temporally extended ecological worlds
→ contract-relative state sameness
→ quotient-level ecological laws

FINITE MATHEMATICS
finite carrier
→ least-information required state
→ evidence licensing
→ capability–resolution divergence

ECOLOGICAL CONSEQUENCES
current functional equivalence need not survive a changed future responsibility
→ history and mechanism matter only when response-relevant
→ monitoring success need not identify full state
→ representational stability differs from dynamical stability
→ conservation/management repertoire changes require state-adequacy re-audit
```

The theorem-level headline is

\[
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m
\]

for arbitrary finite \(m\), with full-state licensing lost under fixed evidence while a coarse target remains reportable.

The novelty claim is deliberately narrow: CREST does **not** claim novelty for purpose-relative adequacy, predictive equivalence, POMDP/PSR expressivity, state/action abstraction coupling, ecological history dependence, or generic partition refinement. The defended contribution is the ecology-specific separation of admissible worlds, task-required state, evidence-identified state, reportable target, and quotient-law validity, together with the connected no-bound construction across these layers.

## Verified submission state

- Abstract: 216 words
- Main text before References: 5,818 words
- Keywords: 6
- Double-blind identifier hits: 0
- Automated blockers: 0
- Active regression suite: 132 tests passed
- Submission verifier: pass

Run:

```bash
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
git diff --check
test -z "$(git status --porcelain)"
```

The deterministic verifier record is `../artifacts/crest_philosophy_submission_report.json`.
