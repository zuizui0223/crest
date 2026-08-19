# CREST — Contract-Relative Ecological State Theory

CREST is the cross-contract synthesis unit connecting four independent mathematical-ecology programs:

- **CCOC — future sufficiency:** which distinctions an enlarged future grammar can expose;
- **MLTR — semantic coherence:** which inherited ecological meanings survive structural change;
- **MRM — mechanism robustness:** which retained response alternatives support one prediction;
- **CED — evidential licensing:** which distinctions finite imperfect evidence permits reporting.

Its central representational principle is:

> Treating two ecological configurations as the same state is a scientific commitment about which differences may be ignored for a declared future, inherited meaning, retained mechanism family, evidence contract, and target.

The companion-level scientific spine is:

- present functional equivalence need not imply open-future causal equivalence;
- inherited ecological categories are historically and structurally conditional;
- visible-state equivalence need not support one mechanism-robust prediction; and
- a model-required distinction need not be an evidence-licensed report.

See [`docs/companion_spine_and_publication_decision_2026-08-19.md`](docs/companion_spine_and_publication_decision_2026-08-19.md).

## Current finite synthesis results

- **J1:** unique coarsest four-audit state and evidence gate;
- **J2:** faithful-lift invariance;
- **J3:** maximal universal common carrier or finite no-go certificate;
- **J4:** universal-carrier repair characterization;
- **J5:** one-sided lift refinement bounds;
- **J6:** maximal controlled common carrier and safe selector;
- **J7:** controlled-carrier repair characterization;
- **O1:** the cheapest carrier repair need not be the cheapest evidence-licensed repair.

J4-REPAIR and J7-REPAIR are NP-complete in general. The included solvers are exact finite exhaustive oracles, not polynomial-time claims.

## Ownership firewall

CREST owns only results that essentially couple two or more companion contracts. It does not absorb the headline theorems of CCOC, MLTR, MRM, or CED, and it claims no novelty for generic partition refinement, fixed points, safety games, model repair, weighted set cover, or abstraction morphisms.

## Publication sequence

The current decision is a **1 + 1 + 3 strategy**:

```text
CCOC full theorem paper / citable preprint
  -> CREST full Biology & Philosophy paper
  -> MLTR, MRM, and CED as independent focused full papers
```

Do not wait for four thin short reports before submitting CREST. Do not retarget the present philosophy manuscript to a broad general-ecology journal without a genuinely new cross-contract ecological theorem or worked application. See the [2026-08-19 decision](docs/companion_spine_and_publication_decision_2026-08-19.md); the [2026-08-18 sequence note](docs/publication_sequence_2026-08-18.md) is retained as the earlier decision record.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

## Provenance

The independent repository was migrated from `zuizui0223/mrm` at audited source SHA `72550fa8335cbffb901785f8a171c647b3cf8cc6`. Physical extraction is complete; see `PROVENANCE.md` and the synthesis proof ledger for theorem-level sources and boundaries.
