# CREST obstruction-spectrum comparison

## Purpose

The obstruction spectrum is most useful when two declared contracts can be compared on the same named responsibility set. The comparison surface answers a change question:

> Which part of the required state burden changed, was the change direct or interaction-generated, did burden increase or decrease, and at what interaction order did the change occur?

For before/after spectra with the same named audits, CREST now reports changes in:

- required joint state count;
- joint state debt and its direction (`increase`, `decrease`, `unchanged`);
- standalone responsibility debts;
- Shapley responsibility attribution;
- per-responsibility interaction attribution;
- exact Möbius/Harsanyi interaction dividends for every coalition; and
- interaction change aggregated by coalition order.

The comparison is conditional on each declared finite carrier and baseline. A numeric difference is therefore a contract-relative representational change, not an intrinsic ecological constant.

## Exact accounting identity

For before/after changes,

\[
\delta D_{\rm joint}
=
\sum_i\delta D_i
+
\delta\Delta.
\]

Because singleton Möbius dividends are the standalone debts,

\[
\delta\Delta
=
\sum_{|S|\ge2}\delta m(S).
\]

Therefore if every standalone debt is unchanged, the entire change in joint debt is interaction-generated:

\[
\boxed{
\delta D_i=0\ \forall i
\Longrightarrow
\delta D_{\rm joint}=\delta\Delta
=
\sum_{|S|\ge2}\delta m(S).
}
\]

The implementation classifies every comparison into one of four diagnostic classes:

| class | standalone change | interaction change |
|---|---|---|
| `direct-only` | yes | no |
| `interaction-only` | no | yes |
| `mixed` | yes | yes |
| `null` | no | no |

These labels are accounting diagnostics, not causal categories supplied by nature.

## Direction and interaction order

Three separate directions are reported:

- `joint_debt_direction` for \(\delta D_{\rm joint}\);
- `direct_direction` for \(\sum_i\delta D_i\); and
- `interaction_direction` for \(\delta\Delta\).

Each is `increase`, `decrease`, or `unchanged` at the declared numerical tolerance.

The Möbius changes are also aggregated by order,

\[
M_k
=
\sum_{|S|=k}\delta m(S).
\]

Thus

\[
\delta D_{\rm joint}=\sum_{k\ge1}M_k,
\qquad
M_1=\sum_i\delta D_i,
\qquad
\delta\Delta=\sum_{k\ge2}M_k.
\]

The comparison reports all nonzero `active_interaction_orders` with \(k\ge2\), and the `dominant_interaction_order` is the active order with the largest absolute \(|M_k|\), breaking exact ties toward the smaller order. This is a compact anatomy of whether representational change is primarily pairwise, three-way, or higher-order.

## Canonical comparison

Use the six-world CCOC/MLTR/MRM witness in two configurations.

**Before:** CCOC can split one state, while MLTR and MRM transitions are inert relative to the baseline.

**After:** the full activation chain is enabled:

```text
CCOC split
   ↓
activates MLTR split
   ↓
activates MRM split
```

The before contract requires 3 states from the 2-state baseline. The after contract requires 5.

| quantity | before | after | change |
|---|---:|---:|---:|
| joint states | 3 | 5 | **+2** |
| joint debt | 0.584963 bit | 1.321928 bit | **+0.736966 bit** |
| standalone CCOC | 0.584963 | 0.584963 | **0** |
| standalone MLTR | 0 | 0 | **0** |
| standalone MRM | 0 | 0 | **0** |

Thus the entire increase in joint burden occurs with **zero change in all three standalone debts**. The compact diagnosis is

```text
change_class            interaction-only
joint_debt_direction    increase
direct_direction        unchanged
interaction_direction   increase
active_interaction_orders  [2, 3]
dominant_interaction_order 2
```

The added burden decomposes exactly as

\[
0.7369655942
=
0.4150374993
+
0.3219280949
\quad\text{bits},
\]

where

- order 2, `CCOC × MLTR`, contributes **+0.4150374993 bit**;
- order 3, `CCOC × MLTR × MRM`, contributes **+0.3219280949 bit**;
- all other pairwise terms change by zero.

Therefore 56.3% of the interaction-generated increase is pairwise and 43.7% is genuinely three-way in this witness. The reverse comparison is classified as the same `interaction-only` source class but with `joint_debt_direction=decrease` and both active-order contributions negative.

This comparison is the cleanest numeric demonstration that a system can become harder—or easier—to represent jointly even when none of its responsibility-wise standalone scores changes.

## CLI

Single-contract spectrum:

```bash
python scripts/compute_obstruction_spectrum.py contract.json
```

Before/after comparison:

```bash
python scripts/compare_obstruction_spectra.py before.json after.json
```

The comparison output contains the complete before and after spectra plus a `comparison` object containing the source class, directions, interaction-order anatomy, and all numeric deltas.

## Interpretation firewall

The comparison algebra is standard finite cooperative-game accounting applied to the CREST coalition value function. CREST does not claim novelty for Shapley values, Möbius inversion, Harsanyi dividends, or grouping dividends by coalition order. The substantive CREST use is to quantify how declared ecological state responsibilities interact under a common finite-state construction.
