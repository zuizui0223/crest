# Ecology-grounded CREST worked case — shallow-lake eutrophication and restoration

> **Status:** literature-grounded conceptual validation, not an empirical parameter fit and not a new theorem. No numerical parameter values are invented. The purpose is to show that every CREST layer can be mapped to real ecological mechanisms and management options documented in the shallow-lake restoration literature.

## 1. Why this system is useful

Shallow eutrophic lakes are a strong CREST test because the same current water-quality description can sit inside different histories and feedback structures, and management responses depend on those hidden distinctions.

Published restoration literature establishes the following background:

- shallow lakes can exhibit contrasting clear-water and turbid regimes and abrupt regime shifts as resilience is lost (Scheffer et al. 2001);
- after external phosphorus loading is reduced, recovery can be delayed by sediment phosphorus accumulated during the previous high-loading period;
- biological inertia can also persist through fish-community structure and delayed return of submerged macrophytes;
- restoration therefore commonly combines external-load reduction with interventions such as sediment phosphorus control, fish biomanipulation, and macrophyte restoration;
- long-term recovery can fail or relapse when external loads remain too high, internal phosphorus persists, or the biological feedbacks that stabilize clear water are not re-established.

These are documented ecological mechanisms, not CREST assumptions.

## 2. Present snapshot

Let a management snapshot be

\[
X=(\text{current turbidity / chlorophyll / water-column nutrient status}).
\]

CREST does **not** claim that the routinely measured variables above are always identical in lakes with different mechanisms. The worked comparison asks a conditional question:

> if two possible lake worlds are compatible with the same current management-level snapshot, can they safely be assigned the same state for a restoration decision?

That is a state-adequacy question, not an assertion that a particular pair of named lakes has identical observations.

## 3. Temporally extended worlds

Consider possible worlds with the same current coarse snapshot but different relevant coordinates.

### World A — sediment phosphorus legacy dominates delayed recovery

Relevant history:

- prolonged high external phosphorus loading accumulated a mobile sediment phosphorus pool;
- external loading has subsequently been reduced.

Relevant future-response structure:

- external-load reduction alone may produce delayed improvement because internal sediment release can sustain water-column phosphorus;
- a sediment-focused intervention can therefore alter the future response.

### World B — food-web / macrophyte feedback dominates delayed recovery

Relevant history and structure:

- the lake remains dominated by a fish/community configuration characteristic of turbid conditions;
- submerged macrophytes have not yet re-established.

Relevant future-response structure:

- external-load reduction can be insufficient for rapid recovery because biological feedbacks maintain turbidity;
- fish biomanipulation or macrophyte restoration can alter the future response.

The literature supports both kinds of lag/resistance. CREST does not assume that every real lake belongs cleanly to one world; mixed mechanisms are expected and can be represented by additional worlds.

## 4. CREST mapping

| CREST object | Shallow-lake mapping |
|---|---|
| present snapshot \(X\) | current coarse water-quality status: turbid/eutrophic descriptor, supported by routine water-column observations |
| relevant history \(h\) | past external phosphorus loading and the sediment phosphorus pool accumulated under that history |
| future grammar \(\Gamma\) | external nutrient reduction; sediment-P control/dredging or chemical binding; fish biomanipulation; macrophyte restoration |
| retained mechanism family \(\Theta\) | internal-P persistence; fish-mediated trophic feedback; macrophyte-mediated clear-water feedback; mixtures thereof |
| inherited semantics \(\mathcal H\) | a management label such as “eutrophic/turbid lake” or “restoration-ready after load reduction” carried from the pre-intervention classification into a structurally changed post-load-reduction system |
| evidence map \(D\) | routine water-column monitoring versus added sediment-P, fish-community, and macrophyte observations |
| target \(T\) | e.g. “is external-load reduction alone expected to be sufficient?” or “which supplementary restoration channel is required?” |

## 5. Snapshot-sufficiency audit

For a target that asks only

> is the lake currently turbid/eutrophic?

a coarse current snapshot may be sufficient.

For the target

> is external-load reduction alone sufficient for recovery, or which supplementary intervention is required?

the same coarse snapshot may be insufficient if Worlds A and B imply different intervention responses.

Thus the worked case illustrates the factorization question

\[
X(\omega)=X(\omega')
\centernot\Rightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega')
\]

for a restoration-response contract, while allowing snapshot sufficiency for a purely descriptive current-status contract.

## 6. CCOC reading — future/intervention insufficiency

If the only contemplated action is external-load reduction, two worlds may be treated similarly at a coarse management interface.

Once the action repertoire is enlarged to include a sediment-specific treatment and a food-web-specific intervention, latent distinctions can become operationally addressable. A world dominated by sediment-P legacy and a world dominated by food-web resistance need not have the same response to those actions.

This is the ecological analogue of the CCOC point:

\[
\text{current or restricted-future equivalence}
\not\Rightarrow
\text{equivalence under a richer future grammar}.
\]

No claim is made that the published lake literature proves the CCOC extremal bit lower bound; the literature supplies an ecology-grounded interpretation of the future-grammar distinction.

## 7. MLTR reading — inherited category after structural change

Suppose a management classification was established under sustained external nutrient loading. After major external-load reduction, the system has structurally changed, but a coarse inherited label may still be reused.

The question is then not whether the old label is linguistically understandable. It is whether it remains operationally sufficient for the new restoration actions. Sediment legacy and food-web/macrophyte feedbacks can make the post-reduction system require distinctions that the pre-reduction classification did not need.

This is a natural source-relative transport problem: retain the inherited category only where its operational merges remain valid; refine it where the altered management problem exposes different successors.

## 8. MRM reading — mechanism ambiguity

Internal phosphorus release and biological feedback can both contribute to persistent turbid conditions, but they do not imply identical responses to all restoration actions.

Therefore a current turbid state can be compatible with multiple retained response mechanisms. If the management target depends on which intervention will work, the mechanism ambiguity is state-relevant. If the target is only current-status reporting, the same mechanism distinction can remain safely hidden.

This is exactly the MRM principle that mechanism identity matters only where retained response types disagree on a required future response.

## 9. CED reading — required state versus identified state

Routine water-column measurements can establish current water quality without necessarily identifying whether persistent recovery resistance is dominated by sediment phosphorus, fish-community feedback, macrophyte absence, or a mixture.

This last sentence is an **inference from the distinct mechanisms and measurement channels documented in the restoration literature**, not a claim that a specific standard monitoring protocol is universally non-identifying.

CREST therefore separates:

- **required state:** the mechanism/history distinction needed for the restoration-response target;
- **identified state:** whichever of those distinctions are resolved by the actual sediment, fish, macrophyte and water-column evidence collected;
- **reportable target:** a current-status target can remain reportable even when the supplementary-intervention target remains unresolved.

The practical prediction is qualitative but falsifiable: adding a measurement channel that directly targets the unresolved mechanism should be more informative for that restoration target than arbitrarily increasing replication of an aggregate water-quality variable that leaves the mechanism ambiguity intact.

## 10. What this case validates and what it does not

### Validated as an ecology-grounded mapping

The published literature independently supports:

- historical nutrient-load legacy;
- internal sediment phosphorus as a recovery lag;
- fish and macrophyte feedbacks as biological resistance/inertia;
- multiple restoration actions acting on different channels;
- hysteresis and delayed or failed recovery after nutrient reduction.

Therefore CREST's history, mechanism, future-action, and evidence distinctions are not merely computer-science variables renamed with ecological nouns.

### Not yet validated empirically

This document does **not** establish from a real dataset that:

- two named lakes have exactly the same snapshot but different CREST states;
- a fitted CREST partition predicts restoration outcomes better than an alternative POMDP/PSR or mechanistic lake model;
- the J1 finite partition inferred from field data is uniquely correct;
- a particular sediment/fish/macrophyte monitoring package is minimum-cost.

Those would require an empirical application with explicit data and model comparison.

## 11. Closest literature anchors

- Scheffer, M., Carpenter, S., Foley, J., Folke, C. & Walker, B. (2001). *Catastrophic shifts in ecosystems*. Nature 413:591–596. DOI 10.1038/35098000.
- Søndergaard and collaborators' work on shallow-lake restoration and internal phosphorus loading documents sediment-P legacy and delayed recovery after external-load reduction.
- Reviews of biomanipulation and shallow-lake restoration document chemical inertia, fish-community feedback, delayed macrophyte return, hysteresis, and the need for lake-specific combinations of external-load reduction and supplementary restoration.

## 12. Decision

This case satisfies the current requirement for **one end-to-end ecology-grounded worked mapping without invented parameter values**. It is a conceptual validation, not empirical performance validation.

For stronger generality, the next application should come from a structurally different ecology—e.g. fragmented terrestrial metacommunities, island pollination networks, or invasion management—rather than another shallow-lake variant.