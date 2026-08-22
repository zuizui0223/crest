# Hotarubukuro discriminating-observation design — 2026-08-22

> **Status:** prospective CREST evidence design derived from the locked `zuizui0223/hotarubukuro` results. This document does not add an empirical result and does not assign effect sizes, sample sizes, costs, or causal probabilities that have not been estimated.

## 1. Why the next step is a new measurement channel, not more of the same raster support

The real-data CREST replay leaves two scientifically important branches unresolved:

1. **Bombus mechanism:** the focal Bombus suitability surface shows only weak local consistency with sharp colour transitions; the current evidence does not license pollinator-mediated selection.
2. **Human/provenance mechanism:** isolated pigmented occurrences show a reproducible human-context overlay, but the current evidence does not identify horticultural origin, planting, escape, establishment, or human causation.

In both branches, increasing precision on the same aggregate proxy does not automatically identify the missing causal distinction.

For pollination, flower visitation or pollinator availability is not equivalent to pollination effectiveness. King, Ballantyne & Willmer (2013, *Methods in Ecology and Evolution*, doi:10.1111/2041-210X.12074) explicitly show why visitation can be a poor proxy and recommend single-visit pollen deposition on virgin stigmas as a direct effectiveness measure. A later meta-analysis likewise treats single-visit stigma deposition as a direct pollinator-effectiveness quantity (Földesi et al. 2021, *Journal of Applied Ecology*, doi:10.1111/1365-2664.13798).

For provenance, population-genetic clustering/assignment can estimate ancestry or membership relative to reference samples, but ancestry assignment is not by itself proof of intentional planting or human-mediated establishment. Historical and site-history evidence remains a distinct channel.

CREST therefore asks which new observation first splits the currently compatible world classes relevant to each claim.

## 2. Current licensed endpoints

### Bombus branch

Current licensed statement:

> focal Bombus support is weakly consistent with a local colour-transition association at the strictest scale, but this does not demonstrate pollinator-mediated selection.

Unlicensed stronger states:

- `Bombus visits pigmented flowers more often because of colour`;
- `Bombus transfers more conspecific pollen to pigmented flowers`;
- `Bombus causes a reproductive-fitness advantage of pigmentation`;
- `pollinator-mediated selection explains the observed geographic colour pattern`.

### Human-context branch

Current licensed statement:

> relative isolation among pigmented occurrences has a positive population-exposure relationship exceeding the fitted natural-colour geography.

Unlicensed stronger states:

- `the isolated pigmented occurrence is horticultural`;
- `the occurrence derives from a cultivated source`;
- `people established the occurrence`;
- `the colour state is caused by urbanization or planting`.

The observation programme should therefore be target-laddered rather than trying to infer the strongest causal state in one jump.

## 3. Bombus branch — evidence ladder

### B0 — current layer: distributional availability

**Input already available:** focal Bombus SDM/support at sharp white–pigmented transition pairs.

**Can address:** whether a local geographic association is consistent with the pollinator hypothesis.

**Cannot address:** actual visits, stigma contact, pollen transfer, colour preference, or fitness consequence.

### B1 — direct flower-use channel

Collect standardized direct or video-based visits at both sides of the locked sharp-transition pairs, recording at minimum:

- visitor identity/taxon;
- flower colour state;
- observation effort and flowering availability;
- time/weather covariates needed to compare paired sites;
- whether the visitor enters/contact geometry relevant to the reproductive organs when observable.

**CREST role:** splits worlds in which Bombus availability is high but realized use of the two colour states is the same from worlds in which realized visitation differs.

**Still insufficient for selection:** visitation differences do not establish pollen transfer or fitness.

### B2 — pollination-effectiveness channel

At the same paired sites, add **single-visit conspecific pollen deposition** on previously unvisited/receptive stigmas, indexed by visitor identity and flower colour state.

**Why this is the pivotal new channel:** it directly observes the transfer event that the suitability/visitation proxies leave latent. Repeating only the SDM or visit counts cannot recover this distinction.

**CREST role:** separates `visitor abundance/use` from `effective pollen delivery` response types.

### B3 — reproductive-consequence channel

Measure female reproductive consequences under a design that separates pollen delivery from later resource limitation, for example with a combination of:

- known-visit or open flowers;
- pollinator-exclusion/bagged flowers;
- hand-pollination or pollen-supplementation controls where biologically appropriate;
- fruit/seed production or another justified reproductive endpoint.

**CREST role:** asks whether the B2 difference propagates to the management/evolutionary target rather than assuming pollen deposition equals fitness.

### B4 — colour-causal intervention

A geographic association can still be produced by colour-correlated traits or habitat. To claim a colour-mediated pollinator mechanism, add an intervention that changes the colour signal while holding the rest of the flower/site context as constant as practicable, or another design with equivalent causal leverage.

**CREST role:** this is the intervention-context expansion that can split `Bombus responds to colour` from `Bombus responds to a correlated site/flower trait`.

### Bombus minimum recommendation

For the current unresolved claim, the highest-value immediate addition is **B1 + B2 at the existing strict transition pairs**, not another distribution-only model. B3/B4 are needed before escalating from pollination effectiveness to colour-mediated selection.

## 4. Human/provenance branch — evidence ladder

### H0 — current layer: human-context geography

**Input already available:** relative same-colour isolation, population exposure, local flower-cell density correction, and natural-map nulls.

**Can address:** whether isolated pigmented occurrences carry a human-context overlay beyond the fitted natural colour geography.

**Cannot address:** ancestry, cultivated source, planting history, establishment mechanism, or causal effect of people.

### H1 — site-history / anthropogenic-process metadata

At isolated pigmented sites and matched comparison sites, record process-facing context that is not reducible to population density alone, such as documented planting, garden/roadside management, substrate disturbance, maintenance history, and evidence of recent establishment when available.

**CREST role:** improves the evidence partition for `human-associated context` but still does not automatically establish genetic provenance.

### H2 — historical/temporal provenance channel

Use dated occurrence information where available (herbaria, historical surveys, local planting/garden records, repeated photographs or other defensible records) to determine whether an occurrence predates, follows, or tracks plausible anthropogenic introduction or habitat change.

**CREST role:** distinguishes present-day co-location with people from a temporally supported establishment history.

### H3 — genetic ancestry/assignment channel

Sample the isolated pigmented occurrences together with appropriate natural populations and, only if identifiable and available, candidate cultivated/horticultural source material. Use population structure/assignment or other justified genomic inference to ask whether isolated occurrences are genetically compatible with a candidate source or with local natural ancestry.

**Claim firewall:** assignment/ancestry can support source compatibility or ancestry structure. It does **not** by itself prove intentional planting, the date of establishment, or human causation.

### H4 — plasticity/inheritance channel

If the provenance-facing claim depends on flower colour itself rather than merely the occurrence, a common-garden/family or other suitable design is required to separate inherited colour differences from environmentally induced phenotypic plasticity.

### H5 — establishment/causation synthesis

A strong `human-mediated establishment` state should require concordance across at least two genuinely different evidence channels—for example source-compatible ancestry plus temporally/process-compatible site history—rather than treating proximity to people as causal proof.

### Human/provenance minimum recommendation

Prioritize **high relative-isolation pigmented occurrences**, because that is where the locked human-context signal is strongest, and compare them with matched low-isolation pigmented occurrences under the fitted natural geography. Add H2/H3 before creating any provenance label. H1 is useful context but cannot replace them.

## 5. Sampling priority inherited from the current results

The design should reuse the strata that generated the unresolved distinctions rather than opening a new unsynchronized sampling universe.

### Pollination stratum

Start from the locked strict sharp-transition pair set and observe both sides under paired temporal effort. The existing 5-km result is the strongest current local signal, so it is the natural discrimination stratum; broader windows are useful as scale controls rather than as substitutes for direct interaction data.

### Human-context stratum

Start from pigmented cells ranked by the already defined **relative isolation** measure. Compare high-isolation and lower-isolation pigmented cells while matching or conditioning on the natural-map/context variables already used in the locked analysis. White cells remain a useful negative/comparative colour class, but the existing evidence says the headline is a pigmented-specific overlay rather than a robust reciprocal pigmented-minus-white contrast.

No new arbitrary binary `human` threshold should be introduced before provenance evidence exists.

## 6. Discriminating-channel matrix

| Desired report | Current raster/context data | Direct visits | Single-visit pollen deposition | Reproductive endpoint / colour intervention | Historical/site history | Genetic assignment |
|---|---|---|---|---|---|---|
| broad environment-associated pigmentation state | sufficient for current paper target | not required | not required | not required | not required | not required |
| realized Bombus use differs by colour/context | insufficient | **directly relevant** | supportive | not yet necessary | no | no |
| Bombus pollination effectiveness differs | insufficient | insufficient alone | **directly relevant** | supportive | no | no |
| colour-mediated pollinator selection | insufficient | insufficient | necessary but not sufficient | **required causal/fitness leverage** | no | potentially controls structure, not selection by itself |
| human-context overlay | **currently reportable** | no | no | no | supportive | no |
| cultivated/natural source compatibility | insufficient | no | no | no | supportive | **directly relevant with reference sources** |
| human-mediated establishment | insufficient | no | no | no | **directly relevant** | supportive/necessary in some designs but not sufficient alone |

The point of this matrix is not that every study needs every column. It identifies when collecting more data from an existing column cannot license a stronger report because the missing distinction belongs to another channel.

## 7. CREST stopping rules

### Pollination

- Stop at `association/consistency` if only availability/SDM evidence exists.
- Permit `differential realized visitation` only after B1.
- Permit `differential pollination effectiveness` only after a direct transfer measure such as B2.
- Do not report `colour-mediated selection` without an appropriate reproductive/causal intervention layer.

### Provenance

- Stop at `human-context overlay` with the current data.
- Do not create a `human-origin` state from population exposure or isolation alone.
- Permit source/ancestry language only after H3 with explicit reference limitations.
- Reserve `human-mediated establishment` for evidence that combines source/ancestry with temporal/process history or another comparably discriminating causal design.

These are claim-allocation rules, not universal biological thresholds.

## 8. Why this is a CREST validation rather than generic “collect more data” advice

The design is derived from the **specific state distinctions that the existing scientific contracts require but the current evidence does not identify**.

- In the Bombus branch, the missing state distinction is not `high vs low predicted Bombus suitability`; it is `mechanisms that differ in actual pollen-transfer/fitness response under the relevant interaction`.
- In the human branch, the missing distinction is not `urban vs rural`; it is `worlds with different provenance/establishment histories that can produce the same present human-context pattern`.

Thus the next observation is chosen to refine the evidence partition toward the required state partition, not to maximize data volume.

## 9. Immediate field-design output

If one season of new data must be prioritized, the CREST order is:

1. **Sharp-transition paired sites:** synchronized direct visitation + single-visit pollen deposition, with flower colour and visitor identity retained.
2. **High-isolation pigmented sites:** provenance-oriented historical/site audit + tissue collection for a reference-aware genetic assignment design.
3. Add reproductive/colour-manipulation experiments only where B1/B2 show a pollinator-response difference worth escalating to selection.

This creates an explicit fail-fast workflow: null B1/B2 prevents a weak geographic signal from expanding into an expensive selection programme, while a lack of H2/H3 support prevents the human-context overlay from becoming an unsupported provenance narrative.
