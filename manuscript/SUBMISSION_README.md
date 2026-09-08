# CREST manuscript and submission surfaces

## Current flagship

The current CREST flagship is:

**When Ecological Responsibilities Interact: Non-additive State Debt in Conservation Representation**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.2.md`.

Its headline quantity is

\[
\Delta=D_{\rm joint}-\sum_iD_i,
\]

with the marked-cycle extremum

\[
\Delta=\log_2 n-1,
\]

and the zero-debt boundary

\[
D_i=0\ \forall i\Longrightarrow D_{\rm joint}=\Delta=0.
\]

Carrier-gain no-bound and the sharp \(H\log_2r\) response-depth law are supporting results rather than the flagship headline. The mathematical novelty claim is deliberately limited: generic closure, fixed-point, partition-refinement, and marked-cycle machinery are classical substrate; CREST contributes the cross-responsibility ecological accounting interpretation on one declared common lift.

## Retained Biology & Philosophy bundle

The previous Biology & Philosophy submission surface remains intact for provenance and comparison:

**When Conservation Capacity Outgrows Conservation Knowledge: A Contract-Relative Theory of Ecological State**

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witnesses, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.
6. `../figures/crest_capacity_knowledge_paradox.svg` — Figure 1 source for that manuscript.

The legacy philosophy submission verifier intentionally continues to target `crest_biology_philosophy_blinded_submission.md`; it is not the verifier for the new Am Nat flagship.

## Current scientific spine

```text
temporally extended ecological worlds
→ declared scientific responsibilities
→ common admissible carrier
→ least-information joint state J
→ individual debts D_i
→ joint debt D_joint
→ interaction debt Delta
→ evidence licensing and reportability
```

The companion responsibilities remain separated:

- CCOC — future/composition obstruction;
- MLTR — inherited semantics/history obstruction;
- MRM — retained mechanism ambiguity versus active resolution;
- CED — downstream evidence licensing.

The synthesis asks what happens when these obligations act on one common state representation. A positive \(\Delta\) means responsibility-wise monitoring/state budgets underestimate the resolution required jointly.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

The general pytest suite verifies the finite CREST theorem surface, including joint-debt and sharp-family regressions. `verify_crest_philosophy_submission.py` remains specific to the retained Biology & Philosophy manuscript. The flagship routing contract is pinned by `../docs/flagship_integration/flagship_integration_manifest.json` and its regression tests.
