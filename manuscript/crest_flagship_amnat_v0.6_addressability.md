# Ecological State at a Temporal Cut: Interface-Dependent Interaction

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as a property measured at one moment. We instead model the present as an observational temporal cut through possible ecological worlds and define state as the least information that must survive that cut for a declared scientific contract. Three non-circular responsibilities motivate the construction: inherited history, latent response structure, and future-query grammar. A realizability audit first rules out a tempting shortcut: fixed precomputed companion partitions cannot generate positive one-cut interaction merely by intersection, immutable history cannot activate an inert future closure, and a nontrivial fixed-grammar mechanism family cannot hide at zero candidate-safe debt. We then replace direct coalition-value assignment with an explicit finite grammar, trace semantics, and induced state quotient. The main characterization theorem shows that the minimal interface prerequisite set of a future decoder determines the Möbius interaction order of its addressability cost. With no prerequisite, the cost is a future main effect; with one interface it is pairwise; with both history and latent-response interfaces it is pure three-way. Thus higher-order state debt is not assumed by accounting: it is induced by compositional access structure.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; open composition; interaction

## 1. Introduction

Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results show that time matters dynamically. They do not by themselves answer a representational question: when several possible worlds look the same now, which distinctions must a scientific state retain?

Related formal literatures construct state through predictive or decision equivalence. Computational mechanics merges histories with identical predictive consequences (Shalizi and Crutchfield 2001). Predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001). Bisimulation and state-abstraction methods merge states while preserving declared behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006).

CREST addresses a different composition problem. We take the visible present as a baseline cut and ask what information must survive that cut when several scientific responsibilities meet there. The companion programmes motivating the finite theory are structurally different: MLTR begins from replacement history and inherited semantics; MRM begins from primitive candidate laws and response equivalence; CCOC fixes a controlled law and varies the legal future grammar. CREST does not identify these as interchangeable coordinates. It asks how the state obligations they induce compose.

The central result of this paper is not that a chosen coalition game can be assigned a large three-way term. Instead, we derive coalition values from an explicit grammar, traces, and quotient. A future decoder may require no component interface, one interface, or several. We prove that its minimal prerequisite set determines where the resulting information appears in the Möbius hierarchy. In the history–latent-response–future case, a decoder that genuinely requires both component interfaces produces pure three-way state debt; relaxing either requirement moves the same information to a lower-order term.

This changes the ecological interpretation. Higher-order state debt is not a mysterious extra property of “time.” It records a failure of modular addressability: some future queries can be answered only when multiple retained interfaces are simultaneously available.

## 2. State at an observational temporal cut

Let \(\Omega\) be a declared finite set of possible ecological worlds. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible-present partition

\[
\boxed{B_t=\ker O_t.}
\]

Two worlds lie in one block of \(B_t\) exactly when they are indistinguishable at the declared cut. The present is therefore not the ecological state. It is the baseline observation relative to which a state must be constructed.

For a required state map \(q_t:\Omega\to Q_t\), the visible present is sufficient exactly when

\[
O_t(\omega)=O_t(\omega')
\Longrightarrow
q_t(\omega)=q_t(\omega').
\]

Equivalently, \(q_t\) factors through \(O_t\). CREST defines the adequate ecological state as the least-information quotient that satisfies the declared scientific contract.

## 3. Primitive responsibilities are defined before state

### 3.1 Retrospective history

MLTR fixes a root semantic map

\[
q_r:S_r\to Q_r
\]

and replacement relations. A root-to-terminal path \(p\) induces, when semantically coherent, a carried map \(c_p\). Historical equivalence is derived afterward:

\[
p\equiv_Hp'
\iff
c_p=c_{p'}.
\]

The raw replacement history is therefore primitive relative to the terminal state; the state does not define its own past.

### 3.2 Latent response structure

MRM fixes a visible macrostate set \(Q\), action grammar, and primitive candidate laws \(\theta\). Candidate \(\theta\) supplies transitions

\[
G_a^\theta:Q\to Q.
\]

Response types are derived by equality of complete declared response tables. The retained latent interface is therefore a quotient of primitive candidate laws, not an ontic mechanism label inferred from the final CREST state.

### 3.3 Future query grammar

CCOC fixes a controlled law \(\mathcal M\) and declares a legal future grammar \(\mathcal L\subseteq A^*\). The response profile

\[
\rho_{\mathcal L}^{\mathcal M}(s)
=
\bigl(\operatorname{Tr}_{\mathcal M}(s,w)\bigr)_{w\in\mathcal L}
\]

induces the exact future-response quotient. The future responsibility is therefore a declared query grammar, not a future state variable.

The dependency direction is

\[
\text{primitive history/candidate law/future grammar}
\longrightarrow
\text{response or semantic equivalence}
\longrightarrow
\text{adequate state}.
\]

There is no reverse dependence from the final state into these primitives.

## 4. Realizability boundaries

The first general result is negative.

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

### 4.2 Immutable-history no-activation theorem

Let a post-cut audit be inert on the visible one-class baseline and preserve raw MLTR history under every legal transition. Then the history partition is already fixed by that audit. A zero-debt future audit cannot become nontrivial merely because immutable history was retained.

This rules out interpreting arbitrary refinement cascades as literal past–future interaction when their transitions change the label being called “past.”

### 4.3 Fixed-grammar MRM zero-debt theorem

If the visible MRM partition is already candidate safe under one fixed grammar, all candidates have the same complete response table under that grammar. Hence the response-type quotient is a singleton. A nontrivial fixed-grammar mechanism distinction cannot have zero exact candidate-safe debt and later emerge only after another fixed partition is supplied.

Together these results show that literal higher-order temporal interaction requires more than relabeling an abstract closure cascade.

## 5. Explicit grammar and trace quotient

We now derive state costs instead of assigning them.

### 5.1 Primitive carrier

Let

\[
\Omega_m=P_H\times P_\Theta\times\{0,1\}^m.
\]

The history primitive set \(P_H\) contains two replacement histories with distinct complete carried maps. The mechanism primitive set \(P_\Theta\) contains two primitive candidate laws with distinct complete response tables. Let

\[
a=(a_1,\ldots,a_m)\in\{0,1\}^m
\]

be an exterior response signature. All worlds share one visible cut observation.

The history and mechanism interfaces are not anonymous bits in the implementation: they are derived from carried maps and response tables respectively.

### 5.2 Typed decoder rule

Each responsibility contributes grammar resources:

- \(H\) makes the carried-map interface observable;
- \(\Theta\) makes the response-table interface observable;
- \(F\) contributes exterior decoder primitives.

Fix a minimal decoder prerequisite set

\[
R\subseteq\{H,\Theta\}.
\]

A decoder word for \(a_i\) is well typed in coalition \(S\) exactly when

\[
F\in S
\quad\text{and}\quad
R\subseteq S.
\]

This is the only structural assumption controlling exterior addressability. The grammar generator then produces legal words mechanically. No coalition is assigned a bit value.

### 5.3 State quotient

For a legal word \(w\), let \(\operatorname{Tr}(\omega,w)\) be its carried-map value, response-table value, or decoded exterior bit. Define

\[
\omega\sim_S\omega'
\iff
\operatorname{Tr}(\omega,w)=\operatorname{Tr}(\omega',w)
\quad\forall w\in\mathcal L_S.
\]

The exact state under coalition \(S\) is the induced quotient

\[
Q_S=\Omega_m/\!\sim_S,
\]

with information burden

\[
v_R(S)=\log_2|Q_S|.
\]

The implementation computes \(Q_S\) by enumerating worlds, generating legal words, evaluating all traces, and grouping equal trace profiles.

## 6. Main theorem: interface prerequisites determine interaction order

### Lemma 1 — generated decoder criterion

An exterior decoder exists in \(\mathcal L_S\) iff

\[
F\in S
\quad\text{and}\quad
R\subseteq S.
\]

This follows directly from compositional typing: \(F\) supplies the decoder primitive, and every interface in \(R\) must be available for the composite word to be well formed.

### Lemma 2 — exact quotient cardinality

Let

\[
\delta_H(S)=\mathbf 1_{H\in S},
\qquad
\delta_\Theta(S)=\mathbf 1_{\Theta\in S},
\]

and

\[
\delta_R(S)=\mathbf 1_{F\in S,\ R\subseteq S}.
\]

Then

\[
\boxed{
|Q_S|
=
2^{\delta_H(S)+\delta_\Theta(S)+m\delta_R(S)}.
}
\]

The two carried maps produce two distinguishable history classes whenever \(H\) is present. The two response tables produce two mechanism classes whenever \(\Theta\) is present. If decoder words are absent, all exterior signatures have identical legal traces; if they are present, the \(m\) decoder words recover the complete exterior signature. Because the carrier is a direct product, these factors multiply.

Thus

\[
\boxed{
v_R(S)
=
\delta_H(S)+\delta_\Theta(S)+m\delta_R(S).
}
\]

Crucially, this formula is now a theorem about an explicit trace quotient rather than the definition used by the code.

### Theorem 1 — addressability-order characterization

The exterior term is the unanimity game

\[
m\,\mathbf 1_{R\cup\{F\}\subseteq S}.
\]

Its Möbius transform has one nonzero dividend: \(m\) bits on coalition

\[
R\cup\{F\}.
\]

Therefore:

\[
R=\varnothing
\Longrightarrow
m\text{ bits are an }F\text{ main effect},
\]

\[
R=\{H\}
\Longrightarrow
m(H,F)=m,
\]

\[
R=\{\Theta\}
\Longrightarrow
m(\Theta,F)=m,
\]

and

\[
\boxed{
R=\{H,\Theta\}
\Longrightarrow
m(H,\Theta,F)=m.
}
\]

The same exterior information therefore changes interaction order when the decoder's interface requirements change.

### Corollary — pure three-way interaction is conditional, not automatic

Pure three-way interaction is forced in this family exactly when the future decoder is interface complete with respect to both companion interfaces. If \(F\) can decode the exterior signature alone, the three-way dividend is zero. If only one companion interface is required, the exterior burden becomes pairwise.

This makes the result falsifiable: changing the grammar rule can destroy the headline interaction.

## 7. Numerical illustration

Take \(m=10\).

Under two-interface completeness \(R=\{H,\Theta\}\), the explicit trace quotient gives:

| contract | classes | bits |
|---|---:|---:|
| visible cut | 1 | 0 |
| history | 2 | 1 |
| mechanism | 2 | 1 |
| future only | 1 | 0 |
| history + mechanism | 4 | 2 |
| history + future | 2 | 1 |
| mechanism + future | 2 | 1 |
| **history + mechanism + future** | **4096** | **12** |

The resulting genuine three-way term is 10 bits, or 83.33% of the full 12-bit state. Relative to the history-plus-mechanism quotient, state cardinality increases from 4 to 4096 classes, a 1024-fold amplification.

But these numbers are not universal. If the decoder rule is changed to \(R=\varnothing\), \(F\) alone distinguishes all 1024 exterior signatures and the three-way term becomes zero. If \(R=\{H\}\) or \(R=\{\Theta\}\), the same 10 bits appear as a pairwise dividend. The numerical table is therefore an illustration of the structural theorem, not evidence that ecology generically contains 10-bit three-way effects.

## 8. What this changes for ecological state construction

The theorem identifies a practical failure mode in modular state design.

Suppose a modeller constructs a history summary, a latent-response summary, and a future-response interface separately and then assumes their information costs can be combined additively. That workflow is safe only if every future query factors through the component interfaces in a way that does not require their joint availability.

When a query is **jointly addressable**—that is, it can be evaluated only after several retained interfaces are simultaneously present—its representational cost does not belong to any component in isolation. The interaction order records the number of interface prerequisites required to make that information scientifically addressable.

This interpretation is stronger than saying that history, mechanism, and future are all important. It says that state complexity depends on the architecture of the questions the state must support. Two systems with identical primitive worlds can require different state decompositions under different legal query architectures.

The result also clarifies what CREST does not infer. The theorem cannot determine from accounting alone whether an ecological future query genuinely requires both history and latent-response interfaces. That is a scientific modelling assumption that must be justified by the system's legal response grammar. CREST supplies the consequence once that interface structure is declared.

## 9. Relation to existing state concepts

Ecological memory, hysteresis, and transient dynamics establish that past conditions can affect present and future behavior (Ogle et al. 2015; Scheffer et al. 2001; Hastings et al. 2018). CREST does not claim novelty for temporal dependence itself.

Predictive and causal state theories construct states from equivalence of future predictions (Shalizi and Crutchfield 2001; Littman, Sutton, and Singh 2001). State abstraction and bisimulation preserve declared transition or decision properties while removing irrelevant distinctions (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST shares this quotient perspective.

The contribution here is the composition layer: primitive companion objects are defined before state, realizability constraints rule out several naive temporal interpretations, and the interaction order of additional state information is derived from the minimal interface set required to address that information.

## 10. Scope and retained supporting results

The paper is finite, exact, and contract conditional. It does not claim that history, latent response, and future exhaust ecological state; that every ecological system has a unique decomposition into these roles; that decoder prerequisites are inferable from observations without additional assumptions; or that the theorem automatically extends to stochastic, approximate, continuous-time, or infinite-state systems.

Earlier CREST marked-cycle and fixed-closure three-audit families remain mathematically valid as abstract closure extrema. The realizability audit shows why they should not be interpreted literally as immutable MLTR history and fixed-grammar MRM response types. They are retained as supporting closure theory rather than as the ecological headline.

The exact prefix-count bridges for future-conditioned history and grammar-conditioned mechanism also remain supporting examples. Their shared \(2^k\) frontier reflects the same binary-signature combinatorics; the present paper no longer treats that coincidence as evidence that MLTR and MRM are structurally identical.

## 11. Discussion

The temporal-cut view separates three questions that are often collapsed. What happened before the cut? What latent response structure is compatible with the visible present? What future questions must the state answer? None of these is defined by the final state quotient.

The negative results show that simply naming these three roles does not create higher-order state complexity. Fixed partitions cannot generate positive one-cut interaction by common refinement, immutable history cannot be changed by a future audit, and fixed-grammar response types cannot hide nontrivial exact candidate debt.

The positive theorem locates higher-order complexity more precisely. It arises when future addressability is compositional. Information may exist in the world yet remain irrelevant to a contract until the interfaces required to query it are simultaneously available. The minimal prerequisite set of the decoder then determines the interaction order of the corresponding state burden.

This reframes the earlier pure-three-way example. Its significance is not that one can choose a grammar giving \(m\) three-way bits. Its significance is conditional: **if** a future response is only well defined through both a history-derived interface and a latent-response interface, **then** the exterior information needed for that response appears as genuine three-way state debt. Remove either prerequisite and the order changes exactly as the characterization theorem predicts.

For ecology, the immediate consequence is methodological. State variables should not be chosen only by asking which past, present, or future quantities matter separately. One must also ask which future questions require combinations of those interfaces to be meaningful or executable. That query architecture can change the dimensionality and decomposition of the adequate state even when the underlying possible worlds are unchanged.

## 12. Conclusion

An ecological state is not necessarily the observation made now. It is the least information that must survive an observational temporal cut for the questions a scientific contract declares.

History, latent response, and future query grammar can be defined non-circularly before that state is constructed. Their costs, however, need not compose modularly. In the explicit finite grammar developed here, the interaction order of an exterior information burden is determined by the minimal interface prerequisite set of its decoder.

For the history–latent-response–future case, a decoder requiring both component interfaces produces pure three-way debt of \(m\) bits; allowing the future grammar to bypass either interface moves those same bits to lower-order terms. Higher-order state debt is therefore not assumed by the accounting scheme. It is induced by compositional addressability.

## Literature Cited

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.
