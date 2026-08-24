# Biology & Philosophy submission handoff — CREST

> **Target:** *Biology & Philosophy*  
> **Canonical review manuscript:** `crest_philosophy_biology_philosophy.md`  
> **Repository status:** finite mathematics, world→state→law philosophical synthesis, novelty firewalls, manuscript, and automated submission controls are synchronized. Remaining blockers are author-controlled metadata/final responsibility review and construction of the exact blinded upload candidate.

## 1. Current manuscript identity

### Title

**What Counts as the Same Ecological State? A Contract-Relative Theory of Temporally Extended Ecological States**

### Higher-level question

> **How can ecological states and ecological laws be well-defined in a temporally extended, partially observed, self-modifying adaptive world?**

### Operational question

> **What counts as the same ecological state?**

CREST's answer is:

> **An ecological state is a scientifically licensed quotient/compression of temporally extended ecological worlds, and a coarse ecological law is an effective law on that quotient.**

The manuscript does not claim that complete world-histories imply a block-universe ontology or physical determinism, that ecosystems are generically mathematically chaotic, or that evolution maximizes one global fitness function.

## 2. Logical hierarchy

```text
possible ecological world-histories Ω
    ↓
self-modifying eco-evolutionary response structure
    ↓
observation / intervention context O_V
    ↓
snapshot-sufficiency question
    ↓
CCOC / MLTR / MRM structural obstructions
    ↓
Gate A — admissible finite common carrier
    ↓
Gate B — least-information adequate state J
    ↓
Gate C — evidence licensing / CED
    ↓
full-state / target-only / set-valued report
    ↓
quotient-level effective law and representational stability
```

CED is downstream evidence licensing, not a fourth co-level ontic obstruction.

## 3. World, state, observation, and law

A possible ecological world can be represented as a complete history

\[
\omega=(x_s)_{s\in\mathbb T},
\]

or relative to a present time as

\[
\omega=(h_t,x_t,\mathcal F_t).
\]

For stochastic systems, \(\mathcal F_t\) may be a conditional distribution over future paths. This is a mathematical representation device; CREST is neutral about eternalism, block-universe metaphysics, and physical determinism.

Scientific access is

\[
O_V:\Omega\to Y_V,
\]

while the state quotient is

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V}.
\]

The state is

\[
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}
=q_{\mathcal C,V}(\omega).
\]

For a required world-level response

\[
R_{\mathcal C}:\Omega\to Z_{\mathcal C},
\]

a coarse law is well-defined exactly when there exists

\[
L_{\mathcal C,V}:Q_{\mathcal C,V}\to Z_{\mathcal C}
\]

such that

\[
R_{\mathcal C}=L_{\mathcal C,V}\circ q_{\mathcal C,V}.
\]

This supports **domain-relative law validity**, not observer-relative truth: the same underlying world can support different valid coarse laws when different scientifically adequate quotients retain different distinctions.

## 4. Ecological adaptive-system interpretation

The manuscript now summarizes eco-evolutionary change as

\[
\boxed{
\text{stochastic variation}
+\text{ context-dependent selective bias}
+\text{ endogenous change of the selective environment}.
}
\]

Natural selection can create local directional bias in differential reproduction, but fitness rankings can change with environment, density, frequency, interacting species, and genetic background. Drift, mutation, migration, and stochasticity remain possible. CREST therefore does not posit one universal evolutionary destination.

Three existing `microdonta` results supply ecology-grounded hidden-structure illustrations without becoming CREST proof premises:

- **basin/path hysteresis:** the same restored external environment can have different long-run states depending on history/basin position;
- **latent causal degeneracy:** multiple mechanism-switch configurations can remain compatible with the same observed pattern;
- **structural channel non-identifiability:** if \(W=FE\), observations depending only on \(W\) cannot identify whether the change occurred in \(F\) or \(E\).

These examples show why a scientifically relevant state distinction need not be directly visible under the current observation map.

## 5. Finite state answer

On a declared admissible finite common carrier \(U\), baseline partition \(B\), and implemented refinement closures,

\[
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique coarsest / least-information common fixed partition under J1's assumptions. The finite CREST state is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

J1 is the **existence/minimality backbone**. Generic closure/fixed-point machinery is classical and is not the principal novelty claim.

For reliability-qualified evidence partition \(E_D\),

\[
\text{full deterministic state report exists}
\iff
J\preceq E_D.
\]

A target can remain reportable even when the full state is unresolved, so CREST keeps distinct

\[
\text{required state}\neq\text{identified state}\neq\text{reportable target}.
\]

## 6. Quantitative mathematical headline

The theorem-level headline remains the connected **capability–resolution divergence** family.

For every integer \(m\ge1\), one newly admitted action `probe`, with a bounded output alphabet, yields in one connected finite response graph

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

Hence no universal finite bound depending only on carrier-size gain can upper-bound representational burden.

The broader philosophical consequence is a failure of **representational stability**: what the ecosystem is scientifically required to be distinguished as can change before the ecosystem changes physically. The law-level consequence is that a quotient-level rule can lose portability when its old state fibers are no longer adequate.

## 7. Current verified repository state

Automated state for the world–state–law integrated manuscript:

- abstract: **240 words**;
- keywords: **6**;
- repository-defined visible words before References: **8,412**;
- repository development target 5,500–7,500: **not met by 912 words; non-blocking**;
- journal hard cap `<=10,000`: **PASS**;
- potential double-blind identifier hits before References: **0**;
- excluded unpublished/preprint audit references in the submission bibliography: **0**;
- theorem/regression suite: **143 tests PASS**;
- Python **3.10 / 3.11 / 3.12** theorem/regression tests: **PASS**;
- Python 3.12 submission verifier: **PASS**;
- automated blockers: **0**.

The restoration/conservation projection is integrated with primary-source and theorem firewalls. The expected deterministic report update is synchronized to the generated values.

Canonical generated record: `../artifacts/crest_philosophy_submission_report.json`.

## 8. Claim firewall

### Safe

- a complete ecological trajectory can be used as a mathematical possible-world object without metaphysical commitment;
- ecological state is a contract-relative quotient of possible worlds;
- CCOC, MLTR, and MRM are three structural reasons a present merge can fail;
- CED is downstream evidence licensing;
- hidden basin position or latent mechanism can be state-relevant when it changes a required response;
- changing observation/intervention context changes scientific access, not underlying truth by description alone;
- coarse ecological laws are effective laws on adequate quotients, with validity tied to their quotient domain;
- natural selection gives context-dependent local bias, not one global fitness arrow;
- one fixed-size capability expansion can add only one viable world while forcing arbitrarily many additional bits of state/monitoring resolution in the constructed family.

### Do not claim

- relativity proves that the actual future is fixed;
- block-universe/eternalist metaphysics is required by CREST;
- quantum physics is simply all random or simply deterministic independent of model/interpretation;
- future events literally cause present states;
- ecosystems are generically mathematically chaotic;
- evolution maximizes one global fitness function;
- changing scientific viewpoint changes underlying ecological truth;
- every latent variable deserves state status;
- the three structural obstruction families are exhaustive;
- empirical validation is required for the finite theorem;
- `microdonta` is the proof foundation of CREST.

## 9. Stability interpretation

Keep separate:

1. **dynamical stability** — persistence/recovery/basin behavior of ecological trajectories;
2. **evolutionary stability** — invasion/stability under a declared evolutionary model;
3. **representational stability** — persistence of an adequate quotient when scientific responsibility changes.

**Law portability** is a downstream quotient-level question, not a fourth theorem family: does the same effective rule remain well-defined when the required quotient changes?

## 10. Remaining work

### Repository-controlled

No new theorem is required by this philosophical integration. After final green CI and merge, repository-controlled development returns to closed status.

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

Do not add another audit, derived-concept family, empirical benchmark, or theorem family to the present submission line. The world–state–law synthesis is an interpretive integration of the existing CREST spine, not a license for theorem proliferation.
