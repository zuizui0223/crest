# GLUE white-clover portability reanalysis — 2026-08-24

> Purpose: test one concrete CREST ecological projection against the public analysis products of Santangelo et al. (2022), without treating the empirical result as a proof of the finite CREST theorem.

## CREST question

Does the coarse state label `urbanization` support one portable cyanogenesis-response law across cities, or does a portable law require retaining additional environmental context?

The relevant CREST contrast is:

```text
coarse quotient:     q_U = urbanization coordinate only
richer quotient:     q_E = urbanization + environmental background/change
response:             city-specific cyanogenesis cline
```

The strong claim being tested is not that `urban` is meaningless. It is whether a single coarse urbanization law is adequate across cities.

## Public source products audited

Upstream repository:

- `James-S-Santangelo/glue_pc`
- phenotypic pipeline README states that cleaned phenotype data and environmental data are merged, city clines are analyzed, and clines are then predicted from environmental data.
- `phenotypic-analyses/analysis/tables/allCities_logisticReg_coefs.csv` contains city-specific logistic cline coefficients.
- `phenotypic-analyses/analysis/tables/eniroMeansSlopes.csv` contains city environmental means and urban-rural environmental slopes.
- `phenotypic-analyses/analysis/tables/elasticNet_coefSummary.csv` summarizes environmental predictors retained across 100 elastic-net fits.
- `phenotypic-analyses/analysis/tables/elasticNet_obs_result.csv` records out-of-sample predictive performance across repeated fits.

Primary paper: Santangelo et al. 2022, *Science* 375:1275–1281, doi:10.1126/science.abk0989.

## Check 1 — one signed urbanization law is immediately rejected

The public city coefficient table contains both positive and negative urban-rural HCN clines, including statistically supported examples in opposite directions.

Examples from the standardized distance model:

| city | betaLog_Dist | p |
|---|---:|---:|
| Albuquerque | -0.839 | 0.004 |
| Amsterdam | +0.800 | 0.012 |
| Antwerp | +2.150 | <0.001 |
| Atlantic City | -0.871 | 0.001 |
| Beijing | -1.668 | 0.001 |
| Brighton | +1.422 | <0.001 |
| Burlington | -0.868 | <0.001 |
| Kyoto | -1.027 | <0.001 |
| New York | +1.151 | <0.001 |
| Lisbon | -1.959 | <0.001 |
| Toronto | +1.463 | <0.001 |
| Uppsala | -1.704 | 0.033 |

Therefore the coarse statement

```text
urbanization -> one universal direction of cyanogenesis change
```

cannot be a portable law over the full city set. This is stronger than merely observing heterogeneous effect sizes: the response direction itself reverses.

The published paper reports significant urban-rural clines in 47% of cities, again showing that the same nominal `urban` category does not imply one uniform response regime.

### CREST reading

The response map does not factor through a quotient that retains only an undifferentiated `urbanization` label if the target is city-portable cyanogenesis response.

This supports:

- quotient-law non-portability;
- representational instability across cities;
- local adaptive direction rather than one global urban evolutionary arrow.

It does **not** prove that no lower-dimensional portable quotient exists.

## Check 2 — environmental context is repeatedly selected when predicting cline strength

The upstream 100-fit elastic-net coefficient summary shows that several environmental background/change terms are retained with very high frequency:

| predictor | non-zero fits / 100 | mean coefficient |
|---|---:|---:|
| annualPET slope × summerNDVI mean | 100 | -0.08876 |
| annualPET slope × GMIS mean | 94 | +0.03418 |
| winterNDVI mean | 94 | +0.03358 |
| NDSI mean | 91 | -0.01162 |
| summerNDVI slope × annualAI mean | 91 | -0.03589 |
| annualPET slope | 76 | +0.00120 |

This is exactly the pattern expected if the effect of an urban-rural environmental change depends on the background environmental state rather than on one universal urbanization coordinate.

In CREST language, these terms are candidate distinctions erased by `q_U` but retained by a richer `q_E`.

## Check 3 — the richer quotient is useful but far from complete

The repeated elastic-net prediction table reports positive but modest held-out R-squared values across runs (roughly 0.05–0.19 in the audited rows, with RMSE around 0.87–0.92).

So the correct conclusion is **not**:

```text
environment-aware quotient solves urban evolution
```

but:

```text
urban-only quotient is demonstrably too coarse;
retaining environmental context recovers reproducible predictive signal,
but substantial city-to-city response variation remains unresolved.
```

This is especially useful for CREST because it separates three possibilities:

1. `urban` alone is insufficient;
2. a richer environmental state improves portability;
3. current evidence still does not identify a fully portable state law.

That is the empirical analogue of the CREST distinction between required state, identified state, and reportable target.

## Current empirical verdict

### Supported

- A single signed `urban -> cyanogenesis` law is not portable across cities.
- Environmental background/change variables contain reproducible information about city-specific cline strength.
- The relevant predictors include interaction terms, consistent with context-dependent response rather than one globally fixed environmental effect.

### Not yet established

- That a particular environmental quotient is the unique minimal adequate state.
- That the environment-aware model outperforms every urban-only baseline under a formally preregistered leave-one-city-out comparison.
- That the remaining unexplained variation is caused by omitted CREST-relevant latent mechanisms rather than sampling/statistical noise.
- Any empirical counterpart of the arbitrary-m capability–resolution theorem.

## Next exact validation

The next analysis should use the upstream city-level tables or population-level cleaned data and preregister two prediction families:

```text
M0: city cline ~ one global urbanization law
M1: city cline ~ environmental means/slopes and interactions
```

with city-level holdout. Primary metric: out-of-city RMSE; secondary: R-squared, sign accuracy, and calibration. The CREST projection is supported if M1 improves portability without requiring city identity itself as a predictor.

The same protocol can then be repeated on urban pollinator connectivity using geometric isolation as M0 and movement/resource/guild-aware state as M1.

## Claim firewall

This source-level reanalysis tests the ecological usefulness of the world→state→law interpretation. It is not evidence for the mathematical correctness of J1 or the capability–resolution theorem, which are proved independently in the finite formal system.
