# Direct seed-bank carrier audit — exploratory empirical boundary (2026-10-13)

**Status: HOLD_EMPIRICAL_MEMORY_CLOSURE.** No new ecology result and no modification of the canonical Paper A. The experiment is post-hoc and not preregistered.

## Source eligibility audit

**DeMalach, Kigel & Sternberg (2021):** [figshare dataset v1](https://doi.org/10.6084/m9.figshare.13175987.v1), CC BY 4.0. Source-level CSV review finds 17 site-aggregated rows at each of Matta (file ID 25349000), Lahav (25348994), and SdeBoker (25349006). Seed-bank years: 2001–2009; vegetation years: 2002–2004 and 2006–2010, with 2005 missing. Only 4 complete vegetation(t−1), vegetation(t), seed bank(t), vegetation(t+1) quadruples exist per site: **12 independent site×time blocks overall**. The 214 / 171 / 53 species columns are *not* independent years. The numeric fractional, annually varying Plot field is not a reproducible replicate-plot identifier. **Decision:** insufficient independent temporal information for an honest long-lag predictive analysis.

**Sonoran Desert winter annuals:** The [Cuello et al. study](https://doi.org/10.1098/rspb.2018.2613) names the original [ESSDesertAnnuals data repository](https://github.com/wscuello/ESSDesertAnnuals). Pin Git SHA **f39210d6adb603e7da7517601317ea9ce50305ae** (master) and file **SpeciesByYear.csv**. This contains 15 taxa observed 1983–2016; 1990–2015 have both soil-seed and germinant density measurements: 15 × 26 = **390** species×year cases. Published [soil-core methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC2710622/) indicate seed bank is measured after germination and before reproduction. The source germination-fraction variable is mathematically derived from the other two fields, so do **not** add it as an independent carrier.

## Reproducible exploratory analysis

Run: **python scripts/explore_sonoran_seedbank_memory.py**

Or reuse your own source CSV with --csv /path/to/SpeciesByYear.csv. The script uses only Python standard-library functions, downloads from the immutable upstream commit, and emits aggregate JSON. **No third-party raw data are committed to CREST.**

Predict the log1p-scaled next-year seedling density. Inputs known by year t: log1p current seedling density, log1p previous-year seedling density, and log1p current measured seed-bank density. Four matched predictive models: present; present+history; present+carrier; present+history+carrier. Shared ridge slopes with unpenalized species intercepts and training-only centering/scaling; lambda=2. Train through 2003 / test 2004–2007, train through 2007 / test 2008–2011, train through 2011 / test 2012–2015: **180 held-out species×year points but only 12 distinct years and 1 field site**.

| Model | Held-out log1p-scale MSE |
|---|---:|
| Present seedlings alone | 2.251238 |
| Present + previous-year seedlings | **2.110445** |
| Present + measured present seed bank | 2.189287 |
| Present + previous-year seedlings + seed bank | 2.141413 |

Relative incremental historical predictive benefit: **6.254%** with present alone, **2.187%** when present seed bank is included; this is **not** a causal mediation contrast. Adding the seed bank to the present-only baseline improves MSE by 2.752%, but **adding it beyond history makes MSE 1.467% worse**.

Ridge sensitivity lambda 0.25 / 2 / 20 / 100 gives direct-carrier incremental benefit beyond history **−1.53%, −1.47%, −0.96%, +0.14%**. Year-block resampling 2,000 times, keeping all fitted models fixed, yields a descriptive interval **[−4.77%, +1.37%]** for this incremental benefit; this is **not** a full-model or causal confidence interval. Under 300 within-species, within-split carrier shuffles (a timing placebo), **217** random alignments score at least as well as the real bank. An earlier 118/300 count was invalid: the previous calculation erroneously reused a single shuffled value for each species across years. The per-year shuffle indexing was corrected before rerunning all 300 placebos. Temporal specificity is not compelling.

## Scientific rejection / acceptance gate

The apparent *attenuation* of historical predictive benefit when carrier is added is **not evidence of dynamical closure**. Correlated regressors, shared environmental forcing, and regularization can cause this pattern; environmental forcing is not adequately controlled here. One ecological location and a limited set of independent held-out years prevent ecological generalization.

This does not test the finite deterministic transport corollary directly; it does not prove stochastic Markov sufficiency, a causal seed-bank memory mechanism, independent seed-bank prediction beyond history, or long-term ecological memory disappearance.

**Keep HOLD:** Do not promote to Paper A or call it an empirical discovery. A next test needs multiple independent locations or perturbation contexts, independently time-stamped present legacy carriers, contemporaneous environmental controls available at prediction time, blocked forecast and meaningful negative-control comparisons. See [Issue #140](https://github.com/zuizui0223/crest/issues/140).

**Redistribution:** This repository contains no raw third-party CSV copies. Reuse upstream files under their applicable publication and repository terms; the ESSDesertAnnuals repository root did not expose a LICENSE file at this audit.
