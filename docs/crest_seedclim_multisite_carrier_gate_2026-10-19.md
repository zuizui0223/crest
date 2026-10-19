# SeedClim as an independent-site candidate: baseline carrier and later vegetation

**Status: SOURCE_METADATA_VALID / HOLD_EMPIRICAL_LINKAGE.** This is a
prospective study-design and provenance audit, **not** a new ecological result,
nor a validation of Paper A's finite quotient/transport theorem.

## Verified sources

- Public [SeedClim / Vestland Climate Grid OSF project](https://osf.io/npfa9/),
  node npfa9. The OSF files API exposes:
  - VCG_clean_seedbank.xlsx (file 634e3a110ecb4203302ed011; 2,415,260 B).
  - seedclim.2020.4.15.zip (file 6078961aeb9cc900a214cde0; 6,977,116 B).
  - VCG_clean_transplant_demography_2009-2012.txt (file
    635bc6c31e47c90b102a867b; 2,441,498 B).
  These are public metadata and URLs; the XLSX/ZIP **contents have not yet been
  downloaded and row-level linked** in this audit.
- [Between-the-Fjords/seedclim-data](https://github.com/Between-the-Fjords/seedclim-data)
  at exact commit a64358a7b34dcf909ca73ccb8590ebd0eb33839c.
- [Vandvik et al. / Oikos seed bank source](https://doi.org/10.1111/oik.02022)
  and its [archived raw data](https://doi.org/10.5061/dryad.q401b).

**Temporal correction:** the Oikos field sampling of standing vegetation and
persistent soil seed bank took place in **late August 2008**. The seed bank was
then grown out in a **2009–2010 greenhouse emergence assay**. The cleaned
seed-bank output currently labels its year 2009, which is NOT by itself proof
of a 2009 field sampling event. Any future time-order test must preserve
field collection and laboratory assay dates separately.

The GitHub cleaning code constructs seed-bank records at
(siteID, Replicate, species, sampling scale), not turfID. The subsequent
community database is relational: site → block → plot → origin/destination
turf → (turfID, species, year) observation, nominally covering 2009–2019.
**Do not invent a one-to-one pairing between seed-bank replicate and turf.**

## Relational integrity audit (metadata only)

Using upstream CSV metadata tables (not the OSF raw seed/vegetation files):

| Entity | Raw table | Rows |
|---|---|---:|
| Climate-gradient sites | site_table.csv | 12 |
| Sampling/experimental blocks | blocks_table.csv | 69 |
| Plot IDs | plots_table.csv | 412 |
| Turf entities | turfs_table.csv | 356 |

A naive equality join between blocks.siteID and the canonical site IDs
fails for **17 of 69 blocks**, affecting **three of twelve sites**:

| Raw blocks.siteID | Canonical site_table.siteID | Blocks |
|---|---|---:|
| Ovstedal | Ovstedalen | 5 |
| Skjellingahaugen | Skjelingahaugen | 7 |
| Ulvhaugen | Ulvehaugen | 5 |

Using only this explicit checked crosswalk gives **zero** unresolved
block-site, plot-block, origin-turf or destination-turf references.

Turf treatment counts, as declared by the upstream metadata:

| Treatment | Number of turfs |
|---|---:|
| TTC (untouched control) | 60 |
| TT1 (local transplant) | 60 |
| TT2 (warmer) | 40 |
| TT3 (wetter) | 45 |
| TT4 (warmer and wetter) | 30 |
| NA (not one of these transplant treatments) | 121 |

The 235 TTC/TT1–TT4 turfs **do not imply 235 independent sites**.
Treatments are not represented equally in all twelve origins: only
a subset of climate-grid site pairs permits warming/wetting transplants,
so naive treatment-by-bank models will confound spatial sampling and
manipulation feasibility. Analysis must cluster or hold out by source
site and respect origin/destination climates.

Run the pinned public metadata audit (network connection needed):
python scripts/audit_seedclim_multisite_keys.py
Offline: supply the four original source CSVs through --source-dir.

## Gate before a new ecological conclusion

1. **Download the actual OSF workbook/SQLite ZIP** and verify rows,
   sampling scale, source plot identity, species names, units, field date,
   missingness and year coverage; the present audit only proved the existence
   and metadata-schema of these files. The archive contents were inaccessible
   to the current source-reading tool, so no row counts or ecological effects
   are asserted.
2. Determine whether seed-bank Replicate can be aligned with a physical
   community block via an independently documented design key. If not,
   retain only origin-site-level seed-bank profiles. Never extrapolate to an
   individual turf-specific reservoir.
3. If time order is verified, preregister a conditional prediction:
   Does the independently measured **baseline persistent seed bank** explain
   later vegetation change / regeneration across independent origin sites,
   beyond observed initial vegetation and climatic treatment assignment?
4. Use leave-one-origin-site-out validation (only 12 site clusters), matched
   2009 source-vegetation observations, non-leaking year windows, and
   explicit origin×destination climate terms. Compare with null site-level
   and baseline-composition models. Report failures and uncertainty; no
   pseudo-replication of species/turfs as origin sites.
5. This is an **initial-state capacity** hypothesis, not a longitudinal
   demonstration that present carriers absorb a time-varying ecological
   memory. One seed-bank snapshot cannot establish ongoing closure of a
   stochastic ecological system.

## Alternative source screens

- [Kellogg Biological Station LTER seedbank elutriation](https://lter.kbs.msu.edu/datatables/24)
  (1990–2008, periodic 3–6-year sampling) and
  [long-term herbaceous biomass](https://lter.kbs.msu.edu/datatables/291)
  have joinable treatment/replicate/station *metadata* and possibly within-site
  experimental contrasts. But publication from core KBS tables requires prior
  written permission; no external raw data were copied or published here.
- The 2026 [ChinaSoilSeedBank](https://www.nature.com/articles/s41597-026-07088-4)
  comprises 3,170 bank communities; the descriptor treats different years and
  seasons as independent observations. Its large record count alone does not
  establish paired future vegetation at the same plot. It is not currently
  eligible to validate one-step ecological memory closure.
- [ForestGEO Flowers, Seeds & Seedlings](https://forestgeo.si.edu/research-programs/flowers-seeds-and-seedlings-initiative)
  has long-term multi-site seed-rain and seedling monitoring, but **seed
  rain ≠ persistent soil seed bank**. Its own data-conditions process and
  potentially requested permissions must be respected; the design is a
  different prospective-capacity question.

**Decision: keep Issue #140 open and HOLD.** The metadata issue is resolved,
but an independent empirical test is not yet completed. No change to canonical
Paper A manuscript or its submission metadata is warranted.
