# Ecological State at a Temporal Cut: Sparse Semantic Access

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as a property measured at one moment. We instead treat the present as an observational temporal cut and define state as the least information that must survive that cut for a declared scientific contract. Retrospective history, latent response structure, and future-query grammar are defined before state through separate companion semantics. A realizability audit rules out several tempting but circular temporal interpretations. We then connect those semantics directly to the state quotient: MLTR routes collapse by carried terminal meaning, MRM candidates collapse by complete response equivalence, and future decoders are licensed only on specified semantic history-by-response pairs. This exposes a distinction hidden by complete-interface models. If N semantic pairs exist but only k are future-addressable, an m-bit decoder yields (N-k)+k2^m joint state classes and a three-way state dividend log2[((N-k)+k2^m)/N], approaching m-log2(N/k). Thus prerequisite order and semantic coverage control different aspects of state interaction. A shallow-lake restoration model makes prerequisite identification executable and target relative rather than a fixed property of the ecosystem.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; semantic access; restoration

## 1. Introduction

Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results establish that time matters dynamically. They do not by themselves answer a representational question: when several possible ecological worlds look the same now, which distinctions must a scientific state retain?

Related formal literatures construct state through predictive or decision equivalence. Computational mechanics merges histories with identical predictive consequences (Shalizi and Crutchfield 2001). Predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001). Bisimulation and state-abstraction methods merge states while preserving declared behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006).

CREST addresses a composition and identification problem. We take the visible present as a baseline cut and ask what information must survive that cut when distinct scientific responsibilities meet there. The companion programmes motivating the finite theory are structurally different. MLTR begins from replacement history and inherited semantics. MRM begins from primitive candidate laws and candidate-safe response equivalence. CCOC fixes a controlled law and varies the legal future grammar. CREST does not treat these as interchangeable coordinates. It asks how their induced state obligations compose, which semantic combinations a future query can actually address, and how that access structure changes the required state.

The paper does not claim mathematical novelty for Möbius inversion or unanimity games. Those provide accounting language. The contribution is a modeling architecture with two separate identification objects:

\[
\boxed{
\text{interface prerequisite set}
\quad\text{and}\quad
\text{semantic access relation}.
}
\]

The first determines which retained interfaces must be present before a future query is well formed. The second determines on which combinations of those semantic interfaces the query is actually licensed. Complete addressability is therefore a special case, not a default assumption.

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

and declared replacement relations. A root-to-terminal path \(p\) induces, when carriage is defined, a complete carried terminal map \(c_p\). Historical equivalence is derived afterward:

\[
p\equiv_Hp'
\iff
c_p=c_{p'}.
\]

The retained history context is therefore not a route identifier. It is a quotient of routes by equality of carried semantics. CREST consumes these completed carried maps rather than reimplementing MLTR's relation-composition proof machinery.

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

There is no reverse dependence from the final state into these primitives.

## 4. Realizability boundaries

The first general results are negative and constrain how temporal interaction may be interpreted.

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

If a post-cut audit is inert on the visible baseline and every legal transition preserves raw MLTR history, then retaining history cannot later activate that audit by changing the past. This rules out reading arbitrary refinement cascades as literal past-future interaction when the transition itself rewrites the variable being called retrospective history.

### 4.3 Fixed-grammar MRM zero-debt result

If the visible MRM partition is already candidate safe under one fixed grammar, all retained candidates have the same complete response table under that grammar. The corresponding response-type quotient is therefore a singleton. A nontrivial fixed-grammar mechanism distinction cannot be invisible at exact candidate-safe state and then emerge only after an unrelated fixed partition is added.

These boundaries force positive temporal interaction to reside in contract-conditioned relevance or addressability rather than in relabeling a generic closure cascade.

## 5. Activating companion semantics

Earlier CREST drafts treated the history and latent-response interfaces too nominally. The current construction uses the semantic outputs themselves.

### 5.1 History modes

Consider three declared replacement histories

\[
p_1,p_2,p_3
\]

whose complete carried terminal maps satisfy

\[
c_{p_1}=c_{p_2}\neq c_{p_3}.
\]

Three raw routes therefore induce two retained semantic history modes:

\[
\boxed{|H_{\min}|=2.}
\]

Replacing \(p_1\) by \(p_2\) leaves the retained interface unchanged because their carried meaning is identical.

### 5.2 Response types

Consider three primitive candidate laws

\[
\theta_1,\theta_2,\theta_3
\]

whose complete response tables satisfy

\[
G^{\theta_1}=G^{\theta_2}\neq G^{\theta_3}.
\]

The exact candidate-safe quotient has two response types:

\[
\boxed{|\Theta|=2.}
\]

Replacing \(\theta_1\) by the distinct but response-equivalent \(\theta_2\) leaves the retained latent interface unchanged.

### 5.3 Semantic access relation

A future decoder is allowed to depend on the derived history mode and derived response type, not on raw route or candidate identity. Let

\[
A_f\subseteq H_{\min}\times\Theta
\]

be the semantic access relation for future query \(f\). A decoder may require both interfaces syntactically yet be licensed on only a subset of their semantic product.

This distinction is the central v0.7 revision. The prerequisite set determines **which interfaces must be present**. The access relation determines **where within their semantic product the decoder is actually meaningful or legal**.

## 6. Sparse semantic access

Let

\[
r=|H_{\min}|,
\qquad
s=|\Theta|,
\qquad
N=rs.
\]

Assume every semantic pair occurs in the finite carrier. Let

\[
A_f\subseteq H_{\min}\times\Theta,
\qquad |A_f|=k.
\]

Suppose the future query has an exterior response signature

\[
a\in\{0,1\}^m
\]

and requires both retained interfaces before it is syntactically well formed. On an addressable semantic pair, the legal decoder distinguishes all \(2^m\) exterior signatures. On a non-addressable pair, all exterior signatures collapse to one inaccessible trace class.

The grand-coalition state therefore has

\[
\boxed{
|Q_{H\Theta F}|=(N-k)+k2^m.
}
\]

The proper-coalition state sizes are

\[
|Q_H|=r,
\quad
|Q_\Theta|=s,
\quad
|Q_F|=1,
\]

\[
|Q_{H\Theta}|=N,
\quad
|Q_{HF}|=r,
\quad
|Q_{\Theta F}|=s,
\]

because the exterior decoder requires both semantic interfaces.

With

\[
v(S)=\log_2|Q_S|,
\]

the three-way state dividend becomes

\[
\boxed{
d_{H\Theta F}
=
\log_2\frac{(N-k)+k2^m}{N}.}
\]

This quantity is generally non-integer. Complete addressability is the boundary case \(k=N\), giving \(d_{H\Theta F}=m\). If \(k=0\), the decoder is nowhere addressable and the dividend is zero.

For fixed \(N\) and \(k>0\),

\[
\boxed{
d_{H\Theta F}
=
m-\log_2(N/k)+o(1)}
\]

as \(m\to\infty\). Thus sparse semantic access creates an asymptotic penalty

\[
\boxed{\log_2(N/k)}
\]

relative to the complete-access case.

This result changes the **magnitude**, not the interaction order, while both history and latent response remain syntactic prerequisites. The higher-order location still follows standard Möbius accounting; semantic coverage controls how much information reaches that location.

## 7. Canonical finite witness

The current companion witness has two history modes and two response types, so

\[
N=4.
\]

Only one semantic pair licenses the future decoder, so

\[
k=1.
\]

Hence

\[
|Q_{H\Theta F}|=3+2^m
\]

and

\[
\boxed{
d_{H\Theta F}=\log_2((3+2^m)/4).}
\]

For three benchmark depths:

| \(m\) | grand classes | grand bits | three-way dividend |
|---:|---:|---:|---:|
| 4 | 19 | 4.24793 | 2.24793 |
| 8 | 259 | 8.01681 | 6.01681 |
| 10 | 1027 | 10.00422 | 8.00422 |

The deficit from complete addressability tends to two bits because

\[
\log_2(N/k)=\log_2 4=2.
\]

The earlier 4096-class, 12-bit, 10-bit-three-way calculation is retained as the full-access boundary \(k=N=4\), not as the canonical semantic witness.

## 8. Target-relative shallow-lake prerequisite identification

Shallow-lake restoration supplies an ecology-grounded finite decision model because the same coarse current water-quality description can be compatible with different nutrient histories and different feedback structures, while restoration questions require different retained information.

The model uses published restoration literature only to justify qualitative ingredients: historical nutrient loading and sediment phosphorus legacy; internal phosphorus persistence; fish-community and macrophyte feedbacks; and multiple restoration actions including load reduction, sediment-focused treatment, biomanipulation, and macrophyte restoration. It is not an empirical estimate of a universal CREST partition.

The executable model contains four worlds behind the same coarse visible status, crossing two retrospective modes with two latent-response types. For each target, CREST tests whether the target output factors through no retained interface, history only, latent response only, or both. It also performs explicit counterfactual substitution of one interface while holding the other fixed.

The resulting minimum prerequisite sets are

\[
R_{\rm status}=\varnothing,
\]

\[
R_{\rm legacy}=\{H\},
\]

\[
R_{\rm mechanism}=\{\Theta\},
\]

and

\[
\boxed{R_{\rm composed}=\{H,\Theta\}.}
\]

For the composed restoration target, substituting either the retained history mode or the latent response type can change the policy output while the other interface and visible cut are held fixed. Thus the two-interface prerequisite is an executable property of the declared finite decision map, not a markdown label.

This does not assert that every real shallow lake or every restoration objective has this prerequisite set. The same ecological system produces four different prerequisite structures because the target changes.

## 9. What the modeling result means

CREST itself cannot infer the correct prerequisite set or semantic access relation from Möbius accounting. Those objects must come from the ecological meaning of the retained interfaces and the legal future task.

This matters for modular state design. A modeler who constructs a history summary, a latent-response summary, and a future-response interface independently may be justified for one target and under-resolved for another. Even when both interfaces are required, assuming complete access across their Cartesian product can overstate state complexity. The relevant questions are therefore

\[
\boxed{
\text{Which interfaces are minimally required?}
}
\]

and, separately,

\[
\boxed{
\text{On which semantic combinations are the future queries actually addressable?}
}
\]

Interaction accounting is a diagnostic consequence of those answers.

## 10. Relation to existing state concepts

Ecological memory, hysteresis, and transient dynamics establish that antecedent conditions can affect current and future behavior (Ogle et al. 2015; Scheffer et al. 2001; Hastings et al. 2018). CREST does not claim novelty for temporal dependence itself.

Predictive and causal state theories construct states from equivalence of future predictions (Shalizi and Crutchfield 2001; Littman, Sutton, and Singh 2001). State abstraction and bisimulation preserve declared transition or decision properties while removing irrelevant distinctions (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST shares this quotient substrate and does not claim it as new mathematics.

The narrower contribution is a scientific modeling architecture in which retrospective semantics, latent-response equivalence, and future-query legality are defined separately before state; strict realizability checks prevent circular temporal interpretations; and both prerequisite structure and semantic coverage are propagated into one exact state quotient.

## 11. Scope and supporting mathematics

The paper is finite, exact, and contract conditional. It does not claim that history, latent response, and future exhaust ecological state; that every ecological system has a unique decomposition into these roles; that prerequisite sets or access relations are inferable from observational data without additional assumptions; or that the framework automatically extends to stochastic, approximate, continuous-time, or infinite-state systems.

Earlier CREST marked-cycle and fixed-closure three-audit families remain mathematically valid as abstract closure extrema. The realizability audit shows why they should not be interpreted literally as immutable MLTR history and fixed-grammar MRM response types. The earlier direct-value compositional module is retained only as a closed-form corollary of the complete-access trace quotient and is regression-tested against it for every coalition.

The sparse-access result should also not be oversold as difficult game theory. Once the semantic quotient and access relation are specified, its cardinality formula follows by finite counting. The modeling contribution lies in making semantic coverage an explicit state-construction object and in separating it from interface prerequisite order.

## 12. Discussion

The temporal-cut formulation separates three questions that are often conflated. What happened before the cut? What latent response distinctions remain possible at the cut? Which future questions must the state support? None of these is defined by the final state itself.

The realizability results show that positive interaction does not appear merely because three labels are intersected. The semantic companion construction then shows why the labels themselves are insufficient: raw histories must be quotiented by carried meaning, and candidate laws by response equivalence, before future access can be specified coherently.

Sparse access adds a second correction. Even after both semantic interfaces are retained, a future query need not be meaningful across their entire product. Complete addressability therefore overestimates the number of exterior distinctions that survive into the state whenever only a subset of semantic combinations licenses the decoder.

The shallow-lake example illustrates the ecological payoff. “What is the lake now?”, “does historical nutrient legacy matter?”, “which mechanism-specific intervention is appropriate?”, and “which composed restoration policy is adequate?” are questions about the same system but induce different prerequisite sets. A second layer of system-specific work would then ask which history-response combinations actually support each future query.

This is the practical sense in which ecological state is contract relative without being arbitrary. The scientific question is declared by the investigator, but admissible compression is constrained by semantic transport, candidate response structure, legal future queries, and the evidence required to distinguish the resulting state classes.

## 13. Conclusion

The present need not be the ecological state. It can be the observational cut at which a state must be constructed.

CREST defines retrospective history, latent response, and future-query obligations before that state, then asks which distinctions must survive their composition. The principal contribution is an identification discipline: derive history modes from carried semantics, derive latent types from candidate-safe response, identify the minimum ecological interfaces required by the future target, identify where within their semantic product that target is actually addressable, and only then compute the induced state quotient and interaction accounting.

In this view, higher-order state interaction is not an intrinsic property of time. It is a signature of joint scientific addressability, attenuated when that addressability is semantically sparse.

## Literature Cited

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.
