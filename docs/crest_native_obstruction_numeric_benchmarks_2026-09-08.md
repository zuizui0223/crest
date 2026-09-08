# CREST native obstruction numeric benchmarks

## Decision

CCOC, MLTR, and MRM can all be expressed in the same **state-resolution bit** unit, but their native theorem families do not automatically live on one common carrier. Their native burdens therefore must not be added directly. Use native-axis benchmarks to compare scale; use the CREST obstruction spectrum only after a common lift has been declared.

## Native-axis benchmark table

| theory | native obstruction | canonical exact law | native state burden |
|---|---|---|---:|
| CCOC | future/composition | closed interface has 2 states; open interface has `2^(m+1)` states | `m` bit |
| MLTR | inherited meaning/history | minimum history mode count is the number `h` of distinct carried terminal maps | `log2(h)` bit raw history context |
| MRM | retained mechanism | fixed candidate law has 2 states; candidate-safe law has `2^(m+1)` states | `m` bit |

The equal `m`-bit form for CCOC and MRM is a numerical coincidence of their canonical sharp families, not a statement that the obstructions are the same. In CCOC, the extra bits encode distinctions exposed by a wider legal future grammar. In MRM, they encode response-relevant distinctions among retained mechanisms.

## CCOC exact family

CCOC's current core README states the strongest explicit family as

`|P_C| = 2`, `|P_O| = 2^(m+1)`, and `K_O-K_C = m`.

Concrete values are therefore:

| m | closed states | open states | state multiplier | added burden |
|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 2x | 1 bit |
| 2 | 2 | 8 | 4x | 2 bit |
| 4 | 2 | 32 | 16x | 4 bit |
| 8 | 2 | 512 | 256x | 8 bit |

Source of theorem law: `zuizui0223/ccoc` README, current CORE-2/CORE-3 publication spine.

## MLTR exact history witness

MLTR proves that the minimum immutable history mode count equals the number `h` of distinct complete carried terminal maps:

`|H_min| = h`, so raw history-context burden is `log2(h)` bit relative to one route-independent context.

The canonical two-route diamond has two distinct carried maps, `(0,1)` and `(1,0)`. Therefore:

| quantity | value |
|---|---:|
| distinct carried maps | 2 |
| minimum history modes | 2 |
| raw history burden | 1 bit |
| root exact states | 2 |
| history-aware repaired exact states | 4 |
| final exact-interface burden | 1 bit |

This is an explicit repository witness, not a hypothetical calibration.

Source: `zuizui0223/mltr/docs/history_augmentation.md`.

## MRM exact family

MRM Theorem 7 gives a canonical `m`-bit response family with `2^(m+1)` candidate-safe states versus a fixed two-state candidate law, hence an exact `m`-bit state surcharge. Theorem 8 adds an experimental frontier: exactly `m` binary probes are necessary and sufficient in the worst case to identify one of `2^m` response signatures; after `k` distinct probes, exactly `2^(m-k)` signatures remain compatible.

Concrete values:

| m | fixed-law states | candidate-safe states | state multiplier | state burden | minimum binary probes |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 4 | 2x | 1 bit | 1 |
| 2 | 2 | 8 | 4x | 2 bit | 2 |
| 4 | 2 | 32 | 16x | 4 bit | 4 |
| 8 | 2 | 512 | 256x | 8 bit | 8 |

Source: `zuizui0223/mrm` README and the Theorem 7–8 mechanism-ambiguity frontier.

## Common-lift CREST benchmark

The native numbers above are not directly summable because they come from different theorem contracts. On CREST's explicit six-world common-lift cascade, the same three obstruction names are put on one shared carrier and can be combined exactly.

| quantity | value |
|---|---:|
| baseline states | 2 |
| CCOC standalone states | 3 |
| MLTR standalone states | 2 |
| MRM standalone states | 2 |
| joint states | 5 |
| CCOC standalone debt | 0.5849625007 bit |
| MLTR standalone debt | 0 bit |
| MRM standalone debt | 0 bit |
| joint debt | 1.3219280949 bit |
| interaction debt `Delta` | 0.7369655942 bit |
| normalized joint burden | 83.40437671% of available refinement capacity |
| interaction fraction | 55.74929507% of realized joint debt |

The exact Möbius interaction decomposition is:

- CCOC x MLTR pair interaction: `0.4150374993` bit;
- CCOC x MRM pair interaction: `0` bit;
- MLTR x MRM pair interaction: `0` bit;
- CCOC x MLTR x MRM three-way interaction: `0.3219280949` bit.

Thus 56.31707946% of interaction-generated debt is pairwise and 43.68292054% is genuinely three-way in this witness.

## Interpretation

There are now two distinct numerical surfaces:

1. **Native frontier numbers** answer how large each companion theory's own sharp obstruction can be under its own model contract.
2. **CREST joint-spectrum numbers** answer how the three declared responsibilities combine after they have been placed on one common carrier.

Do not add native CCOC `m` bits, native MLTR `log2(h)` bits, and native MRM `m` bits unless an explicit common-lift construction proves that those quantities refer to the same worlds, baseline, and responsibility contract. The CREST coalition calculation is the mathematically licensed place for addition and interaction accounting.
