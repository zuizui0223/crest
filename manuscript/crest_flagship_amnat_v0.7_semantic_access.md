# Ecological State at a Temporal Cut: Sparse Semantic Access

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as something possessed by a system at one moment. We instead idealize the present as a zero-duration temporal cut: an observational boundary, not a finite interval and not yet an adequate state. Retrospective carried history, transverse latent-present response structure, and prospective query accessibility are defined before state through separate companion semantics. Their role is not to cause the state but to constrain which distinctions may be collapsed at the cut. CREST defines ecological state as the least quotient compatible with those left, transverse, and right constraints. A realizability audit rules out several circular temporal interpretations. Sparse prospective access then changes the induced quotient: if N retrospective-by-transverse semantic pairs exist but only k are future-addressable, an m-bit decoder yields (N-k)+k2^m joint state classes and a three-way state dividend log2[((N-k)+k2^m)/N], approaching m-log2(N/k). A shallow-lake restoration model provides a worked ecological interpretation. The finite theory does not claim a continuous-time epsilon-to-zero limit theorem.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; semantic access; restoration

## 1. Introduction

Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results establish that time matters dynamically. They do not by themselves determine the structure carried by an idealized present boundary. CREST therefore begins by separating the visible observation at a time cut from the state structure that may be required on that cut.

At a cut time t, an observation can leave several latent possibilities unresolved. These are not meant as parallel universes; mathematically they are the fiber of raw configurations compatible with the same visible cut value. Distinctions can reach that fiber from three geometrically different directions: retrospectively from histories to the left of the cut, transversely through latent response differences hidden at the cut, and prospectively through responses exposed by legal queries to the right. The theoretical problem is to determine the least quotient on the cut compatible with those distinctions.

CREST studies this as a finite temporal-boundary state problem. MLTR supplies retrospective carried semantics from the left of the cut. MRM supplies candidate-safe latent response types within the observation fiber; this is the transverse latent-present direction, not an assertion of complete ontic mechanism identity. CCOC supplies prospective response distinctions under a declared right-of-cut query grammar. CREST asks how these pre-state equivalence and access structures induce a minimal cut-state and how partial prospective accessibility changes its complexity.

The paper does not claim mathematical novelty for Möbius inversion or unanimity games. Those provide accounting language. The finite theory isolates two distinct structures controlling the prospective refinement of the cut-state:

\[
\boxed{
\text{interface prerequisite set}
\quad\text{and}\quad
\text{semantic access relation}.
}
\]

The first determines which retained interfaces must be present before a future query is well formed. The second determines on which combinations of those semantic interfaces the query is actually licensed. Complete addressability is therefore a special case, not a default assumption.

## 2. State at a zero-duration temporal cut

Let \(\Omega\) be a declared finite set of possible ecological worlds. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible-present partition

\[
\boxed{B_t=\ker O_t.}
\]

Two raw configurations lie in one block of \(B_t\) exactly when they are indistinguishable at the declared cut. The present is therefore not itself the ecological state. In the finite theory, `zero-duration` means that the present is represented by one indexed boundary rather than by a finite observation interval; it is not a proved limit of shrinking continuous-time windows.

For one visible cut value \(y\), the fiber \(L_t(y)=O_t^{-1}(y)\) is the set of raw possibilities hidden behind that observation. The transverse latent-present structure lives inside this fiber: MRM may distinguish candidate-safe response types even when \(O_t\) does not.

For a required state map \(q_t:\Omega\to Q_t\), the visible present is sufficient exactly when

\[
O_t(\omega)=O_t(\omega')
\Longrightarrow
q_t(\omega)=q_t(\omega').
\]

Equivalently, \(q_t\) factors through \(O_t\). When this fails, the adequate cut-state is the least quotient refining \(B_t\) enough to preserve the declared retrospective, transverse, and prospective distinguishability constraints. State is therefore structure induced on the cut, not a synonym for the visible cut itself.

This leastness has a companion-independent finite form. Let \(g_i:\Omega\to Z_i\) be any finite family of pre-state signatures defined independently of the final state. Define

\[
\omega\sim_*\omega'
\iff
O_t(\omega)=O_t(\omega')
\quad\text{and}\quad
g_i(\omega)=g_i(\omega')\quad\text{for every }i.
\]

Then \(Q_* = \Omega/{\sim_*}\) preserves the cut observation and every declared signature. Moreover, if another quotient \(r:\Omega\to R\) preserves the same objects, every \(r\)-class lies inside one \(Q_*\)-class. Hence \(r\) refines \(Q_*\): the induced cut-state is the unique coarsest admissible quotient, up to relabeling of its classes. The investigator therefore chooses which pre-state signatures define the scientific problem, but once those signatures are fixed the least compatible state is not freely chosen.

## 3. Retrospective, transverse, and prospective structures are pre-state

### 3.1 MLTR: retrospective carried semantics from the left

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

The retained retrospective structure is therefore not a route identifier. It is a quotient of routes by equality of carried semantics. Geometrically it records which distinctions arrive at the cut from its left side. CREST consumes these completed carried maps rather than reimplementing MLTR's relation-composition proof machinery.

### 3.2 MRM: transverse latent-present response structure

MRM fixes a visible macrostate set \(Q\), a declared action grammar, and primitive candidate laws \(\theta\). Candidate \(\theta\) supplies transitions

\[
G_a^\theta:Q\to Q.
\]

Two candidates are response equivalent exactly when their complete declared response tables agree. The retained transverse structure is therefore the candidate-safe quotient of primitive laws hidden behind the visible cut. It partitions the latent-present observation fiber by response type; it is not a claim to recover complete causal or ontic mechanism identity.

### 3.3 CCOC: prospective query structure to the right

CCOC fixes a controlled law \(\mathcal M\) and declares a legal future grammar \(\mathcal L\subseteq A^*\). The response profile

\[
\rho_{\mathcal L}^{\mathcal M}(s)
=
\bigl(\operatorname{Tr}_{\mathcal M}(s,w)\bigr)_{w\in\mathcal L}
\]

induces the exact future-response quotient. The prospective structure is therefore a declared family of legal right-of-cut questions, not a future state variable inferred from the final quotient.

The dependency direction is

\[
\text{primitive history / candidate law / future grammar}
\longrightarrow
\text{semantic or response equivalence}
\longrightarrow
\text{adequate state}.
\]

There is no reverse dependence from the final state into these primitives. The three roles are consequently not three independent state coordinates: they are retrospective, transverse, and prospective constraints that are defined before the cut-state and may be mutually dependent in the underlying ecology.

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

Shallow-lake restoration supplies a worked ecological interpretation of the abstract cut geometry because the same coarse current water-quality description can be compatible with different nutrient histories and different latent response structures, while restoration questions expose different distinctions at the boundary. Internal phosphorus released from sediment accumulated during earlier high loading can delay recovery after external loading is reduced (Søndergaard, Jensen, and Jeppesen 2003). Long-term restoration outcomes also depend on fish dynamics, internal phosphorus loading, and the recovery or persistence of submerged macrophytes (Søndergaard et al. 2007). More broadly, chemical and biological within-lake inertia can delay recovery, motivating combinations of physicochemical and biological restoration measures (Jeppesen et al. 2012).

These studies support the ecological ingredients used by the finite model; they do not specify the exact finite target maps used below. The executable model contains four worlds behind the same coarse visible status, crossing two retrospective modes with two latent-response types. For each target, CREST tests whether the target output factors through no retained interface, history only, latent response only, or both. It also performs explicit counterfactual substitution of one interface while holding the other fixed.

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

The composed target is deliberately minimal. It has only two outputs, `standard_pathway` and `cross_interface_review`, across the four history-by-response combinations. The output records concordance versus mismatch between the retrospective sediment-legacy signal and the present sediment-response signal. For every fixed history mode, varying the response type reaches both outputs; for every fixed response type, varying history also reaches both outputs. Consequently neither \(H\) nor \(\Theta\) alone is sufficient, despite the target having only two output classes. The exact parity-style map is a formal witness of joint dependence, not a biological law asserted by the restoration literature.

This does not assert that every real shallow lake or every restoration objective has this prerequisite set. The same ecological system produces four different prerequisite structures because the target changes.

## 9. What the cut-state result means

CREST does not derive retrospective, transverse, or prospective semantics from Möbius accounting. Those structures are pre-state inputs. Once they are fixed, however, the induced cut quotient and its interaction accounting are mathematical consequences rather than design choices.

The theoretical distinction is between the order of a prospective constraint and its semantic coverage. A prospective query may require both the retrospective and transverse structures while remaining addressable on only part of their product. Complete access therefore yields a different cut-state complexity from sparse access. The corresponding structural questions are

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

CREST sits at the intersection of several literatures that already make time, hidden variables, or task-relative equivalence central to ecological modeling. Its claim is not that these ideas are absent from ecology. The distinction is representational: those literatures usually establish that antecedent conditions, latent processes, or future consequences matter, whereas CREST asks which distinctions among possible worlds must be retained at one observational cut for a declared scientific task.

### 10.1 Ecological memory and historical contingency

Ecological-memory models make antecedent conditions explicit. Ogle et al. (2015), for example, quantify how past environmental conditions contribute to current ecological processes and emphasize the length, temporal pattern, and strength of memory. Historical contingency in community assembly provides a complementary mechanism-level perspective: priority effects can make the order and timing of immigration alter later community structure and function, producing alternative stable or transient outcomes (Fukami 2015). These approaches establish that present behavior can depend on the past, but they do not by themselves determine a minimum retained representation of that past.

CREST therefore does not equate “history matters” with “retain the complete history.” Its retrospective interface is a quotient. Two raw histories are merged when their carried semantics are identical for the declared contract, and separated only when that inherited difference changes what the state must support. In this sense ecological memory motivates the need for retrospective information, while CREST asks which historical distinctions survive compression at the temporal cut.

### 10.2 Hysteresis, alternative states, and restoration

The alternative-states literature makes a second distinction important for CREST. Hysteresis and regime shifts show that similar current environmental conditions can be compatible with different dynamical basins or recovery trajectories (Scheffer et al. 2001). Reviews of alternative stable states emphasize that state changes can be understood through changes in system variables or in underlying drivers and that management requires attention to resilience and hysteresis, not only to the observed configuration (Beisner, Haydon, and Cuddington 2003). Restoration theory likewise shows that strong feedbacks can make degraded systems resistant to attempts that restore only historical disturbance regimes or abiotic conditions (Suding, Gross, and Houseman 2004).

CREST uses these results as a warning against identifying ecological state with the currently visible configuration. However, it makes a narrower move than alternative-state theory: it does not attempt to infer basins of attraction or prove that a system has multiple stable states. Instead it asks whether the declared future task requires distinctions in retrospective history, latent response structure, or both. The shallow-lake example is deliberately framed this way. Sediment legacy and response mechanism are not called two “states” of the lake by fiat; they are candidate interfaces whose necessity is tested relative to a restoration target.

### 10.3 Latent ecological state in state-space models

Ecological state-space models provide perhaps the closest familiar use of the word state. They separate an unobserved process state from an observation process and are widely used for population dynamics, movement, capture-recapture, and other ecological time series (Auger-Méthé et al. 2021). Their central inferential problem is to estimate latent ecological quantities while accounting for process variation and observation error.

CREST addresses a logically earlier question. A state-space model normally begins after the analyst has specified what variables constitute the latent state and how that state evolves. CREST instead asks which distinctions must be represented at all before such estimation is attempted. The observational cut \(O_t\) is therefore not an observation equation for a pre-given latent vector. It is the baseline equivalence from which an adequate state quotient is constructed under the declared contract. This makes CREST complementary to state-space inference rather than a replacement for it: state-space methods estimate a chosen latent representation; CREST audits whether that representation retains the distinctions demanded by the scientific task.

### 10.4 Predictive states and state abstraction

Predictive-state and state-abstraction theories supply the closest mathematical substrate. Computational mechanics groups histories by equality of predictive consequences (Shalizi and Crutchfield 2001), predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001), and bisimulation or state-abstraction methods merge states while preserving declared transition or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST adopts the same general discipline: states are quotients induced by what must be preserved, not arbitrary labels attached to worlds.

The additional theoretical step is to keep several equivalence structures separate before quotient composition. Retrospective carried meaning, transverse latent-response equivalence, and prospective query legality are defined by different companion semantics, and the realizability audit prevents the final cut-state from being used circularly to define those inputs. The sparse-access result then distinguishes two objects often collapsed in a single future-equivalence relation: which pre-state structures a prospective query requires and on which semantic combinations it is actually addressable.

The resulting contribution is therefore not a new generic theory of quotient states. It is a finite theory of state at a temporal boundary: distinguish the visible cut from its induced state, keep retrospective, transverse, and prospective equivalences pre-state, and characterize the least quotient they impose. That placement connects ecological memory, historical contingency, restoration dynamics, latent-state inference, and predictive-state abstraction without treating any of them as interchangeable.

## 11. Scope and supporting mathematics

The paper is finite, exact, and contract conditional. It does not claim that history, latent response, and future exhaust ecological state; that every ecological system has a unique decomposition into these roles; that prerequisite sets or access relations are inferable from observational data without additional assumptions; or that the framework automatically extends to stochastic, approximate, continuous-time, or infinite-state systems.

Earlier CREST marked-cycle and fixed-closure three-audit families remain mathematically valid as abstract closure extrema. The realizability audit shows why they should not be interpreted literally as immutable MLTR history and fixed-grammar MRM response types. The earlier direct-value compositional module is retained only as a closed-form corollary of the complete-access trace quotient and is regression-tested against it for every coalition.

The sparse-access result should also not be oversold as difficult game theory. Once the semantic quotient and access relation are specified, its cardinality formula follows by finite counting. The theoretical contribution lies in making semantic coverage an explicit part of the induced cut-state and in separating its magnitude effect from prerequisite order. The phrase `zero-duration cut` is a finite idealization: CREST has not proved that states on intervals \( [t-\varepsilon,t+\varepsilon] \) converge as \(\varepsilon\to0\), nor does it claim a continuous-time germ theorem in this manuscript.

## 12. Discussion

The temporal-cut formulation separates three questions that are often conflated. What happened before the cut? What latent response distinctions remain possible at the cut? Which future questions must the state support? None of these is defined by the final state itself.

The realizability results show that positive interaction does not appear merely because three labels are intersected. The semantic companion construction then shows why the labels themselves are insufficient: raw histories must be quotiented by carried meaning, and candidate laws by response equivalence, before future access can be specified coherently.

Sparse access adds a second correction. Even after both semantic interfaces are retained, a future query need not be meaningful across their entire product. Complete addressability therefore overestimates the number of exterior distinctions that survive into the state whenever only a subset of semantic combinations licenses the decoder.

The shallow-lake example illustrates the ecological payoff. “What is the lake now?”, “does historical nutrient legacy matter?”, “which mechanism-specific intervention is appropriate?”, and “which composed restoration diagnostic is adequate?” are questions about the same system but induce different prerequisite sets. The ecological ingredients behind those distinctions are supported by restoration studies of internal phosphorus legacy, biomanipulation, fish and macrophyte dynamics, and combined restoration approaches (Søndergaard, Jensen, and Jeppesen 2003; Søndergaard et al. 2007; Jeppesen et al. 2012). A second layer of system-specific work would then ask which history-response combinations actually support each future query.

This is the theoretical sense in which ecological state is cut- and contract-relative without being arbitrary. The pre-state semantics and query structure parameterize the problem, but once fixed they constrain a definite quotient: retrospective carriage, transverse response structure, and prospective accessibility determine which distinctions may or may not collapse at the boundary.

## 13. Conclusion

The present is not identified with the ecological state. In the finite theory it is a zero-duration observational cut on which state structure is induced.

CREST defines retrospective carried history, transverse latent-present response structure, and prospective query accessibility before the state, then asks for the least quotient on the cut compatible with their distinctions. Sparse semantic access determines how much prospective structure reaches that quotient, while prerequisite structure determines where higher-order interaction appears.

In this view, higher-order state interaction is not an intrinsic property of time and state is not a pre-given vector at the present. It is a property of the equivalence geometry induced across a temporal boundary, attenuated when prospective addressability is semantically sparse.

## Literature Cited

Auger-Méthé, M., K. Newman, D. Cole, F. Empacher, R. Gryba, A. A. King, V. Leos-Barajas, J. Mills Flemming, A. Nielsen, G. Petris, and L. Thomas. 2021. A guide to state-space modeling of ecological time series. *Ecological Monographs* 91:e01470. https://doi.org/10.1002/ecm.1470.

Beisner, B. E., D. T. Haydon, and K. Cuddington. 2003. Alternative stable states in ecology. *Frontiers in Ecology and the Environment* 1:376–382. https://doi.org/10.1890/1540-9295(2003)001[0376:ASSIE]2.0.CO;2.

Fukami, T. 2015. Historical contingency in community assembly: integrating niches, species pools, and priority effects. *Annual Review of Ecology, Evolution, and Systematics* 46:1–23. https://doi.org/10.1146/annurev-ecolsys-110411-160340.

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Jeppesen, E., M. Søndergaard, T. L. Lauridsen, T. A. Davidson, Z. Liu, N. Mazzeo, C. Trochine, K. Özkan, H. S. Jensen, D. Trolle, F. Starling, X. Lazzaro, L. S. Johansson, R. B. Hansen, L. Liboriussen, S. E. Larsen, F. Landkildehus, S. Egemose, and M. Meerhoff. 2012. Biomanipulation as a restoration tool to combat eutrophication: recent advances and future challenges. *Advances in Ecological Research* 47:411–488. https://doi.org/10.1016/B978-0-12-398315-2.00006-5.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.

Søndergaard, M., J. P. Jensen, and E. Jeppesen. 2003. Role of sediment and internal loading of phosphorus in shallow lakes. *Hydrobiologia* 506–509:135–145. https://doi.org/10.1023/B:HYDR.0000008611.12704.dd.

Søndergaard, M., E. Jeppesen, T. L. Lauridsen, C. Skov, E. H. van Nes, R. Roijackers, E. Lammens, and R. Portielje. 2007. Lake restoration: successes, failures and long-term effects. *Journal of Applied Ecology* 44:1095–1105. https://doi.org/10.1111/j.1365-2664.2007.01363.x.

Suding, K. N., K. L. Gross, and G. R. Houseman. 2004. Alternative states and positive feedbacks in restoration ecology. *Trends in Ecology & Evolution* 19:46–53. https://doi.org/10.1016/j.tree.2003.10.005.
