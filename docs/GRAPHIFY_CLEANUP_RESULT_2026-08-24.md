# Graphify cleanup result — 2026-08-24

## Decision

The repository now has one submission authority:

`manuscript/crest_biology_philosophy_blinded_submission.md`.

The active manuscript surface contains only the blinded manuscript, separate title page, bundle README, blocker ledger, and canonical scope contract. Superseded scientific material was archived, not deleted.

## Graph evidence

The combined PR #61 + PR #62 deep pass covered 138 files. The final graph contained 759 nodes, 1,366 edges, and 59 communities. The principal implementation hubs were `ComponentCoverage`, `ControlledSynchronizedLiftProblem`, `JointCRESTContract`, `AuditRefinement`, and `SynchronizedLiftProblem`.

The central cross-community connection is `JointCRESTContract`: it links joint-state construction, carrier repair, controlled repair, and lift bounds. Those implementation and theorem surfaces remain in place.

## Classification applied

- **canonical:** the five-file submission surface and theorem/reproducibility path;
- **support:** mathematical implementation, active theorem tests, citation/novelty audits, and ecological projection material not presented as validation;
- **archive:** superseded manuscripts, handoffs, integrated inserts, obsolete Discussion arcs, and tests that only enforced those older surfaces.

## Verification at the cleanup checkpoint

- abstract: 216 words;
- main text before References: 5,810 words;
- keywords: 6;
- blinded identifier hits: 0;
- automated submission blockers: 0;
- regression suite: 133 tests passed;
- `git diff --check`: passed.

## Graph caveat

The semantic extraction reported 58 dangling endpoints and 202 same-endpoint edge collapses. All 138 detected files were covered, but individual edge counts should not be treated as quantitative scientific evidence. The graph was used for hub detection, community structure, reachability, and cleanup classification.
