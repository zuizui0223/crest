# CREST obstruction-spectrum comparison

## Purpose

The obstruction spectrum is most useful when two declared contracts can be compared on the same named responsibility set. The comparison surface answers a change question:

> Which part of the required state burden changed, and was the change direct, interaction-generated, or both?

For before/after spectra with the same named audits, CREST now reports changes in:

- required joint state count;
- joint state debt;
- standalone responsibility debts;
- Shapley responsibility attribution;
- per-responsibility interaction attribution; and
- exact Möbius/Harsanyi interaction dividends for every coalition.

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

Thus the entire increase in joint burden occurs with **zero change in all three standalone debts**. The comparison is therefore classified as

```text
interaction-only
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

- `CCOC × MLTR` contributes **+0.4150374993 bit**;
- `CCOC × MLTR × MRM` contributes **+0.3219280949 bit**;
- all other pairwise terms change by zero.

This comparison is the cleanest numeric demonstration that a system can become harder to represent jointly even when none of its responsibility-wise standalone scores changes.

## CLI

Single-contract spectrum:

```bash
python scripts/compute_obstruction_spectrum.py contract.json
```

Before/after comparison:

```bash
python scripts/compare_obstruction_spectra.py before.json after.json
```

The comparison output contains the complete before and after spectra plus a `comparison` object containing `change_class` and all numeric deltas.

## Interpretation firewall

The comparison algebra is standard finite cooperative-game accounting applied to the CREST coalition value function. CREST does not claim novelty for Shapley values, Möbius inversion, or Harsanyi dividends. The substantive CREST use is to quantify how declared ecological state responsibilities interact under a common finite-state construction.
