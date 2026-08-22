# Trajectory-first manuscript contract — 2026-08-22

## Status

This document is the canonical restructuring contract for the Biology & Philosophy manuscript. It changes the manuscript's **logical center**, not the proof status of the finite CREST results.

The current long draft `crest_philosophy_biology_philosophy.md` remains the source text to be revised. It should no longer be treated as conceptually final while its opening still runs from four audits upward.

## Central question

The manuscript should begin from:

> **Why can a finite ecological state exist at all in a world whose relevant dynamics, interactions, response structure, and scientific observables depend on context?**

The answer CREST develops is:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

The older question — *What counts as the same ecological state?* — remains important, but becomes the operational form of this deeper question rather than the sole philosophical starting point.

## World-level framing

A possible ecological world is represented schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where:

- \(h_t\) is relevant ecological history;
- \(x_t\) is present configuration;
- \(\mathcal F_t\) is the future-response structure under the interactions and interventions relevant to the scientific problem.

For a stochastic system, \(\mathcal F_t\) may be a conditional distribution over possible future trajectories. No claim of global determinism, block-universe ontology, mathematical chaos, or universal fitness maximization follows from this notation.

The manuscript should connect this framing to ecological complex-adaptive and eco-evolutionary dynamics cautiously: variation and stochasticity generate alternatives, context-dependent selection biases their contribution, and organisms can alter the environmental and interaction conditions that determine later selective responses.

## State definition

The manuscript's canonical philosophical definition should be

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}
}
\]

with the interpretation:

> two ecological worlds count as the same state when every difference erased by the quotient is irrelevant to the scientific work declared by the observation/intervention context \(V\) and contract \(\mathcal C\).

The finite joint state \(J\) is then the proved finite construction layer realizing this idea under the repository's explicit assumptions; it should not appear before the reader knows what kind of object a CREST state is supposed to represent.

## Observation/intervention context versus scientific contract

Keep these conceptually distinct.

\[
O_V:\Omega\to Y_V
\]

captures scientific access: what a measurement/intervention context can distinguish.

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T)
\]

captures responsibility: which future operations, inherited meanings, mechanisms, evidence conditions, and report target the state must support.

This avoids both naïve intrinsic-state language and subjective observer relativism.

## Snapshot sufficiency as the first formal bridge

The first bridge from philosophy to the finite program should be:

\[
\boxed{
X(\omega)=X(\omega')
\Rightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

A present snapshot is sufficient only if it factors the required CREST state. CREST does not claim snapshots are always insufficient; it makes their sufficiency a condition to be demonstrated.

This criterion organizes the companion programs.

## Companion program hierarchy

### Structural reasons that a present-state merge can fail

1. **CCOC — future insufficiency.** Equal present descriptions can diverge when a wider future grammar makes a dormant distinction addressable.
2. **MLTR — historical / semantic insufficiency.** Equal present descriptors can inherit different operational meaning after replacement or route-dependent structural change.
3. **MRM — mechanistic insufficiency.** Equal visible states can contain retained mechanisms that disagree on a future response required by the contract.

These are three obstruction theories explaining why present sameness need not imply required-state sameness.

### Downstream evidence licensing

4. **CED — evidential licensing.** CED should be presented after representational adequacy. It asks whether the experiment and observation architecture actually identifies enough of the required distinction to justify a deterministic state or target report.

The manuscript must preserve

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

## Finite theorem placement

Only after the world-level and snapshot-sufficiency framing should the manuscript introduce the existing finite common-carrier theorem chain:

1. carrier feasibility;
2. unique least-information adequate state \(J\);
3. evidence licensing;
4. action-expansion / monitoring-debt consequences.

For a finite admissible common carrier \(U\), baseline \(B\), and implemented refinement closures,

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
\]

remains the unique coarsest partition satisfying the declared finite requirements under J1's assumptions.

The generic lattice substrate remains prior art. CREST's philosophical work is to explain why these particular distinctions belong to one ecological state-adequacy problem and how required state differs from empirical identification.

## Ecological rules as quotient laws

The manuscript should promote this from a late interpretation to a main consequence.

An ecological rule is well-defined on a state quotient only while worlds merged by that quotient agree on every response required from the rule.

Hence:

\[
\boxed{
\text{many ecological rules are effective laws of an adequate quotient,
not necessarily laws of the full latent world.}
}
\]

Changing scale, measurement channel, future repertoire, structural context, or retained mechanism can invalidate an old quotient for a new scientific problem without making the original rule false in its original domain.

This is the non-relativist route to context-sensitive ecological laws.

## Stability hierarchy

The discussion should distinguish:

- **dynamical stability** — stability of ecological trajectories or regimes;
- **evolutionary stability** — invasion/stability of strategies under a declared evolutionary model;
- **representational stability** — persistence of an adequate state quotient when scientific context changes.

The existing action-expansion witness already supports the strict statement that representational stability can fail before the underlying ecosystem changes physically.

A general mathematical relation among all three remains open and must not be presented as proved.

## Key sentence to preserve

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to what the state is required to support.**

This is a statement about representation and scientific responsibility, not backward causation.

## Revised manuscript order

```text
1. Why ecological state is a compression problem
   - complex adaptive / eco-evolutionary motivation
   - world trajectories rather than assumed snapshots

2. Scientific access, contract, and state equivalence
   - V versus C
   - State_{C,V}(ω)
   - snapshot sufficiency

3. Why present sameness can fail
   - CCOC: future
   - MLTR: history / inherited meaning
   - MRM: mechanism

4. What evidence licenses
   - CED downstream
   - required / identified / reportable distinction

5. Finite CREST construction
   - carrier feasibility
   - joint least-information state J
   - evidence gate

6. Ecological consequences
   - quotient laws
   - action expansion
   - structural monitoring debt
   - representational stability

7. Limits and relation to prior theories
   - causal/predictive states
   - abstraction and effective theories
   - ecological identity and stability
   - no exhaustive or intrinsic-state claim

8. Conclusion
   - state as scientifically licensed temporal compression
```

## Proposed revised abstract

Ecologists routinely describe ecosystems by present states, yet a present snapshot can conceal differences in history, latent mechanism, and future response that matter for prediction or intervention. We develop Contract-Relative Ecological State Theory (CREST) from the premise that an ecological state is not necessarily a property of an instant, but a scientifically licensed compression of a temporally extended ecological world. CREST separates the ecological world from the observation and intervention context through which it is accessed, and asks whether a present snapshot is sufficient for the scientific work assigned to a state. Three companion theorem programs expose distinct structural failures of snapshot sufficiency: a wider future can make dormant distinctions operationally relevant; structural replacement can break inherited state meaning; and retained mechanisms can disagree on required future responses. A fourth program addresses the downstream epistemic question of whether available evidence identifies the distinctions the state requires. On a declared finite common carrier, the existing CREST construction yields the unique coarsest joint partition satisfying the implemented requirements and separately tests whether evidence identifies that state. This framework also explains how a new intervention can refine the scientifically adequate present state before the ecosystem changes physically, and why ecological regularities can be understood as effective laws on context-adequate quotients rather than context-free laws of the full latent world. CREST therefore links temporal extension, causal response, observation, intervention, and evidence without positing one intrinsic ecological partition or claiming that present snapshots are universally inadequate.

## Revision firewall

When integrating this contract into the long manuscript:

- preserve verified finite theorem statements unless a proof audit requires change;
- do not describe the trajectory-level interpretation as a proved continuous/stochastic theorem;
- do not turn eco-evolutionary motivation into a claim that ecosystems are generically chaotic;
- do not claim a universal fitness-maximizing direction;
- do not present CED as a fourth ontic source of ecological difference;
- do not claim the three structural obstructions are exhaustive;
- do not add new theorem families merely to match the new philosophical vocabulary.
