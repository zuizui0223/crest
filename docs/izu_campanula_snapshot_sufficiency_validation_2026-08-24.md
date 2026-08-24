# Izu Campanula snapshot-sufficiency validation — 2026-08-24

> Purpose: turn the existing `izu-core` direct effective-pollinator dependency pilot into a prospective ecological test of CREST snapshot sufficiency. This does **not** create a second field programme and does **not** prove the finite CREST theorem.

## Historical anchor

The classical Izu studies already show that a coarse `island` label is not one reproductive/pollination state.

- Inoue & Amano (1986) reported *Bombus diversus* as the predominant pollinator on Honshu, *Bombus ardens* plus halictid bees on Oshima, and halictid bees on Niijima, Kozushima, and Hachijo. Island flowers were smaller than mainland flowers. Most Honshu plants were highly self-incompatible; Oshima was mixed; Hachijo plants were self-compatible and potentially autogamous.
- Inoue (1988) extended bagging experiments across six Izu Islands and mainland Honshu. Most Honshu and Oshima plants were self-incompatible, whereas almost all plants on the Izu Islands except Oshima were self-compatible. Bumblebees were absent from the Izu Islands except Oshima.

Sources:
- `10.1111/j.1442-1984.1986.tb00018.x`
- `10.1111/j.1442-1984.1988.tb00178.x`

These studies motivate the modern test, but they do not by themselves identify historical causation.

---

## Existing empirical infrastructure

The active `zuizui0223/izu-core` mainline (Issue #91) already requires linked records for:

- observation effort, including zero-visit windows;
- visitor bouts and conservative functional/contact scores;
- single-visit pollen deposition (SVD) with no-visit controls;
- `open_pollinated` flowers;
- `bagged_autonomous` flowers;
- `supplemental_outcross` flowers;
- mature fruit and seed linkage;
- optional parentage.

CREST therefore does not need a new assay. It only needs the existing channels to be interpreted as a declared future-response grammar.

---

# CREST test

## 1. Deliberately coarse present-state candidates

Test several candidate present quotients separately.

### Q0 — island label only

\[
q_0(\omega)=\text{island / population identity or island regime}.
\]

This is intentionally coarse and is already challenged historically by Oshima.

### Q1 — morphology snapshot

\[
q_1(\omega)=\text{current floral morphology vector}.
\]

Use only measurements available before any pollination treatment or visitor-response readout (for example flower size and other frozen focal floral traits).

### Q2 — morphology + current ambient performance

\[
q_2(\omega)=\bigl(\text{morphology},\text{current open performance}\bigr).
\]

This is a stronger snapshot: two plants/populations may look similar and currently set similar fruit/seed, yet differ in autonomous reproduction or response to pollen supplementation.

No quotient is assumed correct in advance.

---

## 2. Declared future-response grammar

Use the already planned field channels as the intervention/response repertoire

\[
\Gamma_{\rm Izu}=\{
\text{ambient/open},
\text{bagged autonomous},
\text{supplemental outcross},
\text{visitor-group SVD}
\}.
\]

For plant or population world \(\omega\), define a response vector schematically as

\[
R_{\rm Izu}(\omega)=
\left(
Y_{\rm open},
Y_{\rm bag},
Y_{\rm supp},
SVD_{g_1},\ldots,SVD_{g_k}
\right),
\]

where terminal outcomes must be defined in the source-locked `izu-core` field contract (fruit/seed outcomes for treatments; background-adjusted SVD only when controls exist).

This is the ecological object against which snapshot sufficiency is tested.

---

## 3. Exact empirical question

A candidate snapshot \(q\) is adequate for the declared response target only if worlds merged by \(q\) have indistinguishable response distributions after accounting for the prespecified uncertainty model.

Finite exact CREST writes

\[
q(\omega)=q(\omega')\Rightarrow R(\omega)=R(\omega').
\]

The field version is necessarily statistical. The prospective null is:

> after conditioning on the frozen present snapshot, island/population/history adds no reproducible information about the declared intervention-response vector.

A failure occurs when two plants/populations sufficiently similar under the chosen snapshot show reproducibly different responses to the same declared treatment or visitor-functional exposure.

The key point is not statistical significance by itself. The test asks whether a merge licensed by the proposed snapshot remains safe for the declared response.

---

# Primary contrasts

## Contrast A — `island` is too coarse

Historical data already predict that Oshima should not be merged blindly with bumblebee-absent Izu islands under a reproductive-response contract.

Modern test:

\[
R_{\rm Izu}(\text{Oshima})
\stackrel{?}{=}
R_{\rm Izu}(\text{bumblebee-absent island})
\]

after accounting for present morphology and observation effort.

A difference in autonomous reproduction, pollen limitation, or visitor-group effectiveness would demonstrate that island status or present morphology alone erases response-relevant distinctions.

**Claim firewall:** a modern difference does not prove historical bumblebee loss caused the difference.

## Contrast B — same current performance, different hidden dependency

Find plants/populations with overlapping current `open_pollinated` performance. Ask whether they differ in

\[
Y_{\rm bag}
\quad\text{or}\quad
Y_{\rm supp}-Y_{\rm open}.
\]

If so,

\[
\text{same current reproductive output}
\not\Rightarrow
\text{same reproductive state}.
\]

This is a direct ecological example of a present performance snapshot hiding different causal dependence.

## Contrast C — same morphology, different visitor-response structure

Within overlapping floral morphology, compare controlled SVD by visitor functional group.

If two snapshot-similar plants/populations show different background-adjusted SVD under the same visitor group, morphology alone does not factor the relevant response state.

Only visitor groups satisfying the existing `izu-core` no-visit-control and plant-level dispersion gates may enter this contrast.

---

# Analysis hierarchy

Do **not** jump directly to one omnibus model. Test progressively richer quotients.

1. `M0`: island/regime label only.
2. `M1`: frozen floral morphology only.
3. `M2`: morphology + ambient/open performance.
4. `M3`: morphology + direct reproductive-dependency channels (`bagged`, `supplemental`, optional parentage-derived quantities only when identified).
5. `M4`: M3 + visitor-group effective-service/SVD state.

The CREST question is whether added dimensions repair response non-portability, not whether a larger model has a mechanically better in-sample fit.

Preferred evaluation:

- held-out plant and held-out population prediction where sample size permits;
- explicit calibration and uncertainty intervals;
- no pseudo-replication of flowers or visits as independent plants;
- zero-visit windows and losses retained;
- response-specific comparison rather than a single pooled score if mechanisms differ.

A richer quotient is supported only if its added distinctions improve out-of-sample prediction or remove systematic response disagreement in a biologically meaningful way.

---

# Minimum result that would count as a CREST ecological validation

A full causal-history reconstruction is **not** required.

The minimum useful result is one reproducible pair/class of present worlds for which:

\[
q_{\rm snapshot}(\omega)=q_{\rm snapshot}(\omega')
\]

within the declared tolerance, but

\[
R_{\rm Izu}(\omega)\neq R_{\rm Izu}(\omega')
\]

for at least one prespecified response channel with adequate independent-plant support.

That would empirically reject the chosen snapshot as sufficient for that contract.

The stronger result would show that adding one biologically interpretable latent/context variable (for example autonomous reproductive capacity or visitor functional dependence) repairs the disagreement across held-out plants/populations.

---

# What would weaken the ecological CREST projection

The projection is weakened if, across adequately powered populations and years:

- floral morphology/current performance alone predicts all declared treatment/SVD responses with no systematic population/history residual;
- adding breeding-system/dependency or visitor-functional state does not improve held-out response prediction;
- Oshima and bumblebee-absent islands become response-equivalent once current observables are matched.

Such a result would support snapshot sufficiency for this particular scientific contract. It would not refute CREST as mathematics; CREST explicitly allows snapshot sufficiency to hold.

---

# Coordination with `izu-core`

CREST must remain downstream of `izu-core` measurement admission.

Do not import a response into CREST unless the corresponding `izu-core` gate is open:

- SVD requires no-visit/background controls and independent-plant dispersion;
- reproductive treatments require linked terminal outcomes and independent-plant support;
- parentage remains optional and unresolved paternal identity is not selfing;
- final dependency reliability remains a separate repeated-final-estimand problem.

The CREST layer asks whether admitted measurements support or falsify a proposed state quotient. It does not relax any biological measurement requirement.
