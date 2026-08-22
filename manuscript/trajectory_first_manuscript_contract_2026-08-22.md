# Trajectory-first manuscript contract — 2026-08-22

## Status

This document is the canonical logical contract for the Biology & Philosophy manuscript. The long draft is already trajectory-first; the remaining integration task is to make the **mathematical hierarchy and novelty ceiling** match the strengthened CREST spine.

The manuscript should no longer treat the older four-world `rescue` example as the strongest mathematical consequence. J1 is the finite state-existence/minimality backbone; the connected capability–resolution divergence theorem is the main quantitative cross-gate result.

## Central question

The manuscript begins from:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, response structure, and scientific observables depend on context?**

CREST's philosophical answer is:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

The operational question remains *What counts as the same ecological state?*

## World-level framing

Represent a possible ecological world schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) present configuration, and \(\mathcal F_t\) future-response structure under the interactions/interventions relevant to the scientific problem. For stochastic systems, \(\mathcal F_t\) can be a conditional distribution over possible future trajectories.

This notation does not imply block-universe ontology, global determinism, generic chaos, or universal fitness maximization.

## State definition

The canonical philosophical definition is

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}.
}
\]

Two worlds count as the same scientific state when every difference erased by the quotient is irrelevant to the declared observation/intervention context \(V\) and scientific contract \(\mathcal C\).

The finite joint state \(J\) is the proved construction realizing this idea under explicit finite assumptions.

## Access versus responsibility

Keep distinct:

\[
O_V:\Omega\to Y_V
\]

for scientific access, and

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T)
\]

for responsibility: future operations, inherited meanings, retained mechanisms, evidence conditions, and report target.

## Snapshot sufficiency

The first formal bridge remains

\[
\boxed{
X(\omega)=X(\omega')
\Rightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

This is a **factorization criterion**, not a novelty theorem. CREST does not claim that snapshots are generally insufficient; it asks when their fibers are safe state fibers for the declared contract.

## Companion hierarchy

### Structural insufficiency

1. **CCOC — future/composition.** A widened future grammar can expose dormant distinctions.
2. **MLTR — inherited history/semantics.** Structural replacement can invalidate carried state meaning.
3. **MRM — mechanism response.** Retained mechanisms can agree now and disagree under a required future action.

### Downstream evidence licensing

4. **CED — evidence/reportability.** Available records may fail to identify distinctions the required state needs.

Preserve the typed separation

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

## Finite mathematical hierarchy

### Gate A — carrier feasibility

Use J3/J6 to ask whether the declared obligations share an admissible finite world set. Do not hide carrier existence inside the partition notation.

### Gate B — least-information state

On an admissible finite carrier, baseline \(B\), and implemented refinement closures,

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the unique coarsest common fixed point under J1's assumptions.

For a finite world \(u\),

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

**Manuscript role:** J1 tells the reader what one least-information finite CREST state means. The closure-operator/fixed-point substrate is classical and must not be sold as the strongest novelty.

### Gate C — evidence licensing

For evidence partition \(E\),

\[
\boxed{
\text{full deterministic state report exists}
\iff J\preceq E.
}
\]

A requested target may still factor through \(E\) even when the full state does not.

### Cross-gate direction — qualitative action expansion

The older action-expansion theorem establishes the direction:

\[
A_c\uparrow\Rightarrow K^*\uparrow,
\qquad
\Gamma\uparrow\Rightarrow J\text{ refines},
\]

and a strict finite witness shows carrier expansion, state refinement, loss of full-state monitoring, and preserved target reportability can occur together.

### Cross-gate scaling — mathematical headline

The connected capability–resolution divergence theorem strengthens this to arbitrary scale.

For every integer \(m\ge1\), one finite deterministic CREST system and one newly admitted action `probe` satisfy

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m\text{ bits}.
}
\]

On the same retained present slice \(U_0\):

- required exact state: \(1\to2^m\) classes;
- monitoring-resolution debt: \(0\to m\) bits;
- full-state licensing: yes \(\to\) no;
- constant coarse target reportability: yes \(\to\) yes.

The action alphabet changes only from `{hold}` to `{hold, probe}` and the output alphabet remains `{neutral, bit0, bit1, done}`. Repeated `probe` reveals one latent coordinate at a time. The readout trajectories terminate in the same `fragile` world that `probe` newly makes viable, then reach `safe`, so the result is not a direct sum of unrelated gadgets.

The no-bound corollary is

\[
\boxed{
\text{no finite function of }\Delta|K^*|\text{ alone universally upper-bounds }\Delta K_{U_0}.
}
\]

**Manuscript role:** this is the strongest current theorem-level answer to the concern that contract-relativity is merely verbal. A constant-size expansion of what the system can do can have a constant viability benefit but an arbitrarily large consequence for what the scientific state and monitoring must distinguish.

## Prior-art firewall for the action/state result

The manuscript must explicitly concede two nearby traditions:

1. **Predictive State Representations / causal states:** future tests and future distributions can define predictive state.
2. **State/action abstraction coupling:** Konidaris (2019), *On the necessity of abstraction* (doi:10.1016/j.cobeha.2018.11.005), explicitly discusses state and action abstraction as coupled and the direction in which action abstraction drives a state abstraction that supports those actions.

Therefore do **not** claim novelty for:

- future actions changing a useful state abstraction;
- action/state abstraction coupling in general;
- predictive equivalence or intervention-defined state.

The claim belongs to the CREST cross-gate scaling conjunction:

\[
\text{carrier gain fixed at }1
\quad+\quad
\text{state/monitoring burden arbitrary}
\quad+\quad
\text{full-state licensing lost}
\quad+\quad
\text{target retained}.
\]

No historical-firstness claim is needed.

## Ecological rules as quotient laws

Retain the consequence:

\[
\boxed{
\text{ecological rule}
=\text{effective law on a scientifically adequate quotient}
}
\]

as a philosophical interpretation, not as a claim that ecology lacks underlying objective dynamics.

## Stability hierarchy

Keep separate:

- **dynamical stability** — behavior of ecological trajectories/regimes;
- **evolutionary stability** — invasion/stability under a declared evolutionary model;
- **representational stability** — persistence of an adequate quotient under changes in scientific responsibility.

The qualitative and scaling action-expansion theorems establish strict failures of representational stability without a prior physical ecosystem change. They do not prove a general mathematical relation among all three stability notions.

## Key sentence

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to what the state is required to support.**

This is representational, not backward causal.

## Manuscript order

```text
1. Why ecological state is a compression problem
2. Scientific access, contract, and state equivalence
3. Structural failures of present sameness
   - CCOC / MLTR / MRM
4. Finite mathematical answer
   - carrier feasibility
   - J1 least-information state
   - evidence licensing
   - qualitative action expansion
   - capability–resolution divergence / no-bound result
5. Quotient laws and representational stability
6. Relation to predictive states, POMDP/state abstraction, and state/action abstraction
7. Limits
8. Conclusion
```

CED should be introduced conceptually before the finite evidence gate, but the manuscript should avoid a long empirical/monitoring-design detour. Real-data applications are optional illustrations, not proof requirements.

## Proposed revised abstract

Ecologists routinely describe ecosystems by present states, yet a present snapshot can conceal differences in history, latent mechanism, and future response that matter for prediction or intervention. We develop Contract-Relative Ecological State Theory (CREST), in which an ecological state is a scientifically licensed compression of a temporally extended ecological world. CREST separates carrier feasibility, the least-information state required by a declared scientific contract, the state identified by available evidence, and the target that can actually be reported. On a declared finite carrier, the required state is the unique coarsest partition satisfying the implemented future, inherited-semantic, mechanism-response, and reporting obligations; evidence identifies that state exactly when it resolves the resulting partition. The main cross-gate result concerns intervention capability. For every integer \(m\ge1\), we construct one finite deterministic system in which adding a single controllable action makes exactly one additional world viable while forcing a retained present-state slice to refine from one class to \(2^m\) classes. Under unchanged monitoring, the resulting state-resolution deficit is exactly \(m\) bits: full-state identification is lost although a coarse target remains reportable. Thus viability gain alone cannot upper-bound the representational burden created by an expanded future repertoire. CREST does not claim novelty for predictive states, purpose-relative abstraction, or the general coupling of state and action abstraction. Its contribution is to place future/composition, inherited meaning, mechanism response, carrier feasibility, and evidence licensing in one ecological state-equivalence problem and to show that their consequences can diverge without any carrier-gain-only bound.

## Revision firewall

When integrating into the long manuscript:

- preserve verified finite theorem statements;
- keep J1 as foundational, not as a novelty claim for fixed-point theory;
- promote the connected capability–resolution/no-bound result above the old four-world witness;
- explicitly cite the state/action-abstraction prior-art boundary;
- do not describe the trajectory interpretation as a proved continuous/stochastic theorem;
- do not claim generic ecosystem chaos or universal fitness maximization;
- do not present CED as a fourth ontic source of ecological difference;
- do not claim the structural obstructions are exhaustive;
- do not require empirical data to establish the finite theorem;
- do not add another theorem family unless it strengthens the same carrier/state/evidence/target chain.
