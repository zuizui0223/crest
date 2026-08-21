# eco-contract-core

`eco-contract-core` is a deliberately neutral finite-state substrate shared by the CREST companion programs.

It provides only generic computational contracts:

- declared finite states and actions;
- deterministic transitions and legal-action rows;
- canonical partitions and block indexes;
- stable partition refinement by output/action/successor signatures;
- deterministic replay;
- canonical SHA-256 fingerprints.

## Scientific ownership boundary

This package **does not own or implement the headline claims** of CCOC, MLTR, MRM, CED, or CREST. In particular it does not define:

- open-grammar compression lower bounds (CCOC);
- replacement transport, semantic repair, or transport defect (MLTR);
- mechanism-safe laws or ambiguity frontiers (MRM);
- evidence-induced reportability or risk-limited resolution (CED);
- CREST joint-state theorems or carrier results.

Those remain in their scientific repositories. Generic partition refinement is infrastructure, not a novelty claim.

## Install from this staging directory

```bash
python -m pip install ./packages/eco-contract-core
```

For development:

```bash
python -m pip install -e './packages/eco-contract-core[dev]'
pytest packages/eco-contract-core/tests
```

## Extraction plan

This directory is intentionally self-contained so it can later move unchanged into a dedicated `eco-contract-core` repository. Companion repositories should migrate only after parity tests show that replacing local substrate code does not alter theorem witnesses, fingerprints, or replay outputs.
