# CREST Graphify report

Deep analysis of the combined PR #61 + PR #62 repository state, refreshed after cleanup on 2026-08-24.

- Detected files: 138
- Nodes: 759
- Edges: 1,366
- Communities: 59
- Semantic dangling endpoints: 58
- Same-endpoint edge collapses: 202
- Mean query cost: approximately 915 tokens
- Compression relative to full-file scan: approximately 55.4×

## Submission path

`crest_biology_philosophy_blinded_submission.md` is the only active review manuscript. The repository reads as philosophy → finite mathematics → ecological projection.

## Protected hubs

- `ComponentCoverage`
- `ControlledSynchronizedLiftProblem`
- `JointCRESTContract`
- `AuditRefinement`
- `SynchronizedLiftProblem`

No hub implementation was moved.

## Cleanup interpretation

The graph supports a three-way classification: canonical submission/theorem/reproducibility spine, reusable support, and dated archive. See `docs/GRAPHIFY_CLEANUP_RESULT_2026-08-24.md` for the applied moves and validation checkpoint.

This report preserves the verified aggregate diagnostics. Individual semantic edges remain heuristic because of dangling and collapsed endpoints.
