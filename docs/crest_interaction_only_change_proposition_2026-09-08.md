# CREST interaction-only contract-change proposition

## Purpose

The before/after obstruction-spectrum comparison admits a simple but useful exact identity. It tells us when a change in required ecological state resolution is generated entirely by cross-responsibility interaction rather than by any responsibility becoming more demanding in isolation.

Let two finite CREST contracts on the same named responsibility set have coalition-debt games `v^-` and `v^+`, with standalone debts

\[
D_i^- = v^-(\{i\}),\qquad D_i^+ = v^+(\{i\}),
\]

joint debts

\[
D_{\rm joint}^- = v^-(N),\qquad D_{\rm joint}^+ = v^+(N),
\]

and non-additive excesses

\[
\Delta^- = D_{\rm joint}^- - \sum_i D_i^-,\qquad
\Delta^+ = D_{\rm joint}^+ - \sum_i D_i^+.
\]

Define before/after changes with the prefix `delta`, for example

\[
\delta D_{\rm joint}=D_{\rm joint}^+-D_{\rm joint}^-.
\]

## Proposition — interaction-only change identity

If every standalone debt is unchanged,

\[
\delta D_i=0\qquad\text{for all }i,
\]

then

\[
\boxed{\delta D_{\rm joint}=\delta\Delta.}
\]

If `m(S)` denotes the Möbius/Harsanyi interaction dividend of coalition `S`, then because singleton dividends equal standalone debts,

\[
\boxed{
\delta D_{\rm joint}
=
\sum_{|S|\ge 2}\delta m(S).
}
\]

So a change in required state resolution can occur even when no named responsibility changes its isolated burden. In that case the entire change is interaction-generated.

### Proof

Subtract the two definitions of `Delta`:

\[
\delta\Delta
=
\delta D_{\rm joint}-\sum_i\delta D_i.
\]

If every `delta D_i` vanishes, then `delta Delta = delta D_joint`. The Möbius decomposition satisfies

\[
D_{\rm joint}=\sum_{\varnothing\ne S\subseteq N}m(S),
\]

and singleton terms are exactly `m({i})=D_i`. Subtracting before from after and using `delta D_i=0` leaves only coalitions of order at least two.

This is an accounting identity, not a new generic cooperative-game theorem. Its CREST role is diagnostic: it cleanly distinguishes a contract change that makes individual responsibilities harder from one that makes their composition harder.

## Canonical CCOC/MLTR/MRM comparison

The current executable comparison uses a before contract in which only the CCOC-triggered split propagates no further, and an after contract in which the same CCOC split activates MLTR and then MRM.

| quantity | before | after | change |
|---|---:|---:|---:|
| required states | 3 | 5 | +2 |
| CCOC standalone debt | 0.5849625007 | 0.5849625007 | 0 |
| MLTR standalone debt | 0 | 0 | 0 |
| MRM standalone debt | 0 | 0 | 0 |
| joint debt | 0.5849625007 | 1.3219280949 | **+0.7369655942** |
| `Delta` | 0 | 0.7369655942 | **+0.7369655942** |

The interaction-only increase decomposes exactly as

\[
\boxed{
0.7369655942
=
0.4150374993
+
0.3219280949
}
\]

bits, where

- `+0.4150374993 bit` is the new CCOC × MLTR pairwise term;
- `+0.3219280949 bit` is the new CCOC × MLTR × MRM three-way term.

Thus the before/after change is not detectable from the three standalone obstruction scores at all. It appears only in coalition structure.

## Diagnostic interpretation

For a declared before/after comparison, classify the change as:

- **direct-only** if `delta Delta = 0` and at least one `delta D_i != 0`;
- **interaction-only** if every `delta D_i = 0` and `delta Delta != 0`;
- **mixed** if both standalone and interaction terms change;
- **null** if neither changes.

This classification is conditional on the declared carrier, baseline, audit semantics, and responsibility set. It is not an intrinsic property of an ecosystem independent of the scientific contract.

## Executable surfaces

- `crest/obstruction_compare.py` — before/after numeric comparison.
- `scripts/compare_obstruction_spectra.py` — JSON CLI.
- `tests/test_crest_obstruction_compare.py` — canonical interaction-only regression.
- `docs/crest_obstruction_comparison_2026-09-08.md` — worked comparison.
