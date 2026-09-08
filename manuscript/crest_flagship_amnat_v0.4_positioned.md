# Ecological State at a Temporal Cut: Interaction Across Time

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as a property measured at one moment. We instead model the present as an observational temporal cut through possible ecological worlds. The cut induces a baseline partition of worlds that look identical now; a scientifically adequate state may still need distinctions from history, latent contemporaneous response structure, or counterfactual future response. On a declared finite carrier, these responsibilities act as refinement closures, and state is their least-information common fixed point. We show that the required information is not generally separable across temporal positions. In one finite family, history alone costs one bit and future alone zero, yet their joint state requires \(\log_2 n\) bits, giving unbounded interaction \(\log_2 n-1\). In a stronger three-way family, history costs one bit while latent-present and future responsibilities each cost zero alone, but the joint state has \(b\) bits and the genuine three-way interaction is \(b-\log_2 3\). At \(b=10\), one visible present class expands to 1024 required state classes; 9 of 10 bits are interaction-generated and 8.415 bits are genuine three-way interaction. Ecological state is therefore the least information that must survive the present cut, not merely the variables observed there.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; counterfactual response; non-additivity

## 1. Introduction

Ecologists already know that the present can carry signatures of the past. Antecedent conditions can generate measurable ecological memory (Ogle et al. 2015), hysteresis can make ecosystem response depend on history (Scheffer et al. 2001), and long transient dynamics can make instantaneous conditions a poor guide to where a system is going (Hastings et al. 2018). These results establish that time matters dynamically. They do not, by themselves, answer a different representational question: **when several possible worlds look the same now, which distinctions must a scientific state retain?**

A parallel literature has asked related questions in formal state construction. Computational mechanics groups histories that have the same predictive consequences into minimal predictive states (Shalizi and Crutchfield 2001). Predictive state representations encode dynamical state using multi-step, action-conditional predictions (Littman, Sutton, and Singh 2001). In decision processes, bisimulation and state-abstraction theories merge ground states while preserving specified behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). These are direct intellectual neighbors of the present work.

CREST does not claim novelty for the facts that history can matter, future predictions can define state, hidden structure can matter, or state abstraction can be formulated as an equivalence relation. The question here is narrower: **what happens when retrospective, latent-contemporaneous, and prospective responsibilities act on the same present description?**

We formalize the present as an observational temporal cut. The cut itself is not assumed to be the ecological state. Instead, the state is the least information about possible worlds that must remain available at that cut to satisfy the declared scientific responsibilities. We then ask whether the information required from different temporal positions can be computed independently.

The answer is no. In finite exact families, past-by-future interaction is unbounded. More strongly, genuine history-by-latent-present-by-future interaction is unbounded and can asymptotically account for essentially the entire information content of the required state. The contribution is therefore a state-construction theorem about **interaction across temporal positions**, not a generic claim that ecology has memory or that coarse graining exists.

## 2. Model: the present as an observational cut

Let \(\Omega\) be a declared finite set of possible ecological worlds. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the present observational partition

\[
\boxed{B_t=\ker O_t.}
\]

Two worlds lie in the same block of \(B_t\) exactly when they are indistinguishable under the declared observation at the cut.

For a visible value \(y\in Y_t\), define the fiber

\[
L_t(y)=O_t^{-1}(y).
\]

The fiber contains all latent worlds compatible with one observed present. It is not a third time interval. It is the hidden contemporaneous structure behind the observational cut.

This gives the state concept used throughout the paper:

\[
\boxed{
\text{ecological state = the least information that must survive the temporal cut.}
}
\]

“Survive” is representational, not causal. A counterfactual future may change what the state representation must preserve without changing the physical past or implying backward causation.

### 2.1 History: information to the left of the cut

Let \(H_{<t}\) denote retrospective information that may matter for the declared scientific task. In the companion MLTR programme, history enters through carried semantics and replacement routes: two systems with the same present label can inherit different operational meanings after different structural histories. At the CREST level, the required distinctions are represented by a history refinement closure

\[
C_H.
\]

Ecological memory and hysteresis provide biological reasons to expect retrospective dependence (Ogle et al. 2015; Scheffer et al. 2001), but the closure here is a representational responsibility rather than a statistical memory estimator.

### 2.2 Latent present: information transverse to the cut

Two worlds can share the same \(O_t(\omega)\) while differing in response-relevant contemporaneous structure. Write that latent structure schematically as \(\Theta_t\). It lives inside the fiber \(L_t(y)\), transverse to the time cut.

This is the CREST position of MRM: the scientific state need not retain complete mechanism identity, only latent distinctions that alter a declared response, intervention consequence, or report. The corresponding refinement closure is

\[
C_\Theta.
\]

### 2.3 Future: information to the right of the cut

The prospective coordinate is not a single realized future. It is the declared counterfactual response structure the state is expected to support. Newly addressable interactions, interventions, connections, or response tests can make a currently erased distinction scientifically relevant.

This is the CREST position of CCOC, represented by

\[
C_F.
\]

Predictive and action-conditional state representations already show that future tests can define useful state descriptions (Shalizi and Crutchfield 2001; Littman, Sutton, and Singh 2001). CREST asks what happens when that future responsibility is combined with retrospective and latent-present responsibilities on the same observational cut.

The three responsibilities developed here are not claimed to exhaust every legitimate notion of ecological state.

## 3. Methods: least-information state and interaction accounting

On one declared finite common carrier, let \(C_H,C_\Theta,C_F\) be monotone, inflationary, idempotent refinement closures acting above \(B_t\). The adequate CREST state is the least common fixed point

\[
\boxed{
J_t=(C_H\vee C_\Theta\vee C_F)(B_t).
}
\]

The fixed-point and partition-refinement machinery is classical. Comparable minimization questions appear in predictive-state and bisimulation/state-abstraction theories (Shalizi and Crutchfield 2001; Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST uses this machinery to pose a different accounting problem at one temporal cut.

For any coalition \(S\subseteq\{H,\Theta,F\}\), let \(J_S\) be the least common fixed point of the closures in \(S\) above the same baseline and define

\[
v(S)=\log_2|J_S|-\log_2|B_t|,
\qquad v(\varnothing)=0.
\]

The standalone debts are

\[
D_H=v(H),\qquad D_\Theta=v(\Theta),\qquad D_F=v(F),
\]

and the full joint debt is

\[
D_{H\Theta F}=v(H\Theta F).
\]

Define the generic non-additive debt

\[
\boxed{
\Delta=D_{H\Theta F}-(D_H+D_\Theta+D_F).
}
\]

To localize the non-additivity, use the exact Möbius/Harsanyi decomposition of the finite coalition value function. For example,

\[
m(H,F)=v(HF)-v(H)-v(F),
\]

and the genuine three-way term is

\[
\boxed{
\begin{aligned}
m(H,\Theta,F)
={}&v(H\Theta F)-v(H\Theta)-v(HF)-v(\Theta F)\\
&+v(H)+v(\Theta)+v(F).
\end{aligned}
}
\]

Möbius inversion itself is not a novelty claim. The theorem concerns the size of these interaction terms in finite ecological state construction.

## 4. Results I: past-by-future interaction is unbounded

### Theorem 1

For every integer \(n\ge2\), there exists a finite CREST contract in which all latent worlds share one visible present class and

\[
D_H=1,
\qquad
D_F=0,
\]

but

\[
D_{HF}=\log_2 n.
\]

Therefore

\[
\boxed{m(H,F)=\log_2 n-1,}
\]

which is unbounded as \(n\to\infty\).

### Construction

Take \(n\) latent worlds with an indiscrete present-cut partition. The history closure marks one world, producing exactly two classes. The future closure is a directed cycle. Acting on the untouched present partition, the future closure costs zero because all successors remain inside one block. Once the historical mark is retained, successor stability propagates that distinction around the cycle until every world is distinct.

History alone therefore asks for one bit, future alone for no additional bit, yet the conjunction requires \(\log_2 n\) bits.

The result formalizes

\[
\boxed{
\text{how much of the past must survive the present depends on what future the state must support.}
}
\]

This is interaction or coupling, not statistical confounding.

At \(n=1024\), independent accounting sees at most two state classes while the joint state needs 1024. The class-count underestimate is 512-fold. The joint state contains 10 bits, of which 9 bits, or 90%, are past-by-future interaction.

## 5. Results II: genuine three-way temporal interaction is unbounded

The previous theorem could be interpreted as one responsibility activating another. We next ask whether the required state can be dominated by information belonging to no temporal position alone and not even to any pair.

### Theorem 2

For every integer \(b\ge2\), there exists a finite CREST contract with one visible present class such that

\[
D_H=1,
\qquad
D_\Theta=0,
\qquad
D_F=0,
\]

while

\[
\boxed{D_{H\Theta F}=b\text{ bits}}
\]

and

\[
|J_{H\Theta F}|=2^b.
\]

The exact coalition block counts are

| coalition | required classes |
|---|---:|
| none | 1 |
| history | 2 |
| latent present | 1 |
| future | 1 |
| history + latent present | 3 |
| history + future | 2 |
| latent present + future | 1 |
| history + latent present + future | \(2^b\) |

Thus

\[
v(H\Theta)=\log_2 3,
\qquad
v(HF)=1,
\qquad
v(\Theta F)=0,
\]

and the nonzero higher-order dividends are

\[
\boxed{m(H,\Theta)=\log_2(3/2)}
\]

and

\[
\boxed{m(H,\Theta,F)=b-\log_2 3.}
\]

Consequently

\[
m(H,\Theta,F)\to\infty
\]

and

\[
\boxed{
\frac{m(H,\Theta,F)}{D_{H\Theta F}}
=1-\frac{\log_2 3}{b}
\longrightarrow1.
}
\]

The genuine three-way interaction can therefore asymptotically account for the entire required state information.

### Construction

Use \(2^b+1\) latent worlds, all in one present-cut block. History marks one world. The latent-present closure has one response edge into that historical seed and is inert until the history split exists. The future closure contains a chain that remains inert until the latent split exists; once activated, successor consistency propagates the distinction along the chain. Two residual worlds remain merged, leaving exactly \(2^b\) final state classes.

No asymptotic approximation is required for the finite block counts or interaction formula.

## 6. Numerical closure at one cut

Set \(b=10\). There is still only one visible present class, but the full adequate state requires

\[
2^{10}=1024
\]

classes and exactly 10 bits.

| source of required state information | bits | share of joint debt |
|---|---:|---:|
| direct history | 1.0000000000 | 10.00% |
| history × latent present | 0.5849625007 | 5.85% |
| history × future | 0 | 0% |
| latent present × future | 0 | 0% |
| **history × latent present × future** | **8.4150374993** | **84.15%** |
| **joint** | **10.0000000000** | **100%** |

Total interaction debt is 9 bits, so 90% of the required state information is interaction-generated. Of those interaction bits, 93.50% belong to the genuine three-way dividend.

The central numerical point is not merely that a hidden system can have many states. It is that most of the required state information in this family is not attributable to history, latent response, or future separately. It appears only when the responsibilities are imposed together.

## 7. Relation to existing concepts of ecological and dynamical state

### 7.1 Ecological memory, hysteresis, and transients

Ecological memory models quantify how antecedent conditions influence current ecological processes (Ogle et al. 2015). Hysteresis and alternative-state theory show that a system's response can depend on the path by which it arrived at current conditions (Scheffer et al. 2001). Transient ecology emphasizes that systems can remain far from asymptotic behavior for long periods, making current conditions insufficient for forecasting longer-term dynamics (Hastings et al. 2018).

CREST is compatible with all three observations but asks a different question. Those literatures concern dynamical dependence on time. CREST asks what **equivalence relation over possible worlds** is licensed for a declared scientific task at one present cut, and how the information burden of that relation changes when temporal responsibilities interact.

### 7.2 Predictive states and causal states

Causal-state constructions identify histories that induce the same conditional future distribution and produce minimal predictive representations under their assumptions (Shalizi and Crutchfield 2001). Predictive state representations describe state through action-conditional predictions of future observations (Littman, Sutton, and Singh 2001).

These approaches demonstrate that state need not be synonymous with an instantaneous physical configuration. CREST differs in the object it studies: the baseline is an explicitly declared present observation, and multiple responsibility closures—retrospective, latent-contemporaneous, and prospective—act jointly on that same cut. The headline quantity is not predictive-state minimality but **interaction-generated state information across responsibility positions**.

### 7.3 State abstraction and bisimulation

State aggregation and bisimulation merge ground states while preserving properties relevant to control or decision making (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST uses the same broad mathematical idea that state identity is task-relative and that irrelevant distinctions can be erased.

The result here is not a new generic abstraction algorithm. It is a separation theorem: responsibility-wise abstraction can fail to compose additively. A distinction generated by one responsibility can activate another, and higher-order interaction can asymptotically dominate the final quotient.

## 8. Companion theories and evidential boundary

CREST is a synthesis layer rather than a replacement for its companion theories.

**MLTR** develops the history side: carried semantics, route coherence, and minimum historical completion after structural replacement.

**MRM** develops the latent-present side: when visibly compatible mechanisms may safely remain unresolved and when response-relevant mechanism information or active probes are required.

**CCOC** develops the future side: how widening the legal future-response grammar can expose distinctions hidden under a restricted grammar.

**CED** is downstream. Once a state distinction is required, evidence may or may not identify it. CREST therefore keeps

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

The current paper is about the first object: required state information at a temporal cut.

## 9. Scope and novelty boundary

The results are finite, exact, and conditional on a declared common carrier and declared refinement closures.

CREST does **not** claim novelty for closure operators, partition lattices, state abstraction, bisimulation, predictive-state constructions, Möbius inversion, Harsanyi dividends, or logarithmic class-count accounting. Nor does it claim that ecological history, hidden mechanisms, or future conditions can matter; those ideas have substantial prior literatures.

The contribution claimed here is narrower:

1. the present observation is formalized as a temporal cut and its induced partition rather than identified with the state;
2. retrospective history, latent contemporaneous response structure, and prospective response are placed as distinct responsibilities around that cut;
3. their jointly required state information is shown not to be recoverable, in general, by adding the burdens measured separately;
4. past-by-future interaction is unbounded; and
5. genuine three-way history-by-latent-present-by-future interaction is unbounded and can asymptotically dominate the state.

The theory does **not** establish that these three responsibilities exhaust every legitimate ecological notion of state, that every ecological system has a unique natural decomposition into them, that latent response structure is identifiable from the present observation, or that the finite result automatically extends to continuous-time, stochastic, infinite-state, or approximate systems.

## 10. Discussion

The usual language of ecological state encourages a spatial intuition: state is a list of variables located at the present. The temporal-cut formulation replaces that picture with a representational one. The present is the point at which equivalence is declared. The state is whatever information about possible worlds must remain available there.

That shift matters because the required information can be interaction-generated. If history, latent response, and future were independently compressible, the state burden could be designed one responsibility at a time. The theorems show that no such general guarantee exists. In the sharp families, one responsibility creates the distinction on which another responsibility becomes informative. With three responsibilities, almost all required information can belong to the genuine three-way term.

This result also separates two uses of the word “state.” Dynamical state often refers to variables sufficient to evolve a model. Scientific state in CREST is contract-relative: it preserves exactly the distinctions required for the prediction, intervention, semantic continuity, mechanism robustness, or reporting task under consideration. The two may coincide for a particular model and contract, but they need not.

The ecological implication is not that every real system has large positive interaction debt. The theorem is a possibility and no-bound result, not a prevalence claim. Its practical consequence is methodological: when a state representation is expected to support several responsibilities, adequacy should be checked against their joint fixed point rather than against independently constructed state summaries.

A continuous-time extension would naturally replace the finite left and right sides of the cut by temporal germs and represent latent contemporaneous structure by local generators or response kernels compatible with the same observation. That is a future theorem, not part of the present claim.

## 11. Conclusion

The present need not be the state. It can be the cut at which a state must be constructed.

At that cut, worlds that look identical may differ in relevant history, latent contemporaneous response structure, and counterfactual future. The adequate state is the least-information quotient preserving the distinctions those responsibilities jointly require.

The quantitative consequence is nonseparability across time. Past-by-future interaction can be unbounded,

\[
\boxed{m(H,F)=\log_2 n-1,}
\]

and genuine history-by-latent-present-by-future interaction can also be unbounded,

\[
\boxed{m(H,\Theta,F)=b-\log_2 3.}
\]

At \(b=10\), one visible present class expands to 1024 required state classes. The state contains 10 bits; 9 are interaction-generated and 8.415 bits, or 84.15%, belong to the genuine three-way term.

Ecological state is therefore not merely the variables observed now. It is the least information that must survive the temporal cut—and that information cannot, in general, be reconstructed by compressing past, latent present, and future independently.

## Literature Cited

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.
