# Biology & Philosophy submission handoff — CREST

> **Target:** *Biology & Philosophy*  
> **Canonical review manuscript:** `crest_philosophy_biology_philosophy.md`  
> **Repository status:** the finite mathematics, trajectory-first interpretation, novelty firewall, manuscript, and automated submission controls are synchronized. Remaining blockers are author-controlled metadata/final responsibility review and construction of the exact blinded upload candidate.

## 1. Current manuscript identity

### Title

**What Counts as the Same Ecological State? A Contract-Relative Theory of Temporally Extended Ecological States**

### Central question

> **Why can a finite ecological state exist at all when the distinctions relevant to prediction, intervention, inherited meaning, mechanism, and evidence depend on scientific context?**

CREST's working answer is:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

The manuscript does not claim that this trajectory-level formulation is itself historically novel or already proved for general stochastic/continuous systems.

## 2. Logical hierarchy

The current paper is **not** organized as four co-level audits.

```text
temporally extended ecological worlds
    ↓
observation / intervention context
    ↓
snapshot-sufficiency question
    ↓
three structural obstructions
    CCOC — future/composition
    MLTR — inherited semantics/history
    MRM  — retained mechanism response
    ↓
Gate A — admissible finite common carrier
    ↓
Gate B — least-information adequate state J
    ↓
Gate C — evidence licensing / CED
    ↓
full-state / target-only / set-valued report
```

CED is downstream: it asks whether the available evidence identifies distinctions that the state/reporting contract already requires.

## 3. Finite state answer

On a declared admissible finite common carrier `U`, baseline partition `B`, and implemented refinement closures,

\[
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique coarsest / least-information common fixed partition under J1's assumptions. The finite CREST state is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

J1 is the **existence/minimality backbone**. The generic closure/fixed-point machinery is classical and is not the manuscript's principal novelty claim.

For reliability-qualified evidence partition `E_D`,

\[
\text{full deterministic state report exists}
\iff
J\preceq E_D.
\]

A target can remain reportable even when the full state is unresolved, so CREST keeps distinct

\[
\text{required state}\neq\text{identified state}\neq\text{reportable target}.
\]

## 4. Quantitative mathematical headline

The current theorem-level headline is the connected **capability–resolution divergence** family.

For every integer `m >= 1`, one newly admitted action `probe`, with a bounded output alphabet, yields in one connected finite response graph

\[
\boxed{
\Delta |K^*|=1,
\qquad
\Delta K_{U_0}=m.
}
\]

On the retained present slice:

- required state: `1 -> 2^m` classes;
- fixed-monitoring debt: `0 -> m` bits;
- full-state licensing: `yes -> no`;
- coarse target reportability: `yes -> yes`.

Hence there is no universal finite bound depending only on carrier-size gain that upper-bounds the representational burden created by capability expansion.

The qualitative proposition that actions can change useful state abstraction is **not** claimed as new; the manuscript explicitly acknowledges predictive-state, POMDP, causal/bisimulation abstraction, and state/action-abstraction precedents including Konidaris (2019).

## 5. Current verified repository state

Automated state at the current submission-controlled manuscript:

- abstract: **244 words**;
- keywords: **6**;
- repository-defined visible words before References: **6,715**;
- journal hard cap `<=10,000`: **PASS**;
- potential double-blind identifier hits before References: **0**;
- excluded unpublished/preprint audit references in the submission bibliography: **0**;
- theorem/regression suite: **93 tests PASS**;
- Python **3.10 / 3.11 / 3.12**: **PASS**;
- Python 3.12 submission verifier: **PASS**;
- repository hygiene / deterministic submission report: **PASS**;
- automated blockers: **0**.

Canonical generated record: `../artifacts/crest_philosophy_submission_report.json`.

## 6. Current journal-policy check — 2026-08-22

Official journal guidance checked at:

`https://link.springer.com/journal/10539/submission-guidelines`

Current requirements relevant to this manuscript:

- **double-blind peer review**; author-identifying information must be removed from the review manuscript and associated review materials;
- submit a **separate Title Page** containing title, authors, affiliations, corresponding-author contact information, and ORCID(s) if available;
- acknowledgements, disclosures, and funding information belong on the separate title page during blinded review;
- manuscript length: **10,000 words or fewer**;
- abstract: **150–250 words**;
- keywords: **4–6**;
- editable manuscript source is required; Word is standard, while manuscripts with mathematical content may also be submitted in LaTeX;
- generative-LLM use beyond copy editing must be documented in a suitable manuscript section, and human authors remain accountable for the final text.

The current manuscript meets the repository-checkable word/abstract/keyword/anonymity limits. Exact upload-format and declaration placement must still be checked on the final blinded file.

## 7. Claim firewall

### Safe

- CREST gives a contract-relative finite state construction on an admissible declared carrier;
- CCOC, MLTR, and MRM are three structural reasons a present merge can fail;
- CED is downstream evidence licensing;
- carrier feasibility, required state, evidence identification, and target reportability are distinct gates;
- one fixed-size capability expansion can add only one viable world while forcing arbitrarily many additional bits of state/monitoring resolution in the constructed family;
- a coarse target can remain reportable after full-state identification is lost;
- ecological rules may be interpreted as effective laws on adequate quotients.

### Do not claim

- one intrinsic ecological state partition supplied by nature;
- historical firstness for trajectory-sensitive state, predictive state, state/action abstraction, viability, observability, partition refinement, or purpose-relative adequacy;
- that the three structural obstruction families are exhaustive;
- that every action expansion increases information requirements;
- that finite partition bits equal financial or field-sampling costs;
- a proved general stochastic/continuous trajectory theorem;
- empirical validation as a prerequisite for the finite theorem.

## 8. Remaining work

### Repository-controlled

No unresolved scientific theorem, novelty-boundary, or manuscript-structure task is currently known.

### Author-controlled / exact-upload tasks

1. finalize author list and order;
2. complete affiliations, corresponding-author email, and ORCID(s) if used;
3. finalize acknowledgements, funding, and competing-interests statements on the separate title page;
4. complete the human source/claim/mathematics/prose responsibility review;
5. approve the final LLM-use disclosure against the current Springer policy;
6. construct the exact blinded review manuscript, removing development-only placeholders and moving identifying/declaration material to the title page as required;
7. visually inspect the blinded manuscript and any supplements for identifying information;
8. run the verifier/reproducibility suite on the exact upload-candidate commit;
9. submit only after all co-authors, if any, approve the final manuscript.

## Stop rule

Do not add another audit, derived-concept family, empirical benchmark, or theorem family to the present submission line. A future mathematical sequel should start from a genuinely new question, such as structural assumptions that restore an upper bound on capability–resolution divergence.