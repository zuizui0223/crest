# Ecological State at a Temporal Cut: Semantic Access and Interface Dependence

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as a property measured at one moment. We instead treat the present as an observational temporal cut and define state as the least information that must survive that cut for a declared scientific contract. Three non-circular responsibilities motivate the construction: inherited history, latent response structure, and future-query grammar. We first establish realizability limits showing that positive temporal interaction cannot be obtained merely by intersecting fixed companion quotients or by allowing future operations to rewrite immutable history. We then activate the semantics of the companion theories: MLTR history modes are derived from carried terminal maps, MRM response types from candidate-safe response tables, and future decoder access from those derived interfaces. The resulting contribution is a modeling identification principle rather than a new Möbius theorem: the interaction order of additional state burden records the minimum ecological interfaces jointly required to address a future query. A shallow-lake restoration model illustrates that this prerequisite set is target relative, ranging from no retained interface for current-status description to joint history-and-mechanism requirements for a composed restoration decision.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; restoration; interface dependence

## 1. Introduction

Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results establish that time matters dynamically. They do not by themselves answer a representational question: when several possible ecological worlds look the same now, which distinctions must a scientific state retain?

Related formal literatures construct state through predictive or decision equivalence. Computational mechanics merges histories with identical predictive consequences (Shalizi and Crutchfield 2001). Predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001). Bisimulation and state-abstraction methods merge states while preserving declared behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006).

CREST addresses a composition and identification problem. We take the visible present as a baseline cut and ask what information must survive that cut when distinct scientific responsibilities meet there. The companion programmes motivating the finite theory are structurally different. MLTR begins from replacement history and inherited semantics. MRM begins from primitive candidate laws and candidate-safe response equivalence. CCOC fixes a controlled law and varies the legal future grammar. CREST does not treat these as interchangeable coordinates. It asks how their induced state obligations compose, and which ecological interfaces a future query actually requires.

The central contribution is therefore not a new identity about Möbius or Harsanyi dividends. Those provide accounting language. The contribution is a modeling correspondence:

\[
\boxed{
\text{minimum ecological interfaces needed to address a future query}
\longleftrightarrow
\text{interaction order of the resulting state burden}.
}
\]

To make that correspondence non-nominal, we derive retrospective modes from MLTR carried semantics and latent-response types from MRM candidate safety before constructing the future decoder. We then show with a shallow-lake restoration model that the prerequisite set is target relative rather than a fixed property of an ecosystem.

## 2. State at an observational temporal cut

Let \(\Omega\) be a declared finite set of possible ecological worlds. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible-present partition

\[
\boxed{B_t=\ker O_t.}
\]

Two worlds lie in one block of \(B_t\) exactly when they are indistinguishable at the declared cut. The present is therefore not the ecological state. It is the observational baseline relative to which a state must be constructed.

For a required state map \(q_t:\Omega\to Q_t\), the visible present is sufficient exactly when

\[
O_t(\omega)=O_t(\omega')
\Longrightarrow
q_t(\omega)=q_t(\omega').
\]

Equivalently, \(q_t\) factors through \(O_t\). CREST defines the adequate ecological state as the least-information quotient that satisfies the declared scientific contract.

## 3. Companion primitives are defined before state

### 3.1 MLTR: retrospective carried semantics

MLTR fixes a root semantic map

\[
q_r:S_r\to Q_r
\]

and declared replacement relations. A root-to-terminal path \(p\) induces, when semantically coherent, a complete carried terminal map \(c_p\). Historical equivalence is derived afterward:

\[
p\equiv_Hp'
\iff
c_p=c_{p'}.
\]

The minimum retained history context is therefore not the raw route identifier. It is the quotient of routes by equality of carried semantics. Different routes may collapse to the same history mode; routes that induce different carried terminal meanings must remain distinct.

### 3.2 MRM: candidate-safe latent response

MRM fixes a visible macrostate set \(Q\), a declared action grammar, and primitive candidate laws \(\theta\). Candidate \(\theta\) supplies transitions

\[
G_a^\theta:Q\to Q.
\]

Two candidates are response equivalent exactly when their complete declared response tables agree. The retained latent interface is therefore the candidate-safe quotient of primitive laws, not a mechanism label imposed from outside.

### 3.3 CCOC: future query grammar

CCOC fixes a controlled law \(\mathcal M\) and declares a legal future grammar \(\mathcal L\subseteq A^*\). The response profile

\[
\rho_{\mathcal L}^{\mathcal M}(s)
=
\bigl(\operatorname{Tr}_{\mathcal M}(s,w)\bigr)_{w\in\mathcal L}
\]

induces the exact future-response quotient. The future responsibility is therefore a declared family of legal questions, not a future state variable inferred from the final quotient.

The dependency direction is

\[
\text{primitive history / candidate law / future grammar}
\longrightarrow
\text{semantic or response equivalence}
\longrightarrow
\text{adequate state}.
\]

There is no reverse dependence from the final state into the primitives.

## 4. Realizability boundaries

The first general result is negative and constrains how temporal interaction may be interpreted.

### 4.1 Fixed-partition no-go

Suppose a one-class visible baseline is refined only by fixed precomputed partitions \(P_i\). Their common refinement satisfies

\[
|P_{\rm joint}|\le\prod_i|P_i|,
\]

and therefore

\[
\boxed{
\log_2|P_{\rm joint}|-
\sum_i\log_2|P_i|
\le0.
}
\]

Positive state interaction cannot arise merely by intersecting already-computed companion quotients.

### 4.2 Immutable-history no-activation result

If a post-cut audit is inert on the visible baseline and every legal transition preserves raw MLTR history, then retaining history cannot later activate that audit by changing the past. This rules out interpreting arbitrary refinement cascades as literal past–future interaction when the transition changes the label being called retrospective history.

### 4.3 Fixed-grammar MRM zero-debt result

If the visible MRM partition is already candidate safe under one fixed grammar, all retained candidates have the same complete response table under that grammar. The corresponding response-type quotient is therefore a singleton. A nontrivial fixed-grammar mechanism distinction cannot be invisible at exact candidate-safe state and then emerge only after an unrelated fixed partition is added.

These boundaries force interaction to reside in contract-conditioned relevance or addressability rather than in relabeling a generic closure cascade.

## 5. Activating the companion semantics

A key revision from earlier CREST drafts is that MLTR and MRM no longer enter merely as binary interface labels.

### 5.1 A nontrivial MLTR witness

Consider three declared replacement histories

\[
p_1,p_2,p_3.
\]

Their complete carried terminal maps satisfy

\[
c_{p_1}=c_{p_2}\neq c_{p_3}.
\]

Thus three raw routes induce only two semantic history modes:

\[
\boxed{|H_{\min}|=2.}
\]

The collapse of \(p_1\) and \(p_2\) is not imposed by route identity; it follows from equality of their carried meanings. Replacing one route by another with the same carried map leaves the CREST history interface unchanged.

### 5.2 A nontrivial MRM witness

Consider three primitive candidate laws

\[
\theta_1,\theta_2,\theta_3.
\]

Suppose their complete response tables satisfy

\[
G^{\theta_1}=G^{\theta_2}\neq G^{\theta_3}
\]

on the declared action grammar. The exact candidate-safe quotient therefore has two response types:

\[
\boxed{|\Theta|=2.}
\]

Again the reduction is semantic: replacing \(\theta_1\) by the distinct but response-equivalent \(\theta_2\) does not alter the retained latent-response interface.

### 5.3 Semantic access rather than axis labels

A future decoder is allowed to depend on the derived history mode and derived response type, not on raw route or candidate identifiers. Let

\[
A_f\subseteq H_{\min}\times\Theta
\]

be the semantic access relation for future query \(f\). A decoder is legal at a world only through the semantic pair represented by that world. This makes the composition sensitive to path coherence and candidate safety themselves.

The interaction accounting used below is therefore downstream of the companion semantics rather than a substitute for them.

## 6. Modeling identification: prerequisites determine where state cost appears

Let \(R_f\) denote the minimal retained interface set required to make future query \(f\) addressable. In the simplest axis-level projection,

\[
R_f\subseteq\{H,\Theta\}.
\]

If an \(m\)-bit exterior response is decodable whenever \(F\) and all interfaces in \(R_f\) are present, then its state cost appears on coalition

\[
R_f\cup\{F\}.
\]

For the familiar four cases:

\[
R_f=\varnothing
\]

places the exterior burden in the future main effect;

\[
R_f=\{H\}
\]

places it in history–future interaction;

\[
R_f=\{\Theta\}
\]

places it in latent-response–future interaction; and

\[
R_f=\{H,\Theta\}
\]

places it in the three-way term.

This Möbius allocation is standard unanimity-game accounting. CREST does not claim mathematical novelty for that transform. The scientific content is the identification of \(R_f\), or more generally the semantic access relation \(A_f\), from the ecological meaning of the companion interfaces and the legal future task.

The important modeling consequence is therefore:

> higher-order state burden is evidence that a future scientific query is jointly addressable through several retained interfaces, not evidence that “history,” “mechanism,” and “future” are intrinsically higher-order variables.

## 7. A target-relative shallow-lake identification model

Shallow-lake restoration supplies a useful ecology-grounded mapping because the same coarse present water-quality description can be compatible with different nutrient histories and different feedback structures, while restoration decisions query different combinations of those distinctions.

We use the published restoration literature only to justify the qualitative ingredients: historical nutrient loading and sediment phosphorus legacy; internal phosphorus persistence; fish-community and macrophyte feedbacks; and multiple restoration actions including load reduction, sediment-focused treatment, biomanipulation, and macrophyte restoration. This is a literature-grounded finite decision model, not an empirical estimate of a universal CREST partition.

Let the visible cut record a coarse current turbid/eutrophic status. Retrospective modes summarize whether the management-relevant past includes a persistent nutrient/sediment legacy. Latent-response types summarize whether current resistance is compatible with sediment-internal loading versus biological feedback structure. We then consider four targets.

### 7.1 Current-status description

Target:

> Is the lake currently turbid/eutrophic?

No retrospective or latent-response interface is required beyond the visible cut. Hence

\[
R_{\rm status}=\varnothing.
\]

### 7.2 Legacy-sensitive recovery assessment

Target:

> After external-load reduction, is delayed recovery attributable to a retained nutrient/sediment legacy that must be accounted for in the decision?

The target explicitly depends on retrospective legacy semantics. In the finite worked model,

\[
R_{\rm legacy}=\{H\}.
\]

### 7.3 Mechanism-specific intervention choice

Target:

> Which supplementary intervention is indicated by the current latent response structure?

The distinction between sediment-focused and food-web/macrophyte-focused intervention channels depends on response type. In the finite worked model,

\[
R_{\rm mechanism}=\{\Theta\}.
\]

### 7.4 Composed restoration policy

Target:

> Given both the inherited restoration context and the latent response type, which composed restoration policy should be regarded as operationally adequate?

For this explicitly composed target, the finite decision rule is defined on the semantic product

\[
H_{\min}\times\Theta.
\]

Neither interface alone identifies the same decision map, so

\[
R_{\rm composed}=\{H,\Theta\}.
\]

This does not assert that every real shallow lake or every restoration objective has this prerequisite set. The point is target relativity: the same ecological system can induce different state interaction orders because different scientific questions require different interfaces.

## 8. What the shallow-lake case contributes

The worked case closes a gap left by the abstract grammar theorem. CREST itself cannot infer the correct prerequisite set from Möbius accounting. The prerequisite must come from the ecological question and the semantics of the retained interfaces.

This matters for state design. A modeler who builds a history summary, a latent-response summary, and a future-response interface independently may be justified for one target and under-resolved for another. The adequacy of modular state design depends on whether the relevant future query factors through the modules separately or only through their joint semantic product.

For ecology, the useful output is therefore not a universal number of interaction bits. It is a disciplined question:

\[
\boxed{
\text{Which retained ecological interfaces are minimally required to answer this future target?}
}
\]

The interaction decomposition is then a diagnostic consequence of that answer.

## 9. Numerical illustration as accounting, not novelty

For continuity with the finite benchmark, suppose a future query carries \(m=10\) exterior response bits and requires both retained interfaces. With two history modes and two response types, the history-plus-mechanism state has four classes and two bits. When the future query becomes legal, the full state has

\[
4\times2^{10}=4096
\]

classes and 12 bits. Standard Möbius accounting assigns the additional 10 bits to the three-way term.

These values are not ecological constants and are not the paper's mathematical novelty. Changing the prerequisite set moves the same 10-bit burden to a lower-order term. The benchmark serves only to make the representational consequence of prerequisite identification numerically transparent.

## 10. Relation to existing state concepts

Ecological memory, hysteresis, and transient dynamics establish that antecedent conditions can affect current and future behavior (Ogle et al. 2015; Scheffer et al. 2001; Hastings et al. 2018). CREST does not claim novelty for temporal dependence itself.

Predictive and causal state theories construct states from equivalence of future predictions (Shalizi and Crutchfield 2001; Littman, Sutton, and Singh 2001). State abstraction and bisimulation preserve declared transition or decision properties while removing irrelevant distinctions (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST shares this quotient substrate and does not claim it as new mathematics.

The narrower contribution is a scientific modeling architecture in which retrospective semantics, latent-response equivalence, and future-query legality are defined separately before state, strict realizability checks prevent circular temporal interpretations, and target-specific future access determines how those interfaces must compose at a common temporal cut.

## 11. Scope and supporting mathematics

The paper is finite, exact, and contract conditional. It does not claim that history, latent response, and future exhaust ecological state; that every ecological system has a unique decomposition into these roles; that prerequisite sets are inferable from observational data without additional assumptions; or that the framework automatically extends to stochastic, approximate, continuous-time, or infinite-state systems.

Earlier CREST marked-cycle and fixed-closure three-audit families remain mathematically valid as abstract closure extrema. The realizability audit shows why they should not be interpreted literally as immutable MLTR history and fixed-grammar MRM response types. The earlier direct-value compositional module is retained only as a closed-form corollary of the explicit trace quotient and is regression-tested against it for every coalition.

## 12. Discussion

The temporal-cut formulation separates three questions that are often conflated. What happened before the cut? What latent response distinctions remain possible at the cut? Which future questions must the state support? None of these is defined by the final state itself.

The realizability results show that positive interaction does not appear merely because three labels are intersected. The semantic companion construction then shows why the labels themselves are insufficient: raw histories must be quotiented by carried meaning, and candidate mechanisms by response equivalence, before future access can be specified coherently.

The shallow-lake example illustrates the ecological payoff of this separation. “What is the lake now?”, “does historical nutrient legacy matter?”, “which mechanism-specific intervention is appropriate?”, and “which composed restoration policy is adequate?” are questions about the same system but need not induce the same state. Their difference lies in what information the future target can legitimately address.

This is the practical sense in which ecological state is contract relative without being arbitrary. The scientific question is declared by the investigator, but the admissible compression is constrained by semantic transport, candidate response structure, legal future queries, and the evidence required to distinguish the resulting state classes.

## 13. Conclusion

The present need not be the ecological state. It can be the observational cut at which a state must be constructed.

CREST defines retrospective history, latent response, and future query obligations before that state, then asks which distinctions must survive their composition. The principal contribution is not a new Möbius identity. It is an identification discipline: derive history modes from carried semantics, derive latent types from candidate-safe response, identify the minimum ecological interfaces required by the future target, and only then compute the induced state quotient and interaction accounting.

In this view, higher-order state interaction is not an intrinsic property of time. It is a signature of joint scientific addressability.

## Literature Cited

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.
