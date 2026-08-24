# Graphify repository cleanup contract — 2026-08-24

## Goal

Use one deep Graphify pass to separate the CREST repository into a minimal active submission spine, reusable theorem/reproducibility support, and archived development material without deleting scientific provenance.

## Canonical submission spine

These are the only manuscript-facing artifacts that should remain first-class after cleanup:

- `manuscript/crest_biology_philosophy_blinded_submission.md` once PR #61 lands;
- one title-page template / final title page;
- one concise submission README/handoff;
- theorem implementation required by the manuscript headline;
- tests that directly verify theorem statements, blinded-submission constraints, and reproducibility;
- generated submission report / provenance required to reproduce the manuscript claims.

## Preserve but demote

Keep provenance and reusable support, but move it out of the active manuscript surface when Graphify shows it is not on a path to the canonical submission artifact:

- prior-art audits and reviewer-preemption notes;
- old manuscript inserts already integrated into the canonical manuscript;
- empirical/restoration/island/urban projection material that is no longer part of the submission spine;
- superseded trajectory/state contracts;
- development-only theorem notes whose claims are already represented by a canonical theorem document or executable test;
- historical submission handoffs replaced by the final submission handoff.

Preferred destination: `archive/` with dated subdirectories, preserving git history and provenance.

## Do not delete

- theorem code used by active tests;
- frozen witness constructions supporting the manuscript headline;
- provenance, citation audits, and source registries needed to defend claims;
- generated artifacts required by reproducibility checks;
- compatibility surfaces still imported by active code/tests;
- any material whose removal breaks the theorem suite or submission verifier.

## Graphify run

Run from the repository root in a Graphify-enabled coding assistant:

`/graphify . --mode deep`

Expected committed outputs:

- `graphify-out/graph.html`
- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.json`

`graphify-out/cost.json` and `graphify-out/cache/` stay local/ignored.

## Queries to answer before moving files

1. Which files are on a dependency or reference path to the blinded submission manuscript?
2. Which theorem modules are reachable from tests that verify `Δ|K*|=1` and arbitrary `ΔK_U0=m`?
3. Which manuscript inserts have no incoming references from the current submission candidate?
4. Which docs duplicate claims already present in a newer canonical document?
5. Which tests cover only superseded empirical/restoration/Izu material?
6. Which scripts/artifacts are used by the current submission verifier?
7. Which files are graph hubs/god nodes and must not be moved casually?
8. Which open PRs overlap the same graph communities or files?

## Cleanup rule

A file moves to `archive/` only when all of the following are true:

1. it is not on the canonical manuscript/theorem/reproducibility path;
2. its scientific content is already preserved in a canonical artifact or remains available in archive;
3. no active import/test/submission verifier depends on its current path, or the dependent reference is updated in the same PR;
4. the full test and submission verification suites remain green after the move.

Physical deletion is reserved for generated junk or exact duplicates with preserved provenance. Scientific development history should be archived, not erased.

## First-pass structural finding before Graphify

The current `manuscript/` directory mixes active submission artifacts with integrated/superseded material. In particular, the following are obvious candidates for Graphify review rather than first-class manuscript surface:

- `empirical_validation_bridge_note.md`
- `island_urban_examples_insert.md`
- `restoration_conservation_examples_insert.md`
- `psr_boundary_insert_2026-08-22.md`
- `trajectory_first_manuscript_contract_2026-08-22.md`
- `joint_state_section.md`
- older fit-check / handoff files once the final blinded submission path is merged.

The deep graph confirmed that the superseded submission files are outside the active submission/reproducibility path. The applied classification and verification checkpoint are recorded in `GRAPHIFY_CLEANUP_RESULT_2026-08-24.md`.
