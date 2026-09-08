# CREST manuscript and submission surfaces

## Current flagship

The current CREST flagship is:

**Ecological State at a Temporal Cut: Compositional Interaction Across Time**

Target: **The American Naturalist — Major Article**.

Canonical manuscript: `crest_flagship_amnat_v0.5_compositional.md`.

The paper defines ecological state as the least information that must survive an observational temporal cut under a declared composed scientific contract.

The three pre-state companion responsibilities are deliberately non-circular and non-identical:

- **MLTR / history \(H\):** a fixed root semantic law plus immutable declared replacement histories; retained history is a relevance quotient of carried terminal maps.
- **MRM / latent response \(\Theta\):** primitive candidate laws first, response-type equivalence second.
- **CCOC / future \(F\):** a fixed controlled law plus an exogenously declared right-of-cut future grammar; response equivalence is induced by the legal queries.

The final state quotient is downstream of these objects.

## Flagship theorem

The literal conditioned cross-contract family has coalition value

\[
\boxed{
v_m(S)=
\mathbf 1_{H\in S}
+
\mathbf 1_{\Theta\in S}
+
m\,\mathbf 1_{\{H,\Theta,F\}\subseteq S}.
}
\]

Hence

\[
v(H)=1,
\quad v(\Theta)=1,
\quad v(F)=0,
\]

\[
v(H\Theta)=2,
\quad v(HF)=1,
\quad v(\Theta F)=1,
\]

and

\[
v(H\Theta F)=m+2.
\]

All pairwise Möbius dividends are zero and

\[
\boxed{m(H,\Theta,F)=m.}
\]

Therefore the genuine three-way interaction is unbounded and occupies

\[
\frac{m}{m+2}\to1
\]

of the full joint state information.

At \(m=10\): history + mechanism require 4 classes / 2 bits, while the jointly open contract requires 4096 classes / 12 bits. The amplification is **1024×**; **10 bits are genuine three-way interaction**, equal to **83.33% of the full state and 100% of interaction debt**.

## Why v0.5 replaces v0.4

v0.4 established the temporal-cut framing and the exact fixed-closure extrema, but a subsequent companion-definition audit showed that those activation cascades should not be read literally as simultaneous canonical MLTR, MRM, and CCOC models.

v0.5 therefore adds two layers before making the headline claim:

1. **strict realizability no-go:** immutable MLTR history and fixed-grammar MRM rule out the naive zero-debt activation interpretation;
2. **positive conditioned bridge:** future grammar conditions which immutable histories and primitive candidate laws remain state-relevant, while CCOC's jointly open composition supplies an \(m\)-bit exterior coordinate only when all three responsibilities are active.

The old results remain exact supporting mathematics:

- marked-cycle \(\Delta=\log_2 n-1\);
- fixed-closure three-way \(b-\log_2 3\), including the 8.415-bit \(b=10\) endpoint.

They are now labeled **abstract fixed-closure extrema**, not the literal companion-derived headline.

## Literal pairwise frontiers

For an \(m\)-bit MLTR carried-map family, \(k\) declared future queries induce exactly

\[
2^k
\]

relevant history classes and \(k\) bits.

For the matching MRM family, \(k\) declared binary probes induce exactly

\[
2^k
\]

response types and \(k\) bits.

At \(m=10\), both run from 1 class / 0 bits to 1024 classes / 10 bits without changing the raw history or primitive mechanism identity.

## Retained predecessor manuscripts

- `crest_flagship_amnat_v0.4_positioned.md` — temporal-cut manuscript before the strict companion-realizability audit.
- `crest_flagship_amnat_v0.3_temporal_cut.md` — earlier theorem-correct temporal-cut draft.
- `crest_flagship_amnat_v0.2.md` — earlier generic-Delta-centered draft.

All are retained for provenance and are no longer canonical.

## Retained Biology & Philosophy bundle

The previous Biology & Philosophy surface remains intact for provenance and comparison:

1. `crest_biology_philosophy_blinded_submission.md` — retained blinded manuscript.
2. `CREST_supplementary_information.md` — formal definitions, proof details, finite witnesses, worked-case formalization, and reproducibility instructions.
3. `biology_philosophy_title_page_TEMPLATE.md` — separate identifying title page and declarations.
4. `SUBMISSION_BLOCKERS_2026-08-24.md` — author-controlled upload blockers.
5. `crest_canonical_scope_2026-08-24.md` — historical manuscript-scope contract.
6. `../figures/crest_capacity_knowledge_paradox.svg` — retained figure source.

The legacy philosophy verifier intentionally still targets `crest_biology_philosophy_blinded_submission.md`; it is not the Am Nat verifier.

## Current scientific spine

```text
possible ecological worlds Omega
-> observational temporal cut O_t
-> primitive MLTR / MRM / CCOC objects
-> non-circular responsibility equivalences
-> strict realizability audit
-> future-conditioned history + grammar-conditioned mechanism bridges
-> jointly open compositional coalition game
-> pure three-way interaction m bits
-> evidence licensing downstream
```

## Claim firewall

The flagship does **not** claim:

- that history, latent response, and future are independent ontic coordinates;
- that they exhaust every legitimate ecological state responsibility;
- that the old fixed-closure cascades are literal companion realizations;
- statistical confounding;
- a continuous-time infinitesimal-germ theorem;
- stochastic, infinite-state, or approximate generality;
- empirical identification of histories or candidate mechanisms.

The present remains a zero-width observational cut in the finite representation, not a metaphysical claim about physical instants.

## Anonymous review-code package

Generate the deterministic whitelist-only review archive with

```bash
python scripts/build_amnat_anonymous_bundle.py
```

Default output:

`dist/anonymous_review_code.zip`

The v0.5 archive contains the minimal finite code needed for:

- temporal-cut representation;
- strict companion-realizability checks;
- conditioned MLTR/MRM pairwise frontiers;
- the literal compositional three-way theorem;
- the canonical \(m=10\) 4→4096 / 12-bit numeric benchmark.

It excludes `.git` history, provenance notes, empirical application material, public repository URLs, and submission metadata. Regression tests check whitelist-only contents, identity scrubbing, deterministic ZIP bytes, SHA-256 manifest integrity, and focused theorem execution after extraction.

The final anonymous upload location or archive identifier remains author-controlled.

## Submission blockers that remain author-controlled

1. **Anonymous code upload location.** The generator is complete; the review-safe upload surface still depends on the journal workflow.
2. **Data and Code Accessibility Statement.** Insert the final anonymous/archive identifier in `amnat_submission_declarations_TEMPLATE.md`.
3. **Generative-AI disclosure.** Confirm the actual uses and human verification described in the template.
4. **Title page / author metadata.** Names, affiliations, e-mails, ORCIDs, acknowledgments, funding, contributions, and conflicts stay outside the blinded manuscript.
5. **PDF preparation.** Final review PDF needs the journal-required spacing, line/page numbering, and embedded math fonts.

These are packaging/disclosure tasks, not missing mathematical results.

## Reproducibility

Run from a clean environment:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/build_amnat_anonymous_bundle.py
python scripts/verify_crest_philosophy_submission.py --write-report
```

The general pytest suite verifies the theorem surface, non-circularity firewall, strict realizability boundary, conditioned bridges, literal three-way game, AmNat manuscript compliance, and anonymous review bundle. The philosophy verifier remains specific to the retained Biology & Philosophy manuscript.
