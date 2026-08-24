# Urban pollinator closure and connectivity reanalysis — 2026-08-24

> Purpose: test concrete ecological projections of the current CREST world → state → law architecture. These source-level ecological checks do **not** prove the finite CREST theorem.

## Question

Can a coarse urban-patch state such as

\[
q_{\rm geom}(x)=\{\text{isolated},\text{connected}\}
\]

support a portable pollination/connectivity law, or does an adequate state need to preserve realized movement, pollinator guild, resource quality, and network role?

The three source systems below give three independent tests.

---

## Test 1 — Geometric isolation does not certify causal closure

### Source

2024 *Acta Oecologica* 123:103985, **Pollinator-mediated connectivity in fragmented urban green spaces—tracking pollen grain movements in the city center**.

DOI: `10.1016/j.actao.2024.103985`

Open-access article:
`https://www.sciencedirect.com/science/article/pii/S1146609X24000079`

### Design

- four isolated urban green patches;
- fluorescent quantum-dot pollen tracking;
- two focal flowering systems: *Fritillaria imperialis* in spring and *Hemerocallis* sp. in mid-summer;
- no green corridors connecting the focal patches.

### Observed result

Pollen transfer occurred frequently among small isolated flowering patches. Streets, trails, and pavements did not prevent pollen dispersal. The variables associated with transfer were also species-specific: nearby green-area proportion was important for *F. imperialis*, whereas green-area proportion, inter-site distance, and pollinator visitation frequency were important for *Hemerocallis*.

### CREST consequence

The proposition

\[
\text{geometrically isolated patch}\Rightarrow\text{functionally closed pollination state}
\]

is empirically false for this source class.

The patch can be isolated in a map-based quotient while remaining connected in the response map relevant to pollen flow. Hence `isolated` cannot by itself be treated as a causal-closure certificate.

A stronger state needs at least some distinctions related to realized or potential movement through the surrounding matrix.

### What is demonstrated

- direct failure of geometric isolation as a sufficient closure state;
- present map geometry can erase response-relevant connectivity;
- the same coarse geometric state can require different predictors for different plant/pollinator systems.

### What is not demonstrated

- this study does not establish the least CREST quotient;
- it does not imply distance is irrelevant;
- it does not prove the finite CREST theorem.

---

## Test 2 — One connection action does not have one mechanism-independent effect

### Source

Li, Clements & Memmott 2026, *Oecologia* 208:64, **Linear features affect pollination success in experimental plant assemblages**.

DOI: `10.1007/s00442-026-05899-1`

PubMed:
`https://pubmed.ncbi.nlm.nih.gov/42113280/`

### Design

- six artificial linear features;
- each feature 30 m long;
- experiments in urban and rural meadows in Southwest England;
- plant assemblages at both ends of linked features, with unlinked assemblages as controls;
- seven plant species attracting different pollinator groups including bees, flies, and moths;
- seed set used as the functional pollination response.

### Observed result

Adding linear features increased overall seed set. Three bee-pollinated species showed significant pollination improvement, whereas fly- and moth-pollinated species were less affected.

### CREST consequence

The same future action

\[
a=\text{connect patches with a linear feature}
\]

is not associated with one common response across all mechanism/guild states.

A quotient that retains only

\[
q(x)=\{\text{linked},\text{unlinked}\}
\]

cannot support a universal species-level response law when pollinator-guild identity changes the response to the same intervention.

For a response target such as seed set, pollinator guild/mechanism is therefore state-relevant in at least this experimental system.

### What is demonstrated

- direct intervention on future connectivity;
- overall benefit of connection at assemblage level;
- mechanism/guild-dependent heterogeneity under the identical connection intervention.

### What is not demonstrated

- connection always increases pollination;
- all bee-pollinated plants respond equally;
- guild identity alone is the final sufficient state variable.

---

## Test 3 — Habitat label is weaker than quality/network role for city-scale persistence

### Sources

Geppert et al. 2026, *Biological Conservation* 315:111680, **Species-habitat networks inform pollinator conservation strategies in cities**.

DOI: `10.1016/j.biocon.2025.111680`

Article:
`https://www.sciencedirect.com/science/article/pii/S0006320725007177`

Public data:
`https://zenodo.org/records/18059923`

Dataset DOI: `10.5281/zenodo.18059923`

### Design

- 105 sampling sites in Padua, Italy;
- six urban habitat types: abandoned meadows, crop-field margins, gardens, parks, pollinator-friendly-mown parks, and road margins;
- bees and hoverflies sampled for 20-minute transect walks from spring to late summer;
- species–habitat networks and patch-removal robustness analyses.

### Observed result

Most pollinator species used most habitat types, giving a highly generalistic network. Road margins were the main low-quality exception. Landscape green area positively affected wild bees, while local flower cover and low mowing were important. Network robustness declined when the highest-quality patches were removed first; pollinator dependence was concentrated disproportionately on patches with high flower cover and vegetation height.

### CREST consequence

A categorical state such as

\[
q_{\rm habitat}(x)=\text{park/garden/meadow/road margin/...}
\]

is not sufficient to represent the intervention target `city-scale pollinator robustness` by itself.

Patch quality and network role change the response to a removal action even among patches that may share broad habitat labels. Conversely, except for road margins, habitat identity itself was relatively weak compared with resource quality.

A more adequate response-oriented quotient would need to preserve at least some combination of:

- floral resource state;
- mowing/vegetation structure;
- surrounding green area;
- network contribution or dependence.

### Evidence boundary

The public Zenodo record confirms that abundance data for 105 sites are available in `Data_Geppert_2026_BiologicalConservation.xlsx`. In the present ChatGPT execution environment the binary workbook could not be downloaded reliably, so this step is a source-level reanalysis of the published experiment/results rather than a fresh row-level recalculation. A future local replay should reproduce the network-removal curves directly from the archived workbook.

---

# Matched CREST result

The three systems reject three increasingly strong coarse representations:

| Coarse state | Counterevidence | Required added distinction |
|---|---|---|
| `isolated / connected` by map geometry | pollen moves among isolated patches | realized/potential pollinator movement and matrix context |
| `linked / unlinked` | identical corridor action has guild-dependent seed-set effect | pollinator guild / response mechanism |
| habitat-type label | network robustness depends strongly on patch quality and targeted removal order | resource quality and network role |

Thus the empirical pattern is not merely that cities are heterogeneous. It is:

\[
\boxed{
\text{geometric state}
\;<\;\text{functional-connectivity state}
\;<\;\text{response-oriented state}
}
\]

in the sense that progressively stronger scientific responsibilities expose distinctions erased by simpler labels.

This is exactly the kind of ecological situation CREST is designed to audit: the underlying patch may not change, but a new target or intervention can require a finer state representation.

---

# Falsifiable next step

The next exact analysis should use the Padua workbook to compare at least two predictive/state summaries for patch-removal outcomes:

1. **M0 — label-only:** habitat type / geometric patch identity;
2. **M1 — response-aware:** floral cover + mowing/vegetation structure + surrounding green area + network role.

Use held-out-site or bootstrap removal prediction to ask whether M1 predicts abundance/robustness loss materially better than M0.

A null result would weaken the CREST ecological projection that these added distinctions are necessary for this target, while leaving the finite CREST theorem untouched.
