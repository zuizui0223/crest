# CREST batch obstruction ranking

## Purpose

Single-contract obstruction spectra answer how much state resolution one declared contract requires. The batch surface answers the next operational question:

> Given several commensurable finite contracts, which one consumes more representational capacity, and which one is more interaction-dominated?

For each named contract the batch report includes:

- carrier worlds;
- baseline and joint state counts;
- raw joint debt in bits;
- normalized joint burden;
- interaction and direct fractions of realized joint debt;
- non-additive excess `Delta`;
- active interaction orders; and
- dominant interaction order.

Contracts can be ranked by `normalized_joint_burden`, `joint_debt_bits`, `interaction_fraction_of_joint`, or `delta_bits`.

## Canonical two-contract comparison

On the same six-world carrier and two-state baseline:

| contract | joint states | joint debt | normalized burden | interaction fraction |
|---|---:|---:|---:|---:|
| inert MLTR/MRM | 3 | 0.5849625007 bit | **0.3690702464** | **0** |
| full CCOC→MLTR→MRM cascade | 5 | 1.3219280949 bit | **0.8340437671** | **0.5574929507** |

The full cascade therefore uses much more of the same available refinement capacity, and more than half of its realized joint debt is interaction-generated.

This is stronger than comparing state counts alone: both contracts live on the same carrier and baseline, so the normalized change identifies how much of the available representational capacity the added cross-obstruction activation consumes.

## CLI

```bash
python scripts/rank_obstruction_contracts.py contract_a.json contract_b.json
```

Alternative ranking:

```bash
python scripts/rank_obstruction_contracts.py --rank-by interaction_fraction_of_joint contract_a.json contract_b.json
```

## Comparability firewall

The implementation requires the same named responsibility set, but that is only a machine-checkable minimum. Scientific ranking across different systems is justified only when carrier construction and baseline semantics are commensurable. Raw bits and normalized scores remain contract-relative.
