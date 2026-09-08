# CREST manuscript and submission surfaces

## Current flagship

The current CREST flagship is:

**Ecological State at a Temporal Cut: Interface-Dependent Interaction**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.6_addressability.md`.

The paper defines ecological state as the least information that must survive an observational temporal cut under a declared scientific contract.

The three motivating companion responsibilities remain non-circular and non-identical:

- **MLTR / history H:** primitive replacement histories first, carried-map equivalence second;
- **MRM / latent response Theta:** primitive candidate laws first, response-type equivalence second;
- **CCOC / future F:** controlled law plus exogenously declared legal query grammar, response quotient afterward.

## Flagship theorem

v0.6 no longer assigns coalition values directly. It uses an explicit finite carrier, generated legal grammar, trace semantics, and the induced quotient

\[
Q_S=\Omega/\!\sim_S.
\]

A future decoder has a minimal prerequisite set

\[
R\subseteq\{H,\Theta\}.
\]

The decoder for an exterior coordinate is legal exactly when

\[
F\in S
\quad\text{and}\quad
R\subseteq S.
\]

The induced quotient then satisfies

\[
|Q_S|
=
2^{\mathbf 1_{H\in S}+\mathbf 1_{\Theta\in S}+m\mathbf 1_{F\in S,\ R\subseteq S}}.
\]

This formula is a theorem about generated traces, not the definition used by the implementation.

The characterization is:

- `R = empty`: the m-bit exterior burden is an F main effect;
- `R = {H}`: it is pure H x F pairwise interaction;
- `R = {Theta}`: it is pure Theta x F pairwise interaction;
- `R = {H,Theta}`: it is pure H x Theta x F interaction.

Thus the **minimal interface prerequisite set determines interaction order**.

The earlier v0.5 result `m(H,Theta,F)=m` is retained only as the `R={H,Theta}` corollary. It is no longer presented as an unconditional property of the three-axis framework.

## Numerical illustration

For `m=10` and `R={H,Theta}`:

- history + mechanism: 4 classes / 2 bits;
- full grammar: 4096 classes / 12 bits;
- state-count amplification: 1024x;
- genuine three-way term: 10 bits.

But this is explicitly conditional. If F can decode without both interfaces, the same exterior information moves to a lower-order term and the three-way dividend becomes zero.

## Realizability no-go remains a main result

The paper keeps three strict boundaries before the positive theorem:

1. fixed precomputed partitions on a one-class baseline cannot generate positive interaction by common refinement alone;
2. a zero-debt post-cut audit preserving immutable MLTR history cannot later be activated by that history partition;
3. candidate-safe zero debt under one fixed MRM grammar implies a singleton response type.

These results prevent the older abstract closure cascades from being overinterpreted as literal companion models.

## Retained predecessor manuscripts

- `crest_flagship_amnat_v0.5_compositional.md` — pre-characterization draft whose coalition-value function was too directly assigned;
- `crest_flagship_amnat_v0.4_positioned.md` — temporal-cut manuscript before strict companion realizability;
- `crest_flagship_amnat_v0.3_temporal_cut.md` — earlier temporal-cut theorem draft;
- `crest_flagship_amnat_v0.2.md` — earlier generic-Delta-centered draft.

All remain for provenance and are no longer canonical.

## Retained Biology & Philosophy bundle

The previous Biology & Philosophy surface remains intact for provenance and comparison:

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witnesses, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.

The legacy philosophy verifier intentionally continues to target `crest_biology_philosophy_blinded_submission.md`; it is not the verifier for the Am Nat flagship.

## Current scientific spine

```text
possible ecological worlds Omega
-> observational temporal cut O_t
-> primitive MLTR / MRM / CCOC objects
-> strict realizability no-go
-> explicit grammar generation
-> legal traces
-> induced quotient Q_S
-> decoder prerequisite set R
-> interaction-order characterization
-> evidence licensing downstream
```

## Claim firewall

The flagship does **not** claim:

- that history, latent response, and future are independent ontic coordinates;
- that they exhaust every ecological state responsibility;
- that all legal future grammars require both companion interfaces;
- that pure three-way interaction is automatic;
- that decoder prerequisites can be inferred from state accounting alone;
- statistical confounding;
- continuous-time, stochastic, infinite-state, or approximate generality.

The scientific application must justify its decoder/query architecture. CREST gives the representational consequence of that architecture.

## Anonymous review-code package

Generate the deterministic whitelist-only review archive with

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

The v0.6 archive contains the minimal code needed for:

- temporal-cut representation;
- strict companion-realizability checks;
- explicit MLTR/MRM primitive objects;
- compositional grammar generation;
- trace-equivalence quotient calculation;
- counterfactual decoder rules that move the same exterior burden among main, pairwise, and three-way terms.

The canonical benchmark is `artifacts/crest_explicit_grammar_benchmarks_2026-09-08.json`.

## Submission blockers that remain author-controlled

1. **Anonymous code upload location.** The generator is complete; the review-safe upload surface depends on the journal workflow.
2. **Data and Code Accessibility Statement.** Insert the final anonymous/archive identifier in `amnat_submission_declarations_TEMPLATE.md`.
3. **Generative-AI disclosure.** Confirm actual uses and human verification.
4. **Title page / author metadata.** Names, affiliations, e-mails, ORCIDs, acknowledgments, funding, contributions, and conflicts stay outside the blinded manuscript.
5. **PDF preparation.** Final review PDF needs journal-required spacing, line/page numbering, and embedded math fonts.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/verify_crest_philosophy_submission.py --write-report
```

The general pytest suite verifies the temporal-cut state surface, definition firewall, strict realizability no-go, explicit grammar quotient theorem, AmNat manuscript compliance, and anonymous review bundle.
