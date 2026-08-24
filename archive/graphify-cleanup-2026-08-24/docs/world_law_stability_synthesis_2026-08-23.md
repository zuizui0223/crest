# CREST world–law–stability synthesis — 2026-08-23

> **Status:** canonical philosophical synthesis above the finite theorem spine. This document does **not** add a new theorem family. It explains how the existing CREST state/evidence mathematics connects to complex adaptive ecology, hidden causal structure, observation, effective laws, and multiple notions of stability.

## 1. The higher-level question

The finite CREST program asks when a declared scientific contract admits a least-information ecological state and when evidence identifies it. The broader philosophical question is one level higher:

> **How can ecological states and ecological laws exist at all in a temporally extended, partially observed, self-modifying adaptive world?**

The proposed answer is not that nature supplies one privileged snapshot partition. It is:

\[
\boxed{
\text{state and law are well-defined only after declaring which world-differences may be erased.}
}
\]

CREST therefore begins from ecological worlds, then derives state representations and quotient-level laws.

---

## 2. A world may be represented as a complete history without assuming a block universe

Let

\[
\Omega
\]

be a set of admissible ecological world-histories. A convenient trajectory notation is

\[
\omega=(x_s)_{s\in\mathbb T},
\]

where \(x_s\) is the ecological configuration at time \(s\). Relative to a present time \(t\), the same object can be written schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

with relevant history \(h_t\), current configuration \(x_t\), and future-response structure \(\mathcal F_t\).

This is a **mathematical representation choice**, not a metaphysical commitment that future events already exist. Eternalism/block-universe views and causal determinism are distinct claims. CREST requires neither.

- Under a deterministic model, initial conditions plus dynamics may select one admissible trajectory.
- Under a stochastic model, the theory may instead place a probability measure
  \[
  \mu\in\mathcal P(\Omega)
  \]
  over possible world-histories or use conditional future distributions.
- Under either interpretation, a scientific state can ask which differences among possible histories and responses remain relevant now.

Thus CREST preserves the useful intuition that a present ecological state can be **temporally thick** without claiming backward causation or a physically predetermined future.

---

## 3. Ecology adds local adaptive direction without a universal evolutionary destination

Ecological evolution is neither a pure random walk nor a universal ascent to one global fitness maximum.

A schematic decomposition is

\[
\boxed{
\text{variation / mutation / drift / migration}
+\text{ context-dependent differential reproduction}.
}
\]

Natural selection biases change toward variants with greater relative reproductive success **in the current selective environment**, but the ranking itself can depend on environment, density, frequency, interacting species, and genetic background.

Write

\[
w_i=w_i(x,\theta,p,t),
\]

where ecological configuration \(x\), trait configuration \(\theta\), population frequencies \(p\), and time can all alter relative fitness. Then the locally favored direction can change sign as the ecological context changes.

This gives the ecological world a distinctive structure:

\[
\boxed{
\text{stochastic variation}
+\text{ local adaptive bias}
+\text{ endogenous change of the selective environment}.
}
\]

The final term matters most for CREST. Organisms do not merely move through a fixed fitness landscape; their abundance, traits, interactions, and environmental modification can alter the response structure that later determines what is favored.

A generic eco-evolutionary schematic is

\[
\dot x=F(x,\theta),
\qquad
\dot\theta=G(x,\theta),
\]

so changes in \(x\) alter the selective context for \(\theta\), while changes in \(\theta\) alter the ecological dynamics of \(x\). This motivates calling ecosystems **complex adaptive systems**, but CREST does not assume mathematical chaos. Chaos is a special dynamical property; nonlinearity, historical dependence, multiple outcomes, feedback, and self-organization are enough for the philosophical argument.

---

## 4. A present ecological state is a quotient of a temporally extended world

Let the present-snapshot projection be

\[
\pi_t:\Omega\to X_t,
\qquad
\pi_t(\omega)=x_t.
\]

CREST does not identify \(x_t\) with the scientific state by definition. Instead, under observation/intervention context \(V\) and scientific contract \(\mathcal C\), define

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V}.
\]

Then

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=q_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}.
}
\]

Two worlds are the same scientific state only when every difference erased by the quotient is irrelevant to the work assigned to the state.

A present snapshot is sufficient exactly when the required state factors through \(\pi_t\):

\[
\pi_t(\omega)=\pi_t(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
\]

Therefore the statement that a present ecological state can “contain” past and future should be read precisely:

> the state need not literally store the complete past or actual future, but its equivalence classes can depend on history and on counterfactual future responses.

---

## 5. Observation changes access to the same world, not the world itself

A scientific setup accesses the world through an observation/intervention map

\[
O_V:\Omega\to Y_V.
\]

Different contexts \(V_1,V_2\) can retain different distinctions:

\[
O_{V_1}(\omega)=O_{V_1}(\omega')
\quad\text{while}\quad
O_{V_2}(\omega)\neq O_{V_2}(\omega').
\]

This is the mathematical version of changing observational viewpoint.

The world has not changed. What changes is the partition of \(\Omega\) available to science.

This yields three separable objects:

1. **world difference** — two possible worlds are physically/causally distinct;
2. **required state difference** — the scientific task requires that distinction;
3. **observable difference** — the current observation/intervention setup can actually distinguish it.

Hence CREST's central separation:

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

---

## 6. Hidden ecological concepts are legitimate state structure when they change responses

A quantity need not be directly visible to be scientifically real or state-relevant. But CREST does not license arbitrary hidden variables. A latent distinction earns a place in the state only when forgetting it changes a declared response, inherited meaning, or target.

The `microdonta` program already supplies three exact bridges.

### 6.1 Hidden basin position and history

The patch-feedback hysteresis model

\[
\dot x=x(1-x)[\eta A^\alpha x^h-c]
\]

has, for sufficiently large patch area, two stable boundary states separated by an unstable threshold. After degradation and restoration to the **same** patch area, the long-run state can differ because the system occupies a different basin.

Thus

\[
\boxed{
\text{same restored present environment}
\not\Rightarrow
\text{same future ecological state}.
}
\]

The missing information is not necessarily a visible present variable; it can be basin position or history-dependent latent state.

### 6.2 Hidden causal programs

The latent causal generative model keeps multiple mechanism-switch configurations

\[
s\in\{0,1\}^K
\]

compatible with the same observed ecological pattern. Observed co-occurrence does not identify which causal mechanism is active.

This supplies an ecology-facing instance of the MRM/CED distinction: multiple latent causal worlds can remain observationally compatible until a discriminating observation or intervention is added.

### 6.3 Structural observational symmetry

For positive channels

\[
W(z)=F(z)E(z),
\]

the `microdonta` channel-identifiability theorem proves that net-only observations

\[
O=\Phi(W)
\]

cannot distinguish a multiplicative change in \(F\) from the same multiplicative change in \(E\). This remains true even with complete knowledge of every thresholded geometry generated only from \(W\).

Thus a hidden causal distinction can be **structurally unidentifiable under an observation family**, not merely hard to estimate because sample size is small.

This is exactly the kind of “invisible” ecological structure CREST needs: latent distinctions whose relevance and observability can be stated mathematically rather than inferred from metaphor.

---

## 7. Ecological laws are effective laws of quotients

Let a scientific response required by contract \(\mathcal C\) be

\[
R_{\mathcal C}:\Omega\to Z_{\mathcal C}.
\]

A coarse ecological law on state space \(Q_{\mathcal C,V}\) exists only if there is some

\[
L_{\mathcal C,V}:Q_{\mathcal C,V}\to Z_{\mathcal C}
\]

such that

\[
\boxed{
R_{\mathcal C}=L_{\mathcal C,V}\circ q_{\mathcal C,V}.
}
\]

This factorization says exactly when a rule is well-defined on a coarse state representation.

Now change the observational/intervention context or scientific responsibility. The underlying world may be unchanged, but the old quotient can cease to preserve a distinction required by the new response. Then the old law need not factor through the new scientific state.

Therefore:

\[
\boxed{
\text{same world}
+\text{ different scientific projection/responsibility}
\Rightarrow
\text{different domain on which a coarse law is valid}.
}
\]

This is **not** observer-relative truth. It is domain-relative law validity. The full-world response structure constrains whether a proposed quotient law is well-defined.

An ecological rule can therefore be true on one quotient and fail to transfer to another without having been false in its original domain.

---

## 8. Four stability questions should be distinguished

The enlarged synthesis separates four kinds of stability.

### 8.1 Dynamical stability

Does the ecological trajectory resist perturbation, recover, remain in a basin, or preserve a regime?

### 8.2 Evolutionary stability

Does a strategy/trait resist invasion or remain favored under the declared evolutionary model?

### 8.3 Representational stability

Does the same state quotient remain adequate when future actions, mechanisms, inherited meanings, observation channels, or targets change?

### 8.4 Law portability

Does the same quotient-level rule remain well-defined under the new state quotient and scientific responsibility?

The fourth is not introduced as a new theorem family. It is the law-level consequence of representational stability:

\[
R=L\circ q
\]

can cease to hold for the newly required quotient even when the underlying world has not changed physically.

This gives CREST a precise answer to the intuition that “the same ecological world obeys one rule from one viewpoint but not from another”: the full world is not changing laws; rather, a coarse rule loses its valid quotient domain when the projection or responsibility changes.

---

## 9. Capability can destabilize representation before it changes nature

The current finite CREST theorem makes this point quantitatively sharp.

For every \(m\ge1\), one newly admitted action can realize

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m,
}
\]

with present required state

\[
1\to2^m
\]

classes, fixed-monitoring debt

\[
0\to m
\]

bits, full-state licensing

\[
\text{yes}\to\text{no},
\]

and coarse target reportability

\[
\text{yes}\to\text{yes}.
\]

Thus a tiny change in what can be done can produce an arbitrarily larger change in what must be represented and monitored.

The ecosystem does not have to change physically first. The changed intervention repertoire alters which counterfactual response distinctions the present state must preserve.

This is a theorem about **representational instability**, not backward causation.

---

## 10. The combined philosophical story

The program can now be read in one line:

```text
possible ecological world-histories Ω
        ↓
self-modifying eco-evolutionary response structure
        ↓
partial scientific access O_V
        ↓
contract-relative state quotient q_{C,V}
        ↓
quotient-level effective law L_{C,V}
        ↓
carrier / state / evidence / target separation
        ↓
multiple notions of stability and law portability
```

The corresponding central thesis is:

> **An ecosystem is a temporally extended, partially observed, self-modifying adaptive world. An ecological state is a scientifically licensed quotient of such worlds, and an ecological law is an effective law on that quotient. Changes in history, possible futures, mechanisms, observations, interventions, or scientific responsibility can therefore change which state distinctions and which quotient-level laws remain adequate without changing the underlying world by description alone.**

---

## 11. Physical and biological firewalls

Do **not** infer from this synthesis that:

- special or general relativity proves that the actual future is fixed;
- eternalism/block-universe metaphysics is required by CREST;
- quantum mechanics is simply “all random” or simply deterministic independent of interpretation/model;
- future events literally cause present ecological states;
- natural selection creates one universal arrow of increasing global fitness;
- every ecosystem is mathematically chaotic;
- every latent variable deserves state status;
- changing scientific viewpoint changes the underlying ecological truth.

The safe claims are narrower:

- complete trajectories can be used as mathematical world objects without metaphysical commitment;
- stochastic and deterministic world models can both be represented;
- selection gives context-dependent differential reproduction while drift, mutation, migration, and stochasticity remain possible;
- ecosystems can modify the conditions that determine later ecological and evolutionary responses;
- observation/intervention context changes scientific access to the same world;
- a coarse state or law is valid only while erased distinctions remain irrelevant to its declared responsibility.

---

## 12. Relation to the existing CREST spine

No existing theorem needs to be replaced.

- **CCOC** supplies future/composition insufficiency.
- **MLTR** supplies history/inherited-semantic insufficiency.
- **MRM** supplies latent mechanism-response insufficiency.
- **J3/J6** determine admissible finite carriers.
- **J1** gives the unique least-information finite state on an admissible carrier.
- **CED** licenses what evidence identifies and what target can still be reported.
- **Capability–resolution divergence** shows that viability gain and representational burden can separate without a carrier-gain-only bound.
- **microdonta** supplies ecology-grounded witnesses for basin memory, latent causal degeneracy, and structural observational symmetry; it is not a proof foundation for the general CREST theorem.

The next development task is manuscript integration and conceptual compression, not another theorem family.
