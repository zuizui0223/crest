# Ecological State at a Temporal Cut: Sparse Semantic Access

**Target:** *The American Naturalist* — Major Article

## Abstract

When two ecosystems look the same now but differ in what they retain from the past, how they are organized beneath that appearance, or what futures remain possible, are they in the same ecological state? Ecological memory, hysteresis, historical contingency, and long transients all show that instantaneous configuration need not determine ecological identity. We therefore idealize the present as a zero-duration temporal cut and define state from distinctions that remain consequential at that boundary. Retrospective carried history, transverse latent-present response structure, and prospective response accessibility are defined before state. CREST defines ecological state as the least quotient compatible with those distinctions. For prospective refinement, prerequisite topology and semantic accessibility play different roles. At Shannon order, prerequisite sets determine exact Möbius support while accessible occupancy determines coefficient magnitude; non-Shannon orders can mix structural and distributional interaction. Separately, the Hartley support-count endpoint shows that if N retrospective-by-transverse semantic pairs exist but only k support an m-bit future distinction, the joint state has (N-k)+k2^m classes and loses asymptotically log2(N/k) bits relative to complete accessibility. A shallow-lake model shows why one visible present can conceal ecologically distinct recovery capacities.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; semantic access; restoration

## 1. Introduction

When two ecosystems look the same now but differ in what they retain from the past, how they are organized beneath that appearance, or what futures remain possible, are they in the same ecological state? Ecology already supplies many reasons to answer no. Antecedent conditions generate ecological memory (Ogle et al. 2015), historical contingency and priority effects can make later community structure depend on assembly order (Fukami 2015), hysteresis can make similar external conditions compatible with different recovery trajectories (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to subsequent dynamics (Hastings et al. 2018). These are usually studied as different phenomena. Together they imply a more basic problem: the ecological present need not be exhausted by what is instantaneously visible.

A system can carry distinctions whose causal origin lies before the present while those distinctions remain embodied now. It can also contain response-relevant organization that is presently real but hidden inside a coarse observation. And two systems that share the same visible configuration can differ in which ecological futures remain expressible from that configuration. Sediment phosphorus legacy, dormant propagules, physiological condition, feedback structure, or the persistence or loss of a regeneration pathway are not future states smuggled into the present; they are present consequences, structures, or capacities that can make otherwise similar systems ecologically nonequivalent. This interpretation is consistent with resilience theory, which treats the capacity to absorb disturbance and reorganize while retaining function, structure, identity, and feedbacks as a property of the system (Walker et al. 2004). Prospective distinctions in CREST likewise concern present response capacities that would be revealed by future perturbation, not realized future trajectories imported backward into the present.

CREST formalizes this ecological necessity by representing the present as a temporal cut. The cut does not remove the present from time. It identifies the boundary at which distinctions retained from the past, hidden in present response organization, and expressed through possible future responses meet without becoming the same object. Retrospective distinctions arrive from histories to the left of the cut, transverse distinctions separate latent response structures within the same visible present, and prospective distinctions separate systems by the responses that remain available to the right. The theoretical problem is to determine the least state on the cut that does not collapse distinctions that remain ecologically consequential.

CREST studies this as a finite temporal-boundary state problem. MLTR supplies retrospective carried semantics from the left of the cut. MRM supplies candidate-safe latent response types within the observation fiber; this is the transverse latent-present direction, not an assertion of complete ontic mechanism identity. CCOC supplies prospective response distinctions under a declared right-of-cut grammar. These companion structures are not proposed as a workflow for choosing measurements. They provide a finite construction in which the ecological claim can be stated exactly: visible configuration and ecological state need not coincide, because ecological identity at a moment can depend jointly on retained history, hidden present organization, and future-generating capacity.

The paper does not claim mathematical novelty for Möbius inversion or unanimity games. Those provide accounting language. The finite theory isolates two distinct structures controlling the prospective refinement of the cut-state:

\[
\boxed{
\text{interface prerequisite set}
\quad\text{and}\quad
\text{semantic access relation}.
}
\]

The first determines which retained structures must jointly be present before a future distinction exists. The second determines on which combinations of those semantic structures the distinction is actually ecologically expressible. Complete addressability is therefore a special case, not a default assumption.

A second distinction is equally important: **structural interaction and support-space richness are not the same quantity**. CREST uses the Shannon prospective game when asking where prerequisite interaction is structurally supported, because Shannon additivity preserves declared prerequisite support exactly. It uses the Hartley endpoint when asking how many distinguishable state classes remain under sparse semantic access. The two are different Rényi orders of the same selective-refinement structure and answer different ecological questions.

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

This conclusion is representation invariant. Two different pre-state signature families induce the same cut-state exactly when every signature in each family factors through the state induced by the other. Thus relabeling, reordering, duplicating, packing, or splitting signatures cannot alter the state when the generated distinction structure is unchanged. Equivalently, adding any signature already determined by the existing cut-state is redundant. The mathematical object is therefore the equivalence relation generated jointly with the cut, not a particular coordinate encoding of that relation.

For a fixed cut, these representation classes exhaust the entire finite state space. Representation-equivalence classes of signature families are in one-to-one correspondence with partitions that refine \(B_t\): every induced cut-state refines the visible partition, and conversely any refinement of \(B_t\) can be realized by one signature whose kernel is that refinement. Ordering states by retained information is therefore exactly partition refinement. Adding a nonredundant signature can only move to a finer state, so \(\log_2|Q|\) is monotone nondecreasing along this order.

States at different cuts can be connected only when the underlying world evolution respects their quotient equivalences. For a declared deterministic map \(\phi_{t\to s}:\Omega_t\to\Omega_s\), a state-level map \(\bar\phi:Q_t\to Q_s\) exists exactly when \(\omega\sim_t\omega'\) implies \(\phi(\omega)\sim_s\phi(\omega')\). When this descent condition holds, \(\bar\phi([\omega]_t)=[\phi(\omega)]_s\) is unique; identity and composition descend. Failure is a state-sufficiency obstruction: one source state class evolves into multiple target state classes, so no deterministic quotient transition is well defined. This finite transport result does not imply temporal monotonicity of \(|Q_t|\) or a continuous-time limit.

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

### 6.1 Structural interaction at Shannon order

For structural interpretation, let the semantic pairs carry occupancies \(p_i>0\), \(\sum_i p_i=1\), and let

\[
P(A_f)=\sum_{i\in A_f}p_i.
\]

At Shannon order \(q=1\), a query with prerequisite set \(R_f\), decoder depth \(m_f\), and access set \(A_f\) contributes

\[
\boxed{
v_1(S)=m_fP(A_f)\,\mathbf 1\{R_f\cup\{F\}\subseteq S\}.
}
\]

For an arbitrary family of prospective queries, the contributions add, so the Möbius dividend is

\[
\boxed{
d_1(T)=\sum_{f:R_f\cup\{F\}=T}m_fP(A_f).
}
\]

This is the structural result used to interpret prospective interaction in CREST. The prerequisite set determines **where** a Shannon dividend can occur; semantic accessibility and occupancy determine **how much** information appears there. Overlapping access sets do not create additional Shannon support beyond the declared prerequisite hyperedges.

The choice of Shannon order is not merely conventional. Supplementary Information II shows that non-Shannon Rényi orders can generate undeclared higher-order dividends through nonlinear weighting of selectively refined cells. For disjoint access, the leakage has a strict sign change around \(q=1\); with overlapping access, non-Shannon leakage can also cancel exactly on an overlap-balance surface. Thus a zero non-Shannon dividend does not by itself certify prerequisite fidelity. Shannon order is the generally support-faithful diagnostic for prerequisite topology in this finite construction.

### 6.2 Hartley support-count endpoint

A different question is how many distinguishable state classes remain when future differentiation is sparse. The grand-coalition state has

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

With the Hartley/support-count game

\[
v_0(S)=\log_2|Q_S|,
\]

the three-way support-count dividend becomes

\[
\boxed{
d^{(0)}_{H\Theta F}
=
\log_2\frac{(N-k)+k2^m}{N}.}
\]

This quantity is generally non-integer. Complete addressability is the boundary case \(k=N\), giving \(d^{(0)}_{H\Theta F}=m\). If \(k=0\), the decoder is nowhere addressable and the dividend is zero.

For fixed \(N\) and \(k>0\),

\[
\boxed{
d^{(0)}_{H\Theta F}
=
m-\log_2(N/k)+o(1)}
\]

as \(m\to\infty\). Thus sparse semantic access creates an asymptotic Hartley penalty

\[
\boxed{\log_2(N/k)}
\]

relative to the complete-access case.

This Hartley result measures **support-space contraction**, not faithful recovery of prerequisite interaction support. It should therefore not be read as saying that q=0 Möbius support identifies the prerequisite hypergraph. The structural location claim belongs to the Shannon prospective game above; the Hartley endpoint quantifies how sparse future-generating capacity contracts the number of distinguishable states.

Ecologically, sparse access need not mean that an observer failed to sample enough combinations. It can mean that future-generating capacity is itself uneven across the ecological state space. Some history-by-response combinations may retain a response pathway, whereas in others that pathway has been lost, blocked, or rendered biologically irrelevant. The ratio \(k/N\) therefore measures how broadly a prospective distinction is supported across otherwise distinct retrospective-by-transverse combinations, and \(\log_2(N/k)\) measures the resulting contraction of state complexity relative to complete future differentiation.

## 7. Canonical finite witness

The current companion witness has two history modes and two response types, so

\[
N=4.
\]

Only one semantic pair licenses the future decoder, so

\[
k=1.
\]

Under uniform occupancy, \(P(A_f)=1/4\). Therefore the Shannon structural dividend for the canonical query is

\[
\boxed{d_1(\{H,\Theta,F\})=m/4.}
\]

At \(m=10\), this is **2.5 bits**. This is the canonical structural interaction value.

The Hartley support-count endpoint separately gives

\[
|Q_{H\Theta F}|=3+2^m
\]

and

\[
\boxed{
d^{(0)}_{H\Theta F}=\log_2((3+2^m)/4).}
\]

For three benchmark depths:

| \(m\) | grand classes | grand bits | Shannon structural dividend | Hartley support-count dividend |
|---:|---:|---:|---:|---:|
| 4 | 19 | 4.24793 | 1.00000 | 2.24793 |
| 8 | 259 | 8.01681 | 2.00000 | 6.01681 |
| 10 | 1027 | 10.00422 | 2.50000 | 8.00422 |

The Hartley deficit from complete addressability tends to two bits because

\[
\log_2(N/k)=\log_2 4=2.
\]

The earlier 4096-class, 12-bit, 10-bit-three-way calculation is retained as the full-access boundary \(k=N=4\), not as the canonical semantic witness.

## 8. Shallow lakes as a biological witness of a non-instantaneous present

Shallow-lake restoration provides a concrete reason not to identify ecological state with a coarse instantaneous configuration. A lake can retain phosphorus accumulated in sediments during an earlier high-loading period, so recovery can remain delayed after external loading is reduced (Søndergaard, Jensen, and Jeppesen 2003). Long-term trajectories can also differ with fish dynamics, internal phosphorus loading, and the recovery or persistence of submerged macrophytes (Søndergaard et al. 2007). More broadly, chemical and biological inertia can preserve consequences of earlier conditions and alter subsequent recovery (Jeppesen et al. 2012). Thus two lakes with the same coarse present water-quality description can remain ecologically nonequivalent because they carry different legacies or different present response organization.

The finite model does not claim that real lakes instantiate one exact four-state mechanism. It uses ecological ingredients documented by the restoration literature to construct four worlds behind the same coarse visible status, crossing two retrospective modes with two latent-response types. The purpose of this construction is ontological before it is methodological: one visible present can conceal several states that are not interchangeable through time because they differ in what has been retained and in how the system can respond.

The model also shows that those nonequivalences need not all be exposed by the same ecological contrast. The minimum prerequisite sets are

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

The composed contrast is deliberately minimal. It has only two outputs, `standard_pathway` and `cross_interface_review`, across the four history-by-response combinations. The output records concordance versus mismatch between the retrospective sediment-legacy signal and the present sediment-response signal. For every fixed history mode, varying the response type reaches both outputs; for every fixed response type, varying history also reaches both outputs. Consequently neither \(H\) nor \(\Theta\) alone is sufficient, despite the target having only two output classes. The exact parity-style map is a formal witness of joint dependence, not a biological law asserted by the restoration literature.

The biological point is therefore not that ecology should define lake state by whichever management target is currently convenient. It is that the apparently singular present can contain several distinct temporal structures, and different ecological contrasts reveal different parts of that pre-existing nonequivalence. The target-relative prerequisite calculation is secondary evidence about how those distinctions are expressed, not the source of their ecological existence.

## 9. Why ecological state requires a temporal cut

The temporal cut is needed because the ecological present can contain distinctions with three different temporal origins that nevertheless coexist at one moment. Retrospective distinctions have causes to the left of the cut but consequences that remain embodied now. Transverse distinctions are differences in current organization that a coarse observation fails to display. Prospective distinctions concern what responses remain expressible from that organization. None can simply be substituted for another.

This makes the cut more than a bookkeeping convention. Without it, ecological memory can be mistaken for a requirement to retain whole histories, latent organization can be treated as just another historical label, and future response can be mistaken for information imported backward from the future. At the cut, the roles are separated: history contributes only insofar as its consequences remain carried to the present; latent organization is present now even when hidden; and prospective structure distinguishes current systems by response capacities they already possess.

CREST does not derive these distinctions from Möbius accounting. Once the relevant retrospective, transverse, and prospective equivalences are fixed, however, the induced cut quotient is constrained rather than freely chosen. A visible configuration is therefore an adequate ecological state only in the special case where all distinctions that remain consequential at the cut can safely collapse within its observation classes.

Sparse access adds a specifically ecological refinement. Even when two structures are both necessary for a prospective distinction, that distinction need not exist over their entire semantic product. Complete addressability would mean that every history-by-response combination preserves the same future differentiation. Sparse addressability means that future-generating capacity survives only on part of that product. The resulting loss of state complexity is therefore a property of the ecological possibility structure, not merely a limitation of what an investigator happened to measure.

## 10. Relation to existing state concepts

CREST sits at the intersection of several literatures that already show that antecedent conditions, hidden organization, and future consequences can matter to ecological dynamics. Its claim is not that these ideas are absent from ecology. The unresolved point is what they imply collectively about the ecological present. CREST treats them as evidence that ecological state can extend beyond instantaneous visible configuration while still being located at one temporal boundary.

### 10.1 Ecological memory and historical contingency

Ecological-memory models make antecedent conditions explicit. Ogle et al. (2015), for example, quantify how past environmental conditions contribute to current ecological processes and emphasize the length, temporal pattern, and strength of memory. Historical contingency in community assembly provides a complementary perspective: priority effects can make the order and timing of immigration alter later community structure and function, producing alternative stable or transient outcomes (Fukami 2015). These approaches establish more than the generic claim that the past matters. They show that distinctions originating before the present can remain biologically active at the present.

CREST therefore does not equate ecological memory with retention of complete history. Its retrospective interface is a quotient. Two raw histories are merged when their carried semantics are identical at the cut and separated when inherited differences remain ecologically consequential. In this sense ecological memory supplies one route by which past structure becomes constitutive of present ecological identity.

### 10.2 Hysteresis, alternative states, and restoration

The alternative-states literature makes a second distinction important for CREST. Hysteresis and regime shifts show that similar current environmental conditions can be compatible with different dynamical basins or recovery trajectories (Scheffer et al. 2001). Reviews of alternative stable states emphasize that state changes can involve both system variables and underlying drivers and that resilience cannot be read solely from the observed configuration (Beisner, Haydon, and Cuddington 2003). Restoration theory likewise shows that strong feedbacks can make degraded systems resistant to reversal even after historical disturbance regimes or abiotic conditions are restored (Suding, Gross, and Houseman 2004).

CREST uses these results as direct motivation for separating visible configuration from ecological state. It does not attempt to infer basins of attraction or claim that every system has multiple stable states. The narrower theoretical point is that present equivalence cannot be granted merely because two systems look alike now. If their retained legacies, response organization, or remaining response capacities differ, the systems can occupy different ecological states at the same visible cut value.

### 10.3 Latent ecological state in state-space models

Ecological state-space models provide perhaps the closest familiar use of the word state. They separate an unobserved process state from an observation process and are widely used for population dynamics, movement, capture-recapture, and other ecological time series (Auger-Méthé et al. 2021). Their central inferential problem is to estimate latent ecological quantities while accounting for process variation and observation error.

CREST addresses a logically earlier conceptual issue. A state-space model normally begins after the analyst has specified what variables constitute the latent state and how that state evolves. CREST instead asks what makes two possible ecological worlds the same state at the present boundary in the first place. The observational cut \(O_t\) is therefore not an observation equation for a pre-given latent vector. It is the visible equivalence that can prove too coarse when retained history, hidden present organization, or future-generating capacity differ within one observation class. CREST is therefore complementary to state-space inference: one estimates latent states, whereas the other theorizes the equivalence relation that makes a present ecological state.

### 10.4 Predictive states and state abstraction

Predictive-state and state-abstraction theories supply the closest mathematical substrate. Computational mechanics groups histories by equality of predictive consequences (Shalizi and Crutchfield 2001), predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001), and bisimulation or state-abstraction methods merge states while preserving declared transition or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST adopts the same general discipline: states are equivalence classes induced by distinctions that must remain consequential, not arbitrary labels attached to worlds.

The ecological addition is the explicit temporal separation of those distinctions before they are composed. Retrospective carried meaning, transverse latent-response equivalence, and prospective response accessibility occupy different positions relative to the present. The realizability conditions prevent the final cut-state from being used circularly to define them, and sparse accessibility shows that potential future differentiation need not be supported uniformly across all retained histories and response types.

The resulting contribution is therefore not a new generic theory of quotient states. It is a finite theory of the ecological present as a temporal boundary: visible configuration can underdetermine state because ecological identity can depend on what the system retains, what organization it presently embodies, and what responses remain possible from that organization. The quotient mathematics supplies an exact representation of that claim without treating ecological memory, historical contingency, restoration dynamics, latent-state inference, or predictive-state abstraction as interchangeable.

## 11. Scope and supporting mathematics

The paper is finite, exact, and contract conditional. It does not claim that history, latent response, and future exhaust ecological state; that every ecological system has a unique decomposition into these roles; that prerequisite sets or access relations are inferable from observational data without additional assumptions; or that the framework automatically extends to stochastic, approximate, continuous-time, or infinite-state systems.

The finite partition spine in Section 2 is structural support, not a claim of new partition theory. The existence of the common refinement, its unique-coarsest characterization, the representation-equivalence description of signature families, and the descent condition for deterministic transport are elementary consequences of finite quotient and partition structure. Their role is to establish that the cut-state construction is well defined, representation safe, and composable when the declared evolution respects the quotient. They should therefore be read as sanity guarantees for the framework rather than as independent mathematical novelty claims.

Earlier CREST marked-cycle and fixed-closure three-audit families remain mathematically valid as abstract closure extrema. The realizability audit shows why they should not be interpreted literally as immutable MLTR history and fixed-grammar MRM response types. The earlier direct-value compositional module is retained only as a closed-form corollary of the complete-access trace quotient and is regression-tested against it for every coalition.

The information-order distinction is essential to the paper-level contribution. The Shannon prerequisite-support factorization is the structural result: declared prerequisite sets determine the Möbius support of prospective information, while semantic accessibility and occupancy determine the corresponding coefficient weights. This support fidelity is exact for arbitrary query families in the finite model. Non-Shannon Rényi coefficients are distribution sensitive and can contain additional interaction generated by selective refinement; with overlapping access, such leakage can also cancel on a balance surface. They therefore should not be interpreted as prerequisite hyperedges merely because a coefficient is zero or nonzero.

The Hartley result answers a different question. Once the semantic quotient and access relation are specified, its cardinality formula follows by finite counting. The \(\log_2(N/k)\) sparse-access degradation quantifies support-space contraction as future-generating capacity becomes sparse; it is not the theorem that identifies interaction order. Thus the paper retains both results without conflating them: **Shannon for structural prerequisite support, Hartley for distinguishable state-space support**. The finite partition spine remains the supporting layer on which both results are stated. The phrase `zero-duration cut` is a finite idealization: CREST has not proved that states on intervals \([t-\varepsilon,t+\varepsilon]\) converge as \(\varepsilon\to0\), nor does it claim a continuous-time germ theorem in this manuscript.

## 12. Discussion

The central biological claim is that an ecological present can be temporally composite without ceasing to be present. A system can embody consequences retained from the past, response-relevant organization hidden from a coarse observation, and capacities that determine which future responses remain possible. These distinctions meet at one moment but are not reducible to one another. The temporal cut provides a place to state that fact without treating history as a present variable by fiat or treating future outcomes as causes of the present. In this prospective sense, CREST is close to—but not identical with—ecological resilience: both treat response under future disturbance as revealing a capacity of the current system rather than as making the realized future part of the present state (Walker et al. 2004).

This interpretation unifies several familiar ecological phenomena at the level of state. Ecological memory and priority effects show how past distinctions can remain active; hysteresis and restoration dynamics show that similar visible configurations can diverge in recovery; latent ecological organization shows that current response structure can be hidden; and differences in regeneration or response capacity show that identical appearances can support different reachable futures. CREST does not replace those theories. It identifies their shared implication: instantaneous visible configuration is not in general sufficient to define ecological identity at a moment.

The realizability results protect that biological interpretation. Positive temporal interaction does not appear merely because three labels are intersected, raw historical identity is not preserved when histories are semantically equivalent, and a fixed response grammar cannot generate a latent distinction that its own candidate-safe quotient has already erased. These restrictions matter because a theory of ecological state should not manufacture temporal dependence from arbitrary labels.

Sparse access adds a second ecological consequence. Even after retrospective and transverse distinctions are both retained, prospective differentiation can remain localized to only some combinations of them. Complete addressability would treat every semantic combination as equally capable of expressing the future response. The Shannon result states where that prospective interaction is structurally supported and weights it by accessible occupancy. The Hartley endpoint asks instead how much distinguishable support remains when accessibility is sparse. In that sense \(k/N\) describes the breadth of future-generating capacity across the state space, while \(\log_2(N/k)\) quantifies support-space contraction rather than prerequisite topology.

The shallow-lake witness makes the necessity concrete. The same coarse water-quality appearance can coexist with different sediment legacies and different current response configurations, and those differences can alter recovery even before any particular management decision is formulated. The formal prerequisite contrasts then reveal how different consequences of that hidden temporal structure become visible. They do not make state arbitrary; they expose distinctions already present in the ecology.

This is the sense in which ecological state is cut-relative without being merely observer-relative. A temporal cut fixes the moment at which equivalence is assessed. The biological structures carried to, embodied at, and expressible from that moment constrain which worlds can genuinely be called the same state. Once those structures are fixed, the least compatible quotient is a consequence of them rather than a discretionary choice of labels.

## 13. Conclusion

Ecological state is not located entirely in the instantaneous visible present. Systems that look the same at one moment can remain nonequivalent because they retain different histories, embody different latent response organization, or preserve different capacities for future response.

CREST represents the present as a temporal cut at which those three sources of distinction meet. Retrospective carried history, transverse latent-present response structure, and prospective response accessibility are defined before the state, and the ecological state is the least quotient that does not collapse their consequential differences. For prospective refinement, Shannon information preserves declared prerequisite support, whereas the Hartley endpoint quantifies how sparse accessibility contracts the distinguishable state space.

The resulting view is not that state is chosen by whatever question an investigator happens to ask. It is that the ecological present has temporal depth: past consequences can remain embodied, hidden organization can differentiate systems now, and the futures a system can still express are properties of its present organization. A temporal-cut state is the finite representation of that ecological fact.

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

Walker, B., C. S. Holling, S. R. Carpenter, and A. Kinzig. 2004. Resilience, adaptability and transformability in social–ecological systems. *Ecology and Society* 9(2):5. https://doi.org/10.5751/ES-00650-090205.