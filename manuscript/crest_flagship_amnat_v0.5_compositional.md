# Ecological State at a Temporal Cut: Compositional Interaction Across Time

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is often treated as a property measured at one moment. We instead model the present as an observational temporal cut through possible ecological worlds and define state as the least information that must survive that cut for a declared scientific contract. We separate three pre-state responsibilities: inherited history from MLTR, latent response type from MRM, and future-query grammar from CCOC. Their primitive definitions are acyclic. A strict audit shows that earlier fixed-closure cascades cannot be interpreted literally as these companions: immutable history blocks one zero-debt activation, and fixed-grammar MRM cannot hide a nontrivial response type at zero debt. We then construct literal conditioned bridges. Future queries refine relevant history classes as \(2^k\), and intervention grammar refines mechanism response types as \(2^k\). Most strongly, a common finite carrier with one history bit, one mechanism bit, and \(m\) exterior CCOC bits yields zero pairwise interaction but exactly \(m\) bits of genuine three-way interaction under jointly open composition. At \(m=10\), the state expands from four history-mechanism classes to 4096 joint classes, a 1024-fold amplification; 10 of 12 bits are pure three-way interaction.

**Keywords:** ecological state; temporal representation; ecological memory; state abstraction; open composition; non-additivity

## 1. Introduction

Ecologists already know that the present can carry signatures of the past. Antecedent conditions can generate measurable ecological memory (Ogle et al. 2015), hysteresis can make ecosystem response depend on history (Scheffer et al. 2001), and long transient dynamics can make instantaneous conditions a poor guide to where a system is going (Hastings et al. 2018). These results establish that time matters dynamically. They do not, by themselves, answer a different representational question: when several possible worlds look the same now, which distinctions must a scientific state retain?

A parallel formal literature constructs state by predictive or decision equivalence. Computational mechanics groups histories with the same predictive consequences into causal states (Shalizi and Crutchfield 2001). Predictive state representations encode dynamical state through action-conditional predictions (Littman, Sutton, and Singh 2001). Bisimulation and state-abstraction methods merge states while preserving declared behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). These are direct mathematical neighbors of the present work.

CREST does not claim novelty for the facts that history matters, future response can define state, hidden mechanisms can matter, or equivalence relations can formalize state abstraction. The question here is narrower: **what information must survive one observational present when retrospective meaning, latent response law, and future composition are required together, and can their state costs be obtained independently?**

The answer requires a distinction that is easy to blur. History, mechanism, and future are not three interchangeable ontological coordinates. MLTR begins from a declared replacement history and an inherited source law. MRM begins from primitive candidate laws and derives response types. CCOC fixes a controlled law and varies the legal future grammar under which configurations must be distinguished. CREST places the resulting responsibilities at one temporal cut only after these primitive objects have been declared.

This separation exposes both a boundary and a positive result. First, a strict realizability audit shows that an earlier class of abstract refinement cascades cannot simply be renamed as literal MLTR, MRM, and CCOC interactions. Second, once the companion quantifiers are respected, literal bridges exist. Future grammar can determine how many immutable history distinctions are relevant, intervention grammar can determine how many latent response types remain distinct, and jointly open composition can create a pure three-way interaction that is arbitrarily large.

The headline finite family has one history bit, one mechanism bit, and \(m\) exterior bits that become addressable only when the full history–mechanism–future contract is open. Every pairwise Möbius dividend is zero, while

\[
\boxed{m(H,\Theta,F)=m.}
\]

Thus genuinely three-way state information can be unbounded and can asymptotically dominate the required state.

## 2. Model: state at an observational temporal cut

Let \(\Omega\) be a declared finite set of possible ecological worlds. At time \(t\), an observation map

\[
O_t:\Omega\to Y_t
\]

induces the visible present partition

\[
\boxed{B_t=\ker O_t.}
\]

Two worlds lie in the same block of \(B_t\) exactly when they are indistinguishable under the declared observation at the cut. CREST does not model the present as a finite-width interval in the current theorem. The present is the observational cut and the equivalence relation it induces.

For a visible value \(y\), the fiber

\[
L_t(y)=O_t^{-1}(y)
\]

contains all latent worlds compatible with that same visible present. The state concept is

\[
\boxed{
\text{ecological state = the least information that must survive the temporal cut for the declared contract.}
}
\]

“Survive” is representational, not causal. A future contract can change what information must be retained at the cut without changing the physical past.

### 2.1 MLTR: raw history before retained history information

MLTR is source relative. Fix a root semantic map

\[
q_r:S_r\to Q_r
\]

and a finite rooted replacement graph with declared relations \(R_e\). A raw replacement history is a root-to-terminal path

\[
p=(e_1,\ldots,e_k),
\]

with composed relation

\[
R_p=R_{e_1};\cdots;R_{e_k}.
\]

When source labels are consistent through \(R_p\), the path induces a carried terminal map

\[
c_p:S_v\to Q_r.
\]

Only then is historical equivalence defined:

\[
p\equiv_H p'
\iff
c_p=c_{p'}.
\]

The full MLTR minimum-history result therefore retains one mode per distinct complete carried map. The raw path and root law precede the retained history quotient; the terminal CREST state does not define its own past.

### 2.2 MRM: primitive candidate law before response type

MRM fixes a visible macrostate set \(Q\), action set \(A\), and a finite candidate family \(C=\{\theta\}\). Each primitive candidate induces transitions

\[
G_a^\theta:Q\to Q.
\]

Two mechanisms are response equivalent under the declared grammar when their complete transition tables agree:

\[
\theta\equiv_\Theta\theta'
\iff
G_a^\theta(q)=G_a^{\theta'}(q)
\quad\forall q,a.
\]

The response-type set is

\[
R=C/\!\equiv_\Theta.
\]

Thus the CREST “latent present” is more precisely **latent response structure**. MRM does not require preservation of complete ontic mechanism identity; it retains only primitive-candidate differences that alter a declared response.

### 2.3 CCOC: future as a query grammar, not a future state variable

CCOC fixes a finite controlled system

\[
\mathcal M=(S,A,T,h)
\]

and a declared legal future grammar

\[
\mathcal L\subseteq A^*.
\]

For raw configuration \(s\), define the future-response profile

\[
\rho^{\mathcal M}_{\mathcal L}(s)
=
\bigl(\operatorname{Tr}_{\mathcal M}(s,w)\bigr)_{w\in\mathcal L}.
\]

The exact future equivalence is

\[
s\equiv^{\mathcal M}_{\mathcal L}s'
\iff
\rho^{\mathcal M}_{\mathcal L}(s)=\rho^{\mathcal M}_{\mathcal L}(s').
\]

The response interface \(Q_{\mathcal L}=S/\!\equiv_{\mathcal L}\) is derived afterward. CCOC therefore places a **right-of-cut query responsibility** at the temporal cut. It does not posit a separate realized future state.

### 2.4 Quantifier firewall

CCOC and MRM both use future responses but quantify over different primitives:

\[
\text{CCOC: law fixed; raw configuration and legal grammar compared},
\]

whereas

\[
\text{MRM: visible state/grammar fixed; latent candidate law compared}.
\]

MLTR fixes an inherited source law and compares declared replacement histories. These dependencies are acyclic. CREST does not assume the resulting responsibilities are statistically independent, ontologically independent, or exhaustive.

## 3. Methods: two interaction questions

Two mathematically distinct interaction questions must be separated.

### 3.1 Fixed-closure interaction

On one declared carrier, let \(C_1,\ldots,C_k\) be monotone, inflationary, idempotent refinement closures above baseline \(B_t\). For coalition \(S\), let \(J_S\) be its least common fixed point and define

\[
v(S)=\log_2|J_S|-\log_2|B_t|.
\]

The generic non-additive debt is

\[
\Delta=v(N)-\sum_i v(\{i\}).
\]

The Möbius/Harsanyi dividend of a coalition \(S\) is

\[
m(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}v(T).
\]

This is the setting of CREST's earlier marked-cycle and three-audit closure extrema. The audit objects and their legal transition rows are held fixed while coalition membership changes.

### 3.2 Conditioned cross-contract interaction

The companion theories introduce a second question. In CCOC, opening composition changes the legal future grammar itself. In MRM, response-type equivalence is defined relative to the declared action grammar. In a target-specific use of MLTR, the scientific task may require only the parts of a complete carried map that are reachable by the declared future queries.

Accordingly, let each coalition \(S\subseteq\{H,\Theta,F\}\) specify an exogenous scientific contract \(\mathcal C_S\), including its legal future/intervention grammar. Let

\[
v_{\mathcal C}(S)
\]

be the minimum exact state information required under that coalition's declared contract. The same Möbius transform can be applied to this set function, but its interpretation differs from the fixed-closure game: **coalition inclusion may change which queries are legally required.**

This distinction is essential to a literal CCOC bridge and prevents the future grammar from being inferred circularly from the state quotient it later induces.

## 4. Results I: strict realizability boundaries

Before constructing a positive bridge, we ask what cannot work.

### 4.1 Fixed partitions cannot generate positive one-cut interaction

Suppose the visible baseline has one class and each responsibility contributes only a fixed precomputed partition \(P_i\). Their common refinement has at most the product of the individual block counts:

\[
|P_{\rm joint}|\le\prod_i|P_i|.
\]

Therefore

\[
\boxed{
\log_2|P_{\rm joint}|-
\sum_i\log_2|P_i|
\le0.
}
\]

Positive interaction therefore requires more than intersecting fixed companion quotients. Some state obligation must be state dependent or contract conditioned.

### 4.2 Immutable-history no-activation theorem

Let \(H\) be an MLTR history label on the cut carrier and let a post-cut audit \(C_F\) satisfy

\[
C_F(B_t)=B_t.
\]

Assume every legal post-cut transition preserves the raw history label:

\[
H(\tau_a(w))=H(w).
\]

Then the history partition is already fixed by \(C_F\):

\[
\boxed{C_F(P_H)=P_H.}
\]

The proof is immediate from the refinement signature: zero debt on the one-class baseline forbids static-label or legal-row differences, and history-preserving successors of two worlds in the same history block remain in that same block. A zero-debt future closure therefore cannot be activated by immutable history alone.

This boundary matters because an earlier CREST marked-cycle witness used a transition that crossed a static “history” mark. Its closure arithmetic is valid, but that mark cannot literally be an immutable MLTR replacement history.

### 4.3 Fixed-grammar MRM zero-debt no-go

Let \(P_Q\) partition the MRM typed space \(Q\times R\) by visible state. If \(P_Q\) is already candidate safe under a fixed action grammar, then

\[
G_a^r(q)=G_a^{r'}(q)
\quad\forall q,a,r,r'.
\]

Hence every complete response table is identical and

\[
\boxed{|R|=1.}
\]

A nontrivial fixed-grammar MRM response-type family therefore cannot have zero standalone candidate-safe debt and become nontrivial only after another fixed partition is added.

These no-go results do not invalidate the older abstract closure extrema. They delimit their literal companion interpretation.

## 5. Results II: literal pairwise conditioned bridges

The no-go results suggest the correct repair: keep raw history and primitive mechanism fixed, but allow the **relevance equivalence** to depend on the declared future grammar.

### 5.1 Future-conditioned MLTR history

Let the MLTR root have two states \(u_0,u_1\) with \(q_r(u_b)=b\). Let the terminal set be

\[
S_v=\{z_0,z_1,x_1,\ldots,x_m\}.
\]

For each binary signature \(r=(r_1,\ldots,r_m)\), declare one replacement history with composed relation

\[
R_r=
\{(u_0,z_0),(u_1,z_1)\}
\cup
\{(u_{r_i},x_i):1\le i\le m\}.
\]

The carried map satisfies

\[
c_r(z_0)=0,
\quad
c_r(z_1)=1,
\quad
c_r(x_i)=r_i.
\]

All \(2^m\) complete carried maps are distinct. Now let the future grammar contain queries reaching only \(x_1,\ldots,x_k\). The target-specific history profile is

\[
\rho^H_k(p_r)=(r_1,\ldots,r_k).
\]

Thus

\[
\boxed{|H_{\min}(k)|=2^k,\qquad K_H(k)=k\text{ bits}.}
\]

Opening the future grammar from zero to all \(m\) queries increases relevant history information by exactly \(m\) bits. The raw past never changes; only which carried-map differences matter to the declared future task changes.

### 5.2 Grammar-conditioned MRM response type

Let \(Q=\{0,1\}\) and candidate mechanisms be indexed by \(r\in\{0,1\}^m\). All candidates share an identical `hold` action, while

\[
G^{\theta_r}_{\mathrm{probe}_i}(q)=r_i.
\]

If the declared intervention grammar contains the first \(k\) probes, two candidates are response equivalent exactly when their first \(k\) signature bits agree. Hence

\[
\boxed{|R(k)|=2^k,\qquad K_\Theta(k)=k\text{ bits}.}
\]

Again the primitive candidates do not change. The declared action grammar changes the response equivalence derived from them.

At \(m=10\), both literal pairwise bridges move from one relevant class and zero bits to 1024 classes and 10 bits.

## 6. Results III: pure literal three-way compositional interaction

We now combine the companion interfaces on one common finite carrier while respecting their quantifiers.

### 6.1 Common carrier

Take one binary MLTR history interface

\[
h\in\{0,1\},
\]

one binary MRM response-type interface

\[
\theta\in\{0,1\},
\]

and an \(m\)-bit CCOC exterior/addressability coordinate

\[
a=(a_1,\ldots,a_m)\in\{0,1\}^m.
\]

Define

\[
\boxed{
\Omega_m=
\{0,1\}_h
\times
\{0,1\}_\theta
\times
\{0,1\}^m_a.
}
\]

All worlds share one visible cut observation.

The history bit can be supplied by the canonical two-mode MLTR path-incoherence witness. The mechanism bit can be supplied by the one-bit MRM binary-signature frontier. CCOC treats \((h,\theta)\) as the already-required inside interface of a larger composition problem and \(a\) as exterior information.

### 6.2 Coalition contracts

For coalition \(S\subseteq\{H,\Theta,F\}\):

- preserve \(h\) if \(H\in S\);
- preserve \(\theta\) if \(\Theta\in S\);
- legalize the CCOC cross-interface future words that decode all \(a_i\) **only** in the jointly open contract \(S=\{H,\Theta,F\}\).

This grammar rule is declared before state minimization. It is the cross-contract analogue of CCOC's closed-versus-open grammar comparison.

The exact coalition value is

\[
\boxed{
v_m(S)
=
\mathbf 1_{H\in S}
+
\mathbf 1_{\Theta\in S}
+
m\,\mathbf 1_{\{H,\Theta,F\}\subseteq S}.
}
\]

Therefore

\[
\begin{aligned}
v(H)&=1,& v(\Theta)&=1,& v(F)&=0,\\
v(H\Theta)&=2,& v(HF)&=1,& v(\Theta F)&=1,\\
v(H\Theta F)&=m+2.
\end{aligned}
\]

### Theorem 1 — pure genuine three-way interaction

All pairwise dividends vanish:

\[
\boxed{
m(H,\Theta)=m(H,F)=m(\Theta,F)=0.}
\]

The genuine three-way dividend is

\[
\boxed{m(H,\Theta,F)=m.}
\]

### Proof

The singleton and pair values follow from the two binary component interfaces and the absence of a cross-interface exterior decoder outside the full contract. In the full coalition, the jointly open CCOC grammar makes all \(m\) exterior bits response relevant, so the exact state is \((h,\theta,a)\) with \(2^{m+2}\) classes and \(m+2\) bits. Thus the pairwise Möbius terms are \(2-1-1=0\), \(1-1-0=0\), and \(1-1-0=0\). The three-way term is

\[
(m+2)-2-1-1+1+1+0=m.
\]

\(\square\)

The standalone sum is two bits, so the generic interaction debt for this conditioned contract game is

\[
\boxed{\Delta=m.}
\]

All of that interaction debt is genuine three-way interaction. Its share of the full state is

\[
\boxed{
\frac{m}{m+2}\longrightarrow1.
}
\]

This is the literal companion-derived unbounded interaction result.

## 7. Numerical closure

At \(m=10\), the conditioned coalition values are:

| contract | classes | bits |
|---|---:|---:|
| visible cut | 1 | 0 |
| history | 2 | 1 |
| mechanism | 2 | 1 |
| future only | 1 | 0 |
| history + mechanism | 4 | 2 |
| history + future | 2 | 1 |
| mechanism + future | 2 | 1 |
| **history + mechanism + jointly open future** | **4096** | **12** |

The full state therefore contains

\[
\boxed{10\text{ bits of pure genuine three-way interaction}.}
\]

Every pairwise interaction is zero. The three-way term is

\[
\frac{10}{12}=83.33\%
\]

of the full state and 100% of the interaction debt. Relative to the history-plus-mechanism interface, state cardinality increases

\[
4\longrightarrow4096,
\]

an exact

\[
\boxed{1024\times}
\]

amplification. At \(m=18\), the three-way share reaches 90%; as \(m\to\infty\), it approaches 100%.

## 8. The older fixed-closure extremum remains a separate theorem

CREST also has an exact fixed-closure three-audit family with

\[
m(H,\Theta,F)=b-\log_2 3
\]

and, at \(b=10\), 1024 required classes, 10 total bits, and 8.415 bits in the order-three Möbius term. Those arithmetic statements remain correct for the declared closure operators.

The strict companion audit changes only their interpretation. The marked seed in that construction is not a literal immutable MLTR replacement history, and its zero-standalone latent audit is not a literal nontrivial fixed-grammar MRM response-type quotient. We therefore retain that family as an **abstract fixed-closure extremum** showing what state-dependent closures can do, not as the flagship companion-derived temporal model.

The new conditioned theorem answers the literal bridge question instead:

\[
\boxed{m(H,\Theta,F)=m}
\]

with raw history and primitive mechanism fixed and the CCOC future grammar declared exogenously by contract.

## 9. Relation to existing concepts of ecological and dynamical state

### 9.1 Ecological memory, hysteresis, and transients

Ecological memory models quantify effects of antecedent conditions on current processes (Ogle et al. 2015). Hysteresis and alternative-state theory show path dependence in ecosystem response (Scheffer et al. 2001). Transient ecology emphasizes that instantaneous conditions can be poor guides to longer-term behavior (Hastings et al. 2018).

CREST is compatible with those phenomena but asks a representational question: given possible worlds that agree at the present cut, which past distinctions are relevant under a declared future task, and how does that requirement compose with latent response and future-query obligations?

### 9.2 Predictive and causal states

Causal-state constructions merge histories with identical predictive distributions (Shalizi and Crutchfield 2001), while predictive state representations encode state through action-conditional future predictions (Littman, Sutton, and Singh 2001). These theories demonstrate that state need not be synonymous with an instantaneous physical snapshot.

CREST differs by keeping the present observation as an explicit baseline cut and by separating primitive companion responsibilities before examining their composition. The headline theorem is not predictive-state minimality; it is the non-additive state cost created when separately defined semantic, latent-response, and future-composition contracts are combined.

### 9.3 State abstraction and bisimulation

Bisimulation and state-abstraction methods merge states while preserving specified transition or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006). CREST uses the same broad mathematical principle that scientifically irrelevant distinctions may be erased.

CREST does not claim novelty for that substrate. The contribution claimed here is narrower: an observational cut can support multiple non-circular responsibility definitions, naive fixed-quotient composition has sharp limitations, and a literal cross-contract construction can have arbitrarily large pure three-way state interaction.

## 10. Companion theories, evidence, and scope

**MLTR** supplies retrospective carried semantics and minimum history modes from declared replacement routes.

**MRM** supplies latent response types and candidate-safe state from declared candidate laws and intervention grammars.

**CCOC** supplies future-response equivalence and open-composition lower bounds under declared legal future grammars.

**CED** remains downstream evidence licensing. Required state, identified state, and reportable target are not generally identical:

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}.
}
\]

The present paper is finite, exact, and conditional. It does not claim that the three responsibilities exhaust ecological state, that every system has a unique decomposition into them, that the contracts can be inferred from data without additional assumptions, or that the results automatically extend to continuous-time, stochastic, infinite-state, or approximate settings.

The MLTR root semantic map is an explicit source-relative premise. MRM candidate mechanisms are declared rather than inferred. CCOC future grammar is declared rather than learned from the state quotient. These are scientific-contract assumptions, not hidden outputs of CREST.

## 11. Discussion

The temporal-cut formulation makes a distinction between **what exists** and **what must be retained**. Raw history exists as a path before the terminal state is constructed. Candidate mechanisms exist before they are grouped into response types. Legal future queries are declared before the response interface is minimized. CREST asks only which equivalence relation over the resulting worlds remains licensed when those obligations meet at one cut.

The no-go results are useful because they prevent an attractive but incorrect shortcut. If history is truly retrospective, a future action cannot activate a zero-debt closure by changing the past label. If MRM response types are defined under one fixed grammar, a nontrivial response-type difference cannot be invisible to the exact candidate-safe state and then appear only after another partition is supplied. A temporal interpretation therefore has to respect the companion quantifiers rather than merely relabel an arbitrary refinement cascade.

The positive bridges show that this restriction does not make temporal interaction disappear. Instead, interaction moves to the scientifically meaningful object: **contract-conditioned relevance**. A future grammar can expose distinctions among immutable histories because different parts of their carried semantics become query relevant. A wider intervention grammar can expose differences among fixed candidate mechanisms because additional response coordinates enter the response-type definition. And open composition can make exterior information addressable only when multiple component interfaces are simultaneously available.

The pure three-way theorem is particularly transparent. History and mechanism each cost one bit. Future alone costs zero. No pair creates interaction. Yet the full jointly open contract adds \(m\) bits that belong to no singleton or pair. This provides a strict finite sense in which state information can be created by the composition of scientific responsibilities rather than assigned to one temporal side in isolation.

A continuous-time theory could replace declared finite histories and future words with left/right temporal germs and local response kernels, but such an extension would require new assumptions and proofs. It is not implied by the current finite result.

## 12. Conclusion

The present need not be the ecological state. It can be the cut at which a state must be constructed.

At that cut, retrospective history, latent response law, and future-query responsibility can be defined without using the state they later induce. Their individual definitions are therefore non-circular. But their relevance need not compose additively.

The literal companion-derived finite theorem gives

\[
\boxed{m(H,\Theta,F)=m,}
\]

with every pairwise interaction equal to zero. At \(m=10\), history and mechanism together require four classes and two bits; the jointly open state requires 4096 classes and 12 bits. The increase is 1024-fold in state count, and 10 bits—83.33% of the full state—are pure genuine three-way interaction.

Thus ecological state is not merely the variables observed now, nor is it obtained by independently compressing “past,” “mechanism,” and “future.” It is the least information that must survive a temporal cut under the **composed scientific contract**.

## Literature Cited

Givan, R., T. Dean, and M. Greig. 2003. Equivalence notions and model minimization in Markov decision processes. *Artificial Intelligence* 147:163–223. https://doi.org/10.1016/S0004-3702(02)00376-4.

Hastings, A., K. C. Abbott, K. Cuddington, T. Francis, G. Gellner, Y.-C. Lai, A. Morozov, S. Petrovskii, K. Scranton, and M. L. Zeeman. 2018. Transient phenomena in ecology. *Science* 361:eaat6412. https://doi.org/10.1126/science.aat6412.

Li, L., T. J. Walsh, and M. L. Littman. 2006. Towards a unified theory of state abstraction for MDPs. In *Proceedings of the 9th International Symposium on Artificial Intelligence and Mathematics (AI&M 2006)*, Fort Lauderdale, Florida.

Littman, M. L., R. S. Sutton, and S. Singh. 2001. Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

Ogle, K., J. J. Barber, G. A. Barron-Gafford, L. P. Bentley, J. M. Young, T. E. Huxman, M. E. Loik, and D. T. Tissue. 2015. Quantifying ecological memory in plant and ecosystem processes. *Ecology Letters* 18:221–235. https://doi.org/10.1111/ele.12399.

Scheffer, M., S. Carpenter, J. A. Foley, C. Folke, and B. Walker. 2001. Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000.

Shalizi, C. R., and J. P. Crutchfield. 2001. Computational mechanics: pattern and prediction, structure and simplicity. *Journal of Statistical Physics* 104:817–879. https://doi.org/10.1023/A:1010388907793.
