# Sonoran seed-bank memory pilot: prior-year rainfall sensitivity (2026-10-19)

**Status: HOLD_NO_INDEPENDENT_CARRIER_PREDICTIVE_BENEFIT.**
Exploratory source audit only, not an empirical discovery, a causal analysis, or a
test of stochastic/deterministic Markov closure. Do not promote it to Paper A.

## What was tested

Extends the [direct seed-bank carrier audit](crest_empirical_seedbank_carrier_gate_2026-10-13.md)
and Issue [#140](https://github.com/zuizui0223/crest/issues/140).
Both demographic and rainfall tables are retrieved from
[wscuello/ESSDesertAnnuals](https://github.com/wscuello/ESSDesertAnnuals)
at the **fixed upstream commit** f39210d6adb603e7da7517601317ea9ce50305ae:

- SpeciesByYear.csv: 15 taxa with 1990–2015 annual soil seed-bank density.
- LTERDATA1982_2016.csv: daily CAP station 1 precipitation (mm) and a
  per-day quality flag.

CAP precipitation is **not an exactly matched field-plot microclimate**.
As a plausibility screen, its January–March 1990–2005 totals and the
original Venable Jmprec series in DataFig2Venable2007.csv have approximate
Pearson correlation **0.979**, but their amounts do not match identically.

### Missingness and time-direction safeguards

- Use only months with a complete daily calendar and all daily Flag=G.
- CAP **2015** contains 306 empty quality flags, despite numeric zeros
  in the raw field; these records must NOT be assumed to represent zero rain.
- **March 2002** has two Flag=M missing observations. Consequently its
  January–March total is not complete; the double-climate condition excludes
  the 15 species rows for predictor year t=2003.
- At predictor year **t**, climate features use only October–December of
  calendar year t-1, and optionally January–March of calendar year t-1.
  There is no use of actual future climate from t+1, nor any 2015 rainfall.
- Previous-year seasonal rainfall is a **lagged environmental proxy**. It is
  not a complete adjustment for rainfall during the current or future plant
  growing season; notably the exact biological cut/sampling date is not known.

## Reproducible analysis

Run with network available:

    python scripts/explore_sonoran_rainfall_sensitivity.py

Or use previously downloaded source CSVs without network:

    python scripts/explore_sonoran_rainfall_sensitivity.py \
      --seedlings-csv /path/to/SpeciesByYear.csv \
      --rainfall-csv /path/to/LTERDATA1982_2016.csv

No third-party raw data are stored in CREST. The script uses only Python
standard library, emits JSON summaries, and reuses the model definitions
from explore_sonoran_seedbank_memory.py.

Same four predictive contracts as before, evaluated on exactly matching
species×year observations within each climate condition:

1. Current seedling abundance, plus declared rainfall controls.
2. The same + prior-year seedling abundance (history).
3. The same + measured current soil seed bank (carrier).
4. The same + history + carrier.

Outcome: log1p(next-year seedling density). Common ridge slopes with
species-specific intercepts, train-only scaling, and penalties 0.25, 2, 20,
and 100. Chronological folds: train through 2003, 2007, 2011 and evaluate
2004–07, 2008–11, 2012–15, respectively. The test comprises only **12
calendar years at one location**, even though 180 species×year predictions
contribute to MSE. Climate states are common to all species within a year.

## Exact descriptive results, ridge lambda=2

| Covariates available by t | Species×year predictor rows | MSE: present+history | MSE: present+history+seed bank | Independent seed-bank gain beyond history |
|---|---:|---:|---:|---:|
| No rainfall control | 390 | 2.110445 | 2.141413 | **−1.47%** |
| October–December of t−1 | 390 | 2.233920 | 2.309291 | **−3.37%** |
| October–December plus January–March of t−1 | 375 | 2.179223 | 2.310412 | **−6.02%** |

The last row excludes 2003 predictor observations because March 2002 rain
is incomplete. Its training samples differ from the first two conditions,
even though the same 180 species×year observations are held out.

Across lambda ∈ {0.25, 2, 20, 100}, seed-bank incremental gains beyond
history were, respectively:
- No climate: −1.53%, −1.47%, −0.96%, +0.14%.
- Prior October–December: −3.48%, −3.37%, −2.48%, −0.66%.
- Prior October–December + prior January–March:
  −6.40%, −6.02%, −3.69%, −0.89%.

**Verdict:** There is no stable held-out benefit from the measured present
seed bank once past seedling abundance is already included. A smaller
percentage gain from history after conditioning on correlated predictors
does not prove that the state is dynamically closed, identify a memory
mechanism, or imply that ecological memory can generally be erased.

## Next possible replication source (screen only, not approved)

The [Kellogg Biological Station LTER seed-bank experiment](https://lter.kbs.msu.edu/datatables/24)
has experimental treatments and spatial replicates, and its [plant biomass
records](https://lter.kbs.msu.edu/datatables/154) cover later years.
However, seed-bank sampling was **every 3–6 years**, not annually; the
treatment overlap and site-year joins must be checked. The KBS data-use
policy requires **written permission for publication**. No data were copied
from that source, and it is not yet an eligible independent-site replication.

## Scientific boundary

- Rainfall proxies are not complete causal climate controls.
- Species responses share a site, drought sequence, and other disturbances.
- No independent-site replication, causal instrument or intervention exists.
- A deterministic one-step quotient refinement in CREST does not imply
  stochastic Markov sufficiency in an observational time series.
- Negative results are retained and not promoted to the canonical manuscript.
