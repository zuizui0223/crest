# Trajectory-first manuscript contract — updated 2026-08-23

## Status

This is the canonical logical contract for the Biology & Philosophy manuscript.

The manuscript is already trajectory-first and already contains the connected capability–resolution theorem. The 2026-08-23 integration raises the philosophical center by one level **without adding a new theorem family**:

> **How can ecological states and ecological laws exist at all in a temporally extended, partially observed, self-modifying adaptive world?**

The finite theorem spine remains unchanged. The new work is to connect world → state → law → stability more explicitly and to use `microdonta` only as an ecology-grounded witness source for hidden basin state, latent causal degeneracy, and structural observational symmetry.

## Central question and answer

The manuscript should open from two nested questions.

### Higher-level question

> **How can state and law be well-defined in an ecological world whose interactions, selective conditions, possible responses, and scientific access change with context?**

### Operational question

> **What counts as the same ecological state?**

CREST's philosophical answer is:

> **An ecological state is a scientifically licensed quotient of temporally extended ecological worlds; an ecological law is an effective law on such a quotient.**

The earlier wording remains valid:

> **An ecological state is a scientifically licensed compression of a temporally extended ecological world.**

The new wording makes explicit what the compression is for: it defines the domain on which a coarse ecological rule is well-defined.

## World-level framing

Let \(\Omega\) be a set of admissible ecological world-histories. A world can be represented either as

\[
\omega=(x_s)_{s\in\mathbb T}
\]

or, relative to a present time \(t\), schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) present configuration, and \(\mathcal F_t\) future-response structure under the interactions/interventions relevant to the problem.

For stochastic systems, use a probability measure or conditional future distribution rather than one predetermined path.

### Physical-metaphysical firewall

The manuscript may say that a **complete trajectory is used as a mathematical world object**. It must not say that modern physics proves that the actual future is already fixed.

Keep distinct:

- eternalism/block-universe metaphysics;
- causal/nomological determinism;
- probabilistic or stochastic physical models.

CREST requires none of these as an ontology. Complete world-histories are a representation device that works for deterministic or stochastic model families.

Do not claim that quantum physics is simply “all random,” that relativity proves one predetermined future, or that the future literally causes the present.

## Ecological adaptive direction without global teleology

The ecology-facing motivation should be stronger than “ecosystems are complicated,” but weaker than global optimization.

Use the decomposition

\[
\boxed{
\text{stochastic variation}
+\text{ context-dependent selective bias}
+\text{ endogenous change of the selective environment}.
}
\]

Natural selection can bias population change toward variants with greater relative reproductive success in the current selective environment. But fitness can depend on environment, density, frequency, interacting species, and genetic background; its ranking can change sign when context changes. Drift, mutation, migration, and stochasticity remain possible.

A schematic eco-evolutionary system

\[
\dot x=F(x,\theta),
\qquad
\dot\theta=G(x,\theta)
\]

is sufficient motivation: ecological state changes selective conditions, while changing traits/strategies modify ecological interactions and future response structure.

Use **complex adaptive system** as the ecological framing. Do not use “chaos” as a synonym for complexity unless a specific mathematical chaotic property is proved.

## State definition

The canonical world-level definition remains

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}.
}
\]

Equivalently, define a quotient map

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V}.
\]

Two worlds count as the same scientific state when every difference erased by the quotient is irrelevant to the declared scientific responsibility.

The finite joint state \(J\) is the proved construction realizing this idea under explicit finite assumptions.

## Access versus responsibility

Keep distinct

\[
O_V:\Omega\to Y_V
\]

for scientific access and

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T)
\]

for responsibility: future operations, inherited meanings, retained mechanisms, evidence conditions, and report target.

Changing \(V\) changes which distinctions are scientifically accessible. It does **not** change the underlying world by description alone.

This distinction should now be connected explicitly to law validity.

## Snapshot sufficiency

Let \(\pi_t(\omega)=x_t\) be the present-snapshot projection. A snapshot is sufficient exactly when the required state factors through \(\pi_t\):

\[
\boxed{
\pi_t(\omega)=\pi_t(\omega')
\Rightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

This remains a **factorization criterion, not a novelty theorem**.

The temporally thick claim should be worded precisely:

> a present scientific state need not literally store the entire past or actual future, but its equivalence classes can depend on history and on counterfactual future responses.

## Hidden ecological structure

The manuscript should make explicit that a scientifically relevant state component need not be directly visible.

A latent distinction earns state status only if forgetting it changes a declared future response, inherited meaning, or target. This is not permission to add arbitrary hidden variables.

### `microdonta` bridge — illustrative, not proof foundation

Use three existing `microdonta` results as compact examples:

1. **Basin/path hysteresis:** after degradation and restoration to the same patch environment, different histories/basin positions can yield different long-run states.
2. **Latent causal switch degeneracy:** multiple mechanism configurations can remain compatible with the same observed ecological pattern.
3. **Channel-identifiability symmetry:** if \(W=FE\), net-only observation \(O=\Phi(W)\) cannot distinguish an \(F\)-channel change from the corresponding \(E\)-channel change.

These show three kinds of “invisible” ecological structure — basin state, causal mechanism, and structurally unidentifiable channel — without claiming that all ecological hidden variables have this form.

## Companion hierarchy

### Structural insufficiency

1. **CCOC — future/composition:** a widened future grammar can expose dormant distinctions.
2. **MLTR — inherited history/semantics:** structural replacement can invalidate carried state meaning.
3. **MRM — mechanism response:** retained mechanisms can agree now and disagree under a required future action.

### Downstream evidence licensing

4. **CED — evidence/reportability:** available records may fail to identify distinctions the required state needs.

Preserve

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

## Ecological laws as quotient laws

This is now a central consequence rather than a late metaphor.

Let the response required by contract \(\mathcal C\) be

\[
R_{\mathcal C}:\Omega\to Z_{\mathcal C}.
\]

A coarse law on the state quotient exists only if there is

\[
L_{\mathcal C,V}:Q_{\mathcal C,V}\to Z_{\mathcal C}
\]

such that

\[
\boxed{
R_{\mathcal C}=L_{\mathcal C,V}\circ q_{\mathcal C,V}.
}
\]

This factorization formalizes the claim that many ecological regularities are **effective laws on adequate quotients**.

When observation, intervention, history, mechanism family, or scientific responsibility changes, the underlying world need not change but the old quotient can become inadequate. The old coarse law can then fail to transfer because it is no longer well-defined on the newly required state fibers.

Use the phrase **domain-relative law validity**, not observer-relative truth.

## Finite mathematical hierarchy

### Gate A — carrier feasibility

Use J3/J6 to ask whether the declared obligations share an admissible finite world set.

### Gate B — least-information state

On an admissible finite carrier, baseline \(B\), and implemented refinement closures,

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the unique coarsest common fixed point under J1's assumptions.

For finite world \(u\),

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

**Manuscript role:** J1 tells the reader what one least-information finite CREST state is. Generic closure/fixed-point machinery is classical.

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

The qualitative theorem gives the direction: capability can enlarge the viable carrier while stronger future responsibility refines the required state and can defeat fixed monitoring.

### Cross-gate scaling — mathematical headline

For every integer \(m\ge1\), the connected capability–resolution family satisfies

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m\text{ bits}.
}
\]

On the same retained present slice:

- required exact state: \(1\to2^m\) classes;
- monitoring-resolution debt: \(0\to m\) bits;
- full-state licensing: yes \(\to\) no;
- constant coarse target reportability: yes \(\to\) yes.

The no-bound corollary remains

\[
\boxed{
\text{no finite function of }\Delta|K^*|\text{ alone universally upper-bounds }\Delta K_{U_0}.
}
\]

This is the theorem-level anchor for the broader philosophical idea that **representational change can be radically larger than the physical/capability change that makes a distinction relevant**.

## Stability hierarchy

The manuscript should now distinguish four questions, while making clear that only the first three are standard labels and the fourth is a law-level consequence rather than a new theorem family.

1. **Dynamical stability:** persistence/recovery/basin behavior of ecological trajectories.
2. **Evolutionary stability:** invasion/stability under a declared evolutionary model.
3. **Representational stability:** persistence of an adequate state quotient under changed scientific responsibility.
4. **Law portability:** whether the same quotient-level rule remains well-defined after the required quotient changes.

The action-expansion and capability–resolution results prove strict failures of representational stability without requiring prior physical ecosystem change. They do not prove a general mathematical relation among dynamical and evolutionary stability.

Law portability follows from the quotient factorization question; do not name a new theorem unless a genuinely new bound or iff-condition is proved.

## Prior-art firewall

Explicitly concede:

- dynamic ecosystem identity and resilience accounts;
- causal states / Predictive State Representations;
- POMDP and task-specific state reduction;
- causal/state abstraction;
- state/action abstraction coupling;
- purpose-relative model adequacy;
- adaptive monitoring and target-oriented experimental design;
- complex adaptive ecosystems and eco-evolutionary feedback;
- effective/coarse-grained law traditions.

Do not claim novelty for any one of those ingredients.

CREST's defended contribution remains the ecology-specific typed architecture plus the finite cross-gate scaling conjunction.

## Revised manuscript order

```text
1. Why state and law are compression problems in ecology
   - complex adaptive / eco-evolutionary motivation
   - local selection bias without global teleology
   - complete world-history as mathematical object, with physics firewall

2. Scientific access, state quotient, and snapshot sufficiency
   - O_V versus C
   - q_{C,V}
   - temporally thick present state

3. Why present sameness can fail
   - CCOC: future
   - MLTR: history / inherited meaning
   - MRM: mechanism
   - compact microdonta examples: basin / latent mechanism / observation symmetry

4. Finite CREST answer
   - carrier feasibility
   - J1 least-information state
   - evidence licensing
   - qualitative action expansion
   - capability–resolution divergence / no-bound result

5. Ecological laws and stability
   - R = L ∘ q
   - quotient-level effective laws
   - dynamical / evolutionary / representational stability
   - law portability as a consequence of quotient change

6. Position relative to existing theories
   - ecosystem identity / resilience
   - predictive states / POMDP / causal abstraction
   - state/action abstraction
   - adequacy-for-purpose / effective-law traditions

7. Limits
   - no metaphysical block-universe commitment
   - no determinism claim
   - no global fitness arrow
   - no generic mathematical chaos claim
   - finite exact theorem boundary

8. Conclusion
   - world → quotient state → quotient law
   - capability can destabilize representation before changing nature
```

CED should remain downstream evidence licensing. Real-data applications remain optional illustrations, not proof requirements.

## Abstract direction

Do **not** rewrite the current verified abstract until the full manuscript integration is complete. The next abstract should preserve the mathematical headline while adding only one sentence of the world→state→law idea. Avoid spending abstract space on block-universe metaphysics or detailed `microdonta` examples.

## Key sentences to preserve

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to what the state is required to support.**

> **The same ecological world can support different valid coarse laws under different scientific quotients without making ecological truth observer-relative.**

> **Natural selection supplies context-dependent directional bias, not a universal trajectory toward one global fitness maximum.**

## Revision firewall

When integrating into the long manuscript:

- preserve verified finite theorem statements;
- keep J1 foundational, not novelty for fixed-point theory;
- keep the connected capability–resolution/no-bound result as mathematical headline;
- do not turn the complete-world representation into block-universe or determinism claims;
- do not describe quantum physics as simply random;
- do not use mathematical chaos as a synonym for ecological complexity;
- do not claim universal fitness maximization or evolutionary progress;
- use `microdonta` only as an ecology-grounded witness source, not CREST's proof foundation;
- do not present CED as a fourth ontic source of ecological difference;
- do not claim the structural obstructions are exhaustive;
- do not require empirical data to establish the finite theorem;
- do not add another theorem family unless it strengthens the same carrier/state/evidence/target chain.
