# What Counts as the Same Ecological State?
## A Contract-Relative Theory of Temporally Extended Ecological States

## Abstract

Ecologists routinely describe ecosystems by present states, yet a present snapshot can conceal differences in history, latent mechanism, and future response that matter for prediction or intervention. We develop Contract-Relative Ecological State Theory (CREST) from the premise that an ecological state is not necessarily a property of an instant, but a scientifically licensed compression of a temporally extended ecological world. CREST separates the ecological world from the observation and intervention context through which it is accessed and asks when a present snapshot is sufficient for the work assigned to a state. Three companion theorem programs expose distinct structural failures of snapshot sufficiency: a wider future can make dormant distinctions operationally relevant; structural replacement can break inherited state meaning; and retained mechanisms can disagree on required future responses. A fourth program addresses the downstream epistemic question of whether available evidence identifies the distinctions the state requires. On a declared finite common carrier, the existing CREST construction yields the unique coarsest joint partition satisfying the implemented requirements and separately tests whether evidence identifies that state. This framework also shows how a newly available intervention can refine the scientifically adequate present state before the ecosystem changes physically, and why ecological regularities can be understood as effective laws on context-adequate quotients rather than context-free laws of the full latent world. CREST therefore links temporal extension, causal response, observation, intervention, and evidence without positing one intrinsic ecological partition or claiming that present snapshots are universally inadequate.

**Keywords:** philosophy of ecology; ecological state; scientific representation; temporal extension; causal abstraction; model adequacy

## 1. Why ecological state is a compression problem

Ecologists routinely speak as if an ecosystem has a state now. A lake is eutrophic or clear-water, a population is persistent or declining, a community is pollination-maintained or pollination-limited, and a landscape is connected or fragmented. Such descriptions are indispensable because they compress. They assign many physically different configurations one scientifically useful label. The difficult question is therefore not whether ecology simplifies, but **which differences may be forgotten without invalidating the scientific work assigned to the state**.

That question becomes especially important in ecology because the present configuration is embedded in a history and in a changing field of possible responses. Ecosystems have long been described as complex adaptive systems in which higher-level patterns emerge from localized interaction, selection, nonlinearity, and historical dependency (Levin, 1998). Eco-evolutionary work adds a reciprocal point: ecological interactions can shape selection, while evolutionary change can alter ecological interactions and ecosystem function (Post & Palkovacs, 2009; Schoener, 2011). Nothing in CREST requires a universal evolutionary direction, one globally increasing fitness function, mathematical chaos, or deterministic futures. The relevant motivation is weaker and more general: ecological histories, interactions, traits, and environments can alter the response structure that determines what happens next.

A schematic eco-evolutionary system might be written

\[
\dot x=F(x,\theta),
\qquad
\dot\theta=G(x,\theta),
\]

where \(x\) denotes ecological configuration and \(\theta\) traits or strategies. The point is not that these equations are a universal ecological model. It is that the response of \(x\) depends on \(\theta\), while the dynamics of \(\theta\) depend on ecological context. The effective selective environment and the ecological interaction structure can therefore be mutually coupled. Variation and stochasticity generate alternatives; context-dependent selection biases their contribution; altered phenotypes can feed back on later ecological conditions. A fixed present observation need not summarize all distinctions that remain relevant to this coupled response structure.

This motivates a different starting point for ecological state theory. Rather than assume that the state is a snapshot \(x_t\), CREST begins with a space \(\Omega\) of possible ecological worlds. A world is represented schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) the present configuration, and \(\mathcal F_t\) the future-response structure under the interactions and interventions relevant to the scientific problem. In a stochastic system, \(\mathcal F_t\) can be a conditional distribution over possible future trajectories rather than one predetermined future. This notation is not a block-universe thesis and does not assert physical determinism. It is a bookkeeping device for asking whether a present scientific state must retain information inherited from the past or information that matters only under counterfactual futures.

The central philosophical proposal is therefore:

\[
\boxed{
\text{an ecological state is a scientifically licensed compression of a temporally extended ecological world.}
}
\]

The word *compression* matters. CREST does not propose that every ecological state should contain the entire past, every hidden mechanism, and every possible future. Such a representation would defeat the purpose of a state variable. Instead, CREST asks for the coarsest representation that may safely erase differences for a declared scientific responsibility.

This shifts the original question, *What counts as the same ecological state?*, into a deeper one: **why can a finite ecological state exist at all when the distinctions relevant to prediction, intervention, and evidence can change with context?** CREST's answer is conditional. A finite state exists for a declared problem when sufficiently many possible worlds can be treated as interchangeable without violating the responsibilities assigned to the representation.

This position is continuous with existing work rather than a claim that ecology previously lacked state theory. Philosophy of ecology has analyzed ecosystem identity and continuity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has proposed explicit equivalence criteria for ecosystem states (Boit & Spencer, 2019) and adequacy protocols that scrutinize state variables, controls, data determinacy, and coarse graining (Getz et al., 2018). State-and-Transition Models make ecological state intervention-sensitive (Stringham et al., 2003). Conservation decision theory separates hidden state from observation and has developed management-relevant state reduction in POMDPs (Nicol & Chadès, 2012; Chadès et al., 2021), while structural and observational uncertainty can be treated jointly (Fackler & Pacifici, 2014). Causal states and causal abstraction formalize prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling treats adequacy as purpose-sensitive (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021), including explicit adequacy-for-purpose accounts in environmental science (Parker et al., 2026).

CREST's narrower contribution is to connect these concerns through one ecological state-sameness relation and to separate three questions that are easily conflated: what distinctions the world and scientific task require, what minimum representation preserves them, and what the available evidence actually licenses us to report.

## 2. From temporally extended worlds to scientific states

### 2.1 Scientific access is not the world itself

A scientist does not observe \(\omega\) directly. A measurement and intervention context \(V\) determines which features of the possible world are scientifically accessible. Schematically,

\[
O_V:\Omega\rightarrow Y_V.
\]

A biomass survey, a pollination assay, a genetic history reconstruction, and an intervention experiment can induce different accessible distinctions on the same underlying ecological system. This does not mean that the observer creates ecological truth. The world constrains every observation and intervention. The distinction is instead between the world, the projection through which it is scientifically accessed, and the responsibilities imposed on the resulting state representation.

CREST therefore separates observational or interventional **access** from the scientific **contract**. The current program writes the contract schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where \(\Gamma\) declares future interactions or operations the representation must survive, \(\mathcal H\) inherited meanings or history that must remain coherent, \(\Theta\) retained mechanisms or response alternatives, \(D\) the declared observation/evidence architecture, and \(T\) the requested report or decision target. The components can be debated and revised. CREST does not prove that nature supplies one uniquely correct contract. But once a contract is declared, a proposed state merge can fail for explicit dynamical, semantic, mechanistic, or evidential reasons.

The resulting state equivalence is written

\[
\omega\sim_{\mathcal C,V}\omega'
\]

when the two worlds may be treated as interchangeable for the scientific work specified by \((\mathcal C,V)\). The corresponding state is

\[
\boxed{
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}.
}
\]

Contract-relativity is therefore not arbitrary relativism. Scientists declare the work; ecological dynamics and evidence determine whether a proposed compression can do it.

### 2.2 Snapshot sufficiency is a condition, not an assumption

Let \(X(\omega)\) denote the present snapshot. The present snapshot is sufficient for the CREST state exactly when the required state factors through \(X\):

\[
\boxed{
X(\omega)=X(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

If a pair of worlds shares the same current snapshot while belonging to different required state classes, then the snapshot is not sufficient for that contract. CREST does **not** claim that present snapshots are always insufficient. In many systems and for many tasks, current observables can be adequate. The proposal is that snapshot sufficiency should be demonstrated rather than built into the meaning of state.

A forest illustrates the distinction. Two stands can have the same current biomass yet differ in relevant disturbance history, basin position, recruitment limitation, pathogen reservoir, or response to restoration. If none of these differences changes the scientific target, they may be safely compressed. If one difference changes a permitted future response, the same present biomass no longer guarantees the same state for that task. Conversely, two present configurations can differ numerically while supporting the same relevant future responses and therefore legitimately share one coarse state.

The criterion also clarifies temporal language. Saying that an ecological state is temporally extended does not mean that the future literally causes the present. It means that the scientific equivalence relation on present worlds can depend on counterfactual futures. A distinction can become necessary today because an intervention becomes part of the set of futures the representation is required to support.

### 2.3 From state adequacy to quotient laws

A coarse ecological rule is well-defined only if the state quotient erases no distinction needed by that rule. If worlds \(\omega\) and \(\omega'\) are assigned the same state, every response the effective rule is required to return must agree across that state fiber. Thus many ecological regularities can be understood as **effective laws on a scientifically adequate quotient** rather than automatically as laws of the full latent world.

This interpretation explains a familiar ecological phenomenon without reducing it to observer preference. A rule can be stable under one scale, measurement set, future repertoire, or mechanism family and fail after that context changes. The original rule need not have been false. Its domain was the quotient on which the distinctions it erased remained irrelevant. The central portability question is therefore not merely whether a fitted relation repeats, but whether the coarse state on which the relation is defined remains adequate under the new scientific responsibility.

## 3. Three structural obstructions and one evidence gate

The companion theorem programs are best understood as consequences of the snapshot-sufficiency problem rather than as four parallel definitions from which CREST is assembled. CCOC, MLTR, and MRM provide three structural reasons that equal present descriptions can require different scientific states. CED addresses a downstream epistemic question: whether the available evidence identifies the distinctions already required for the task.

### 3.1 Future insufficiency — CCOC

Two configurations can be equivalent under every currently legal future and still require different state information once colonization, reconnection, dispersal, rewiring, or intervention possibilities are opened. CCOC formalizes this as a cross-grammar compression problem. A state representation is exact relative to a declared future grammar when configurations merged by that representation remain indistinguishable under every legal future word.

The central CCOC family compares one fixed controlled system under a closed and an enlarged legal-future grammar. Under the closed grammar, many micro-configurations can share one exact response class because the futures that would expose their differences are unavailable. Under the open grammar, dormant differences become individually addressable. The same physical configuration family can therefore admit a small exact interface under one future contract and require a much finer interface under another.

The CREST reading is

\[
\boxed{
\text{present functional equivalence}
\not\Rightarrow
\text{causal equivalence under an enlarged future}.
}
\]

For a pollination example, two communities can both be classified as `pollination maintained` while no substitute pollinator or dispersal route is relevant. If a later connection makes one dormant response difference operationally important, the earlier merge was not retrospectively false. The future contract changed, and the state needed for that contract became finer.

### 3.2 Historical and semantic insufficiency — MLTR

A different failure appears when a state label is carried across structural change. After pollinator turnover, habitat reconfiguration, extinction, recolonization, or interaction rewiring, the label `pollination maintained` may remain syntactically available while no longer grouping target configurations with the same legal actions or future responses.

MLTR fixes an inherited source classification and asks whether its operational meaning remains exact in a target system. When the carried partition fails, iterative refinement yields the unique coarsest exact **source-relative** repair. The repair introduces only those splits forced by target output, legal-action, or successor differences while preserving inherited merges that remain valid.

This is not the same as constructing the smallest target abstraction from scratch. If all source meaning could be discarded, a new target state variable could simply replace the old one. MLTR treats semantic inheritance as part of the scientific responsibility. Different declared replacement histories can also carry incompatible meanings, in which case finite history context must be retained only to the extent necessary to preserve those distinctions.

The CREST reading is

\[
\boxed{
\text{same present descriptor}
\not\Rightarrow
\text{same inherited operational state after structural change}.
}
\]

History is therefore not automatically part of every ecological state. It becomes state-relevant when forgetting it changes what the inherited state is required to mean or do.

### 3.3 Mechanistic insufficiency — MRM

The same visible present state can be compatible with several retained causal mechanisms. Suppose two candidate mechanisms agree on current pollination but disagree about the response to competitor removal, habitat restoration, or another declared intervention. A single candidate-independent deterministic forecast is then not uniformly supported.

MRM collapses raw mechanisms into **response types**. Candidates that induce the same declared response behavior are equivalent for the task. Full mechanism identity need not be retained. Conversely, response types that disagree under a relevant action cannot be forgotten if one deterministic prediction is required. When disagreement remains, the scientifically honest output can be typed or set-valued, or a discriminating intervention can be chosen if the experimental contract permits one.

The CREST reading is

\[
\boxed{
\text{same visible present state}
\not\Rightarrow
\text{same required state under response-relevant mechanism uncertainty}.
}
\]

This is a state issue only where mechanism differences change required responses. Mechanisms that are distinct in description but identical for the declared future can remain compressed.

### 3.4 Evidence licensing — CED

CED is deliberately downstream of these structural questions. A distinction can be required for prediction without being one that the current observation system licenses us to report. Camera records, visitation observations, environmental DNA, demographic surveys, or experiments can leave multiple target-relevant worlds compatible with one record.

CED begins from the record classes induced by a declared finite experiment and observation contract. A deterministic target report is licensed only when the target is constant across the worlds compatible with the evidence. If compatible worlds imply different target values, the honest output remains ambiguity-explicit.

CED also supplies target-safe representational resolution. The distinction is important: a target-safe quotient specifies **what resolution would be sufficient for deterministic tracking**, whereas the evidence partition specifies **what distinctions the current record has actually earned**. A required refinement is not itself an observation.

Thus CREST separates

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}
}
\]

in general. Evidence can fail to identify the full required state while still licensing a requested target if that target is constant on the unresolved evidence class.

## 4. The finite mathematical answer: carrier, state, and evidence

The trajectory-first interpretation is broader than the current proved mathematics. The formal results implemented here concern declared finite latent-world carriers and exact finite transitions. Their role is to show, under explicit assumptions, how the philosophical compression problem can be made mathematically sharp. The theorem order is carrier feasibility, state construction, and evidence licensing.

### 4.1 Gate A — Can the requirements share an admissible ecological world set?

The conditional state theorem presupposes a common carrier. This cannot be hidden inside notation. CREST-J3 addresses a universal-action contract by descending to the greatest synchronized transition-closed carrier \(U^*\). CREST-J6 addresses a controlled contract in which all uncontrollable moves must remain safe while at least one admissible control choice is available, yielding a greatest robustly controlled-invariant carrier \(K^*\).

If the relevant common carrier is empty or fails required coverage, there is no fully adequate joint finite state under that declared synchronization. This failure is not repaired by merely splitting a partition more finely; the common ecological world set itself is incoherent under the declared requirements. CREST-J4 and J7 characterize finite repair languages for the universal and controlled carrier problems.

The conceptual dependency is therefore

\[
\text{admissible common carrier}
\longrightarrow
\text{required state}
\longrightarrow
\text{evidence licensing}.
\]

These are mathematical dependencies, not a mandatory chronological order for fieldwork.

### 4.2 Gate B — What is the least-information adequate state?

Conditional on one admissible finite common carrier \(U\), let \(B\) be a baseline partition containing distinctions the analysis is committed to preserving. The current finite implementation represents the declared requirements by refinement closures

\[
C_\Gamma,\qquad
C_{\mathcal H},\qquad
C_\Theta,\qquad
C_{D,T}.
\]

Here the \(D,T\) contribution should not be confused with empirical identification. It encodes the target/action-stable resolution required by the declared evidence/reporting contract; the actual record-induced evidence partition is tested separately at Gate C.

Under CREST-J1's assumptions, the common closure above the baseline is

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B).
}
\]

J1 proves that \(J\) is the **unique coarsest, least-information partition** satisfying the implemented finite requirements. For a finite latent world \(u\in U\),

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

This is the finite construction corresponding to the world-level equivalence relation introduced above. It gives conditional joint minimality, not one intrinsic partition of nature. A different future repertoire, inherited meaning, mechanism family, target, observation contract, or carrier can yield a different adequate state.

The construction also blocks a tempting shortcut. Independently minimizing each audit once and taking a one-pass combination can be insufficient because a distinction created by one refinement can make another refinement expose an additional distinction. Pairwise commutation is not required. On the finite carrier, fair repeated refinement reaches the least common fixed point even when intermediate partitions and pass counts depend on order.

The lattice and closure-operator substrate is classical. CREST does not claim invention of generic fixed-point or partition-refinement machinery. The theoretical content lies in how the ecological requirements are represented, how they are kept distinct, and how state requirement is separated from evidence.

### 4.3 Gate C — Does the evidence identify that state?

Let \(E_D\) be the reliability-qualified evidence partition: worlds in one \(E_D\)-block remain observationally compatible under the declared experiment, detection, failure, and risk assumptions. The finite licensing condition is

\[
\boxed{
\text{deterministic full-state report exists}
\iff
J\preceq E_D.
}
\]

If \(J\preceq E_D\), every evidence class lies inside one required state block. If the relation fails, \(J\) still specifies the resolution an adequate state would require, but the current evidence does not identify one unique block. The sharp report is then the set of \(J\)-blocks compatible with the evidence.

A requested target can remain deterministic without full-state identification. This makes the distinction among required state, identified state, and reportable target operational rather than merely terminological.

CREST-O1 illustrates the separation. In its finite witness, the cheapest structural carrier repair leaves the downstream full J1 state unresolved by the declared evidence, whereas a costlier repair is fully licensed. The target remains reportable under the cheaper repair. The result does not make the costlier repair normatively preferable; it demonstrates that carrier feasibility, representational adequacy, and evidential identification are distinct optimization problems.

### 4.4 Cross-gate result — when management changes what must be known

Let \(J_{\mathcal C}\) be the required finite state under a contract \(\mathcal C\), and let

\[
\mathcal S_{\mathcal C}(e)
=
\{[u]_{J_{\mathcal C}}:u\text{ remains compatible with }e\}
\]

be the state blocks compatible with record \(e\). Changing the contract can alter the viable carrier, the required state resolution, and the number of state blocks compatible with unchanged evidence in different directions.

A finite control-enrichment witness makes this strict. Before enrichment, a controlled contract admits a two-world viable carrier whose two required states are identified by the evidence. Adding one controllable `rescue` action makes a third world viable. The same new action also gives two candidate worlds different future behavior, so the required state must split them. The viable carrier expands while the required state count rises from two to three. Because the original monitoring record still merges the split worlds, full-state identification is lost, while the requested target remains constant and reportable.

This supports a precise representational claim:

> **The future does not have to happen to change the present scientific state; a counterfactual future only has to become relevant to what the state is required to support.**

There is no backward causation in this statement. The ecosystem need not change physically. What changes is the scientific equivalence relation applied to the present worlds because a new future response has entered the contract.

For fixed evidence partition \(E\) and required state partition \(J\), the unique coarsest refinement that preserves existing evidence distinctions while identifying \(J\) is

\[
E\vee J.
\]

The finite monitoring-resolution debt is

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

In the `rescue` witness, full-state debt becomes positive while target debt remains zero. In the existing CCOC extremal family, a newly relevant future operation can generate arbitrarily large finite state-memory inflation across the family. The common-refinement calculation itself is classical; the CREST point is the coupling between changed scientific responsibility, required state, and unchanged evidence.

## 5. Quotient laws and representational stability

### 5.1 Ecological rules as effective laws of a quotient

The state account changes how ecological rules should be interpreted. Suppose a coarse state map merges two worlds. An effective transition or prediction rule is well-defined on that state only if the worlds agree on every output or future response that the rule is responsible for returning. The rule therefore inherits the domain assumptions of the quotient on which it is defined.

This yields the program-level interpretation

\[
\boxed{
\text{ecological rule}
=\text{effective law on a scientifically adequate quotient}.
}
\]

The statement does not imply that all ecological laws are merely conventional or that no general laws exist. It says that a coarse-grained rule cannot outrun the distinctions erased by its state representation. If a wider future, a structural replacement, a response-relevant mechanism, or a new target splits an old state fiber, the old rule can cease to be adequate for the enlarged task while remaining valid on its original quotient.

This provides one way to connect CREST to the long-standing difficulty of generalization in ecology without claiming to solve the philosophy of ecological laws in general. Model transferability under novel conditions is already an established problem (Yates et al., 2018). CREST adds a specific diagnostic question: did the transfer change which latent distinctions must remain visible to make the effective state law well-defined?

### 5.2 Three kinds of stability should not be conflated

Ecological stability is already multidimensional. CREST introduces another distinction at the level of representation.

**Dynamical stability** concerns whether the ecological system resists perturbation, returns, remains within a basin, or preserves a relevant regime.

**Evolutionary stability** concerns whether a strategy or trait resists invasion under a declared evolutionary model.

**Representational stability** concerns whether the same state quotient remains adequate when observation, intervention, future, mechanism, semantic, or reporting responsibility changes.

These properties can vary independently. A state quotient can remain adequate while the underlying ecosystem changes dynamically, if the change occurs within one scientifically relevant coarse class. Conversely, the ecosystem can remain physically unchanged while the adequate state representation changes because a new intervention or observation channel makes a previously ignored distinction consequential.

The action-expansion witness proves one strict finite separation of this kind. It does not establish a general mathematical relation among dynamical, evolutionary, and representational stability. That broader theory remains open.

### 5.3 Context-dependent selection does not imply global progress

The trajectory framing should also not be confused with teleology. Eco-evolutionary feedbacks motivate a changing response structure, not a claim that evolution moves toward one global optimum. Variation, mutation, recombination, drift, and demographic stochasticity can contribute random components; selection biases reproduction relative to the current ecological context. When frequency dependence, species interactions, or abiotic conditions change, the fitness ranking of the same variants can change as well.

The relevant philosophical point for CREST is that a scientific state responsible for evolutionary prediction may need to preserve context that a purely descriptive snapshot safely ignores. The stronger claim that there exists one global adaptive arrow is neither required nor made here.

### 5.4 Monitoring debt can be structural rather than merely quantitative

An observation programme can fail because it measures the wrong channel, not merely because it has too few replicates. Consider a trait-specific performance quantity

\[
W(z)=F(z)R(z),
\]

where \(F\) and \(R\) are two positive causal channels. For any positive multiplier \(a(z)\), the changes

\[
(F,R)\mapsto(aF,R)
\qquad\text{and}\qquad
(F,R)\mapsto(F,aR)
\]

produce the same net performance \(W_1(z)=a(z)F(z)R(z)\). A monitoring scheme that is only a function of \(W\) therefore leaves these causal worlds observationally equivalent, however precisely \(W\) is repeatedly measured.

If a newly relevant intervention acts specifically on \(F\), the two worlds can have different counterfactual successors and can no longer safely occupy one required state. The resulting monitoring deficit cannot be repaired by more observations of the same aggregate output. A channel-resolved observation is needed to break the symmetry. Thus \(E\vee J\) should not automatically be interpreted as a request for greater sampling effort. It can imply a qualitatively new measurement type.

This is a useful point of contact between representation and field design. CREST does not prescribe a universal sensor-selection algorithm. It identifies which distinctions a state must support and whether the current evidence architecture can, in principle, support them.

## 6. Position relative to existing theories

CREST is intentionally cumulative. Ecological identity theory already analyzes what makes systems the same through change (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological model-adequacy work asks whether state variables, controls, data, and validation are sufficient for a modelling purpose (Getz et al., 2018). General philosophy of modelling evaluates models and data for adequacy to purpose (Parker, 2020; Bokulich & Parker, 2021). State-and-Transition Models connect ecological states to thresholds and intervention (Stringham et al., 2003). POMDP and adaptive-management theory combine hidden state, observations, actions, and model uncertainty (Nicol & Chadès, 2012; Fackler & Pacifici, 2014). Causal states and causal abstraction formalize predictive or interventional coarse graining (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). Complex-adaptive and eco-evolutionary accounts already emphasize history, feedback, emergence, and reciprocal ecological-evolutionary change (Levin, 1998; Post & Palkovacs, 2009; Schoener, 2011).

CREST should therefore not be judged by whether any one ingredient is new. J1 does not claim novelty for closure operators, partition lattices, or least common fixed points. Snapshot sufficiency is not a claim to have invented predictive-state thinking. Purpose-relativity is not new, nor are hidden-state models, viability analysis, or intervention-sensitive abstraction.

The ecology-specific synthesis lies in the architecture. CREST starts from a possible ecological world rather than assuming a current descriptor is the state. It asks whether present sameness remains valid under a declared set of future, historical-semantic, and mechanistic responsibilities; constructs the least-information finite state satisfying the implemented requirements when a common carrier exists; and then separately asks what the evidence licenses. This turns the companion theorem programs into different failure modes of one ecological compression problem rather than four unrelated quotient constructions.

The distinction from a POMDP is likewise one of explanatory target rather than expressive power. A sufficiently rich POMDP can encode hidden states, models, observations, and actions. CREST asks a different philosophical question: which distinctions are being erased when ecologists call two possible worlds the same state, and under what changes to the scientific responsibility does that erasure cease to be legitimate?

The distinction from computational mechanics is also important. Causal-state approaches group histories by their predictive futures (Shalizi & Crutchfield, 2001). CREST draws on the general lesson that predictive equivalence can define state, but adds inherited semantics, declared interventions, retained mechanism alternatives, evidence licensing, and report targets as separable responsibilities in an explicitly ecological adequacy problem. No claim of historical priority for the generic equivalence-class idea is needed.

CREST also differs from a metaphysics of ecosystem identity. It does not decide whether two temporally separated ecosystems are numerically the same ecological individual. One ecosystem can retain numerical identity while a scientific state variable becomes inadequate, and different ecosystems can legitimately share one state for a declared comparison. The object of the theory is **state-representation adequacy**, not the numerical identity of ecosystems.

## 7. Limits

CREST does **not** establish one universal joint state independent of scientific contract. The finite J1 result is narrower: conditional on one admissible finite common carrier and its stated closure assumptions, there is a unique coarsest joint state satisfying the implemented finite requirements. Different carriers, targets, mechanism families, futures, inherited meanings, or evidence contracts can yield different adequate states. The result is therefore not one intrinsic partition of nature.

CREST also does not infer the correct future grammar, source-target relation, mechanism family, evidence model, action roles, report target, or latent-world carrier from ecological data. Those are scientific inputs that require empirical and theoretical justification. The framework tests consequences once they are declared.

The trajectory-level interpretation remains an organizing philosophical account, **not yet a general theorem for continuous or stochastic trajectories**. The present proofs are finite and exact. A general infinite-state, continuous-time, stochastic, approximate, delayed-control, or partially observed version requires additional mathematics.

The theory does not claim that every present snapshot is insufficient. Snapshot sufficiency can hold, and when it does, a present descriptor legitimately factors the required state. Nor does CREST claim that future, historical-semantic, and mechanistic insufficiency exhaust every way a snapshot can fail.

The complex-adaptive motivation does not imply that ecosystems are generically mathematically chaotic, that every component continuously changes its own governing law in a literal sense, or that natural selection maximizes one global fitness function. CREST requires only that relevant response distinctions can depend on context and can therefore be missed by an overly coarse state.

Nor does every ecological state variable need to be implemented literally as a finite quotient. Many useful classifications are approximate, qualitative, continuous, probabilistic, or historically negotiated. The finite exact theory provides a benchmark: if a proposed merge fails even under the declared exact contract, it cannot be justified by appealing to compression alone.

Finally, CREST does not decide normative priorities. A management programme may prefer robustness to fine prediction, accept ambiguity to reduce cost, or preserve historical categories for institutional reasons. Contract-relativity requires these commitments to be explicit; it does not rank them without additional normative premises.

## 8. Conclusion

CREST begins from a simple but consequential reversal. Ecology should not assume that a present description is the state and then ask what that state predicts. It should first ask what possible ecological worlds the scientific task is allowed to treat as equivalent.

On this view,

\[
\boxed{
\text{ecological state}
=\text{scientifically licensed compression of a temporally extended ecological world}.
}
\]

A present snapshot is sufficient when it factors that required equivalence. When it does not, CCOC, MLTR, and MRM identify three distinct structural reasons: a wider future can expose a dormant difference; structural change can break inherited meaning; and retained mechanisms can disagree on a required response. CED then asks whether the evidence identifies the distinctions that the state and target require.

For the current finite theory, this conceptual architecture has an exact construction. On one admissible common carrier,

\[
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B),
\qquad
\operatorname{State}_{\mathcal C}(u)=[u]_J,
\]

and full deterministic state reporting is licensed exactly when \(J\preceq E_D\). The mathematical result is conditional, but the philosophical distinction is general: **the state the model requires and the state the evidence identifies are not the same question**.

The action-expansion witness adds a specifically ecological consequence. A new intervention can refine the scientifically adequate state before the ecosystem changes physically. Existing monitoring can therefore become inadequate not because the sensors deteriorated or a regime shift already occurred, but because the scientific future assigned to the state expanded. This is representational change, not backward causation.

The same logic supports a cautious account of ecological laws. A coarse ecological rule can be an effective law on a quotient whose erased distinctions remain irrelevant to its declared domain. Changing the future, structure, mechanism set, observation context, or target can make a different quotient necessary. The underlying world has not become relative; the scientific compression has acquired a different responsibility.

What ecologists call a present state is therefore often more than a description of what is visible now. It can be a compressed claim about the history that produced the present and the futures the system can still enter. CREST makes that compression explicit, defeasible, and testable.

## Statements and Declarations

### Competing Interests

**AUTHOR INPUT REQUIRED BEFORE SUBMISSION.**

### Funding

**AUTHOR INPUT REQUIRED BEFORE SUBMISSION.**

### Use of generative AI

OpenAI ChatGPT was used during manuscript development to assist with literature triage, organization of claim and citation audits, and drafting and revision of portions of the text. [FINAL HUMAN REVIEW REQUIRED BEFORE SUBMISSION: confirm that all cited sources, mathematical claims, interpretations, and final wording have been reviewed and approved by the human author(s).]

## References

Beckers, S., & Halpern, J. Y. (2019). Abstracting Causal Models. *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(01), 2678–2685. https://doi.org/10.1609/aaai.v33i01.33012678

Boit, A., & Spencer, M. (2019). Equivalence and dissimilarity of ecosystem states. *Ecological Modelling*, 396, 12–22. https://doi.org/10.1016/j.ecolmodel.2019.01.009

Bokulich, A., & Parker, W. (2021). Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science*, 11(1), Article 31. https://doi.org/10.1007/s13194-020-00345-2

Chadès, I., Pascal, L. V., Nicol, S., Fletcher, C. S., & Ferrer-Mestres, J. (2021). A primer on partially observable Markov decision processes (POMDPs). *Methods in Ecology and Evolution*, 12(11), 2058–2072. https://doi.org/10.1111/2041-210X.13692

Collier, J., & Cumming, G. S. (2011). A Dynamical Approach to Ecosystem Identity. In *Philosophy of Ecology*, Handbook of the Philosophy of Science, Vol. 11, pp. 201–218. Elsevier. https://doi.org/10.1016/B978-0-444-51673-2.50008-X

Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129

Cury, P. M., Mullon, C., Garcia, S. M., & Shannon, L. J. (2005). Viability theory for an ecosystem approach to fisheries. *ICES Journal of Marine Science*, 62(3), 577–584. https://doi.org/10.1016/j.icesjms.2004.10.007

Delettre, O. (2021). Identity of ecological systems and the meaning of resilience. *Journal of Ecology*, 109, 3147–3156. https://doi.org/10.1111/1365-2745.13655

Fackler, P., & Pacifici, K. (2014). Addressing structural and observational uncertainty in resource management. *Journal of Environmental Management*, 133, 27–36. https://doi.org/10.1016/j.jenvman.2013.11.004

Getz, W. M., Marshall, C. R., Carlson, C. J., Giuggioli, L., Ryan, S. J., Romañach, S. S., Boettiger, C., Chamberlain, S. D., Larsen, L., D'Odorico, P., & O'Sullivan, D. (2018). Making ecological models adequate. *Ecology Letters*, 21(2), 153–166. https://doi.org/10.1111/ele.12893

Giere, R. N. (2010). An Agent-Based Conception of Models and Scientific Representation. *Synthese*, 172(2), 269–281. https://doi.org/10.1007/s11229-009-9506-z

Kassara, K. (2012). Observability by using viability kernels. *Journal of Control Theory and Applications*, 10(3), 303–308. https://doi.org/10.1007/s11768-012-1022-x

Levin, S. A. (1998). Ecosystems and the biosphere as complex adaptive systems. *Ecosystems*, 1(5), 431–436. https://doi.org/10.1007/s100219900037

Lindenmayer, D. B., & Likens, G. E. (2009). Adaptive monitoring: a new paradigm for long-term research and monitoring. *Trends in Ecology & Evolution*, 24(9), 482–486. https://doi.org/10.1016/j.tree.2009.03.005

Lindenmayer, D. B., Likens, G. E., Haywood, A., & Miezis, L. (2011). Adaptive monitoring in the real world: proof of concept. *Trends in Ecology & Evolution*, 26(12), 641–646. https://doi.org/10.1016/j.tree.2011.08.002

Massimi, M. (2022). *Perspectival Realism*. Oxford University Press.

Nicol, S., & Chadès, I. (2012). Which States Matter? An Application of an Intelligent Discretization Method to Solve a Continuous POMDP in Conservation Biology. *PLoS ONE*, 7(2), e28993. https://doi.org/10.1371/journal.pone.0028993

Parker, W. S. (2020). Model Evaluation: An Adequacy-for-Purpose View. *Philosophy of Science*, 87(3), 457–477. https://doi.org/10.1086/708691

Parker, W. S., Carey, C. C., Olsson, F., & Thomas, R. Q. (2026). An adequacy-for-purpose perspective for the environmental sciences. *Frontiers in Ecology and the Environment*, Early View, e70058. https://doi.org/10.1002/fee.70058

Post, D. M., & Palkovacs, E. P. (2009). Eco-evolutionary feedbacks in community and ecosystem ecology: interactions between the ecological theatre and the evolutionary play. *Philosophical Transactions of the Royal Society B: Biological Sciences*, 364(1523), 1629–1640. https://doi.org/10.1098/rstb.2009.0012

Schoener, T. W. (2011). The newest synthesis: understanding the interplay of evolutionary and ecological dynamics. *Science*, 331(6016), 426–429. https://doi.org/10.1126/science.1193954

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational Mechanics: Pattern and Prediction, Structure and Simplicity. *Journal of Statistical Physics*, 104, 817–879.

Stringham, T. K., Krueger, W. C., & Shaver, P. L. (2003). State and transition modeling: An ecological process approach. *Journal of Range Management*, 56(2), 106–113. https://doi.org/10.2307/4003893

Yates, K. L., Bouchet, P. J., Caley, M. J., Mengersen, K., Randin, C. F., Parnell, S., Fielding, A. H., Bamford, A. J., Ban, S., Barbosa, A. M., et al. (2018). Outstanding Challenges in the Transferability of Ecological Models. *Trends in Ecology & Evolution*, 33(10), 790–802. https://doi.org/10.1016/j.tree.2018.08.001

---

## Submission-control note

- This file is the Biology & Philosophy target manuscript, not the general development draft.
- The manuscript is organized trajectory-first: world -> scientific access/contract -> snapshot sufficiency -> structural obstructions -> finite state construction -> evidence licensing -> quotient-law and stability consequences.
- The finite theorem statements remain conditional on declared finite carriers and exact assumptions; the temporally extended world interpretation is not presented as a proved general trajectory theorem.
- CED is treated as downstream evidence licensing rather than a fourth ontic source of ecological difference, while its target-safe finite refinement remains part of the implemented state requirement where explicitly declared.
- Six keywords are supplied.
- The manuscript distinguishes unconditional/cross-contract global minimality (not claimed) from J1 conditional unique coarseness on a declared admissible finite common carrier (proved).
- Levin (1998), Post and Palkovacs (2009), and Schoener (2011) are used only to ground the complex-adaptive and eco-evolutionary motivation, not as sources for the CREST finite theorems.
- Author-controlled Competing Interests and Funding statements must be completed before submission.
- Review-manuscript anonymization and separate title-page metadata remain required before upload.
