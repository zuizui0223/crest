# What Counts as the Same Ecological State?
## A Contract-Relative Account of State-Representation Adequacy

## Abstract

Ecology routinely compresses heterogeneous configurations into shared states for prediction, comparison, and management. We ask when that compression remains scientifically adequate as the work assigned to a state changes. CREST distinguishes four currently formalized obligations: future sufficiency under declared operations, semantic coherence after structural change, robustness across retained response mechanisms, and evidence-relative target resolution. On one admissible finite common carrier, these obligations induce a unique coarsest joint partition \(J\); the CREST state of configuration \(u\) is its block \([u]_J\), the least-information equivalence class preserving every distinction forced by the declared contract. A separate evidence gate asks whether the required block is actually identified. Within CREST, these three quantities define what we call an ecological state adequacy frontier: changes in scientific obligations can alter carrier feasibility, required state resolution, and evidential identifiability in different directions. A finite control-enrichment witness shows that adding one management action can enlarge the viable carrier while increasing the least-information state resolution beyond fixed monitoring, even though a requested target remains reportable. We use management-induced information debt for this specific cross-gate pattern rather than as a claim to a new generic theory of representational obsolescence. CREST therefore treats ecological state equivalence as a testable scientific commitment and shows why increased management capability can increase, rather than reduce, what must be known about the system. The account is contract-relative but not arbitrary, and it does not claim that the four obligations are exhaustive or that nature supplies one intrinsic state partition.

**Keywords:** philosophy of ecology; ecological state; scientific representation; model adequacy; causal abstraction; uncertainty

## 1. From ecosystem identity to state-representation adequacy

Ecologists routinely decide what counts as the same ecological state. A lake can be classified as eutrophic or clear-water, a population as persistent or declining, a community as pollination-maintained or pollination-limited, and a landscape as connected or fragmented. Such labels are useful precisely because they ignore many differences among underlying configurations. The scientific question is therefore not whether ecological descriptions simplify. It is **which differences a state representation is permitted to ignore for the work assigned to it**.

Philosophy of ecology has long examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has gone further than merely using state labels: explicit equivalence criteria for ecosystem states have been proposed (Boit & Spencer, 2019), model-adequacy protocols already scrutinize state variables, control variables, data determinacy and coarse graining (Getz et al., 2018), and State-and-Transition Models make ecological states intervention-sensitive (Stringham et al., 2003). Conservation decision theory likewise separates hidden ecological state from observation and has developed management-relevant state reduction in POMDPs, including explicit arguments for reducing state and observation variables to the smallest ensemble needed for the decision problem (Nicol & Chadès, 2012; Chadès et al., 2021), while structural and observational uncertainty can be treated jointly (Fackler & Pacifici, 2014). Monitoring itself is already understood as adaptive: long-term programmes may be redesigned as scientific and policy questions change (Lindenmayer & Likens, 2009; Lindenmayer et al., 2011). Ecological model transferability under novel conditions is also an established problem (Yates et al., 2018). In adjacent formal fields, causal states, state abstraction, and causal abstraction provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling treats adequacy as purpose-sensitive rather than reducible to one context-free notion of fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021), and this adequacy-for-purpose perspective has now been articulated explicitly for the environmental sciences (Parker et al., 2026).

CREST begins from this literature rather than from a claim that ecology previously lacked state theory or context-sensitive representation. Its narrower target is a particular scientific commitment made whenever a coarse variable assigns two configurations the same label. Let a representation \(q:X\to Q\) map ecological configurations \(x\in X\) to coarse states. Whenever \(q(x)=q(y)\), the representation declares at least some differences between \(x\) and \(y\) irrelevant to the scientific task. That merge may be harmless for one purpose and unacceptable for another.

This issue is distinct from the numerical identity of the ecological system. A lake can remain the same lake through an intervention while a management-state variable ceases to be an adequate predictive description. Conversely, two numerically distinct systems may legitimately share one coarse functional state for a declared comparison. CREST is therefore not a rival metaphysics of ecosystem identity. It is an account of **state-representation adequacy**: under what declared scientific commitments are two configurations allowed to count as the same state?

The program currently formalizes four such commitments. **Future sufficiency** asks whether an enlarged legal future can expose a distinction that the coarse state erased. **Semantic coherence** asks whether an inherited state meaning remains operationally valid after structural replacement. **Mechanism robustness** asks whether retained response mechanisms agree on the future prediction requested from the state. **Evidential licensing** asks whether the available experiment and observation contract actually justify reporting the distinction that the prediction requires. These four obligations are not asserted to exhaust every legitimate ecological notion of state adequacy.

The philosophical claim is contract-relative but not arbitrary. Scientists choose which futures, inherited meanings, candidate mechanisms, observations, and targets belong to a model contract; CREST does not prove that one such contract is uniquely correct for nature. But once those commitments are declared, a proposed merge can fail for explicit reasons. A legal future can distinguish two merged configurations; a structural replacement can make an inherited label operationally incoherent; retained mechanisms can disagree on a successor; and an evidence class can contain multiple target values. Contract-relativity therefore relocates the question from “what is the one true state of the ecosystem?” to “what distinctions must this scientific state preserve?”

## 2. One state label, four different obligations

Consider the coarse ecological state **pollination maintained**. Suppose two configurations receive this label because both currently sustain an adequate amount of pollination. That agreement does not yet tell us whether the configurations should count as the same state for every scientific use of the label. Table 1 summarizes the four obligations currently formalized in CREST. The rows are constraints on one joint state representation, not four rival definitions of ecological state.

**Table 1. Four scientific obligations constraining one contract-relative ecological state.**

| Obligation | Contract varied | A proposed merge fails when | Formal response in CREST |
|---|---|---|---|
| **Future sufficiency** | Legal future operations / composition grammar | A legal future distinguishes configurations that the current state merges | Retain response-relevant distinctions or accept the exact-compression lower bound under the enlarged future repertoire |
| **Semantic coherence** | Structural target and inherited source meaning | A carried state label groups target configurations with different outputs, legal actions, successors, or required history meaning | Apply the coarsest source-relative repair and retain finite history context only where required |
| **Mechanism robustness** | Retained response mechanisms / response types | Mechanisms compatible with the visible state disagree on a requested future response | Retain response-relevant mechanism distinctions, use typed/set-valued prediction, or discriminate experimentally |
| **Evidential / target resolution** | Experiment, observation, reliability, and target contract | One evidence class spans distinctions needed for full-state or target reporting | Keep required resolution separate from earned evidence; preserve ambiguity or strengthen the evidence design |

The four obligations can interact under refinement, so independently minimizing each row once need not recover the joint state. Their common resolution is constructed later through the J1 least common fixed point, after the common-carrier gate.

### 2.1 Future sufficiency

Two configurations can be equivalent under every currently allowed future yet require different state information once future colonization, reconnection, dispersal, or intervention possibilities are opened. CCOC formalizes this as a cross-grammar compression problem. A state representation is exact relative to a declared future grammar when configurations merged by that representation remain indistinguishable under every legal future word.

The central CCOC family compares one fixed controlled system under a closed and an enlarged legal-future grammar. In the closed regime, many micro-configurations can share one exact response class because the futures that would reveal their differences are illegal. In the open regime, dormant differences become individually addressable. The important point for CREST is comparative: the same physical system can support a small exact state under one future contract and a much finer exact state under another.

The lesson is not that future-sensitive state definitions are new; predictive states, bisimulation, MDP abstraction, and causal abstraction already make future or intervention behavior central. The narrower lesson is that **present or closed-context functional equivalence need not remain sufficient under an enlarged future repertoire**. A state label can therefore be exact for its original task without being portable to a newly opened future.

For the pollination example, two communities may behave identically while no substitute pollinator or dispersal route can become active. If a later corridor connection or colonization event makes one dormant difference response-relevant, the earlier merge was not retrospectively false. Rather, the scientific contract has changed. Future-sufficiency failure calls for retaining additional response-relevant information or accepting the resulting lower bound on exact compression.

### 2.2 Semantic coherence

A different failure appears when a state label is inherited across structural change. After pollinator turnover, the label `pollination maintained` may still be syntactically available while no longer grouping target configurations with the same legal actions or future responses.

MLTR fixes an inherited source classification and asks whether its operational meaning remains exact in a target system. When the carried partition fails, iterative refinement yields the unique coarsest exact **source-relative** repair. The repair introduces only those splits forced by target output, legal-action, or successor differences while preserving inherited merges that remain valid.

This is not the same problem as choosing the smallest target abstraction from scratch. If the target system were allowed to adopt any convenient new state space, the inherited meaning could simply be discarded. MLTR instead treats semantic inheritance as a constraint on admissible repair. The question is whether the old variable can continue to mean enough of what it meant before the structural change to remain a valid interface for the target system.

Historical context can matter at the same semantic level. If different declared histories carry incompatible inherited terminal meanings that must be preserved, one route-free inherited label map is insufficient. The formal result retains the minimum finite history context needed to keep those meanings distinct. This does not imply that different histories must always produce different final unlabeled partitions; the claim concerns preservation of the carried meanings.

In the pollination example, a state once adequate under one pollinator assemblage may need to split after turnover into configurations with and without substitute-response capacity. The appropriate correction is not merely “remember more.” It is to repair the inherited classification while preserving as much of its prior operational meaning as the target permits.

### 2.3 Mechanism robustness

The same visible pollination state can also be compatible with several retained response mechanisms. Suppose two candidate mechanisms agree on the present macrostate but disagree about the result of competitor removal, habitat restoration, or another declared intervention. A single deterministic forecast is then not uniformly supported over the retained family.

MRM formalizes this by collapsing raw candidate mechanisms into **response types**. Candidates that induce the same declared transition behavior are predictively equivalent for the task; mechanism distinctions that never change a requested future response need not automatically remain in the state. Conversely, response types that disagree under a relevant action cannot be forgotten if the goal is one candidate-independent deterministic prediction.

This makes mechanism uncertainty a state issue only where it changes the requested response. The result does not say that full mechanism identity must always be represented. When retained mechanisms disagree, the scientifically honest output can instead be typed or set-valued, or a discriminating intervention can be chosen if the declared experimental contract permits one.

This problem is adjacent to adaptive management and POMDP theory, which already combine model uncertainty, action, and observation (Fackler & Pacifici, 2014). CREST uses MRM more narrowly: it asks what equivalence relation on configurations remains safe while a specified family of response alternatives is still retained.

### 2.4 Evidential licensing

Finally, a distinction can be prediction-relevant without being one that current observations license us to report. Camera records, visitation observations, environmental DNA, demographic surveys, or experiments may leave multiple target-relevant worlds compatible.

CED begins from the record induced by a declared finite experiment and observation contract. A deterministic target report is licensed exactly when the target is constant on the compatible evidence class. If compatible worlds imply different target values, the sharp honest report remains ambiguity-explicit.

CED also constructs a target-safe quotient, but its interpretation is crucial. That quotient is the **minimum additional resolution sufficient for target-constant, action-stable deterministic tracking**. It is not a claim that the current data have already identified the true refined state. If one evidence class spans several target-safe blocks, the quotient states what the representation would need to resolve, not what the evidence has earned.

This separates two questions that are often blurred in modelling practice: what distinction would make the model adequate for a requested prediction, and what distinction the observation system currently justifies reporting. More detailed state variables do not become evidence simply because the model would benefit from them.

For the pollination example, a model may correctly identify substitute-response capacity as the distinction required for a management prediction while field observations remain compatible with both possibilities. The remedy is not to refine the reported state by fiat. It is to preserve ambiguity, strengthen the evidence contract, or redesign the experiment.

## 3. Why the four obligations should not be collapsed

The most important philosophical claim of CREST is not that there are exactly four boxes. A sufficiently expressive POMDP, causal model, or other decision framework may encode future actions, histories, mechanism alternatives, observations, and targets in one formal object. Encoding the ingredients together, however, does not make the obligations synonymous.

Future sufficiency begins with a proposed coarse representation and varies the admissible future repertoire. Semantic coherence begins with one inherited representation and constrains target repair by the meaning carried from the source. Mechanism robustness varies over retained response laws while asking what prediction can be supported uniformly. Evidential licensing varies over worlds compatible with a record and reliability contract while asking what can be reported. Their quantifier orders and failure certificates differ.

These differences matter because the remedies differ. Future insufficiency can require more response-relevant state information. Semantic non-portability can require source-relative repair or explicit history context. Mechanism disagreement can require typed or set-valued prediction or discrimination. Evidential non-resolvability can require ambiguity-retaining reporting or stronger evidence. A single scalar “adequacy score” could be useful for a decision problem, but it would obscure which scientific obligation failed.

The distinction is especially clear when representation requirements and empirical achievements are separated. CCOC can identify a distinction that an open-future interface must retain. MLTR can identify a distinction required to preserve inherited semantics. MRM can identify a response-type distinction required for candidate-independent prediction. CED can then show that the current observations still do not license one of those distinctions. More observations do not by themselves repair inherited semantics; a semantic split does not resolve a mechanism family; choosing one mechanism does not make an observation-supported claim; and an evidence-rich description can still be inadequate for an enlarged future.

Nor are the four audits assumed to be logically independent in every possible application. Structural replacement may enlarge the legal future repertoire; an observation design may simultaneously discriminate mechanisms; one split induced by a future audit may cause a later semantic audit to split again. CREST therefore does not infer that the four operators commute or that they can always be solved once and combined without feedback.

### 3.1 From four obligations to one ecological state

Keeping the four obligations distinct does not mean that ecology must end with four different states. The motivating synthesis question is the opposite: **if one ecological state is expected to support all four kinds of scientific work, what should that state be?**

The answer is conditional because the companion theories do not automatically share one world set. Let \(U\) be a declared finite set of latent ecological worlds rich enough to carry the distinctions relevant to the future grammar, inherited semantic labels or history, retained response mechanisms, evidence relation, and report target. Let \(B\) be a baseline partition containing distinctions the analysis is committed to preserving before the four audits are applied.

Represent the four obligations on the partition lattice \(\Pi(U)\) by refinement closures

\[
C_\Gamma,\qquad C_{\mathcal H},\qquad C_\Theta,\qquad C_{D,T}.
\]

Under the conditions of CREST-J1, their common closure above the baseline is

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B).
}
\]

J1 proves that \(J\) is the **unique coarsest, least-information partition satisfying all four declared representational obligations**. For one configuration represented by world \(u\in U\), its CREST state is therefore

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

This gives a precise answer to what the “one state” is. Two configurations count as the same CREST state when the least-information representation satisfying the declared scientific contract is permitted to merge them. They count as different states when at least one obligation, possibly after interacting with refinements generated by another obligation, requires their distinction.

The qualifier is essential. The theorem does not say that the same \(J\) is minimal under a different future repertoire, inherited meaning, mechanism family, target, evidence contract, or latent-world carrier. CREST therefore establishes **conditional joint minimality**, not one intrinsic partition of nature.

The construction also refutes a tempting shortcut. One might independently compute a minimum partition for each audit and combine the four results once. The J1 cascade witness shows that one pass can be insufficient: a distinction created by one audit can make another audit able to expose a new distinction, which can trigger further refinements. Pairwise commutation is not required. Fair repeated refinement reaches the same least common fixed point even when intermediate partitions and pass counts depend on order.

### 3.2 Carrier existence comes before state construction

The conditional state theorem presupposes a common carrier. That assumption cannot simply be hidden inside the notation.

CREST-J3 addresses a universal-action contract by descending to the greatest synchronized transition-closed carrier \(U^*\). CREST-J6 addresses a controlled contract in which all uncontrollable moves must remain safe while at least one admissible control choice is available, yielding a greatest robustly controlled-invariant carrier \(K^*\). If the relevant carrier is empty or fails required coverage, there is no fully adequate joint state under that declared synchronization.

This failure is different from an insufficiently fine partition. If no common carrier exists, further splitting states cannot create a coherent joint world set. The contract itself must be repaired or revised. CREST-J4 and J7 characterize two finite repair languages for the universal and controlled carrier problems, respectively.

The conceptual order is therefore:

\[
\text{common carrier}
\;\longrightarrow\;
\text{required joint state}
\;\longrightarrow\;
\text{evidence licensing}.
\]

These are theorem dependencies, not a mandatory order for fieldwork or modelling practice.

### 3.3 Required state is not necessarily identified state

Even when \(J\) is mathematically well defined, the available evidence may not determine which \(J\)-block is occupied.

Let \(E_D\) be the reliability-qualified evidence partition: worlds in one \(E_D\)-block remain observationally compatible under the declared experiment, detection, failure, and risk assumptions. CREST-J1 gives the exact gate

\[
\boxed{
\text{deterministic full-state report exists}
\iff
J\preceq E_D.
}
\]

If \(J\preceq E_D\), every evidence class lies within one required state block, so the full joint state is reportable. If the relation fails, \(J\) still specifies the resolution an adequate representation would require, but the current evidence does not identify one unique block. The sharp report is then the set of \(J\)-blocks compatible with the evidence.

A requested target can nevertheless remain deterministic without full-state identification. If the target is constant on each evidence class, the target is reportable even when the complete joint state is not. Thus

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{target report}
}
\]

in general.

CREST-O1 makes the separation operational. In its finite witness, the cheapest structural carrier repair costs one unit but leaves the downstream full J1 state unresolved by the declared evidence, whereas a costlier repair is fully licensed. The target remains reportable under the cheaper repair. This does not make the costlier repair normatively better. It shows that carrier feasibility, state adequacy, and evidence licensing are distinct optimization targets.

### 3.4 The ecological state adequacy frontier

The preceding results suggest that one ecological state should not be viewed only as the output of a fixed modelling contract. A second question is how the required state changes when the scientific contract itself changes. Let \(\mathcal C\) denote a declared contract and let \(J_{\mathcal C}\) be its J1 state whenever the relevant carrier gate is admissible. For an evidence record \(e\), let

\[
\mathcal S_{\mathcal C}(e)
=
\{[u]_{J_{\mathcal C}}:u\text{ remains compatible with }e\}.
\]

CREST therefore associates a contract not only with a state partition but with three separable quantities: whether a coherent carrier exists, how fine the least-information adequate state must be, and how many such state blocks remain compatible with the evidence. We call changes among these regimes the **ecological state adequacy frontier**.

The frontier has an order-theoretic asymmetry. Along a comparison in which a stronger contract requires a refinement of the earlier state while the evidence is held fixed, the required state-information burden cannot decrease. If that fixed evidence already fails to identify the coarser state, refining the state cannot restore identification. Conversely, evidence that identifies a finer state necessarily identifies its coarsenings. Scientific requirements can therefore outrun an unchanged monitoring programme.

This effect need not be gradual. The CCOC extremal family shows that adding one previously illegal primitive future action can increase exact state memory by an arbitrary number of bits across a finite family. The point is not a generic priority claim about representation phase transitions. It is that a small change in the ecological future or intervention contract can make a previously adequate ecological classification severely under-resolved even before the physical configuration has changed.

A finite cross-gate witness makes the management implication sharper. Before enrichment, a controlled contract admits a two-world viable carrier whose two required states are identified by the declared evidence. Adding one controllable `rescue` action makes a third world viable. Yet the same action gives two candidate worlds different future behavior, so J1 must split them. The viable carrier therefore expands while the required state count increases from two to three. Because the original monitoring record still merges those two worlds, full-state identification is lost. The requested target remains constant across them and is still reportable.

We call this **management-induced information debt**: expanding what managers can do can expand what they must know. The claim is existential, not universal. New actions need not always increase state resolution. The witness establishes only that greater control authority and easier state identification are not generally aligned.

The associated monitoring burden can be stated exactly. For a fixed evidence partition \(E\) and required state partition \(J\), the unique coarsest refinement of the existing evidence that both preserves its distinctions and licenses deterministic full-state reporting is the common refinement \(E\vee J\). CREST therefore defines the finite monitoring-resolution debt

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

In the `rescue` witness, full-state debt becomes \(\log_2(3/2)>0\) while target debt remains zero. Across the existing CCOC extremal family, one newly relevant future action can induce \(m\) bits of such debt for arbitrary finite \(m\). The common-refinement construction is classical; the point here is its coupling to the CREST carrier/state/evidence gates.

## 4. Contract-relative does not mean arbitrary

The most natural objection is that a contract-relative state is merely conventional: choose a different purpose and obtain a different state. That conclusion does not follow. CREST concerns the adequacy of a **scientific representation**, not the claim that underlying ecological processes depend on our descriptions.

A future grammar specifies which counterfactual operations the representation must survive. An inherited-semantic contract specifies which earlier meanings must be preserved. A mechanism contract specifies which response alternatives remain live. An evidence contract specifies what observation and reliability assumptions license a report. These choices can be debated, revised, or empirically challenged, but once they are stated, the adequacy of a merge is not arbitrary.

This position is compatible with realism about ecological systems and with perspectival or pragmatic accounts of representation (Giere, 2010; Massimi, 2022). A coarse state need not mirror one intrinsic partition of nature to be scientifically constrained. Conversely, usefulness in one setting does not authorize unqualified reuse in another.

The contract also does not make every scientifically defensible state equally good for every purpose. For a fixed admissible contract, J1 picks out the unique coarsest representation that satisfies the declared obligations. The convention enters in declaring the scientific work; the dynamics, inherited semantics, retained alternatives, and evidence determine whether a proposed merge can perform it.

This distinction is especially relevant in ecology because boundaries, scales, and interventions are scientifically consequential. A plot, island, watershed, or community can be represented at multiple levels. CREST does not tell ecologists which level is uniquely correct. It specifies what follows once a state at a chosen level is asked to support a declared set of predictive, semantic, mechanistic, and evidential tasks.

## 5. Consequences for ecological explanation and measurement

The joint-state account changes how ecological state variables should be discussed.

First, **descriptive sameness should be distinguished from predictive sameness**. Two communities can share current observables while differing under a future intervention. A state adequate for current reporting should not automatically be exported to futures outside its original contract.

Second, **transfer of ecological categories is a semantic operation** rather than mere relabelling. Functional groups, resilience classes, occupancy categories, or management states can be reused across sites or time periods only insofar as their operational meaning survives the relevant structural change.

Third, **mechanism uncertainty should be represented only at the level at which it changes conclusions**. If multiple mechanisms induce the same relevant future response, preserving all mechanism identities in the reported state can be unnecessary. If they disagree, collapsing them into one deterministic prediction hides a live scientific alternative.

Fourth, **measurement should be separated from representational requirement**. A model can identify the distinction required for an adequate state without the field protocol having resolved it. The state \(J\) is therefore not automatically an observation. Evidence must earn the right to report a specific \(J\)-block.

Fifth, **state design and monitoring design can be coupled without being identical**. Once \(J\) identifies which distinctions are required, an observation programme can ask which of those distinctions are unresolved and which target decisions remain possible without full-state identification. This turns the state concept into a bridge between representation and measurement without collapsing one into the other.

Sixth, **monitoring adequacy can fail before the ecosystem changes state physically**. A monitoring programme may correctly identify the least-information state required under one intervention repertoire. If restoration, reconnection, colonization, invasion, or management innovation makes new futures scientifically relevant, the required state can refine while the observations remain unchanged. The monitoring programme can therefore become inadequate because the counterfactual responsibilities assigned to the state expanded, not because sensor quality deteriorated or because the ecosystem already crossed a physical regime threshold.

Seventh, **more management capacity can create an epistemic burden**. Additional management options can make previously irrelevant differences consequential. In that regime, increasing control authority and increasing knowledge requirements occur together. This suggests that the design of a new intervention should be coupled to an audit of whether existing monitoring resolves the state distinctions that the intervention makes consequential.

These consequences do not impose a mandatory pipeline in which future sufficiency must be checked first, followed by semantics, mechanism, and evidence. The order used here is explanatory. In an empirical project the evidence model may be specified first; a mechanism family may define relevant actions; or a structural transfer problem may determine the target. CREST's point is that the obligations and their dependencies should remain explicit.

## 6. Position relative to existing adequacy and abstraction theories

The account is intentionally cumulative. Ecological identity theory already analyzes what makes systems the same through change (Cumming & Collier, 2005; Delettre, 2021). Ecological model-adequacy work already asks whether state variables, controls, data, and validation are sufficient for a modelling purpose (Getz et al., 2018). General philosophy of modelling evaluates models and data for adequacy to purpose (Parker, 2020; Bokulich & Parker, 2021). State-and-Transition Models connect ecological states to thresholds and intervention (Stringham et al., 2003). POMDP and adaptive-management theory combine hidden state, observations, actions, and model uncertainty (Nicol & Chadès, 2012; Fackler & Pacifici, 2014). Causal states and causal abstraction formalize predictive or interventional coarse graining (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019).

CREST should therefore not be judged by whether any one ingredient is new. Nor does J1 claim novelty for closure operators, partition lattices, or least common fixed points. Those are established mathematical substrates.

The ecology-specific contribution is therefore not generic purpose-relativity, minimal abstraction, partial observability, representation phase transitions, viability analysis, or a generic link between viability and observability. Viability kernels are established tools in ecosystem management (Cury et al., 2005), and control theory has explicitly connected observability to viability-kernel constructions (Kassara, 2012). CREST's narrower contribution is the architecture produced when four separately owned obligations—future sufficiency, inherited-semantic coherence, retained-mechanism robustness, and evidence/target licensing—are imposed on one coarse ecological state equivalence and passed through an explicit carrier/state/evidence sequence. The ecological state adequacy frontier is the CREST bookkeeping of how those three gate outputs move as the contract changes, not a priority claim for generic adequacy regions. The management-enrichment witness then supplies the stronger cross-gate result: one additional control can enlarge the viable domain, force a finer adequate state, make that state unidentifiable under fixed monitoring, and still leave the declared target reportable. The exact state-versus-target monitoring debt makes that coupling quantitative.

This positioning also explains why CREST is not simply a replacement name for POMDPs or causal abstraction. Those frameworks can encode many of the relevant ingredients and remain indispensable neighbors. The philosophical argument here concerns what scientific commitments are made when ecologists use one coarse state label and what must be true for that label to carry several kinds of scientific work.

Whether this exact ecology-specific synthesis warrants any historical-priority claim remains open and is not needed for the argument. CREST should remain publishable if its contribution is read as a theorem-grounded synthesis rather than the first general theory of adequate representation.

## 7. Limits

CREST does not infer the correct future grammar, source-target relation, mechanism family, evidence model, target, action roles, fallback options, or latent-world carrier from ecological data. These are declared scientific inputs that require empirical and theoretical justification.

The framework does **not** establish one universal joint state independent of scientific contract. What J1 establishes is narrower and stronger than the earlier blanket non-claim: conditional on one admissible finite common carrier and the stated closure conditions, there is a unique coarsest joint state satisfying the four declared obligations. Different carriers, targets, mechanism families, future repertoires, inherited meanings, or evidence contracts can yield different adequate states.

The framework also does not establish that the four obligations exhaust all legitimate criteria for ecological representation, or that one scalar complexity measure can combine CCOC memory, MLTR transport defect, MRM ambiguity, and CED evidence/risk quantities. It does not provide a general stochastic, continuous, infinite-state, approximate, delayed-control, or partial-observation version without additional assumptions.

Nor does every ecological state variable need to be implemented literally as a formal quotient. Many ecological classifications are approximate, qualitative, historically negotiated, or operationally defined. The finite exact results function as conceptual benchmarks that make representational commitments explicit.

Finally, CREST does not decide normative priorities. A management programme may prefer robustness to fine prediction, tolerate ambiguity to reduce monitoring cost, or preserve historical categories for institutional reasons. Contract-relativity requires such commitments to be stated; it does not rank them without additional normative premises.

## 8. Conclusion

CREST makes a more specific claim than the already established point that ecological representations can be purpose-relative. For a fixed coherent contract, the adequate state is the unique coarsest equivalence that preserves the distinctions required for the declared scientific work:

\[
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B),
\qquad
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

Across changing contracts, however, state adequacy has a frontier: the coherent carrier, the minimum required state resolution, and the evidence-compatible state set can move differently. A state may remain mathematically well defined after it ceases to be observationally identifiable; a target may remain reportable after full-state identification is lost; and a strengthened contract may eventually cease to admit any fully adequate joint state.

The finite management-enrichment witness exposes an ecological consequence. Adding an available intervention can make more configurations viable while simultaneously increasing the distinctions that a usable state must encode. Existing monitoring may then become inadequate before the ecosystem has undergone any physical regime shift. In this sense, management capability can create information debt: expanding what can be done can expand what must be known.

This does not turn CREST into a universal theory of ecological ontology. The framework remains conditional on declared futures, meanings, mechanisms, evidence, targets, and synchronization. Its philosophical proposal is instead that ecological sameness is a defeasible scientific commitment whose burden can change as scientific responsibilities change. What counts as the same ecological state is therefore not only contract-relative; it has a structured, testable response to changes in the contract.

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

Lindenmayer, D. B., & Likens, G. E. (2009). Adaptive monitoring: a new paradigm for long-term research and monitoring. *Trends in Ecology & Evolution*, 24(9), 482–486. https://doi.org/10.1016/j.tree.2009.03.005

Lindenmayer, D. B., Likens, G. E., Haywood, A., & Miezis, L. (2011). Adaptive monitoring in the real world: proof of concept. *Trends in Ecology & Evolution*, 26(12), 641–646. https://doi.org/10.1016/j.tree.2011.08.002

Massimi, M. (2022). *Perspectival Realism*. Oxford University Press.

Nicol, S., & Chadès, I. (2012). Which States Matter? An Application of an Intelligent Discretization Method to Solve a Continuous POMDP in Conservation Biology. *PLoS ONE*, 7(2), e28993. https://doi.org/10.1371/journal.pone.0028993

Parker, W. S. (2020). Model Evaluation: An Adequacy-for-Purpose View. *Philosophy of Science*, 87(3), 457–477. https://doi.org/10.1086/708691

Parker, W. S., Carey, C. C., Olsson, F., & Thomas, R. Q. (2026). An adequacy-for-purpose perspective for the environmental sciences. *Frontiers in Ecology and the Environment*, Early View, e70058. https://doi.org/10.1002/fee.70058

Shalizi, C. R., & Crutchfield, J. P. (2001). Computational Mechanics: Pattern and Prediction, Structure and Simplicity. *Journal of Statistical Physics*, 104, 817–879.

Stringham, T. K., Krueger, W. C., & Shaver, P. L. (2003). State and transition modeling: An ecological process approach. *Journal of Range Management*, 56(2), 106–113. https://doi.org/10.2307/4003893

Yates, K. L., Bouchet, P. J., Caley, M. J., Mengersen, K., Randin, C. F., Parnell, S., Fielding, A. H., Bamford, A. J., Ban, S., Barbosa, A. M., et al. (2018). Outstanding Challenges in the Transferability of Ecological Models. *Trends in Ecology & Evolution*, 33(10), 790–802. https://doi.org/10.1016/j.tree.2018.08.001

---

## Submission-control note

- This file is the Biology & Philosophy target manuscript, not the general development draft.
- The abstract is within the current 150–250-word requirement.
- Six keywords are supplied.
- The manuscript now distinguishes unconditional/cross-contract global minimality (not claimed) from J1 conditional unique coarseness on a declared admissible finite common carrier (proved).
- The manuscript now foregrounds the ecological state adequacy frontier and the finite management-induced information-debt witness; neither is presented as a historical-firstness claim.
- Swanson (2026) and Huang (2026) remain in internal novelty audits but are excluded from this reference list under the journal's current published/accepted-only reference rule.
- Author-controlled Competing Interests and Funding statements must be completed before submission.
- Review-manuscript anonymization and separate title-page metadata are controlled by `manuscript/biology_philosophy_submission_handoff.md`.