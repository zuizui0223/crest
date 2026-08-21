# CREST prior-art review protocol and evidence matrix — 2026-08-21

> **Status:** reproducible systematic-prior-art-style review protocol executed over publicly searchable sources on 2026-08-21. This is stronger and more reproducible than the earlier broad audit, but it is **not called a PRISMA systematic review** because no complete Web of Science/Scopus database export, database-level deduplication, or dual-reviewer screening was available. Negative searches are not treated as proof of historical firstness.

## 0. Review question and decision rule

The review asks:

> Which parts of CREST are already established in ecology, decision theory, state-abstraction theory, causal abstraction, and philosophy of scientific representation, and which contribution survives after those overlaps are removed?

The decision rule is deliberately conservative:

- if a prior work already states the same generic idea, CREST does **not** claim that idea as novel;
- if prior work contains the same mathematical substrate in a different domain, CREST does **not** claim priority for the substrate;
- a negative search supports only `no direct match located in this audit`, never `first`;
- preprints and unpublished manuscripts can lower the novelty ceiling even when they are excluded from the journal reference list;
- the remaining CREST contribution must survive if every generic word such as `new`, `first`, `minimal`, `adequacy`, `obsolescence`, or `state abstraction` is removed from the novelty claim.

Search cutoff: **2026-08-21**.

---

## 1. Sources actually searched

Discovery and verification used publicly searchable records from:

- PubMed and PubMed Central;
- publisher pages (Wiley, Springer Nature, Elsevier/ScienceDirect, PLOS, Royal Society and others surfaced by search);
- USGS Publications Warehouse;
- institutional publication repositories that expose bibliographic metadata and, in some cases, Scopus citation counts;
- PhilPapers / PhilArchive;
- arXiv;
- broad web scholarly search over exact titles, author-title combinations, concept phrases, and citation-chain terms.

### Important coverage limitation

This workflow did **not** obtain a complete Web of Science or Scopus result export. Institutional pages sometimes exposed Scopus links or counts, but this is not equivalent to searching those proprietary databases comprehensively. Google Scholar was used only indirectly through web discovery and publisher/institutional citation links, not as a reproducible bulk export.

Therefore the present artifact is best described as a **reproducible broad prior-art review with citation-chain screening**, not an exhaustive bibliometric review.

---

## 2. Inclusion and exclusion criteria

### Include when a source does at least one of the following

1. defines or analyzes ecological/system state identity or equivalence;
2. analyzes ecological state transitions, intervention, restoration or resilience;
3. explicitly addresses model adequacy, coarse graining, state/control-variable selection or adequacy-for-purpose;
4. analyzes transferability/generalization across ecological contexts or novel conditions;
5. combines ecological management with hidden state, observational uncertainty, structural/model uncertainty, multiple candidate models, or learning;
6. constructs task-, policy-, prediction-, or intervention-relevant state abstractions;
7. links monitoring design or information acquisition to changing management questions or decision value;
8. formalizes scientific-representation adequacy, minimal adequate representations, obsolescence, certification or repair;
9. provides a close mathematical analogue to a CREST-derived concept.

### Exclude from novelty ownership when

- the match is only terminological without the relevant structure;
- the source concerns a different use of `state` with no representational/decision connection;
- the source is a generic tutorial that adds no relevant claim beyond an included anchor;
- the source is duplicated across repositories/publisher mirrors.

Preprints are retained in the **internal novelty firewall** even when they are unsuitable for the published-reference list.

---

## 3. Search strata and reproducible query families

The searches used combinations of the following query families, with exact-title searches for all anchor papers discovered.

### S1 — ecological state / identity / equivalence

```text
("ecosystem state" OR "ecological state") equivalence relation identity resilience
"Equivalence relations on ecosystems"
"Equivalence and dissimilarity of ecosystem states"
"Identity of ecological systems" resilience state identity
```

### S2 — State-and-Transition Models / restoration / intervention

```text
"state-and-transition" ecological states intervention thresholds restoration
alternative stable states ecosystem state management restoration
```

### S3 — ecological model adequacy / coarse graining

```text
"Making ecological models adequate"
ecological model adequacy state variables control variables coarse graining
```

### S4 — adequacy-for-purpose / scientific representation

```text
"adequacy-for-purpose" environmental sciences
"Model Evaluation: An Adequacy-for-Purpose View"
"Data models, representation and adequacy-for-purpose"
```

### S5 — transferability / novel conditions

```text
"ecological model transferability" novel conditions
"Model application niche analysis"
"Outstanding Challenges in the Transferability of Ecological Models"
```

### S6 — POMDP / hidden state / management-relevant state reduction

```text
"Which States Matter" conservation POMDP
"A primer on partially observable Markov decision processes" ecology
"adaptive management" state uncertainty model uncertainty POMDP ecology
```

### S7 — structural/mechanism uncertainty / multiple models

```text
"Managing and learning with multiple models" ecology
"Uncertainty, learning, and the optimal management of wildlife"
"Adaptive management under structural uncertainty" model set
multimodel adaptive management ecological response management actions
```

### S8 — adaptive monitoring / value of information

```text
"adaptive monitoring" ecology changing questions management
"Adaptive monitoring in the real world"
"value of information" ecological monitoring management
"Which uncertainty?" expected value of information adaptive program
```

### S9 — state abstraction / bisimulation / causal abstraction

```text
state abstraction MDP bisimulation task-specific minimal representation
multi-task state abstraction common representation multiple tasks
"Transferring state abstractions between MDPs"
"Learning Robust State Abstractions for Hidden-Parameter Block MDPs"
"causal abstraction" intervention consistency exact transformation
```

### S10 — representation adequacy / obsolescence / certification

```text
"Carriers and Adequacy for Purpose"
"representational obsolescence" adequacy
"Self-Certification of Representation Adequacy"
representation adequacy repair certification task loss
```

### S11 — abrupt representational change

```text
"Phase Transitions for the Information Bottleneck in Representation Learning"
representation phase transition abstraction compression
```

### S12 — full CREST-combination searches

```text
"ecological state" future intervention mechanism uncertainty observation evidence representation equivalence
"ecological state" transferability model uncertainty monitoring intervention
"state equivalence" ecology intervention observation uncertainty management
"state representation" ecology monitoring management uncertainty abstraction
```

No direct source matching the complete four-contract + carrier-gate + evidence-gate architecture was located by S12. This is a **search result, not a priority proof**.

---

## 4. Citation-chain anchors screened

The following anchors were used not only as isolated hits but to expose older and newer neighboring work through their references, related-paper lists, reviews, or institutional citation metadata.

### A1 — ecological identity / equivalence

- Cumming & Collier (2005), *Change and identity in complex systems*.
- Collier & Cumming (2011), *A Dynamical Approach to Ecosystem Identity*.
- Delettre (2021), *Identity of ecological systems and the meaning of resilience*.
- Spencer / Boit & Spencer line: *Equivalence relations on ecosystems* (preprint 2017) and *Equivalence and dissimilarity of ecosystem states* (Ecological Modelling, 2019).

Key consequence: ecological `state identity` and ecosystem equivalence relations are explicit prior art.

### A2 — ecological adequacy

- Getz et al. (2018), *Making ecological models adequate*.
- Parker (2020), *Model Evaluation: An Adequacy-for-Purpose View*.
- Bokulich & Parker (2021), *Data models, representation and adequacy-for-purpose*.
- Parker, Carey, Olsson & Thomas (2026), *An adequacy-for-purpose perspective for the environmental sciences*.

Key consequence: purpose-relative adequacy, state/control-variable adequacy, data determinacy and coarse graining are established.

### A3 — management-relevant state reduction / POMDP

- Nicol & Chadès (2012), *Which States Matter?*.
- Chadès et al. (2017), *Optimization methods to solve adaptive management problems*.
- Chadès et al. (2021), *A primer on partially observable Markov decision processes (POMDPs)*.

The 2021 primer explicitly states that reducing state and observation variables to the smallest ensemble possible is critical, and places *Which States Matter?* in that lineage.

Key consequence: task/policy-relevant state reduction and partial observability are established within ecology itself.

### A4 — adaptive management under changing futures

- Nicol et al. (2015), *Adapting environmental management to uncertain but inevitable change*.
- Memarzadeh/Boettiger line, including *Adaptive management of ecological systems under partial observability* (2018).

Key consequence: multiple future scenarios, non-stationarity, state uncertainty, model uncertainty, observation and policy adaptation are established.

### A5 — structural uncertainty / alternative mechanisms

- Williams (2001), *Uncertainty, learning, and the optimal management of wildlife*.
- Probert et al. (2011), *Managing and learning with multiple models: Objectives and optimization algorithms*.
- Fackler & Pacifici (2014), *Addressing structural and observational uncertainty in resource management*.
- Rozowski & Fackler (2025), *Adaptive management under structural uncertainty: A linear opinion pool approach to expanding the model set*.

Key consequence: keeping multiple response models alive, updating them, using actions to learn, and combining structural with observational uncertainty are established ecological decision-theory topics.

### A6 — adaptive monitoring / value of information

- Lindenmayer & Likens (2009), *Adaptive monitoring: a new paradigm for long-term research and monitoring*.
- Lindenmayer & Likens (2011), *Adaptive monitoring in the real world: proof of concept*.
- McCord & Pilliod (2022), *Adaptive monitoring in support of adaptive management in rangelands*.
- Williams, Eaton & Breininger (2011), *Adaptive resource management and the value of information*.
- Runge/Converse-era adaptive-management literature, including *Which uncertainty? Using expert elicitation and expected value of information to design an adaptive program* (2011).
- Nicol et al. (2018), *Making the best use of experts' estimates to prioritise monitoring and management actions*.
- lake/water-quality VOI applications (2020, 2024).

Key consequence: monitoring redesign when questions change, selective uncertainty reduction, and the fact that not all state information is worth acquiring are established.

### A7 — transferability

- Moon et al. (2017), *Model application niche analysis*.
- Yates et al. (2018), *Outstanding Challenges in the Transferability of Ecological Models*.
- later ecological forecasting/generalization work under novel environmental and biotic conditions.

Key consequence: generic non-portability under novel contexts is established. MLTR's defensible difference is source-relative exact semantic transport/repair under a declared relation, not generic transferability.

### A8 — abstraction theory outside ecology

- Shalizi & Crutchfield (2001), causal states / minimal predictive representation.
- stochastic bisimulation and MDP abstraction literature (Ferns et al.; Li, Walsh & Littman and successors).
- Walsh, Li & Littman (2006), transferring state abstractions between MDPs.
- Zhang et al. (ICLR 2021), robust abstractions for hidden-parameter/multi-task MDPs.
- Beckers & Halpern / Rubenstein et al. causal-abstraction line.
- recent multi-task/context-sensitive abstraction work through 2026.

Key consequence: minimal predictive/action-preserving abstractions, reusable abstractions across tasks, and multi-task shared representations are established mathematical neighborhoods.

### A9 — formal representation adequacy closest to CREST vocabulary

- Swanson (2026), *Carriers and Adequacy for Purpose: A Formal Framework for Representation-Constrained Adequacy* (PhilArchive/PhilPapers manuscript).
- Huang (2026), *Self-Certification of Representation Adequacy: Sequential Certification at Minimum Task Loss* (arXiv).

Swanson is especially close: refinement preorder, minimal adequate carriers, regime-indexed adequacy, residue, representational obsolescence and revision are already explicit.

Key consequence: CREST-derived vocabulary such as adequacy envelope, obsolescence and minimal refinement must not be marketed as generic conceptual inventions.

---

## 5. Claim-by-claim evidence matrix

| CREST proposition or vocabulary | Closest prior-art neighborhood | Degree of overlap | What remains for CREST | Novelty verdict |
|---|---|---:|---|---|
| Ecological state as equivalence class | Boit & Spencer; Delettre | **direct** | different criterion and contract architecture | **not novel generically** |
| State identity can depend on what variables/state notion matter | Delettre; resilience/identity literature | **direct** | formal four-contract diagnostic map | **not novel generically** |
| Intervention-sensitive state | State-and-Transition Models; adaptive management | **direct** | exact open-future/interface lower bounds in CCOC | generic idea blocked |
| Purpose-relative adequacy | Parker; Bokulich & Parker; Parker et al. 2026 | **direct** | ecology-specific coupled contract architecture | generic idea blocked |
| Model/state variables should be adequate for management | Getz et al. | **direct** | exact state-equivalence obligations and failure certificates | generic idea blocked |
| Minimal task/policy-relevant ecological state | Nicol & Chadès; POMDP primer | **direct** | joint fixed point across heterogeneous obligations | generic idea blocked |
| Full state need not be known for a good decision | Nicol & Chadès; VOI/adaptive management | **strong** | exact `state unresolved / target singleton` reporting distinction | useful formal specialization, not priority claim |
| State process differs from observation process | HMM/POMDP ecology | **direct** | required-state vs evidence-licensed-state vs target separation | generic distinction blocked |
| Multiple mechanisms/models may imply different management responses | Williams; Probert; Fackler; Rozowski | **direct** | MRM exact response-type quotient/lower bounds and CREST coupling | generic idea blocked |
| Monitoring should change as questions/management change | adaptive monitoring literature | **direct** | exact contract-refinement failure criterion and debt within CREST | generic idea blocked |
| Value of additional monitoring depends on decision | VOI literature | **direct** | resolution debt is not VOI; exact partition requirement before costing | vocabulary useful, not general novelty |
| Model/state may fail under novel conditions | Moon; Yates; forecasting transfer literature | **direct** | MLTR inherited-label exact repair and route/history structure | generic transferability blocked |
| Minimal/reusable state abstractions across tasks | RL multi-task/state abstraction literature | **strong** | CREST four separately interpreted ecological obligations | common abstraction not novel |
| Intervention-consistent causal abstraction | causal-abstraction literature | **direct** | CREST diagnostic separation / ecology mapping | generic abstraction blocked |
| Representation adequacy can become obsolete after regime change | Swanson 2026 | **direct** | CREST exact ecological cross-gate mechanisms | generic obsolescence blocked |
| Minimal refinement restores adequacy | classical partition order; Swanson-style revision | **strong/direct substrate** | CREST evidence-specific `E ∨ J` and state/target debt interpretation | not generic novelty |
| Abrupt representation complexity change | information-bottleneck/state-abstraction literature | **strong** | CCOC's specific same-system open-grammar extremal construction | generic phase-transition claim blocked |
| One management-action enrichment yields viability↑, required-state-resolution↑, full-state-identifiability↓, target still reportable | no direct matching ecological theorem located in this audit | **partial neighbors only** | exact cross-gate finite witness | **strong surviving candidate** |
| Structural-repair optimum differs from fully evidence-licensed optimum | model repair + VOI are neighbors, but no direct match located | **partial** | O1 cross-gate noncommutation | **strong surviving candidate** |
| Four independently motivated obligations require a common carrier before one joint state can be constructed | no direct full match located | **partial neighbors** | J3/J6 → J1 → evidence gate architecture | **strongest architectural candidate** |
| One newly relevant action can induce arbitrary `m`-bit exact monitoring-resolution debt across finite family | state abstraction/representation complexity are neighbors; no direct ecological match located | **partial** | CCOC extremal family + R1 reinterpretation | **strong quantitative candidate, priority unresolved** |

---

## 6. Backward/forward-chain findings that materially changed the paper

### 6.1 `Decision-Safe Ignorance` is not a safe novelty label

The 2012 *Which States Matter?* paper does more than use a POMDP: it explicitly constructs only the state resolution needed to maintain the optimal management policy and finds that accurate population-state discovery can matter less than management for long-run persistence. The 2021 POMDP primer explicitly continues this minimal-state/minimal-observation program.

Therefore CREST may retain the exact reporting regime

\[
E\text{ licenses }T,
\qquad
E\text{ does not license }J,
\]

but should not claim the underlying insight `we need not know the full ecological state to decide well` as new.

### 6.2 `Monitoring changes when responsibilities change` is established

Adaptive-monitoring literature explicitly defines monitoring as evolving with new management questions, environmental conditions, tools and information. The 2011 proof-of-concept redesigns pre-existing monitoring to answer new policy/scientific questions while preserving time series.

Therefore CREST's stronger claim must be mathematical and narrower: under an order-compatible state refinement with fixed evidence, exact full-state identifiability can fail in a characterized way, and R1 gives the unique minimum partition refinement required to restore it.

### 6.3 Mechanism uncertainty + management + learning is established

Williams (2001), Probert et al. (2011), Fackler & Pacifici (2014) and later adaptive-management work explicitly combine multiple models/structural uncertainty, monitoring, state uncertainty and management action. Some actions can be chosen partly for learning.

Therefore MRM's philosophical role is not `ecology should keep multiple mechanisms`. Its defensible formal role is the exact candidate-independent/typed/set-valued response criterion and minimal candidate-safe quotient, then its use as one obligation in the CREST joint-state construction.

### 6.4 `One representation for multiple tasks` has a large AI/RL neighborhood

Multi-task and transferable state-abstraction literature already asks for shared latent state structures and abstractions that generalize across task families. This makes the anticipatory common-refinement idea mathematically unsurprising.

Therefore `State Shadow` can be retained as CREST vocabulary for a derived object, but not as a stand-alone novelty pillar.

### 6.5 Swanson changes the safe philosophy framing

Swanson's 2026 manuscript already provides generic formal language for representation-constrained adequacy, minimal adequate carriers, regime-dependent obsolescence and revision. Even if unpublished and excluded from a journal bibliography, it defeats a broad priority claim.

Therefore the philosophy manuscript should not be framed as `the first formal theory of state-representation adequacy`. The safe claim is a theorem-grounded **ecology-specific architecture and cross-gate result set**.

---

## 7. What survives as the CREST contribution

After the stronger prior-art screen, the contribution should be written at two levels.

### 7.1 Architectural contribution

One proposed coarse ecological state is subjected to four scientifically different obligations:

\[
\boxed{
\text{future sufficiency}
+\text{inherited-semantic coherence}
+\text{retained-mechanism robustness}
+\text{evidence/target licensing}
}
\]

CREST does **not** assume these obligations automatically share a world space. It first asks for a compatible carrier, then constructs the unique least-information joint state, then asks whether evidence licenses that state or only the target:

\[
\boxed{
\text{carrier existence}
\rightarrow
\text{joint state requirement}
\rightarrow
\text{evidence / target licensing}
}
\]

No direct source found in this review reproduces this exact architecture. This remains a candidate contribution, not a firstness claim.

### 7.2 Cross-gate mathematical contribution

The strongest non-obvious results are interactions between gates rather than generic concepts:

1. carrier failure can make a fully adequate joint state impossible even though individual abstractions exist;
2. structural repair and fully evidence-licensed repair can have different optima (O1);
3. one added management action can simultaneously
   \[
   \text{viability}\uparrow,
   \quad |J|\uparrow,
   \quad \text{full-state identifiability}\downarrow,
   \]
   while the target remains reportable;
4. the unique minimum evidence refinement needed for full-state recovery is
   \[
   E\vee J,
   \]
   allowing an exact state-resolution debt distinct from target debt;
5. the CCOC extremal family makes this debt arbitrarily large across finite instances from one newly relevant future action.

These are the pieces that should carry the manuscript's substantive load.

---

## 8. Final novelty language after this review

### Reject

> CREST introduces ecological state equivalence.

> CREST is the first purpose-relative theory of ecological state.

> CREST introduces minimal task-relevant ecological states.

> CREST is the first theory that monitoring must adapt when management questions change.

> CREST introduces representational obsolescence, monitoring envelopes, state shadows, or minimal adequate representations.

> CREST is the first framework combining ecological management, model uncertainty and observation uncertainty.

### Defensible

> **CREST is a theorem-grounded architecture for asking whether one coarse ecological state can simultaneously satisfy future, inherited-semantic, mechanism-robust and evidence-licensing obligations. It separates the existence of a coherent common carrier from the least-information state required on that carrier and from whether available evidence identifies that state or only the requested target.**

And the strongest concrete consequence:

> **Within that architecture, additional management capability can enlarge the viable ecological domain while increasing the state resolution required for exact prediction beyond what unchanged monitoring can identify; full-state monitoring debt can become positive even when target debt remains zero.**

Historical firstness is not asserted.

---

## 9. What remains before the word `systematic` can be used without qualification

To upgrade this artifact to a database-complete systematic prior-art review, the remaining external steps are:

1. run the frozen search strings in Web of Science and Scopus with full export;
2. export a reproducible Google Scholar/OpenAlex/Semantic Scholar complement if permitted;
3. deduplicate records by DOI/title;
4. log title/abstract screening decisions against the inclusion criteria above;
5. run explicit backward and forward citation export for the closest anchors;
6. record exclusions with reasons;
7. ideally have a second human reviewer audit the closest-match classifications;
8. freeze a final search date and PRISMA-style flow count.

The current review has already performed substantial anchor-based backward/forward discovery through reviews, publisher reference lists and related-paper searches, but it does not fabricate database coverage that was not available.

---

## 10. Stop rule for CREST novelty development

Further terminology generation should stop unless it produces one of:

- a cross-gate impossibility not reducible to a generic state-abstraction result;
- a necessary-and-sufficient coupling between at least two CREST gates;
- a sharp lower bound that depends essentially on the ecological four-contract architecture;
- an empirical consequence that distinguishes CREST from ordinary adaptive monitoring/POMDP/VOI practice.

Otherwise the correct next task is manuscript positioning and specialist human literature review, not another named concept.
