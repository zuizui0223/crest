# CREST manuscript and submission surfaces

## Current flagship

**Ecological State at a Temporal Cut: Sparse Semantic Access**  
Target: **The American Naturalist — Major Article**  
Canonical manuscript: `crest_flagship_amnat_v0.7_semantic_access.md`.  
AmNat Supplementary Information I: `CREST_AmNat_supplementary_information.md`.  
AmNat Supplementary Information II: `CREST_AmNat_supplementary_prerequisite_support.md`.

CREST treats the present as a zero-duration observational cut and defines ecological state as the least quotient induced on that cut by retrospective, transverse latent-present, and prospective distinguishability constraints.

The three companion responsibilities remain non-circular and non-identical:

- **MLTR / retrospective H:** primitive replacement histories first, complete carried-map equivalence second; left-of-cut structure.
- **MRM / transverse latent present Theta:** primitive candidate laws first, complete response-type equivalence second; hidden response structure within the observation fiber, without claiming full ontic mechanism identity.
- **CCOC / prospective F:** controlled law plus exogenously declared right-of-cut query grammar, response quotient afterward.

## v0.7 scientific center

The flagship distinguishes two structures controlling prospective refinement of the cut-state:

1. the minimum prerequisite set of retained interfaces needed before a future target is well formed; and
2. the semantic access relation describing on which retained history-mode x response-type combinations that target is actually addressable.

It also distinguishes two information questions that earlier drafts conflated.

### Structural prerequisite interaction: Shannon order

For prospective query `f` with prerequisite set `R_f`, decoder depth `m_f`, and accessible occupancy mass `P(A_f)`, the Shannon prospective game has

\[
d_1(T)=\sum_{f:R_f\cup\{F\}=T}m_fP(A_f).
\]

Thus prerequisite topology determines **where Shannon prospective information is supported**, while semantic accessibility and occupancy determine **how much** appears there. Supplement II proves this support fidelity for arbitrary query families in the finite model. Non-Shannon Rényi orders can generate additional distribution-sensitive interaction, and overlapping access can create exact non-Shannon cancellation; zero non-Shannon interaction therefore does not certify prerequisite fidelity.

For the canonical witness, `N=4`, one of four uniformly occupied semantic pairs is accessible, and `m=10`, so

\[
d_1(\{H,\Theta,F\})=10/4=2.5\text{ bits}.
\]

This **2.5-bit Shannon dividend is the canonical structural interaction value**.

### Support-space contraction: Hartley endpoint

If `N` semantic pairs exist, `k` are addressable, and an addressable future query distinguishes `2^m` exterior signatures, then

\[
|Q_{H\Theta F}|=(N-k)+k2^m.
\]

At the Hartley (`q=0`) support-count endpoint,

\[
d^{(0)}_{H\Theta F}=\log_2\frac{(N-k)+k2^m}{N}
\]

and asymptotically

\[
d^{(0)}_{H\Theta F}=m-\log_2(N/k)+o(1).
\]

This quantity measures **distinguishable state-space support**, not faithful recovery of prerequisite topology. The canonical witness has `N=4`, `k=1`; at `m=10` the grand coalition has 1027 classes / 10.00422 Hartley bits and the support-count dividend is 8.00422 bits. The earlier 4096-class / 12-bit / 10-bit-three-way result is retained only as the complete-access boundary `k=N=4`.

## AmNat Supplement I: occupancy-aware access spectrum

Supplement I generalizes the support-count result to nonuniform semantic-cell occupancies `p_i`. It does **not** claim Rényi entropy, Shannon entropy, Hill numbers, or ordinary partition-refinement information theory as new mathematics. The new object is CREST's selective semantic-access refinement, in which only licensed cells receive prospective splitting.

For Rényi order `q`, the exact access gain is

\[
G_q=
\frac{1}{1-q}\log_2
\frac{\sum_{i\notin A}p_i^q+2^{m(1-q)}\sum_{i\in A}p_i^q}
{\sum_i p_i^q},
\]

with the Shannon limit

\[
G_1=mP_A.
\]

The Hartley support-count formula is recovered exactly at `q=0`. For nontrivial sparse access, Supplement I proves the large-decoder slope law

\[
\lim_{m\to\infty}G_q/m=
\begin{cases}
1,&q<1,\\
P_A,&q=1,\\
0,&q>1,
\end{cases}
\]

plus sharp fixed-`k` placement extrema and a heterogeneous local-capacity extension `G_1 = sum_i p_i log2 M_i`.

## AmNat Supplement II: prerequisite support and Rényi-order leakage

Supplement II asks when an interaction coefficient can be read literally as prerequisite structure. At Shannon order, the prospective game is a weighted sum of unanimity games and its Möbius support coincides with declared prerequisite hyperedges. For disjoint semantic access, every finite `q != 1` produces strict undeclared joint interaction. With overlapping access, the exact four-region balance

\[
\mathcal B_q=W_qZ_q-X_qY_q
\]

controls the sign, and non-Shannon leakage can vanish on the balance surface `W_q Z_q = X_q Y_q`. Accordingly, **Shannon is the generally support-faithful structural diagnostic; non-Shannon zero interaction can also be distributional cancellation**.

## Realizability no-go

The paper keeps three strict boundaries before the positive construction:

1. fixed precomputed partitions on a one-class baseline cannot generate positive interaction by common refinement alone;
2. a zero-debt post-cut audit preserving immutable MLTR history cannot later be activated by rewriting that history;
3. candidate-safe zero debt under one fixed MRM grammar implies a singleton response type.

These results prevent older abstract closure cascades from being overinterpreted as literal companion models.

## Supporting finite mathematics and novelty boundary

The finite partition/quotient/transport spine is **structural support, not a claim of new partition theory**. Common refinement, its unique-coarsest characterization, representation-equivalence of signature families, and the deterministic transport descent condition are treated as elementary finite-structure guarantees that make the cut-state construction well defined, representation safe, and composable when the declared evolution respects the quotient.

The flagship therefore does **not** claim mathematical novelty for Möbius/Harsanyi inversion, unanimity games, generic quotient-state abstraction, common-refinement lattice facts, finite counting once an access relation is fixed, or Rényi/Hill entropy theory itself.

The **paper-level theoretical contribution** is the ecological temporal-cut state construction plus the separation of prerequisite topology from semantic accessibility. Its information-theoretic statement is explicitly two-layered: **Shannon order diagnoses structural prerequisite support; the Hartley endpoint quantifies distinguishable support-space contraction under sparse access**. The sparse-access degradation `log2(N/k)` remains a quantitative result, but no longer carries the structural-support interpretation by itself.

The phrase `zero-duration cut` remains a finite idealization. The manuscript does not claim an epsilon-to-zero continuous-time limit theorem, continuous-time germ theorem, stochastic generality, approximate-state theorem, or infinite-state extension.

## Executable shallow-lake audit

The shallow-lake worked case is an ecological interpretation with an executable finite model, not empirical validation. Four worlds behind one coarse visible status cross two retrospective modes with two latent-response types. Target factorization and counterfactual substitution return:

- current status: `R = empty`;
- legacy-sensitive recovery: `R = {H}`;
- mechanism-specific intervention: `R = {Theta}`;
- composed restoration diagnostic: `R = {H,Theta}`.

The exact parity-style two-output map is a minimal formal witness of joint dependence rather than a biological law asserted by the restoration literature.

## AmNat submission metadata

Machine-readable metadata: `amnat_submission_metadata.json`  
Current pinned text word count: **5265**  
Short title: **Sparse Semantic Access**.

Generate the anonymous title-page metadata with:

```bash
python scripts/build_amnat_title_page.py
```

Default output: `dist/amnat_anonymous_title_page.md`.

The reported text word count is computed reproducibly from Introduction through Conclusion without subtracting display/inline mathematics or table rows. Literature Cited is outside the count. Supplementary Information is tracked separately and does not alter the pinned main-text count.

## Current submission-readiness checklist

Use **`AMNAT_SUBMISSION_READINESS.md`** as the active blocker/readiness surface for the flagship. It separates repository-controlled checks from author-controlled fields and the literal-upload PDF gate.

The older `SUBMISSION_BLOCKERS_2026-08-24.md` is historical and belongs to the retained Biology & Philosophy submission surface; it is not the active AmNat checklist.

## Anonymous review-code package

Generate the deterministic whitelist-only review archive with:

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output: `dist/anonymous_review_code.zip`.

The v0.7 archive contains the minimal code needed for temporal-cut representation, strict companion-realizability checks, companion semantic quotients, sparse semantic access, semantic trace-equivalence quotient calculation, exact `N-k+k*2^m` benchmark checks, the Rényi/Hill semantic-access generalization, the Shannon prerequisite-support theorem, the non-Shannon leakage / overlap-balance laws, and the executable shallow-lake prerequisite/counterfactual-substitution audit.

## Remaining author-controlled fields

Author-controlled items are tracked in `AMNAT_SUBMISSION_READINESS.md`: final author metadata, affiliations/contact details, ORCIDs if used, acknowledgements, funding, conflicts, author contributions if requested, final Data and Code Accessibility wording, final generative-AI disclosure, and confirmation of author approval / no simultaneous consideration.

The final review PDF must be checked visually for double spacing, line numbering, page numbering, anonymity, equation rendering, and embedded math fonts. A cover letter is not treated as a blocker; necessary editor-facing notes belong in the submission system's author-comments field.

## Retained predecessor and historical surfaces

Noncanonical AmNat predecessors remain for provenance: `crest_flagship_amnat_v0.6_addressability.md`, `crest_flagship_amnat_v0.5_compositional.md`, `crest_flagship_amnat_v0.4_positioned.md`, `v0.3`, and `v0.2`.

The earlier Biology & Philosophy bundle is retained separately: `crest_biology_philosophy_blinded_submission.md`, `CREST_supplementary_information.md`, `biology_philosophy_title_page_TEMPLATE.md`, `SUBMISSION_BLOCKERS_2026-08-24.md`, and `crest_canonical_scope_2026-08-24.md`. The legacy verifier remains separate from the AmNat verifier.

## Current scientific spine

```text
raw ecological possibilities Omega
-> zero-duration observational cut O_t
-> visible-cut fibers O_t^{-1}(y)
-> retrospective / transverse / prospective pre-state structures
-> strict realizability no-go
-> prerequisite topology + semantic access relation A_f
-> Shannon structural prerequisite-support game
-> Hartley support-count contraction under sparse access
-> occupancy-aware Rényi/Hill access spectrum and leakage boundaries
-> least induced cut-state quotient Q_S
-> ecological interpretation / evidence downstream
```

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/build_amnat_title_page.py
```

The test suite verifies the temporal-cut surface, definition firewall, strict realizability no-go, semantic-access quotient, Rényi access spectrum and extremal laws, Shannon prerequisite-support / leakage boundaries, shallow-lake prerequisite audit, AmNat manuscript compliance, submission metadata, generated anonymous title page, and anonymous review bundle.
