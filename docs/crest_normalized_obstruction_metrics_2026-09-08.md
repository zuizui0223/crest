# CREST normalized obstruction metrics

## Purpose

Raw state debt is measured in bits and is the primary finite quantity. For comparisons across declared finite carriers with different available refinement capacity, CREST also reports a normalized diagnostic layer.

Let a carrier contain `N` worlds and let the baseline partition have `B` blocks. The largest possible refinement is the discrete partition, so the available refinement capacity is

\[
K_{\max}=\log_2(N/B).
\]

For joint debt `D_joint`, define

\[
\boxed{R_{\rm joint}=D_{\rm joint}/K_{\max}}.
\]

When `K_max>0`, `R_joint` lies in `[0,1]`. It answers: what fraction of all refinement capacity available above this baseline is actually consumed by the declared joint responsibilities?

The interaction fraction of realized joint debt is

\[
\boxed{F_{\rm int}=\Delta/D_{\rm joint}},
\]

with direct fraction

\[
F_{\rm direct}=\sum_iD_i/D_{\rm joint}=1-F_{\rm int}.
\]

These fractions are signed. Negative `F_int` indicates redundancy/overlap rather than synergistic refinement.

For Möbius/Harsanyi interaction dividends `m(S)`, aggregate by interaction order

\[
M_k=\sum_{|S|=k}m(S),\qquad k\ge2.
\]

CREST also reports absolute order shares

\[
A_k=|M_k|/\sum_{j\ge2}|M_j|,
\]

which identify the dominant interaction order even when positive and negative interaction terms partially cancel.

## Canonical CCOC / MLTR / MRM witness

The six-world witness has `N=6`, baseline blocks `B=2`, and joint blocks `5`.

| quantity | value |
|---|---:|
| maximum available debt `K_max` | 1.5849625007 bit |
| realized joint debt `D_joint` | 1.3219280949 bit |
| normalized joint burden `R_joint` | **0.8340437671** |
| interaction fraction `F_int` | **0.5574929507** |
| direct fraction | **0.4425070493** |
| order-2 interaction | 0.4150374993 bit |
| order-3 interaction | 0.3219280949 bit |
| order-2 absolute share | **0.5631707946** |
| order-3 absolute share | **0.4368292054** |
| dominant interaction order | **2** |

Thus the canonical contract consumes about **83.4%** of the refinement capacity available above its baseline, and about **55.7%** of its realized joint state debt is interaction-generated.

## Interpretation firewall

These normalized quantities are contract-relative diagnostics, not intrinsic ecological constants. They depend on the declared carrier and baseline. Adding admissible worlds that never participate in the realized obstruction structure can change `K_max` and therefore `R_joint`. Cross-system comparison is meaningful only when carrier construction and baseline semantics are commensurable.

Raw bit quantities remain authoritative. The normalized layer exists to make scale explicit, not to erase the carrier dependence of CREST state.

## Implementation

- `crest/obstruction_normalized.py`
- JSON surface: `crest/obstruction_io.py`
- canonical artifact: `artifacts/crest_obstruction_spectrum.json`
- regression tests: `tests/test_crest_obstruction_normalized.py`
