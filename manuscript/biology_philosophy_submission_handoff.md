# Biology & Philosophy submission handoff — CREST philosophy paper

> **Target:** Biology & Philosophy — Original Research  
> **Repository status:** scientific architecture, manuscript structure, and automated controls are synchronized to the single-question CREST spine. Actual submission remains blocked only by author-controlled metadata, final human responsibility review, final blinded-file preparation, and live-policy recheck.

## A. One-question manuscript

### Title

**What Counts as the Same Ecological State? A Contract-Relative Account of State-Representation Adequacy**

### Central philosophical question

> **When are two ecological configurations scientifically allowed to count as the same state?**

CREST treats ecological sameness as a declared scientific commitment rather than one intrinsic partition of nature.

Four currently formalized obligations constrain one sameness relation:

1. **future sufficiency / CCOC** — can a newly relevant future expose a difference the state erased?
2. **semantic coherence / MLTR** — does an inherited ecological category retain its operational meaning after structural change?
3. **mechanism robustness / MRM** — do retained latent response mechanisms agree on the response demanded from the state?
4. **evidential licensing / CED** — has the observation system actually resolved the distinction the state requires?

These are constraints on one state, not four rival definitions.

## B. Mathematical answer — three gates

The manuscript now presents the theorem dependency in the following order.

### Gate A — carrier

The four obligations must first admit a common ecological world set. J3/J6 characterize the maximal universal/controlled finite carriers. An empty or coverage-incomplete carrier is a contract-level failure; it cannot be repaired merely by splitting a partition more finely.

### Gate B — least-information joint state

For a declared admissible finite carrier \(U\), baseline partition \(B\), and four refinement closures,

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

is the unique coarsest / least-information joint partition satisfying all four obligations. The CREST state of world/configuration \(u\) is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

This is conditional joint minimality, not a universal ontology.

### Gate C — evidence

For reliability-qualified evidence partition \(E_D\),

\[
\text{full deterministic state report exists}
\iff
J\preceq E_D.
\]

A requested target may remain deterministic even when the full state is unresolved. Hence CREST keeps distinct:

\[
\text{required state}
\neq
\text{identified state}
\neq
\text{target report}.
\]

## C. Main cross-gate ecological result

The manuscript no longer treats the ecological-state-adequacy frontier as the mathematical headline. It is retained only as descriptive bookkeeping for the three gate outputs.

The stronger result is the strict action-expansion witness:

\[
|K^*|\uparrow,
\qquad
|J|\uparrow,
\qquad
\text{full-state identification: yes}\to\text{no},
\qquad
\text{target reporting: yes}\to\text{yes}.
\]

Thus a new management capability can enlarge the domain that becomes viable while forcing a finer ecological state that unchanged monitoring no longer identifies.

The finite minimum evidence refinement is

\[
E\vee J,
\]

with monitoring-resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

A channel-factorization example \(W(z)=F(z)R(z)\) shows that this deficit can be **structural**: more replication of the same net output can fail to distinguish latent causal worlds, while a new channel-resolved measurement can break the symmetry.

## D. Ecology-facing interpretation

The manuscript now explicitly bridges the finite mathematics to ecology.

A declared latent ecological world may contain relevant history, current population/community configuration, latent mechanism structure, and counterfactual responses to future actions. This motivates a **temporally thicker interpretation** of ecological state:

> a state can be understood as a least-information scientific compression that may retain past- or future-relevant distinctions when the declared scientific work makes them consequential.

This is explicitly presented as an interpretation of the current finite latent-world formalism, **not yet a general theorem for continuous or stochastic trajectories**.

Current future-theorem candidates remain outside the proved manuscript claims:

- snapshot sufficiency;
- observation-symmetry obstruction;
- stochastic/trajectory extension;
- representational resilience.

## E. Current automated manuscript status

Verifier:

```bash
python scripts/verify_crest_philosophy_submission.py --write-report
```

Current verified state after the single-question manuscript refactor:

- abstract: **234 words**;
- keywords: **6**;
- repository-defined visible words before References: **5,942**;
- development band 5,500–7,500: **PASS**;
- hard cap `<=10,000`: **PASS**;
- potential double-blind identifiers before References: **0**;
- excluded unpublished/preprint audit references in submission bibliography: **0**;
- J1 joint-partition formula present: **PASS**;
- explicit state block `[u]_J` present: **PASS**;
- conditional unique-coarseness wording present: **PASS**;
- explicit Gate A carrier structure present: **PASS**;
- evidence gate `J \preceq E_D` present: **PASS**;
- global/intrinsic-state overclaim rejected: **PASS**;
- obsolete pre-J1 phrases: **0**;
- automated blockers: **0**.

Theorem/obstruction tests pass on Python **3.10, 3.11, and 3.12**. The Python 3.12 job also passes the submission verifier and repository hygiene/deterministic-output checks.

## F. Claim boundary

### Safe manuscript claims

- four declared obligations constrain one proposed ecological state equivalence;
- on one admissible finite common carrier, J1 yields the unique coarsest joint state satisfying them;
- carrier existence, state construction, and evidence identification are distinct gates;
- pairwise audit commutation is not required and one-pass independent minimization can fail;
- a target can remain reportable when the full state is unresolved;
- one added management action can, in a finite witness, expand viability while increasing required state resolution and defeating unchanged full-state monitoring;
- the minimum evidence refinement identifying \(J\) while preserving existing evidence distinctions is \(E\vee J\);
- monitoring deficit can be structural rather than merely a shortage of replication.

### Do not claim

- a nature-given ecological partition independent of contract;
- exhaustiveness of the four obligations;
- historical firstness for generic partition refinement, fixed points, viability kernels, partial observability, state abstraction, model repair, or purpose-relative adequacy;
- that every added management action increases information requirements;
- that finite partition bits are monetary/logistical sampling cost;
- that the temporally thick interpretation is already a proved trajectory theorem;
- that current Campanula or other empirical observations identify the abstract channel states used in the structural-monitoring example.

## G. Separate title page and declarations — author input required

Keep outside the blinded review manuscript:

- author name(s): **AUTHOR INPUT REQUIRED**;
- affiliation(s): **AUTHOR INPUT REQUIRED**;
- corresponding author and email: **AUTHOR INPUT REQUIRED**;
- ORCID(s), if used: **AUTHOR INPUT REQUIRED**;
- acknowledgements: **AUTHOR INPUT REQUIRED**;
- funding statement: **AUTHOR INPUT REQUIRED**;
- competing-interests statement: **AUTHOR INPUT REQUIRED**.

Do not infer a no-conflict or no-funding statement from repository history.

## H. Generative-AI disclosure — final human approval required

The manuscript contains a disclosure placeholder. Before submission, the human author(s) must review the cited sources, mathematical claims, interpretations, and final prose and be able to take responsibility for the complete manuscript. Only then should the AI-use disclosure be finalized against the live publisher policy.

## I. Double-blind and upload finalization

Repository scanning is clean, but the exact upload candidate still needs a human visual/read-through. Before upload:

1. create the separate title page;
2. remove development-only submission-control material/placeholders from the blinded review file as appropriate;
3. complete final source/claim/interpretation/prose review;
4. approve declarations and AI-use disclosure;
5. recheck the live Biology & Philosophy / Springer Nature instructions;
6. run one immutable verifier/reproducibility replay on the exact upload candidate SHA.

## Current verdict

**Repository-controlled scientific work is synchronized. CREST now reads as one philosophical question, four constraints on ecological sameness, a three-gate mathematical answer, one strict cross-gate ecological result, and an ecology-facing interpretation. Remaining blockers are author-controlled submission tasks rather than unresolved repository science.**
