# CREST — Contract-Relative Ecological State Theory

CREST asks a more basic question than how to classify an ecosystem at one instant:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, mechanisms, and scientific observables depend on context?**

The working answer is:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

A present ecological snapshot is therefore not assumed to be the state. CREST asks which differences among possible ecological worlds may safely be erased under a declared scientific responsibility, and what happens when several such responsibilities must be satisfied together.

```text
self-modifying ecological dynamics
        ↓
temporally extended possible worlds
        ↓
observation / intervention context
        ↓
scientific contract
        ↓
carrier feasibility
        ↓
least-information adequate state
        ↓
joint responsibility debt
        ↓
obstruction spectrum / change diagnosis
        ↓
evidence licensing and reportability
```

The proved mathematics is finite and exact. The trajectory-level framing organizes that finite latent-world theory; CREST does **not** yet claim a general continuous or stochastic trajectory theorem.

## 1. World before state

Write a possible ecological world schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) the present ecological configuration, and \(\mathcal F_t\) the declared future-response structure. For stochastic systems, \(\mathcal F_t\) may be a conditional distribution over future trajectories rather than one fixed future.

CREST does not require every coordinate of \(\omega\) to be retained. It asks which differences can be erased without invalidating the scientific work assigned to the state.

## 2. Scientific contract and Snapshot sufficiency

A scientific contract is written schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where \(\Gamma\) is future-response responsibility, \(\mathcal H\) inherited semantic/history responsibility, \(\Theta\) retained mechanism responsibility, \(D\) the evidence architecture, and \(T\) the requested report or decision target.

State identity is **context- and contract-relative but not arbitrary**: scientists specify the task, but dynamics, causal structure, and evidence determine whether a proposed merge survives it.

Let \(X(\omega)\) be the present snapshot and \(q_{\mathcal C,V}(\omega)\) the required CREST state. Snapshot sufficiency is the factorization condition

\[
X(\omega)=X(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
\]

## 3. Four responsibility layers

CREST keeps three structural obstructions and one evidential layer distinct.

| responsibility | companion | role |
|---|---|---|
| **future sufficiency** | [CCOC](https://github.com/zuizui0223/ccoc) | future/composition distinctions exposed by newly addressable interactions or interventions |
| **semantic coherence** | [MLTR](https://github.com/zuizui0223/mltr) | inherited meaning and replacement-history distinctions after structural change |
| **mechanism robustness** | [MRM](https://github.com/zuizui0223/mrm) | retained mechanisms that disagree on required responses; ambiguity versus active resolution |
| **evidence licensing** | [CED](https://github.com/zuizui0223/ced) | whether observations identify an already-required distinction and what can still be reported |

These are not rival definitions of ecological state. They are different scientific responsibilities that can act on one common ecological carrier.

CREST therefore separates

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}
}
\]

in general.

## 4. Finite mathematical spine

On one admissible finite common carrier \(U\), let \(B\) be a baseline partition and let

\[
C_1,\ldots,C_k
\]

be the refinement closures induced by the declared responsibilities. Their common fixed point above the baseline is

\[
\boxed{
J=(C_1\vee\cdots\vee C_k)(B),
}
\]

the unique coarsest / least-information partition satisfying all implemented requirements.

The finite theory is organized by three gates:

1. **carrier feasibility** — can the required descriptions be synchronized on one admissible world set?;
2. **representational adequacy** — what is the least-information state preserving the required distinctions?;
3. **evidential licensing** — does the observation contract identify which required state is occupied?

For evidence partition \(E\), full deterministic state reporting exists exactly when \(J\preceq E\).

## 5. Quantitative headline — non-additive joint ecological state debt

The CREST flagship quantity is defined only after multiple responsibilities are placed on the same common lift.

For responsibility \(i\), define its individual debt from baseline \(B\) by

\[
D_i=\log_2|C_i(B)|-\log_2|B|.
\]

Define the joint debt by

\[
D_{\rm joint}=\log_2|J|-\log_2|B|,
\]

and the interaction term

\[
\boxed{
\Delta=D_{\rm joint}-\sum_iD_i.
}
\]

A marked directed-cycle family gives

\[
D_1=1,
\qquad
D_2=0,
\qquad
D_{\rm joint}=\log_2n,
\]

hence

\[
\boxed{
\Delta=\log_2n-1,
}
\]

which is unbounded. Responsibility-wise additive accounting can therefore underestimate the state or monitoring resolution required after the responsibilities are enforced jointly: one audit-created distinction can activate another audit.

The sharp converse boundary is

\[
D_i=0\ \forall i
\Longrightarrow
D_{\rm joint}=0
\Longrightarrow
\Delta=0.
\]

The marked-cycle, closure, fixed-point, and partition-refinement mathematics are classical substrate. CREST's claimed contribution here is the **cross-responsibility ecological accounting interpretation**, not a new generic bisimulation theorem.

### Numeric obstruction spectrum

For a small declared responsibility set, CREST now evaluates every coalition

\[
v(S)=\log_2|J_S|-\log_2|B|
\]

and reports standalone debts, joint debt, Shapley attribution, and exact Möbius/Harsanyi interaction dividends. In the canonical six-world CCOC/MLTR/MRM cascade,

```text
baseline                         2 states
CCOC alone                       3 states   0.5849625007 bit
MLTR alone                       2 states   0 bit
MRM alone                        2 states   0 bit
CCOC + MLTR                      4 states   1.0000000000 bit
CCOC + MLTR + MRM                5 states   1.3219280949 bit
interaction excess Delta                    0.7369655942 bit
```

The joint burden decomposes as

\[
1.3219280949
=
0.5849625007_{\rm\ CCOC}
+
0.4150374993_{\rm\ CCOC\times MLTR}
+
0.3219280949_{\rm\ CCOC\times MLTR\times MRM}
\quad\text{bits}.
\]

Thus MLTR and MRM can have zero standalone debt while still contributing to the state resolution required jointly.

### Before/after change diagnosis

For two contracts on the same named responsibility set,

\[
\boxed{
\delta D_{\rm joint}
=
\sum_i\delta D_i+\delta\Delta.
}
\]

The comparison engine classifies the source of change as `direct-only`, `interaction-only`, `mixed`, or `null`, reports whether joint/direct/interaction burden increased or decreased, and aggregates interaction change by coalition order.

In the canonical activation comparison, every standalone debt is unchanged but the joint state changes from 3 to 5 states:

\[
\delta D_{\rm joint}
=
\delta\Delta
=
+0.7369655942\ \text{bit}.
\]

Its diagnosis is

```text
change_class               interaction-only
joint_debt_direction       increase
direct_direction           unchanged
interaction_direction      increase
active_interaction_orders  [2, 3]
dominant_interaction_order 2
```

with order-2 change `+0.4150374993 bit` and order-3 change `+0.3219280949 bit`. The reverse comparison is an interaction-only decrease with the same active orders and opposite signs.

This gives CREST a finite numerical notion of **representational change**: a system can become harder or easier to represent jointly even when none of its responsibility-wise standalone scores changes.

Executable surfaces:

- [`crest/joint_debt.py`](crest/joint_debt.py) — joint debt and unbounded non-additivity witnesses;
- [`crest/obstruction_spectrum.py`](crest/obstruction_spectrum.py) — coalition spectrum, Shapley attribution, and interaction dividends;
- [`crest/obstruction_compare.py`](crest/obstruction_compare.py) — before/after source, direction, and interaction-order diagnosis;
- [`artifacts/crest_obstruction_spectrum.json`](artifacts/crest_obstruction_spectrum.json) — CI-regenerated canonical numeric report.

## 6. Supporting quantitative results

Two earlier quantitative results remain important, but they are no longer the flagship headline.

First, **carrier-size gain does not upper-bound state burden**. A connected finite controlled family can add exactly one viable world while forcing an arbitrarily large refinement of a retained present slice.

Second, finite counterfactual response capacity does bound one responsibility's debt. For a sequential pathway of response-relevant depth \(H\), with at most \(r_h\) distinguishable outcomes at stage \(h\),

\[
\Delta K\le\sum_{h=1}^{H}\log_2r_h.
\]

For a homogeneous \(r\)-ary pathway,

\[
\boxed{\Delta K\le H\log_2r.}
\]

The package-level sharp family in [`crest/sequential_witnesses.py`](crest/sequential_witnesses.py) attains equality. This is a within-responsibility capacity law; \(\Delta\) instead measures interaction across responsibilities.

## 7. Ecological meaning

A positive \(\Delta\) means that monitoring or representation cannot safely be budgeted by solving each scientific responsibility against the original baseline and adding the results. The distinction created for one task can change which pairs another task must separate.

Operationally, CREST therefore recommends the order

\[
\text{common ecological carrier}
\rightarrow
\text{joint fixed point }J
\rightarrow
D_{\rm joint},\Delta
\rightarrow
\text{obstruction spectrum / change diagnosis}
\rightarrow
\text{evidence design}.
\]

The theorem is structural, not a prevalence claim. Real applications may have \(\Delta<0\), \(\Delta=0\), or \(\Delta>0\). Positive values indicate synergistic refinement; negative values indicate overlap or redundancy among responsibility-specific debts.

## 8. Ecological rules as quotient laws

A coarse ecological rule is an effective law on a scientifically adequate quotient. If a response \(R_{\mathcal C}\) factors as

\[
R_{\mathcal C}=L_{\mathcal C,V}\circ q_{\mathcal C,V},
\]

then the quotient supports the rule. A changed responsibility can invalidate the old quotient without implying that the old rule was false in its original domain.

## 9. Representational stability

CREST distinguishes dynamical, evolutionary, and **representational stability**. Representational stability asks whether the same state quotient remains adequate when observation, intervention, future, mechanism, semantic, or reporting responsibilities change.

The before/after obstruction comparison turns this from a purely qualitative idea into a finite diagnostic: it reports how many required states and bits changed, whether the change was direct or interaction-generated, and which interaction orders carried the change.

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to the contract.**

This is representational, not backward, causation.

## 10. Prior-art and scope firewall

CREST does not claim novelty for generic partition refinement, closure operators, state abstraction, automata minimization, predictive states, purpose-relative modelling, viability kernels, distinguishing sequences, response trees, Shapley values, Möbius inversion, Harsanyi dividends, or the information capacity of an \(r\)-ary sequence. It also does not claim one intrinsic ecological partition independent of scientific context, nor a general infinite/continuous/stochastic theorem.

The flagship claim is narrower: **distinct ecological responsibilities can interact so that their jointly required state resolution is not captured by responsibility-wise additive accounting**, and CREST now makes both the static interaction and its before/after change numerically explicit on a declared common lift.

## 11. Canonical reading order

1. [`manuscript/crest_flagship_amnat_v0.2.md`](manuscript/crest_flagship_amnat_v0.2.md) — canonical Δ-centered flagship manuscript; target: *The American Naturalist*.
2. [`docs/flagship_integration/joint_debt_delta_section.md`](docs/flagship_integration/joint_debt_delta_section.md) — theorem-facing static Δ section and novelty firewall.
3. [`docs/flagship_integration/obstruction_change_diagnostic_section.md`](docs/flagship_integration/obstruction_change_diagnostic_section.md) — manuscript-ready before/after interaction-only diagnosis.
4. [`docs/crest_obstruction_spectrum_2026-09-08.md`](docs/crest_obstruction_spectrum_2026-09-08.md) — numeric spectrum, Shapley attribution, and interaction anatomy.
5. [`docs/crest_obstruction_change_accounting_2026-09-08.md`](docs/crest_obstruction_change_accounting_2026-09-08.md) — exact before/after accounting identities and interaction-order decomposition.
6. [`docs/crest_mathematical_spine.md`](docs/crest_mathematical_spine.md) — finite gate structure and supporting theorem chain.
7. [`docs/contract_relative_ecological_state_theory.md`](docs/contract_relative_ecological_state_theory.md) — trajectory-first philosophical statement and state definition.
8. [`docs/crest_sharp_sequential_state_debt_law_2026-09-06.md`](docs/crest_sharp_sequential_state_debt_law_2026-09-06.md) — sharp sequential \(H\log_2r\) supporting law.
9. [`docs/crest_ecological_projection.md`](docs/crest_ecological_projection.md) — ecology-facing interpretation, quotient laws, and stability.
10. [`manuscript/crest_biology_philosophy_blinded_submission.md`](manuscript/crest_biology_philosophy_blinded_submission.md) — retained Biology & Philosophy manuscript surface; no longer the CREST flagship entrypoint.

## Run

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/report_obstruction_spectrum.py --write-report
python scripts/compute_obstruction_spectrum.py contract.json
python scripts/compare_obstruction_spectra.py before.json after.json
python scripts/verify_crest_philosophy_submission.py --write-report
```

## Provenance

The independent repository was migrated from `zuizui0223/mrm` at audited source SHA `72550fa8335cbffb901785f8a171c647b3cf8cc6`. See `PROVENANCE.md` for migration provenance and `docs/crest_synthesis_proof_ledger_2026-08-17.md` for the full proof inventory.
