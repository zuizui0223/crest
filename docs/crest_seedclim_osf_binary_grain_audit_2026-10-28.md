# SeedClim OSF binary source audit — original grain and temporal alignment

**Status: RAW_XLSX_ZIP_CONTENTS_UNVERIFIED / HOLD_EMPIRICAL_LINKAGE until a live audit reports otherwise.** No ecological mechanism or empirical memory-closure result is asserted. Canonical Paper A and its submission surfaces are not modified.

## Independent source evidence

The public [SeedClim Vestland Climate Grid](https://betweenthefjords.w.uib.no/vestland-climate-grid/) consists of twelve calcareous grassland sites across three temperature and four precipitation classes. Public [OSF node npfa9](https://osf.io/npfa9/) lists two critical original files:

- VCG_clean_seedbank.xlsx (OSF id 634e3a110ecb4203302ed011, nominal 2,415,260 B)
- seedclim.2020.4.15.zip (OSF id 6078961aeb9cc900a214cde0, nominal 6,977,116 B)

The original [Vandvik et al. Oikos paper](https://doi.org/10.1111/oik.02022) and [Dryad archive](https://doi.org/10.5061/dryad.q401b) describe collection in **August 2008**, with **three independent 64 × 64 cm field sampling plots per site**. The soil-seed-bank greenhouse emergence assay took place in **2009–2010**. Finer sampling areas (2 × 2 cm to 32 × 32 cm, up to 4096 cm² at the largest scale) are nested species–area samples and are **not independent field sites**.

The upstream [seedclim-data cleaning script](https://github.com/Between-the-Fjords/seedclim-data/blob/a64358a7b34dcf909ca73ccb8590ebd0eb33839c/cleaning_code/1_seed_data/clean_seedbank_seedrain.R) assigns **year=2009** to its cleaned sheets. That is a **data/assay label**, not evidence that field sampling occurred in 2009. It selects the seed-bank columns year, siteID, replicate, sampling_scale_cm2, nr_individual, nr_species, species, nr_seeds. Critically **no blockID, plotID or turfID mapping** is declared for this source. The community database uses turfID × species × year and separate origin/destination plot relations.

A similarly numbered seed-bank replicate and transplant block is NOT enough to establish linkage. The paper independently warns that soil-seed-bank/standing-vegetation similarity depends strongly on sampling area. Never treat raw seed counts from 4–4096 cm² as identical-effort abundance, and never treat nested scales or 356 transplant turfs as 356 independent origin sites.

## Binary and relational audits

Online command:

    python scripts/audit_seedclim_osf_raw.py --download --output /tmp/seedclim_source_gate.json

Offline command:

    python scripts/audit_seedclim_osf_raw.py --seedbank-xlsx /path/VCG_clean_seedbank.xlsx --community-zip /path/seedclim.2020.4.15.zip --output /tmp/seedclim_source_gate.json

The read-only source-level script inspects actual OOXML sheet keys and SQLite ZIP aggregates; no workbook is modified. Checks include rows, year labels, site/replicate/scale samples, actual blockID/turfID columns, duplicate taxa and missing seed-count cells, and SQLite table/year/turf counts. A separate non-blocking GitHub Action attempts the public OSF download and uploads JSON metadata **only**. Raw files are never committed or uploaded as CI artifacts. If the download is blocked, the explicit result is RAW_SOURCE_NOT_VERIFIED; a green job is not a scientific success.

## Scientific boundary

Even after a successful source-level audit, only a **site-level baseline carrier hypothesis** would be eligible, not an individual-turf mechanism: independently measured persistent seed-bank composition, sampled in 2008, may contribute to later vegetation prediction after conditioning on initial visible vegetation and origin/destination climate. The conservative prediction landmark is 2010, with target outcomes from 2011 onward, because the greenhouse assay spanned 2009–2010. An earlier landmark requires verified assay completion dates.

Required next evidence: source-row audit; an independently documented replicate-to-block/turf key or an explicitly site-level analysis; matched area and species processing; preregistered **leave-one-origin-site-out (12 sites)** prediction that beats climate+baseline-community controls, and independent-site replication. The single baseline snapshot does NOT prove that ecological memory is dynamically absorbed or that stochastic Markov closure holds.

See [Issue #140](https://github.com/zuizui0223/crest/issues/140) and previous [metadata-only audit](crest_seedclim_multisite_carrier_gate_2026-10-19.md).
