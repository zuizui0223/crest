# CREST mathematical program map — from four theorem families to one philosophy of ecological state

> **Status:** synthesis/consolidation document, 2026-08-21. No new theorem is introduced here. This document organizes the already-proved CCOC, MLTR, MRM, CED, and CREST results into one mathematical hierarchy and makes explicit where the argument changes from mathematics to philosophy.

## 0. One-line verdict

The four companion repositories are not four rival definitions of ecological state. They are four mathematically distinct ways in which a proposed ecological equivalence can fail.

Their common upstream problem is:

> **Given a set of ecological configurations and a declared scientific contract, which differences may be ignored while treating configurations as the same state?**

CREST lifts this into the joint question:

> **Does one fully adequate ecological state exist under the declared contract; if so, what is the least-information state; and does the available evidence identify which state is occupied?**

The resulting finite theory has three logically separate gates:

```text
compatible world/carrier existence
        -> required least-information state
        -> evidential identification / target report
```

---

## 1. Upstream mathematical concept: contract-relative distinguishability

Let `U` be a finite set of latent ecological worlds/configurations. A coarse ecological state representation is mathematically a partition `P` of `U`, or equivalently an equivalence relation.

If two worlds `u,v` lie in the same block, the representation asserts that their difference may be ignored for the scientific work assigned to that state.

A scientific contract specifies which distinctions must survive. Depending on the problem, the contract may include:

- legal future actions or action words;
- outputs and successor behavior;
- source labels inherited through structural replacement;
- retained response mechanisms;
- experiment/observation records and failure assumptions;
- report targets;
- coverage obligations over a synchronized latent-world carrier.

The common mathematical question is therefore not merely clustering. It is a **factorization/exactness problem**:

> Which outputs, legal-action rows, successors, inherited meanings, mechanism-conditioned responses, or target values must factor through the proposed partition?

When a block violates a declared requirement, the block must split. When no split is forced, the difference may remain compressed.

This gives the shared mathematical vocabulary:

- **equivalence / partition** — what is being called the same state;
- **refinement** — which previously ignored distinctions must be restored;
- **coarsest adequate quotient** — maximum exact compression for the declared task;
- **carrier** — which latent worlds can coherently host the joint contract at all;
- **evidence partition** — which latent worlds remain observationally indistinguishable;
- **set-valued report** — the sharp answer when one deterministic state/target is not licensed.

The four repositories differ in **what is allowed to vary and what obligation the state is required to preserve**.

---

## 2. Four companion repositories as four axes of ecological sameness

| Repository | What varies? | Central equivalence question | Mathematical failure | Canonical response |
|---|---|---|---|---|
| **CCOC** | legal future grammar / composition | Will currently merged configurations remain indistinguishable under enlarged futures? | a newly legal future separates a merged pair; exact interface size can inflate | retain more response-relevant state information |
| **MLTR** | structural replacement / inherited semantics / history | Can an existing macrostate meaning be transported to a changed ecological system? | carried source labels cease to be exact or become route-dependent | source-relative refinement and, if needed, minimal history context |
| **MRM** | retained mechanism / response-law alternatives | Can one state support one prediction while several mechanisms remain live? | retained response types disagree under a declared action | typed state, set-valued prediction, or active discrimination |
| **CED** | experiment / observation / failure / target contract | Which required distinctions are actually licensed by finite evidence? | one evidence class spans multiple target values or required state blocks | honest ambiguity, stronger observation design, or target-focused experiment |

These axes are related but not interchangeable. A state can pass one and fail another.

---

## 3. CCOC — future sufficiency and open-composition compression

### 3.1 Canonical exact response interface

For a finite controlled system `M=(S,A,T,h)` and legal future grammar `L`, define

\[
s\equiv_L t
\iff
\forall w\in L,\;\operatorname{Tr}(s,w)=\operatorname{Tr}(t,w).
\]

Then

\[
Q_L=S/\!\equiv_L,
\qquad
K_L=\log_2|Q_L|
\]

is the canonical exact response interface and its memory.

This fixed-grammar quotient is substrate, not the claimed novelty.

### 3.2 Cross-grammar operational lower bound

For a jointly reachable product-like family

\[
I\times E_1\times\cdots\times E_q,
\]

if legal open futures independently decode the inside coordinate and each exterior coordinate, then

\[
K_{\rm open}\ge
\log_2|I|+\sum_j\log_2|E_j|.
\]

If closed context `j` factors through only `(I,E_j)`, then

\[
K_{{\rm closed},j}\le
\log_2|I|+\log_2|E_j|,
\]

and therefore

\[
K_{\rm open}-\max_jK_{{\rm closed},j}
\ge
\sum_j\log_2|E_j|-\max_j\log_2|E_j|.
\]

### 3.3 Constrained-codebook form

The product premise is not essential. If a finite jointly realizable codebook `C` is pairwise separated by legal open futures, then

\[
|Q_{\rm open}|\ge |C|,
\]

with the corresponding projected closed-context bound.

### 3.4 Fixed-regular extremal family

For every `m>=1`, CCOC constructs a bounded-local finite system with

\[
D_m=\{0,1\}^{m+1},
\qquad
A=\{0,1,\mathsf{fire},\mathsf{tick}\},
\]

such that opening only the previously illegal action `fire` changes

\[
|P_C|=2,
\qquad
|P_O|=2^{m+1},
\]

so

\[
K_O-K_C=m.
\]

This saturates the absolute finite-domain maximum. The witness uses a degree-at-most-three tree, one-edge focal/exterior cut, bounded local alphabets, and worst canonical query length

\[
2\lceil\log_2m\rceil+2.
\]

Thus the effect is not an artifact of a growing primitive alphabet or unbounded local degree.

### 3.5 Positive portability and forced split

CCOC also supplies the positive boundary: if all stages map coherently to the same macrostate set with preserved macro outputs/transitions, one portable macro-law exists across nested stages.

Conversely, if a newly legal future word distinguishes two states that the old macrostate merged, the merge must split.

### 3.6 Mathematical meaning inside CREST

CCOC contributes the **future-sufficiency closure**: distinctions that future action/interaction possibilities can operationally expose cannot safely be discarded by a state expected to survive that future contract.

---

## 4. MLTR — semantic transport, source-relative repair, and history

MLTR studies a different problem. The future grammar is not the only thing changing; the ecological structure itself can be replaced, while an inherited source classification is carried into the target.

### 4.1 Theorem A — supplied common macro-law transport

If source and target already project exactly to one macro-dynamics and the declared replacement relation preserves labels, output, legal-action rows, and related successors, then the same macro-law is shared across the replacement edge and across a finite connected replacement graph.

### 4.2 Theorem B — derive the target labels

Given an exact source projection and a total replacement relation satisfying target-fiber label consistency, output preservation, legal-action-row preservation, and successor closure, the target projection can be **derived** from the source labels rather than assumed.

### 4.3 Theorem C — conservative transport with target-only actions

Target-only actions are permitted when their availability and target macro-successor are uniform within each carried target macro fiber. The source law then embeds as a restriction of an expanded target schema.

### 4.4 Proposition D — newly legal target word forces a semantic split

If a future word illegal at source but legal after replacement separates two states inside one carried macro fiber, the carried merge is not exact in the target.

### 4.5 Theorem E — unique coarsest source-relative repair

Starting from the carried target partition `c_R`, repeatedly split blocks by target output, legal-action row, and successor block. The fixed point is the

> **unique coarsest exact target projection refining the carried source partition**.

The relative transport defects are

\[
\Delta_{\#}=|Q_T^{\min}|-|Q_S|,
\qquad
\Delta_K=\log_2|Q_T^{\min}|-\log_2|Q_S|.
\]

In the accumulating binary witness,

\[
|Q_S|=2,
\qquad
|Q_T^{\min}|=2^m+1,
\qquad
\Delta_{\#}=2^m-1.
\]

The minimality is **source-relative**. It is not a claim that the repaired partition is the globally smallest target abstraction after discarding source provenance.

### 4.6 Theorem F — path-label coherence

On a rooted finite replacement DAG, if every root-to-terminal path induces the same carried terminal map pointwise, then the carried partition, its unique source-relative repair, and the transport defect are route independent.

### 4.7 Theorem G — minimum history augmentation

When path-specific carried terminal maps disagree, the minimum number of history modes needed to preserve all declared carried meanings is

\[
|H_{\min}|=|\{c_p\}|.
\]

The raw context cost and final repaired-interface cost are distinct:

\[
\Delta_H^{\#}=|H_{\min}|-1,
\qquad
\Delta_H^K=\log_2|H_{\min}|,
\]

versus

\[
\Delta_{\rm HA}^{\#}=|Q_{T\times H}^{\min}|-|Q_r|,
\qquad
\Delta_{\rm HA}^K=\log_2|Q_{T\times H}^{\min}|-\log_2|Q_r|.
\]

### 4.8 Mathematical meaning inside CREST

MLTR contributes the **semantic-coherence closure**: a state inherited through turnover, extinction, recolonization, or rewiring may keep its name while losing the operational meaning required for the declared target system. CREST therefore treats inherited meaning as a constraint, not as a free target reclustering problem.

---

## 5. MRM — mechanism robustness and ambiguity-aware prediction

MRM fixes a common observable macrostate space but retains multiple possible response laws/mechanisms.

### 5.1 Result I — universal deterministic law criterion

A candidate-independent deterministic law exists exactly when all retained candidate transition maps agree for every declared action. Equivalently, the number of distinct response types is

\[
R=1.
\]

### 5.2 Result II — typed and set-valued reports

If `R>1`, retaining response type yields deterministic dynamics on `Q x R`. If response type is forgotten, the exact report is set-valued:

\[
F_a(q)=\{G_a^\theta(q):\theta\in C\}.
\]

### 5.3 Result III — candidate-safe product lower bound

Under uniform operational separation of response types,

\[
K_{\rm typed}\ge\log_2|Q|+\log_2R.
\]

### 5.4 Result IV — joint exterior + mechanism uncertainty

When the entire product is jointly operationally addressable,

\[
K_{\rm joint}\ge
\log_2|I|+\sum_j\log_2|E_j|+\log_2R.
\]

This is a joint-injection result, not arithmetic addition of unrelated lower bounds.

### 5.5 Result V — minimal candidate-safe quotient

Starting from observable-state blocks, repeatedly refine the typed product `(q,r)` by successor blocks under every action. The fixed point is the unique coarsest observation-preserving deterministic candidate-safe quotient.

Response type is retained only where it changes declared future behavior.

### 5.6 Result VI — active discrimination

Dynamic programming over

\[
Q\times\{S:\varnothing\ne S\subseteq R\}
\]

returns a minimum-worst-case adaptive intervention tree that identifies the retained response type, or certifies that no finite declared intervention policy can do so.

### 5.7 Results VII–VIII — canonical mechanism-ambiguity and identification frontiers

For

\[
R_m=\{0,1\}^m,
\qquad Q=\{0,1\},
\]

with probe actions reading response bits,

\[
|Q||R_m|=2^{m+1},
\qquad K=m+1,
\]

so unresolved mechanism ambiguity contributes exactly `m` extra bits relative to one fixed candidate.

Identifying `2^m` response types needs at least `m` binary-outcome intervention levels; the canonical `m` probes attain the lower bound. After `k` distinct probes, exactly `2^{m-k}` response types remain.

### 5.8 Result IX — cost-aware exact discrimination

With positive action costs,

\[
V(q,S)=\min_a\left[c(a)+\max_x V(x,S_{a,q,x})\right]
\]

with singleton base case, giving an exact minimum worst-case intervention cost or no-plan certificate within the declared finite action grammar.

### 5.9 Result X — robust bounded-error update

For observation-error supports `N(x)`, posterior-compatible response types are updated conservatively by

\[
S'=\{r\in S:G_a^r(q)\in N(x)\}.
\]

Singleton means identification under the declared support; multiple types require retained ambiguity; empty set is a contradiction against the retained family/error contract.

### 5.10 Result XI — probabilistic observation update

Given likelihoods and a prior,

\[
\pi'(r)=
\frac{\pi(r)L(x\mid G_a^r(q))}
{\sum_s\pi(s)L(x\mid G_a^s(q))}.
\]

The framework supports posterior uncertainty, credible sets, entropy, and threshold-based resolution without turning MAP into certainty.

### 5.11 Result XII — one-step value of information

MRM computes expected posterior entropy and

\[
\mathrm{EIG}(a)=H(\pi)-\mathbb E[H\mid a],
\]

optionally net of action cost. This is a one-step design diagnostic, not a full sequential optimal-control theorem.

### 5.12 Mathematical meaning inside CREST

MRM contributes the **mechanism-robustness closure**: two configurations may be visibly identical yet fail to support the same deterministic prediction because retained response laws disagree. The relevant state need not encode full mechanism identity; it must retain only mechanism distinctions that alter the declared response.

---

## 6. CED — evidential licensing, target-safe resolution, and experiment design

CED changes the direction of the problem. It begins from what a finite experiment can actually distinguish.

### 6.1 Result 1 — experiment-induced quotient and honest reporting

A declared finite experiment partitions latent worlds by their complete records. Every record-based report must be constant on one such evidence class.

A deterministic target report is justified exactly when the target is constant on the compatible class. Otherwise the sharp report is the set of compatible target values.

### 6.2 Result 2 — unique coarsest target-safe quotient

Starting from the evidence-induced partition, refine only as much as needed so that the declared target is constant and deterministic successors remain stable under declared actions.

This gives the unique coarsest record-preserving, target-constant, action-stable refinement.

Critical boundary:

> this quotient is the **minimum resolution required** for target-safe tracking, not a claim that current data already identify its blocks.

### 6.3 Result 3 — failure architecture determines trustworthy refinement

A nominal record difference is not automatically trustworthy under imperfect observation.

Main structural results include:

- finite negative evidence does not become deductive absence under imperfect sensitivity;
- repetition inside one shared failure domain is not equivalent to independent failure diversity;
- under a declared availability lower bound `a`, a worst-case guarantee ceiling

\[
1-(1-a)^m
\]

can remain even with arbitrarily many repeats inside the same failure mode;
- equal effort spread across independent modes can provide stronger worst-case guarantees than the same replicate count concentrated within one shared mode.

### 6.4 Result 4 — adaptive risk-limited target resolution

Within a declared finite policy family, policies are evaluated by correct deterministic reporting, wrong deterministic reporting, honest ambiguity, and expected cost.

The objective is least-cost defensible target resolution under an explicit false-resolution contract, not maximal information about the full latent world.

A central benchmark shows that full-world information gain can prefer a target-irrelevant measurement while target-safe design chooses the experiment that resolves the declared prediction.

### 6.5 Supporting theorem families

CED also retains supporting mathematics for:

- delayed-exposure / no-uniform finite passive closure certification;
- imperfect detection;
- independent mode diversity;
- overlapping failure factors;
- dependent and non-reset repeats;
- false-positive thresholds;
- multiple-coordinate error control;
- calibration-derived bounds;
- false-discovery budgets;
- heterogeneous thresholds;
- adaptive alpha spending;
- independent concentration bounds;
- posterior-sample finite-support bridges.

These support the evidence contract and methods but are not all equal-weight headline results.

### 6.6 Mathematical meaning inside CREST

CED contributes two logically different objects:

1. a **required target-safe resolution** that may need to be represented; and
2. an **evidence partition** describing what has actually been earned by the data.

This distinction is what allows CREST to separate state existence from state identification.

---

## 7. The deeper relationship among the four repositories

The four families can be written as variations of one abstract schema.

Let `P` be a proposed partition of ecological worlds. Each audit supplies a condition of the form

\[
\text{if }u\sim_P v,\text{ then all distinctions relevant to contract }i
\text{ must agree/factor through }P.
\]

When this fails, the audit generates a forced refinement.

Schematically:

\[
P
\xrightarrow{\;C_\Gamma\;}
\text{future-safe refinement},
\]

\[
P
\xrightarrow{\;C_{\mathcal H}\;}
\text{semantically coherent refinement},
\]

\[
P
\xrightarrow{\;C_\Theta\;}
\text{mechanism-safe refinement},
\]

\[
P
\xrightarrow{\;C_{D,T}\;}
\text{target-safe required refinement}.
\]

When the companion problems are synchronized on one carrier, CREST treats these as refinement closures on one partition lattice.

This is the precise sense in which CCOC, MLTR, MRM, and CED become four **constraints on one state**, rather than four states.

---

## 8. CREST synthesis mathematics

The CREST repository adds mathematics that genuinely couples the companion contracts.

### 8.1 J3 — maximal universal common carrier

Descending iteration returns the unique greatest compatible transition-closed carrier `U*`.

It proves:

- a nonempty universal common lift exists iff `U*` is nonempty;
- a coverage-complete lift exists iff `U*` represents every required label;
- removed worlds have finite rank-decreasing action-chain no-go certificates.

### 8.2 J6 — maximal controlled common carrier

Under universal safety for uncontrollable actions and existential choice over controllable actions, descending iteration returns the unique greatest robustly controlled-invariant carrier `K*`.

It additionally yields a memoryless safe selector and finite typed AND/OR no-go certificates.

J3 and J6 differ by action quantifier and neither supersedes the other.

### 8.3 J4/J7 — minimum declared carrier repair

J4 characterizes the exact fixed-subset repair cost for the universal carrier problem; J7 does the controlled analogue with fallback/control operations.

Their global optima are finite subset minimizations. Both repair decision problems are NP-complete by weighted set-cover reductions.

The repair solvers are exact exponential oracles, not polynomial-time claims.

### 8.4 J1 — unique coarsest joint state

On one admissible finite common carrier `U`, baseline `B`, and monotone inflationary idempotent audit closures,

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B)
}
\]

is the unique coarsest / least-information common fixed point.

The notation denotes the common closure reached by fair repeated refinement; one pass can be insufficient and pairwise commutation is not required.

For a world `u`,

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

J1 also proves the evidence gate:

\[
\text{full deterministic state report exists}
\iff
J\preceq E_D.
\]

If the gate fails, the sharp report is the set of `J`-blocks compatible with the evidence class. A target may still be deterministic even when the full state is unresolved.

### 8.5 J2 — faithful-lift invariance

For a faithful surjective projection `pi:U->V`,

\[
J_U=\pi^*J_V,
\qquad
U/J_U\cong V/J_V.
\]

Scientifically invisible latent duplication therefore does not create new CREST state distinctions or change licensing.

### 8.6 J5 — one-sided contract comparison

Under the stated projection premises,

\[
\text{source stronger}
\Rightarrow
\pi^*J_V\preceq J_U,
\]

whereas

\[
\text{source weaker}
\Rightarrow
J_U\preceq\pi^*J_V.
\]

Thus contract-relativity has a controlled refinement order rather than arbitrary movement.

### 8.7 O1 — structural optimum and licensed optimum can differ

The finite obstruction proves

\[
\boxed{
R_{\rm structural}^*=1<R_{\rm licensed}^*=2.
}
\]

The cheapest repair restoring a valid carrier/state can leave the full state unresolved by evidence, while a more expensive repair is fully licensed. The requested target may remain reportable under the cheaper repair.

This refutes automatic collapse of feasibility, state adequacy, and evidential licensing into one optimization objective.

---

## 9. Three extremal mathematical objects

The synthesis becomes especially clear when the partial orders are separated.

### 9.1 Greatest coherent carrier

In subset order, J3/J6 seek the **largest set of worlds** on which the declared synchronization/action contract can coherently live:

\[
U^*\text{ or }K^*.
\]

This is an upper-envelope problem: retain as much of the candidate world space as possible while preserving viability/coherence.

### 9.2 Coarsest adequate state

On an admissible carrier, J1 seeks the **coarsest partition** satisfying all required distinctions:

\[
J.
\]

This is a compression problem: preserve as little information as possible while remaining adequate.

### 9.3 Smallest honest uncertainty set

Given one evidence record `e`, a convenient derived notation is

\[
\mathcal S(e)=\{[u]_J:u\text{ is compatible with }e\}.
\]

If `|S(e)|=1`, the state is identified. If it contains several blocks, any single-block report would discard an evidence-compatible possibility. Thus the compatible-block set is the sharp ambiguity-retaining state report.

The three objects answer different questions:

```text
largest coherent world set
        U* / K*
            ↓
least-information adequate state partition
            J
            ↓
smallest honest evidence-compatible state set
            S(e)
            ↓
target report, possibly deterministic even when |S(e)|>1
```

This is one of the strongest unifying mathematical pictures in the program.

---

## 10. Where mathematics ends and philosophy begins

The philosophical paper should not claim that closure operators, quotient minimization, viability kernels, set cover, or evidence factorization are new. Those are mathematical substrates.

The **mathematical results** establish conditional facts such as:

- a proposed merge must split under specified operational distinctions;
- a unique coarsest adequate partition exists under specified closure premises;
- a common carrier can fail to exist;
- a state can exist without being identifiable from evidence;
- faithful descriptive duplication cannot change the quotient;
- stronger/weaker contracts constrain refinement direction;
- structural repair and evidence-licensed repair can have different optima.

The **philosophical elevation** is the interpretation of these formal facts as an account of scientific state representation.

### 10.1 From quotient to scientific commitment

Mathematics:

\[
u\sim_J v.
\]

Philosophy:

> Calling `u` and `v` the same ecological state is a commitment that every distinction demanded by the declared scientific work may safely ignore their remaining differences.

Thus **sameness is a testable scientific commitment**, not merely a label.

### 10.2 From contract dependence to non-arbitrary perspectivism

Mathematics:

`J` changes when the declared future, inherited meaning, mechanism family, target, or evidence contract changes.

Philosophy:

> State adequacy is purpose/contract relative, but not arbitrary. Scientists choose the work demanded of the representation; once that contract is declared, the world/model can objectively refute proposed merges.

This is the formal bridge between purpose-sensitive representation and constraint.

### 10.3 From carrier no-go to limits on statehood

Mathematics:

`U*` or `K*` can be empty or coverage-incomplete.

Philosophy:

> Not every bundle of scientific demands admits one coherent state representation. Sometimes the problem is not that the state is too coarse; the scientific contract itself is jointly unsatisfiable on the declared world model.

This prevents “add more variables” from being treated as the universal cure.

### 10.4 From J1 to a positive account of ecological state

Mathematics:

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

Philosophy:

> For a coherent declared contract, an ecological state is the least-information equivalence class that preserves every distinction required for the scientific work assigned to it.

This is not one intrinsic partition of nature. It is a positive, constrained account of **scientific statehood**.

### 10.5 From evidence gate to ontology/epistemology separation

Mathematics:

\[
J\not\preceq E_D
\]

can occur even though `J` exists.

Philosophy:

> The state required by the scientific task and the state identified by current evidence are different questions.

Therefore

\[
\text{state existence}
\neq
\text{state identification}
\neq
\text{target reportability}.
\]

A state may be well-defined but unknown; a target may still be knowable without full-state identification.

### 10.6 From J2 to representation independence

Mathematics:

faithful latent duplication leaves the quotient unchanged up to isomorphism.

Philosophy:

> Ecological state is not simply the number or naming of latent variables in a chosen model. Scientifically invisible redescription should not create a new state distinction.

This is important if CREST is to be a theory of representational adequacy rather than a coding convention.

### 10.7 From J5 to disciplined contract relativity

Mathematics:

stronger obligations refine; weaker obligations coarsen, under the theorem premises.

Philosophy:

> Changing purpose does not license arbitrary state changes. When purposes can be ordered by their scientific burden, the corresponding state resolutions inherit an order.

### 10.8 From O1 to plural scientific objectives

Mathematics:

\[
R_{\rm structural}^*<R_{\rm licensed}^*.
\]

Philosophy:

> Structural feasibility, representational adequacy, and evidential warrant are distinct scientific virtues. One scalar “best model” or “cheapest repair” objective can conceal which obligation has actually been optimized.

This is a stronger philosophical use of O1 than merely saying that operations fail to commute.

---

## 11. Ecological significance of the full hierarchy

The synthesis is directly relevant whenever ecology uses state categories under changing systems, uncertain mechanisms, and incomplete monitoring.

Examples include:

- ecosystem regime/state classification under climate or community change;
- occupancy/persistence states under altered connectivity;
- pollination-maintained versus pollination-limited communities after pollinator turnover;
- restoration states after rewiring or intervention;
- invasion/pathogen states under newly available future interactions;
- management categories transported across sites, islands, watersheds, or time periods;
- monitoring designs that must decide which distinctions are worth measuring.

The mathematical hierarchy supports a corresponding ecological diagnostic:

```text
Can the relevant ecological configurations be made mutually coherent
under the declared actions/coverage?
        ↓
If yes, which distinctions must a valid state retain?
        ↓
Are those distinctions stable under future opening, structural transfer,
and retained mechanisms?
        ↓
Has the monitoring system actually resolved the required distinctions?
        ↓
If not, is the management target nevertheless still identifiable?
```

This converts “the model/state is inadequate” into typed diagnoses with different remedies.

---

## 12. What belongs to which paper

### CCOC owns

- cross-grammar future-sufficiency lower bound;
- constrained codebook robustness;
- fixed-regular one-action extremal family and sharpness;
- positive portability / forced-split boundary.

### MLTR owns

- source-to-target macro-law transport conditions;
- derived target labels;
- conservative target-only action transport;
- unique coarsest source-relative repair and transport defect;
- path coherence;
- minimum history augmentation.

### MRM owns

- response-type criterion for universal deterministic prediction;
- typed/set-valued reporting;
- candidate-safe lower bounds and minimal quotient;
- exact active discrimination and cost-aware variants;
- mechanism ambiguity frontiers;
- robust/probabilistic update and one-step VOI diagnostics.

### CED owns

- experiment-induced evidence quotient and honest report criterion;
- unique coarsest target-safe required resolution;
- failure-architecture guarantees;
- risk-limited target-oriented experiment/report design;
- supporting calibration/detection/error-control mathematics.

### CREST owns

- common-carrier existence/no-go synthesis (J3/J6);
- declared carrier-repair synthesis and complexity (J4/J7);
- unique coarsest four-audit joint state and evidence gate (J1);
- faithful-lift invariance and one-sided comparison (J2/J5);
- structural-versus-licensed repair obstruction (O1);
- the philosophical synthesis of ecological state equivalence as a contract-relative scientific commitment.

The companion theorems should not be re-proved inside the CREST philosophy paper. CREST should use them as formal anchors for the higher-level state argument.

---

## 13. What is mathematical substrate rather than program novelty

The program must continue to firewall established substrate from the ecology-specific contribution.

Do not claim novelty for generic:

- Myhill–Nerode-style distinguishability and fixed-grammar minimization;
- partition lattices, refinement, closure operators, and fixed points;
- bisimulation/state aggregation as a generic idea;
- viability/invariant kernels and finite safety games;
- memoryless safety policies;
- weighted set cover and exponential subset search;
- Bayesian updating, entropy, information gain, or standard calibration bounds;
- target factorization/reportability in isolation;
- model transferability or purpose-sensitive representation in general.

The candidate contribution is the **specific ecology-facing contract architecture, quantitative extremal families, source-relative semantics, mechanism-safe reporting, evidence licensing, and their cross-contract synthesis**.

---

## 14. Current theorem boundary

The present exact theory is finite. It does not yet prove:

- a nature-given canonical carrier or scientific contract;
- one state across all contracts;
- empirical truth of a declared latent-world model;
- exhaustive repair languages;
- arbitrary-redescription invariance outside faithful projections;
- a total order over arbitrary scientific purposes;
- stochastic/continuous/infinite-state/approximate generalizations of the entire CREST stack;
- philosophical exhaustiveness of the four audit axes.

These are future research boundaries, not current submission-blocking proof gaps.

Across finite problem families, however, state complexity can be unbounded as problem size grows: CCOC and MRM both contain canonical families whose required state cardinality grows as `2^(m+1)` while the corresponding memory surcharge grows linearly in `m`.

---

## 15. Final synthesis

The entire program can be compressed to one hierarchy:

```text
latent ecological worlds
        +
declared scientific contract
        ↓
Which worlds can coherently be considered together?
        -> J3/J6 carrier existence / no-go
        ↓
Which differences must not be ignored?
        -> CCOC / MLTR / MRM / CED obligations
        ↓
What is the least-information state satisfying all of them?
        -> J1 joint state J
        ↓
Is that state invariant to scientifically invisible redescription?
        -> J2 / J5
        ↓
Did the evidence actually identify the required block?
        -> J1/CED evidence gate
        ↓
If not, what is the sharp ambiguity set and is the target still reportable?
        ↓
If the contract itself fails, what repair is possible and at what cost?
        -> J4/J7/O1
```

The corresponding philosophical thesis is:

> **An ecological state is not simply a present description or an intrinsic label of nature. It is a scientifically constrained permission to ignore differences among configurations. For a declared coherent contract, CREST identifies the least-information equivalence class that can carry the assigned scientific work; when no such carrier exists it explains why, and when the state exists but evidence does not identify it, the theory preserves exactly the remaining uncertainty rather than inventing resolution.**
