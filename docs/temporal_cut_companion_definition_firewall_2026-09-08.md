# CREST temporal-cut companion definition firewall — 2026-09-08

## Decision

The CREST temporal-cut flagship should not describe history, latent mechanism, and future as three independent ontic coordinates whose definitions are supplied by the final state itself.

The safe finite formulation is:

> **Each companion supplies a pre-state primitive object and a contract-relative responsibility map on raw worlds. CREST constructs the state only after those maps have been declared.**

The three responsibilities may overlap or depend on common dynamics. Orthogonality is not assumed. The interaction theorem concerns non-separability of the induced state-refinement responsibilities, not statistical independence of three random variables.

## 1. Present cut

Let `Omega` be the declared finite possible-world carrier and

\[
O_t:\Omega\to Y_t
\]

be the visible observation at the cut. The baseline partition is

\[
B_t=\ker O_t.
\]

`B_t` is not yet the adequate state.

## 2. MLTR: raw past first, retained history type second

Primitive MLTR inputs are:

- a rooted finite replacement DAG;
- declared edge relations `R_e`;
- an accepted root semantic map `q_r:S_r -> Q_r`.

A raw history is a root-to-terminal path `p`. Its composed relation `R_p` induces, when consistent, a carried terminal map

\[
c_p:S_v\to Q_r.
\]

The retained history type is then the equality class

\[
p\equiv_H p'
\iff
c_p=c_{p'}.
\]

Thus the history responsibility map on a raw world may be written

\[
H_t(\omega)=c_{p_t(\omega)}.
\]

The final CREST state is not used to define `p`, `R_p`, or `c_p`. MLTR is source-relative because `q_r` is a declared root contract. Its rooted-DAG formulation is well founded and contains no terminal-to-root semantic recursion.

## 3. MRM: primitive candidate law first, response type second

Primitive MRM inputs are:

- a finite observable macrostate set `Q`;
- a fixed declared intervention alphabet `A`;
- a finite retained candidate-law family `C={theta}`;
- deterministic candidate transitions `G_a^theta:Q -> Q`.

Candidate laws are response-equivalent when

\[
\theta\equiv_\Theta\theta'
\iff
\forall q,a,\ G_a^\theta(q)=G_a^{\theta'}(q).
\]

The response-type set is

\[
R=C/\!\equiv_\Theta.
\]

For a raw world whose latent law is `theta_t(omega)`, the MRM responsibility map is

\[
\Theta_t(\omega)=[\theta_t(\omega)]_\Theta.
\]

This is **latent response structure**, not an assertion that complete causal mechanism identity must be retained.

The candidate-safe state quotient is downstream of this definition. Therefore MRM does not define mechanism by appealing to the final state it later helps refine.

## 4. CCOC: future query responsibility from a fixed raw law

Primitive CCOC inputs are a finite controlled system

\[
\mathcal M=(S,A,T,h)
\]

and a declared legal future grammar

\[
\mathcal L\subseteq A^*.
\]

For a raw configuration `s`, define the response profile

\[
\rho^{\mathcal M}_{\mathcal L}(s)
=
\bigl(\operatorname{Tr}_{\mathcal M}(s,w)\bigr)_{w\in\mathcal L}.
\]

The CCOC equivalence is

\[
s\equiv_F s'
\iff
\rho^{\mathcal M}_{\mathcal L}(s)
=
\rho^{\mathcal M}_{\mathcal L}(s').
\]

For a raw CREST world with cut configuration `s_t(omega)`, the future responsibility map is

\[
F_{t,\mathcal L}(\omega)
=
\rho^{\mathcal M}_{\mathcal L}(s_t(\omega)).
\]

The legal grammar and raw transition law are declared before the exact response quotient. CCOC therefore does not define future sufficiency using the state quotient it is trying to construct.

## 5. Why CCOC and MRM are not the same axis

Both use counterfactual response differences, but the quantifiers sit on different primitive coordinates.

### CCOC

\[
\mathcal M\ \text{fixed};\qquad s,s'\ \text{vary};\qquad \mathcal L\ \text{is declared or enlarged}.
\]

It asks which **raw configurations** remain mergeable under a fixed controlled law when the right-of-cut query family is specified or enlarged.

### MRM

\[
q\ \text{fixed/visible};\qquad A\ \text{fixed};\qquad \theta,\theta'\ \text{vary}.
\]

It asks which **latent laws** behind the same visible configuration remain mergeable under a fixed intervention grammar.

Thus:

\[
\boxed{
\text{CCOC varies configuration/query responsibility at fixed law; MRM varies law at fixed visible configuration/grammar.}
}
\]

They need not be independent. In fact mechanism determines future response, so some structural dependence is expected. CREST interaction accounting is designed for such non-separability.

## 6. Why MLTR is not a hidden circular bootstrap

MLTR assumes one root semantic map `q_r`. This makes its theorem conditional, not circular.

The dependency direction is

\[
q_r,\ \{R_e\},\ p
\to c_p
\to H_t
\to C_H
\to J_t.
\]

There is no theorem-level arrow

\[
J_t\to q_r.
\]

If CREST is applied recursively across multiple historical stages, every application must declare its root contract. The current finite theory does not claim a self-originating first state or a closed temporal semantic loop.

## 7. State comes last

Once the baseline and three responsibility maps are declared, their induced closures/refinements may be combined:

\[
J_t=(C_H\vee C_\Theta\vee C_F)(B_t).
\]

The intended dependency order is therefore

\[
\boxed{
\text{raw worlds + declared contracts}
\to
(H_t,\Theta_t,F_t)
\to
(C_H,C_\Theta,C_F)
\to
J_t.
}
\]

No companion responsibility may depend definitionally on `J_t`.

## 8. Interpretation of the interaction theorem

The Möbius/Harsanyi quantities in CREST are interactions among **responsibility-induced closure operators**. They are not statistical confounding coefficients and do not require the raw inputs `p`, `theta`, and the future-response profile to be independent coordinates.

This matters especially for the three-way theorem. The statement is:

> there exist finite pre-state responsibilities interpretable as retrospective, latent-law, and prospective-response obligations whose joint least-information refinement contains an unbounded genuine three-way interaction term.

It is not:

> every ecological world factors canonically as an independent Cartesian product `past x mechanism x future`.

## 9. Remaining theorem boundary

The current companion repositories prove their own finite conditional objects. CREST has not proved that:

- every legitimate ecological state responsibility belongs to exactly one of these three classes;
- every abstract CREST audit closure is realizable by a canonical CCOC, MLTR, or MRM model without additional construction;
- the three companion primitive objects are statistically independent;
- a continuous-time factorization into left germ, latent generator, and right germ follows automatically.

Those are separate possible theorems. They must not be smuggled into the temporal-cut interpretation.

## Machine-readable circularity contract

`artifacts/temporal_cut_definition_dependency_dag_2026-09-08.json` records the dependency graph above. `tests/test_temporal_cut_definition_dependency_dag.py` verifies that it is acyclic, that the final state is a sink, and that no pre-state history/mechanism/future definition depends on the final state.
