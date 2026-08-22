# CREST — Contract-Relative Ecological State Theory

CREST asks one question:

> **What counts as the same ecological state?**

More precisely: when an ecosystem is temporally extended, adaptively changing, only partly observed, and open to new interactions or interventions, **which differences may science safely ignore when two configurations are assigned the same state label?**

CREST answers that question in three stages:

```text
one philosophical question
        ↓
four scientific obligations on sameness
        ↓
finite mathematical existence / minimality / evidence theorems
        ↓
ecological consequences for open systems, structural change,
latent mechanisms, monitoring, and management
```

## The four obligations

The four companion programs are not four rival state definitions. They are four ways a proposed ecological-state merge can fail.

| obligation | companion | question | ecological failure |
|---|---|---|---|
| **future sufficiency** | CCOC | Can a newly relevant future interaction or intervention expose a distinction we erased? | present functional equivalence fails in an open future |
| **semantic coherence** | MLTR | Does an inherited ecological category still mean the same thing after structural change? | old state labels cease to be operationally portable |
| **mechanism robustness** | MRM | Do retained latent mechanisms agree on the future response required from the state? | visible sameness hides response-relevant mechanism differences |
| **evidential licensing** | CED | Does the observation/experiment actually identify the distinction the state requires? | required state resolution outruns available evidence |

The compact program contract is

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where future grammar, inherited semantics, retained mechanisms, evidence, and target jointly determine which distinctions matter.

## The mathematical spine

CREST's main mathematics is intentionally smaller than the full theorem inventory.

### Gate A — can one common ecological world set be used?

J3/J6 compute the maximal admissible carrier under universal or controlled action semantics. A failed carrier is a genuine no-go: there is no fully adequate common state under the declared contract.

### Gate B — what is the least-information adequate state?

On one admissible finite common carrier `U`, with baseline partition `B`, let the four obligations induce refinement closures

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}.
\]

CREST-J1 proves

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the **unique coarsest / least-information** partition satisfying all four obligations. The CREST state of world `u` is

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

The lattice/fixed-point substrate is classical. The CREST result is the explicit coupling of four ecology-specific obligations on one state representation.

### Gate C — has that state actually been identified?

For evidence partition `E`,

\[
\boxed{
\text{full deterministic state report exists}
\iff
J\preceq E.
}
\]

If this fails, `J` still specifies the required state, but evidence supports a set of compatible `J` blocks. A declared target can remain reportable even when the full state is unresolved.

### Cross-gate result — more control can require more state information

The strongest current ecological consequence is not generic purpose-relativity. Under explicit one-sided assumptions, enlarging a management repertoire can

\[
|K^*|\uparrow,
\qquad
|J|\uparrow,
\qquad
\text{full-state identifiability}\downarrow,
\]

while target reportability remains unchanged.

So **an intervention can change what must count as a state before that intervention is ever executed**.

The minimum evidence refinement needed to recover full-state identification is

\[
E\vee J,
\]

with finite monitoring-resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

A microdonta-derived channel example further shows that some monitoring debt is **structural**: collecting more measurements of the same net output cannot break an observational symmetry; a new discriminating measurement channel may be required.

## Ecological interpretation

CREST treats ecological state as a scientific compression, not as a claim that nature supplies one context-free partition.

A useful working interpretation is that the latent world represented by CREST may contain more than a present snapshot: relevant history, current hidden structure, response mechanisms, and counterfactual future responses can all be coordinates of the common carrier. Under that interpretation,

> **what ecologists call a present state can be a compressed claim about the past that produced it and the futures it can still enter.**

This trajectory-level reading is a philosophical extension of the current finite theory, not yet a separate continuous/stochastic theorem.

The ecological projection is developed in [`docs/crest_ecological_projection.md`](docs/crest_ecological_projection.md).

## Canonical reading order

1. [`docs/contract_relative_ecological_state_theory.md`](docs/contract_relative_ecological_state_theory.md) — the philosophical answer and four obligations.
2. [`docs/crest_mathematical_spine.md`](docs/crest_mathematical_spine.md) — the minimal proved theorem chain.
3. [`docs/crest_ecological_projection.md`](docs/crest_ecological_projection.md) — projection back to ecology.
4. [`manuscript/crest_philosophy_biology_philosophy.md`](manuscript/crest_philosophy_biology_philosophy.md) — Biology & Philosophy target manuscript.
5. [`docs/README.md`](docs/README.md) — map of supporting proofs, literature audits, and archived development concepts.

## What is supporting rather than headline mathematics

CREST retains J2/J5 lift comparison, J4/J7 carrier repair and complexity, and O1 repair/evidence noncommutation as proved supporting results. They protect the theory's boundaries and executable correctness, but they are not separate answers to the philosophical question.

Likewise, Monitoring Adequacy Envelope, Counterfactual Obsolescence, State Shadow, and Decision-Safe Ignorance are retained as derived descriptions/regimes rather than additional headline theorem families.

## Scope firewall

CREST does **not** currently claim:

- one intrinsic ecological partition independent of scientific contract;
- that the four obligations exhaust every legitimate notion of ecological state;
- that purpose-relative adequacy, state abstraction, viability kernels, observability, or partition refinement are new;
- that finite state-memory bits equal financial or field sampling costs;
- a general infinite, continuous, stochastic, approximate, or delayed-observation theorem;
- that a present snapshot is always insufficient — only that its sufficiency is a contract-dependent question.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

## Provenance

The independent repository was migrated from `zuizui0223/mrm` at audited source SHA `72550fa8335cbffb901785f8a171c647b3cf8cc6`. See `PROVENANCE.md` for migration provenance and `docs/crest_synthesis_proof_ledger_2026-08-17.md` for the full proof inventory.
