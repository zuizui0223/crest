# What Counts as the Same Ecological State?
## A Contract-Relative Theory of Temporally Extended Ecological States

## Abstract

Ecologists routinely describe ecosystems by present states, yet a present snapshot can conceal differences in history, latent mechanism, and future response that matter for prediction or intervention. We develop Contract-Relative Ecological State Theory (CREST), in which two ecological worlds count as the same state only when the distinctions between them are irrelevant to a declared scientific responsibility. This makes ecological state a scientifically licensed quotient of temporally extended ecological worlds rather than an intrinsic label attached to a momentary snapshot. CREST separates four questions that are often conflated: which ecological worlds are jointly admissible, which distinctions the scientific task requires, which of those distinctions the available evidence identifies, and which target can nevertheless be reported. On a declared finite carrier, the required state is the unique coarsest partition satisfying the implemented future, inherited-semantic, mechanism-response, and reporting obligations. The main quantitative result shows that for every integer \(m\ge1\), adding a single controllable action can increase the viable carrier by exactly one world while forcing a retained present slice to refine from one state to \(2^m\) states. Under unchanged monitoring, the resulting resolution deficit is exactly \(m\) bits, although a coarse target can remain reportable. CREST therefore distinguishes physical, evidential, and representational change and provides a formal basis for asking when ecological differences require different states.

**Keywords:** philosophy of ecology; ecological state; scientific representation; temporal extension; causal abstraction; model adequacy

## 1. The ecological state problem

Ecologists routinely speak as if an ecosystem has a state now. A lake is eutrophic or clear-water, a population is persistent or declining, a community is pollination-maintained or pollination-limited, and a landscape is connected or fragmented. Such descriptions are indispensable because they group many physically different configurations under one scientifically useful label. The difficult question is not whether ecology simplifies. It is **when different ecological worlds should count as the same ecological state**.

That question is easy to hide when state is identified with a present measurement vector. Suppose two forests have the same biomass, two lakes have the same nutrient concentration, or two communities have the same species richness. If the scientific task is purely descriptive, those equalities may be sufficient. But if the task includes prediction, intervention, comparison across structural change, or inference under mechanism uncertainty, equal present descriptors need not imply equal scientific states. The two systems may have different histories, occupy different basins, support different latent mechanisms, or respond differently to the same future action.

CREST begins from this mismatch. A state is not defined by asking which variables are convenient to record and then treating their joint values as the system. Instead, the state question is posed relationally: **which possible ecological worlds may legitimately be treated as interchangeable for the scientific work at hand?** The answer depends on what the representation is required to support, but it is not arbitrary. Ecological dynamics, intervention responses, inherited meanings, and evidence constrain whether a proposed merge is admissible.

This problem is especially sharp in ecology because ecological response structure is context dependent. Ecosystems have long been described as complex adaptive systems in which higher-level patterns emerge from localized interactions, feedback, historical dependence, selection, and self-organization (Levin 1998). Eco-evolutionary theory adds a reciprocal relation: ecological interactions can alter selection, while evolutionary change can alter ecological interactions and ecosystem function (Post and Palkovacs 2009; Schoener 2011). The point required here is modest. CREST does not assume that ecosystems are generically mathematically chaotic or that evolution follows one universal direction. It requires only that the responses relevant to a scientific task can depend on history, interaction context, latent mechanism, or future operations.

A schematic eco-evolutionary system can be written

\[
\dot x=F(x,\theta),
\qquad
\dot\theta=G(x,\theta),
\]

where \(x\) represents ecological configuration and \(\theta\) traits or strategies. Changes in \(x\) can alter the selective context for \(\theta\), while changes in \(\theta\) can alter the ecological dynamics of \(x\). Variation, mutation, migration, drift, and demographic stochasticity can generate alternatives; natural selection biases differential reproduction relative to the current selective environment. Because the relevant fitness ordering itself can depend on density, frequency, interacting species, abiotic conditions, and genetic background, the response structure that an adequate ecological state must summarize can change with context.

Rather than assuming that state is the snapshot \(x_t\), CREST therefore begins with a set \(\Omega\) of admissible ecological worlds. A world can be represented as a trajectory

\[
\omega=(x_s)_{s\in\mathbb T},
\]

or, relative to a present time \(t\), schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) the present configuration, and \(\mathcal F_t\) the future-response structure under interactions or interventions relevant to the problem. In a stochastic model, \(\mathcal F_t\) may be a conditional distribution over future trajectories rather than one predetermined path.

Using complete trajectories as mathematical world objects does not commit CREST to a block-universe metaphysics or to physical determinism. Eternalism and determinism are distinct claims, and CREST requires neither. The role of a temporally extended world is representational: two present snapshots can be numerically identical while belonging to different histories or supporting different counterfactual responses, and those differences may or may not matter to the scientific task.

The central proposal is therefore

\[
\boxed{
\text{an ecological state is a scientifically licensed quotient of temporally extended ecological worlds.}
}
\]

Equivalently, it is a compression of possible ecological worlds, but the operational question is clearer than the metaphor of forgetting: **when may two different worlds be treated as the same state?** CREST answers by making the relevant scientific responsibility explicit and asking whether a proposed state merge preserves what that responsibility requires.

## 2. Contract-relative ecological state

### 2.1 Scientific access and scientific responsibility

A scientist does not observe \(\omega\) directly. A measurement and intervention context \(V\) determines which distinctions are scientifically accessible:

\[
O_V:\Omega\to Y_V.
\]

Different measurements can preserve different distinctions among the same underlying worlds. This does not make ecological truth observer-relative. The world constrains every observation and intervention; what changes is the scientific access to the world.

CREST separates this access from the scientific responsibility assigned to a state representation. Write the contract schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where \(\Gamma\) specifies future interactions or operations that the state must support, \(\mathcal H\) specifies inherited meanings or historical distinctions that must remain coherent, \(\Theta\) specifies retained mechanism or response alternatives, \(D\) specifies the evidence architecture, and \(T\) specifies the requested report or decision target. The components are not claimed to be exhaustive or uniquely supplied by nature. They are an explicit statement of the work assigned to the representation.

The corresponding state relation is

\[
\omega\sim_{\mathcal C,V}\omega'
\]

when the two worlds can be treated as interchangeable for the scientific work specified by \((\mathcal C,V)\). Let

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V}
\]

be the quotient map. Then

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}
=q_{\mathcal C,V}(\omega).
}
\]

Contract-relativity is therefore not conventionalism. Scientists specify the responsibility, but ecological dynamics and evidence determine whether a proposed identification of worlds can satisfy it. A historical difference need not enter the state merely because it is historical. A latent mechanism need not enter the state merely because it exists. Such a difference requires a distinct state only when it changes a response, inherited meaning, or target that the declared task requires.

### 2.2 Snapshot sufficiency

Let the present-snapshot map be

\[
X:\Omega\to\mathcal X.
\]

A present snapshot is sufficient for the CREST state precisely when the required state factors through the snapshot:

\[
\boxed{
X(\omega)=X(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

This is a factorization criterion, not a claim that snapshots are generally inadequate. In many systems and for many purposes, current observables may be sufficient. CREST instead rejects the stronger assumption that a current descriptor is a state merely because it is current.

The criterion also clarifies what it means to call ecological state temporally extended. The state need not literally store a complete past or actual future. Its equivalence classes can nevertheless depend on history and on counterfactual response. Two worlds with the same present measurement can require different state labels if they respond differently to a future operation included in \(\Gamma\). Conversely, two visibly different configurations can legitimately share one scientific state if every difference between them is irrelevant to the declared task.

### 2.3 Ecological laws as quotient laws

The same state relation determines when a coarse ecological rule is well-defined. Let

\[
R_{\mathcal C}:\Omega\to Z_{\mathcal C}
\]

be the response that the contract requires. A rule on the coarse state space exists only if there is a map

\[
L_{\mathcal C,V}:Q_{\mathcal C,V}\to Z_{\mathcal C}
\]

such that

\[
\boxed{
R_{\mathcal C}=L_{\mathcal C,V}\circ q_{\mathcal C,V}.
}
\]

This condition says that worlds merged into one ecological state must agree on the response the coarse law is required to return. A coarse ecological law is therefore an effective law on an adequate quotient.

The claim is not that ecological truth changes with viewpoint. It is that a coarse rule has a domain of validity determined by the distinctions its state representation preserves. If a new future action, structural change, mechanism family, observation channel, or reporting responsibility separates worlds that the old state merged, then the old rule can cease to be adequate for the enlarged task without having been false in its original domain.

This gives CREST a direct connection between two problems often treated separately: what ecological state is, and why an ecological regularity transfers successfully across some contexts but not others. The portability question becomes: does the quotient on which the rule was defined remain adequate after the scientific responsibility changes?

## 3. Why equal present descriptions can require different states

CREST is supported by three structural obstruction families and one downstream evidence gate. These are not four equivalent definitions. CCOC, MLTR, and MRM describe three reasons a proposed present-state merge can fail. CED asks whether the evidence identifies the distinctions that are already required.

### 3.1 Future insufficiency

Two configurations can be equivalent under all currently legal futures and cease to be equivalent when the future repertoire is enlarged. CCOC formalizes this as a cross-grammar compression problem. Under a restricted future grammar, many micro-configurations can share one exact response class because no permitted action exposes their differences. Under an enlarged grammar, previously dormant differences can become individually addressable.

The ecological reading is

\[
\boxed{
\text{present functional equivalence}
\not\Rightarrow
\text{causal equivalence under an enlarged future}.
}
\]

This does not make the earlier state classification retrospectively false. The earlier state was adequate for a narrower future contract. Once the set of responses that the state must support changes, the equivalence relation itself can require refinement.

The important point is structural. Complexity need not arise because local rules become more complicated. Even systems with small local rule sets can require increasingly rich interface state when more external or future distinctions become operationally addressable. What matters is not only what the system is doing now, but which differences can become consequential under admitted futures.

### 3.2 Historical and semantic insufficiency

A second failure occurs when a state label is carried across structural change. After turnover, replacement, extinction, recolonization, or interaction rewiring, the same label can remain syntactically available while no longer grouping target configurations with the same legal actions or future responses.

MLTR fixes an inherited source classification and asks whether its operational meaning remains exact in a target system. When the carried partition fails, iterative refinement produces the coarsest source-relative repair: only those state splits forced by target output, legal-action, or successor differences are added, while inherited mergers that remain valid are preserved.

The ecological reading is

\[
\boxed{
\text{same present descriptor}
\not\Rightarrow
\text{same inherited operational state after structural change}.
}
\]

History therefore becomes state-relevant conditionally, not automatically. If two histories lead to present worlds that remain indistinguishable for all required responses and inherited meanings, the histories need not define different states. If the route into the present changes what the state is required to mean or predict, then the historical distinction must be represented.

This is compatible with familiar ecological phenomena such as hysteresis and alternative stable regimes without reducing CREST to a theory of hysteresis. In a positive-feedback system, restoring the same external environment need not restore the same long-run regime if histories place the system on different sides of a basin boundary. CREST extracts the representational consequence: equal current environmental descriptors need not imply equal scientific states when their future-response classes differ.

### 3.3 Mechanistic insufficiency

A third failure occurs when the same visible present state is compatible with several retained causal mechanisms. Suppose candidate mechanisms agree on current behavior but disagree under a future intervention that the scientific task requires. One deterministic state-level forecast cannot then be uniformly justified across the retained mechanism family.

MRM therefore groups mechanisms by response type rather than by raw identity. Mechanisms that induce the same declared response behavior can remain in one state. Mechanisms that disagree on a required future response cannot be merged if a single deterministic prediction is required.

The ecological reading is

\[
\boxed{
\text{same visible present state}
\not\Rightarrow
\text{same required state under response-relevant mechanism uncertainty}.
}
\]

Again, latent mechanism is not automatically state. It becomes state-relevant only when the task is sensitive to the response difference.

The distinction between relevance and observability matters. Two mechanism states can be response-relevant yet structurally indistinguishable under the current measurement family. For positive causal channels \(F(z)\) and \(E(z)\) with net performance \(W(z)=F(z)E(z)\), the transformations

\[
(F,E)\mapsto(aF,E)
\qquad\text{and}\qquad
(F,E)\mapsto(F,aE)
\]

produce the same \(W\) for any positive multiplier \(a(z)\). Any observation depending only on \(W\) therefore cannot identify which channel changed. If a future action acts specifically on one channel, the two latent worlds can nevertheless have different successors and require different scientific states. More precise measurement of the same aggregate channel cannot solve that structural non-identifiability.

### 3.4 Evidence licensing

A distinction can be required by the scientific task without being identified by the available evidence. Camera records, demographic surveys, environmental DNA, or experiments can leave multiple target-relevant worlds compatible with one record.

CED represents the declared observation architecture as an evidence partition. A deterministic target report is licensed only when the target is constant across the worlds compatible with the evidence. If compatible worlds imply different target values, an ambiguity-explicit output is required.

This yields the central separation

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}
}
\]

in general. A scientific task can require a finer ecological state than current observations identify. Yet a coarse target can remain deterministically reportable if it is constant across the unresolved evidence class. CREST therefore distinguishes representational adequacy from evidential identification rather than treating a refined theoretical state as if it had automatically been observed.

## 4. The finite mathematical answer

The world-level interpretation is broader than the proved mathematics. The current formal results concern finite latent-world carriers and exact finite transitions. Their purpose is to show that the state-sameness problem can be made mathematically precise under explicit assumptions.

### 4.1 Gate A: admissible carrier

The conditional state theorem presupposes that the relevant obligations can be expressed on a common finite carrier. This condition cannot be hidden inside the notation. CREST uses two carrier constructions corresponding to different action contracts.

For universal-action responsibility, the admissible set descends to a greatest synchronized transition-closed carrier \(U^*\). For a controlled contract, all uncontrollable moves must remain safe while at least one admissible control is available; the corresponding construction yields a greatest robustly controlled-invariant carrier \(K^*\).

If the common carrier is empty or fails a required coverage condition, there is no fully adequate joint finite state under that synchronization. Refining a partition cannot repair a contradiction in the world set itself. Carrier feasibility therefore precedes state construction:

\[
\text{admissible carrier}
\longrightarrow
\text{required state}
\longrightarrow
\text{evidence licensing}.
\]

### 4.2 Gate B: least-information adequate state

Conditional on an admissible finite carrier \(U\), let \(B\) be a baseline partition containing distinctions that the analysis is committed to preserving. The implemented responsibilities are represented by refinement closures

\[
C_\Gamma,\qquad
C_{\mathcal H},\qquad
C_\Theta,\qquad
C_{D,T}.
\]

Under the stated assumptions, their common closure above the baseline is

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B).
}
\]

The J1 result states that \(J\) is the unique coarsest, least-information partition satisfying the implemented finite requirements. For \(u\in U\),

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

This gives a finite realization of the world-level state relation. It does not yield one intrinsic state partition of nature. Different futures, inherited meanings, mechanism families, evidence contracts, targets, or admissible carriers can yield different adequate states.

The generic lattice and closure-operator machinery is classical. CREST does not claim novelty for fixed-point theory or partition refinement. The role of J1 is foundational: it specifies when a least-information finite ecological state is well-defined within the declared architecture.

A practical subtlety is that the obligations need not commute. A distinction introduced by one refinement can expose a new distinction required by another. Fair repeated refinement converges to the common fixed point on the finite carrier, although intermediate partitions and the number of passes can depend on update order.

### 4.3 Gate C: evidence identification

Let \(E_D\) denote the reliability-qualified evidence partition: worlds in one block remain observationally compatible under the declared experiment, detection, failure, and risk assumptions. Full deterministic state reporting is licensed exactly when

\[
\boxed{
J\preceq E_D.
}
\]

If this relation holds, every evidence class lies within one required state block. If it fails, \(J\) still specifies the resolution that the task requires, but the current evidence does not identify one unique state. The sharp report is then the set of required-state blocks compatible with the evidence.

A requested target can nevertheless remain deterministic if it factors through the evidence partition. This makes required state, identified state, and reportable target operationally distinct rather than merely terminological.

### 4.4 Capability expansion and state refinement

Let controllable action repertoires satisfy

\[
A_c\subseteq A_c',
\]

with old and uncontrollable dynamics preserved. The greatest controlled carrier is monotone:

\[
\boxed{K^*(A_c)\subseteq K^*(A_c').}
\]

On a retained carrier, if the future responsibility \(\Gamma'\) strengthens \(\Gamma\), the least adequate state can only become finer:

\[
\boxed{J_\Gamma\preceq J_{\Gamma'}.}
\]

With fixed evidence, identifying that finer state can only be at least as demanding. A strict finite witness realizes all three changes simultaneously: an added action makes an additional world viable, forces a finer required state, makes unchanged monitoring cease to identify the full state, yet leaves a coarse target reportable.

This gives a precise form to a central representational claim: a new possible intervention can change which distinctions must be represented before the intervention is executed and before the physical ecosystem changes. There is no backward causation. The scientific responsibility has changed because a new counterfactual response is now part of what the present state must support.

### 4.5 Capability-resolution divergence

The main quantitative theorem asks how large the representational consequence can be relative to the change in viability.

For every integer \(m\ge1\), let the retained present slice contain one world \(p_{x,0}\) for every binary address \(x\in\{0,1\}^m\). The old action set contains only `hold`. The expanded set adds one action `probe`. The output alphabet is fixed:

\[
\{\texttt{neutral},\texttt{bit0},\texttt{bit1},\texttt{done}\}.
\]

Repeated `probe` exposes one binary coordinate at a time through a chain of readout states. The readout paths enter one additional compatible world that lacks a safe old control but is rescued by the same new `probe` action. Thus state refinement and viability expansion occur in one connected finite response graph.

The controlled carrier increases by exactly one world:

\[
\boxed{|K_m^{*+}|-|K_m^{*-}|=1.}
\]

Under `hold` alone, every present address world has the same output and self-loop response, so the least exact state has one present class. After `probe` is admitted, any two distinct addresses differ at some first bit, and a finite repeated-probe word exposes that difference. Therefore

\[
|J_m^-\restriction_{U_0}|=1,
\qquad
|J_m^+\restriction_{U_0}|=2^m.
\]

Define present-slice state complexity as

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|.
\]

Then

\[
\boxed{\Delta K_{U_0}=m\text{ bits}}
\]

while viability gain remains one world.

Now hold the evidence on \(U_0\) fixed at one record class. Before expansion it identifies the single required state class. After expansion it merges \(2^m\) required classes, so the minimum evidence refinement needed for full-state identification carries exactly \(m\) additional bits on the retained slice. Full-state licensing changes from yes to no. Yet any target constant on \(U_0\) remains reportable before and after.

Hence for arbitrary finite \(m\), one fixed-size capability expansion realizes

\[
\boxed{
\Delta|K^*|=1,
\quad
\Delta K_{U_0}=m,
\quad
D_{U_0}:0\to m,
\quad
\text{full state: yes}\to\text{no},
\quad
\text{target: yes}\to\text{yes}.
}
\]

A direct corollary is that no universal finite function depending only on carrier-size gain can upper-bound the representational burden:

\[
\boxed{
\text{there is no finite }f\text{ such that }
\Delta K_{U_0}\le f(\Delta|K^*|)
\text{ for all such contracts.}
}
\]

The theorem does not claim that ecological management interventions generically produce exponential state growth. It proves an existence result: without additional structural assumptions, a small capability gain does not by itself bound the state resolution that an adequate representation may require.

### 4.6 Monitoring-resolution debt

For fixed evidence partition \(E\) and required state partition \(J\), the coarsest refinement that preserves the existing evidence distinctions while identifying \(J\) is

\[
E\vee J.
\]

Define finite monitoring-resolution debt as

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

The common-refinement calculation is classical. Its role in CREST is to keep three objects separate: changed scientific responsibility, required state, and unchanged evidence. In the capability-resolution family, the debt rises by exactly \(m\) bits while carrier gain remains one world.

This debt should not be interpreted automatically as “collect more samples.” Some deficits are structural rather than quantitative. If the current measurement map collapses two response-relevant causal channels by symmetry, repeated measurement of the same aggregate variable cannot distinguish them. Repair requires a different measurement channel, not only greater replication.

## 5. Ecological consequences

### 5.1 Functional equivalence is responsibility-relative

Ecology frequently groups systems by function: pollination maintained, nutrient cycling intact, predator control present, biomass stable. CREST does not reject functional states. It identifies the condition under which they are legitimate. Two systems count as the same functional state when the differences between them do not change any response, inherited meaning, or target assigned to that state.

The consequence is

\[
\boxed{
\text{current functional equivalence}
\not\Rightarrow
\text{equivalence under every possible future responsibility}.
}
\]

A functional state can therefore be perfectly adequate for one task and inadequate for another. This is not a defect of coarse graining. It is a reminder that coarse graining has a domain.

### 5.2 History matters conditionally

Historical contingency is familiar in ecology, but CREST gives it a state criterion. A historical difference requires distinct present states exactly when collapsing that difference would merge worlds that disagree on a response or inherited meaning the task requires.

Thus CREST rejects both extremes. It does not assume that history is irrelevant once present variables are measured, and it does not require every historical detail to be stored in the state. The relevant question is whether the historical distinction changes the scientific equivalence relation.

### 5.3 Latent mechanisms matter conditionally

The same logic applies to hidden mechanisms. A causal difference can be real while remaining irrelevant to the state if all mechanisms agree on the declared responses. Conversely, a mechanism difference can require different states even when current observations cannot distinguish it, if a future action produces different consequences.

This separates ontology from representation and representation from evidence. CREST does not turn every hidden variable into state information. It asks whether the hidden distinction changes what the state is responsible for supporting.

### 5.4 Monitoring adequacy is target-relative

Because required state and reportable target are distinct, a monitoring programme can be adequate for a coarse target without identifying the full ecological state required for a richer responsibility. A detection programme may answer whether a focal species is present while leaving population structure unresolved; an aggregate functional indicator may support a management threshold while leaving mechanism identity unresolved.

The important consequence is not that monitoring is generally inadequate. It is that monitoring adequacy must be stated relative to the target and the state resolution that target requires. More detailed ecological description is not always better, and full-state identification is not always necessary for a justified decision.

### 5.5 Representational stability differs from dynamical stability

Ecological stability is already multidimensional. CREST adds a distinct representational question.

**Dynamical stability** concerns whether the ecological system resists perturbation, returns, remains within a basin, or preserves a relevant regime.

**Evolutionary stability** concerns whether a strategy or trait resists invasion under a declared evolutionary model.

**Representational stability** concerns whether the same state quotient remains adequate when future operations, mechanisms, inherited meanings, observation channels, or targets change.

These properties can vary independently. A physical ecosystem can remain unchanged while the scientifically adequate state representation changes because a new operation makes a previously irrelevant distinction consequential. Conversely, the physical ecosystem can change while remaining within one coarse state if the change does not affect the responsibility assigned to that state.

This is the ecological meaning of the capability-resolution theorem. The theorem does not describe a physical regime shift. It demonstrates that representational change can be arbitrarily larger than the small capability change that makes new distinctions relevant.

### 5.6 Law portability follows state portability

A quotient-level ecological rule remains portable only while its state quotient remains adequate for the new responsibility. If a new context splits an old state fiber, the rule may cease to be well-defined on that old coarse state space.

This provides a specific diagnostic for ecological generalization. When a rule fails under novel conditions, one question is whether parameters changed inside the same state representation. CREST adds another: did the new context reveal that the old state representation merged worlds that are no longer equivalent for the task? Model transferability under novel conditions is already recognized as a central ecological problem (Yates et al. 2018); CREST identifies state-adequacy failure as one possible source of non-portability.

The same ecological world can therefore support different valid coarse laws under different scientific quotients without making truth perspective-dependent. The underlying response structure constrains all valid quotients and all valid factorization laws.

## 6. Relation to existing theories

CREST is intentionally cumulative. Philosophy of ecology has examined ecosystem identity and continuity (Cumming and Collier 2005; Collier and Cumming 2011; Delettre 2021). Ecological model-adequacy work asks whether state variables, controls, data, and validation are sufficient for a modelling purpose (Getz et al. 2018). General philosophy of modelling evaluates models for adequacy to purpose (Parker 2020; Bokulich and Parker 2021). State-and-Transition Models connect ecological states to thresholds and intervention (Stringham et al. 2003). Conservation decision theory and POMDPs combine hidden state, observations, actions, and uncertainty (Nicol and Chadès 2012; Chadès et al. 2021; Fackler and Pacifici 2014). Computational mechanics and causal abstraction formalize predictive or interventional coarse graining (Shalizi and Crutchfield 2001; Beckers and Halpern 2019). Predictive State Representations represent controlled-system state through action-conditional predictions of future observations or tests (Littman et al. 2002; Singh et al. 2004). Reinforcement-learning work also treats state and action abstraction as coupled problems (Konidaris 2019).

CREST therefore does not claim novelty for equivalence classes, predictive state, causal abstraction, intervention-sensitive state, purpose-relative adequacy, hidden-state modelling, viability analysis, state/action coupling, or coarse-grained laws as such. The fixed-point machinery used in the finite state construction is classical.

The proposed contribution is architectural and ecological. CREST starts from possible ecological worlds rather than assuming that a current descriptor is the state. It asks when different worlds may count as the same state under future, historical-semantic, and mechanistic responsibilities; checks whether the obligations share an admissible carrier; constructs the least-information finite state satisfying them; distinguishes that required state from what evidence identifies and from what target remains reportable; and treats a coarse ecological law as valid only on a quotient that preserves the response the rule must return.

The distinction from a POMDP is one of explanatory target rather than expressive power. A sufficiently rich POMDP can encode hidden state, history, mechanisms, observations, actions, and targets. CREST instead asks which distinctions are being merged when ecologists call two possible worlds the same state, which scientific responsibility makes a distinction necessary, whether the evidence has earned it, and whether the quotient-level rule remains valid after the responsibility changes. CREST therefore claims an explicit audit decomposition, not non-embeddability in POMDPs.

The same caution applies to Predictive State Representations. PSRs already show that controlled-system state can be defined through predictions of future action-observation tests. CREST does not claim novelty for predictive equivalence or future-test-defined state, and it does not claim greater expressive power than a sufficiently rich PSR. The difference is the separation of future/composition sufficiency, inherited-semantic portability, retained-mechanism robustness, carrier feasibility, evidence identification, target reportability, and quotient-law validity as distinct ecological responsibilities.

The state/action-abstraction boundary must also be explicit. Konidaris (2019) already discusses how action abstractions can determine the state abstraction needed to support them. CREST therefore does not claim the qualitative proposition that changing available actions can change an adequate state abstraction. The theorem-level claim is narrower: within one carrier-state-evidence-target architecture, a single new action can add exactly one viable world while forcing arbitrarily many additional bits of least-state and monitoring resolution, destroying full-state licensing while preserving a coarse target.

CREST also differs from a metaphysics of ecosystem identity. It does not decide whether two temporally separated ecosystems are numerically the same ecological individual. One ecosystem can retain numerical identity while a scientific state variable becomes inadequate, and different ecosystems can legitimately share one state for a declared comparison. The theory concerns state-representation adequacy rather than numerical identity.

## 7. Limits

CREST does not establish one universal ecological state independent of scientific contract. The finite result is conditional: on one admissible finite carrier and under the stated closure assumptions, there is a unique coarsest joint state satisfying the implemented requirements. Different carriers, futures, inherited meanings, mechanism families, evidence models, or targets can yield different adequate states.

CREST also does not infer the correct future grammar, source-target relation, mechanism family, evidence model, action roles, or report target from ecological data. These are scientific inputs that require justification in an application. They are not empirical premises required to prove the finite mathematics.

The trajectory-level interpretation is broader than the present mathematics. The current proofs are finite and exact. Infinite-state, continuous-time, stochastic, approximate, delayed-control, and partially observed extensions require additional theory.

The theory does not claim that every present snapshot is insufficient. Snapshot sufficiency can hold. Nor do the three structural obstruction families claim to exhaust every way a state merge can fail.

The capability-resolution theorem is an existence result, not a prediction that real ecological interventions generically produce exponential state growth. It proves that no upper bound based only on carrier-size gain exists without further structural assumptions. Particular ecological systems may impose stronger bounds.

CREST does not claim historical priority over automata minimization, viability kernels, state complexity, predictive state, state/action abstraction, or purpose-relative modelling. Its theorem-level claim is the cross-gate conjunction and no-bound consequence within the stated architecture.

Finally, CREST does not decide normative priorities. A scientific or management programme may accept ambiguity to reduce cost, prioritize robust coarse targets over fine prediction, or preserve historical categories for institutional reasons. Contract-relativity makes those commitments explicit; it does not rank them without additional normative premises.

## 8. Conclusion

CREST begins from a reversal of the usual order. Ecology should not assume that a present description is the state and then ask what that state predicts. It should first ask **when different ecological worlds can legitimately count as the same state for the scientific task**, and then ask whether the desired ecological rule is well-defined on that equivalence.

On this view,

\[
\boxed{
\text{ecological state}
=\text{a scientifically licensed quotient of temporally extended ecological worlds}.
}
\]

A present snapshot is sufficient only when its fibers remain within the required state classes. A coarse ecological law exists when the required response factors through that quotient. CCOC, MLTR, and MRM identify three ways present sameness can fail: an enlarged future can expose a dormant distinction, structural change can break inherited meaning, and retained mechanisms can disagree under a required response. CED then asks whether the evidence identifies the distinctions that the state and target require.

For the finite theory, the least-information state on an admissible carrier is the unique coarsest common refinement satisfying the implemented obligations, and full deterministic state reporting is licensed exactly when the evidence resolves that state. Yet full-state identification is not always necessary for a justified coarse target.

The capability-resolution theorem gives the sharpest result. For every \(m\ge1\), one newly admitted action can increase the viable carrier by exactly one world while refining a retained present slice from one state to \(2^m\) states. Under unchanged evidence, the corresponding state-resolution debt is exactly \(m\) bits: full-state identification is lost while a coarse target remains reportable. Viability gain alone therefore cannot bound representational burden.

This result separates physical and representational change. A new intervention need not be executed, and the ecosystem need not yet change, for the scientifically adequate present representation to change. What changes is which counterfactual responses the state is responsible for supporting. The future does not act backward on the present; the state relation changes because the scientific task changes.

The same logic applies to ecological rules. A rule can remain valid on its original quotient while failing to transfer to a context in which formerly merged worlds must be distinguished. Ecological laws are therefore not made arbitrary by contract-relativity. Their valid coarse domains are constrained by the ecological response structure and by the scientific responsibilities under which worlds are treated as the same state.

CREST thus reframes ecological state as a problem of justified equivalence. It connects temporal extension, future action, historical meaning, latent mechanism, evidence, and effective law without requiring that every ecological difference be represented. The central question is narrower and more operational: **which ecological differences require different states, and which do not, for the work that ecology asks the state to perform?**

## References

Beckers S, Halpern JY (2019) Abstracting causal models. Proceedings of the AAAI Conference on Artificial Intelligence 33:2678–2685. https://doi.org/10.1609/aaai.v33i01.33012678

Bokulich A, Parker W (2021) Data models, representation and adequacy-for-purpose. European Journal for Philosophy of Science 11:31. https://doi.org/10.1007/s13194-020-00345-2

Chadès I, Pascal LV, Nicol S, Fletcher CS, Ferrer-Mestres J (2021) A primer on partially observable Markov decision processes (POMDPs). Methods in Ecology and Evolution 12:2058–2072. https://doi.org/10.1111/2041-210X.13692

Collier J, Cumming GS (2011) A dynamical approach to ecosystem identity. In: Philosophy of Ecology, Handbook of the Philosophy of Science, Vol 11. Elsevier, pp 201–218. https://doi.org/10.1016/B978-0-444-51673-2.50008-X

Cumming GS, Collier J (2005) Change and identity in complex systems. Ecology and Society 10:29. https://doi.org/10.5751/ES-01252-100129

Delettre O (2021) Identity of ecological systems and the meaning of resilience. Journal of Ecology 109:3147–3156. https://doi.org/10.1111/1365-2745.13655

Fackler P, Pacifici K (2014) Addressing structural and observational uncertainty in resource management. Journal of Environmental Management 133:27–36. https://doi.org/10.1016/j.jenvman.2013.11.004

Getz WM, Marshall CR, Carlson CJ, Giuggioli L, Ryan SJ, Romañach SS, Boettiger C, Chamberlain SD, Larsen L, D'Odorico P, O'Sullivan D (2018) Making ecological models adequate. Ecology Letters 21:153–166. https://doi.org/10.1111/ele.12893

Konidaris G (2019) On the necessity of abstraction. Current Opinion in Behavioral Sciences 29:1–7. https://doi.org/10.1016/j.cobeha.2018.11.005

Levin SA (1998) Ecosystems and the biosphere as complex adaptive systems. Ecosystems 1:431–436. https://doi.org/10.1007/s100219900037

Littman ML, Sutton RS, Singh S (2002) Predictive representations of state. Advances in Neural Information Processing Systems 14:1555–1561

Nicol S, Chadès I (2012) Which states matter? An application of an intelligent discretization method to solve a continuous POMDP in conservation biology. PLoS ONE 7:e28993. https://doi.org/10.1371/journal.pone.0028993

Parker WS (2020) Model evaluation: an adequacy-for-purpose view. Philosophy of Science 87:457–477. https://doi.org/10.1086/708691

Post DM, Palkovacs EP (2009) Eco-evolutionary feedbacks in community and ecosystem ecology: interactions between the ecological theatre and the evolutionary play. Philosophical Transactions of the Royal Society B 364:1629–1640. https://doi.org/10.1098/rstb.2009.0012

Schoener TW (2011) The newest synthesis: understanding the interplay of evolutionary and ecological dynamics. Science 331:426–429. https://doi.org/10.1126/science.1193954

Shalizi CR, Crutchfield JP (2001) Computational mechanics: pattern and prediction, structure and simplicity. Journal of Statistical Physics 104:817–879

Singh S, James MR, Rudary MR (2004) Predictive state representations: a new theory for modeling dynamical systems. Proceedings of the 20th Conference on Uncertainty in Artificial Intelligence, pp 512–519

Stringham TK, Krueger WC, Shaver PL (2003) State and transition modeling: an ecological process approach. Journal of Range Management 56:106–113. https://doi.org/10.2307/4003893

Yates KL, Bouchet PJ, Caley MJ, Mengersen K, Randin CF, Parnell S, Fielding AH, Bamford AJ, Ban S, Barbosa AM et al (2018) Outstanding challenges in the transferability of ecological models. Trends in Ecology & Evolution 33:790–802. https://doi.org/10.1016/j.tree.2018.08.001
