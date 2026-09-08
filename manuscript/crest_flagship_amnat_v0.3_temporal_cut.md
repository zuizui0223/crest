# What Must Survive the Present?
## Ecological State at a Temporal Cut and Interaction Across History, Latent Response, and Future

**Target:** *The American Naturalist* — Major Article

## Abstract

Ecological state is usually described as if it were a property of a system at one moment. We instead treat the present as an observational **temporal cut** through a set of possible ecological worlds. At time \(t\), an observation map \(O_t:\Omega\to Y_t\) induces a baseline partition \(B_t=\ker O_t\): worlds in one block are indistinguishable at the cut. A scientifically adequate state may nevertheless need to retain distinctions lying to the left of that cut in ecological history, within the cut as latent contemporaneous response structure, or to the right of the cut in counterfactual future response. On a declared finite common carrier, we represent those responsibilities by refinement closures \(C_H,C_\Theta,C_F\) and define the state as their least-information common fixed point above \(B_t\). The resulting information need is not generally separable across temporal positions. We prove a finite family with one visible present class in which history alone costs one bit, future alone costs zero, but the history–future joint state has \(\log_2 n\) bits, yielding unbounded interaction \(\log_2 n-1\). We then prove a stronger three-way family in which history alone costs one bit, latent-present and future responsibilities each cost zero alone, yet the joint state has \(b\) bits and the genuine history × latent-present × future Möbius dividend is \(b-\log_2 3\), asymptotically approaching the entire state burden. At \(b=10\), one visible cut class supports 1024 required state classes; 9 of 10 bits are interaction-generated and 8.415 bits (84.15% of the state) are genuine three-way interaction. Thus ecological state cannot in general be reconstructed by independently compressing past, hidden contemporaneous structure, and future. It is the least information that must survive the present cut for a declared scientific responsibility.

**Keywords:** ecological state; temporal representation; coarse graining; history dependence; latent mechanism; counterfactual future; state complexity; non-additivity

## 1. The present as a cut, not a state

Ecology often speaks as if the state of a system were whatever is measured at one moment: biomass, occupancy, composition, colour class, functional guild, or regime label. Such variables can be useful, but usefulness does not make a present observation identical to ecological state. Two worlds that look the same now may have arrived there through different histories, may contain different latent response structures, or may diverge when a future interaction or intervention becomes relevant.

CREST begins from this mismatch. Let \(\Omega\) be a declared finite set of possible ecological worlds. At a time \(t\), science accesses those worlds through an observation map

\[
O_t:\Omega\to Y_t.
\]

The **present observational partition** is

\[
\boxed{B_t=\ker O_t.}
\]

Two worlds lie in the same block of \(B_t\) exactly when they are indistinguishable at the present cut under the declared observation. We do not introduce a finite-width present interval. In the current exact finite theory, the present is only the cut and the equivalence relation it induces.

For a visible value \(y\in Y_t\), the fiber

\[
L_t(y)=O_t^{-1}(y)
\]

contains all latent worlds compatible with that same visible present. The fiber is not another time interval. It is the set of hidden contemporaneous possibilities behind one observed cut value.

This gives a precise way to state the philosophical claim that motivates CREST:

> **An ecological state is not the present observation itself. It is the least information about possible worlds that must survive the present cut for the declared scientific responsibility.**

The phrase “survive the cut” is representational, not causal. CREST does not claim backward causation. A past distinction or counterfactual future can change what the present state representation must retain without changing the physical present because an observer changed vocabulary.

## 2. Three temporal-position responsibilities

The current programme develops three structurally distinct ways in which worlds inside one present fiber can cease to be scientifically interchangeable.

### 2.1 History: information to the left of the cut

Let \(H_{<t}\) denote the retrospective information that a scientific contract may require to remain operationally coherent. Structural replacement, turnover, restoration sequence, or other history can matter when two worlds that look the same at the cut carry different inherited meanings or support different downstream decisions.

In the companion programme MLTR, this is the source-relative and route-relative problem: a classification carried from an earlier system may cease to have one coherent meaning after replacement, and different replacement histories may require distinct history modes.

Within CREST, the resulting requirement is represented abstractly by a refinement closure

\[
C_H.
\]

### 2.2 Latent present: information transverse to the cut

Two worlds can share the same observation \(O_t(\omega)\) while differing in response-relevant contemporaneous structure. Write that hidden structure schematically as \(\Theta_t\). It lives inside the fiber \(L_t(y)\), not to the left or right of the cut.

This is the natural CREST position of MRM. MRM does not require preservation of complete mechanism identity. It requires only those latent distinctions that can change a declared response or report.

CREST represents this responsibility by

\[
C_\Theta.
\]

### 2.3 Future: information to the right of the cut

A distinction currently erased can become necessary when new interactions, interventions, connections, or response tests become part of the future responsibility. This is not the realized future; it is the declared counterfactual response structure the state must support.

CCOC supplies the future-sufficiency programme. Its role in CREST is represented by

\[
C_F.
\]

These three axes are not claimed to exhaust every legitimate ecological state responsibility. They are the three temporal-position responsibilities developed here: retrospective history, latent contemporaneous response structure, and prospective response.

## 3. State as the least common refinement at the cut

On a declared finite common carrier, let \(C_H,C_\Theta,C_F\) be monotone, inflationary, idempotent refinement closures acting above \(B_t\). The CREST state partition is

\[
\boxed{
J_t=(C_H\vee C_\Theta\vee C_F)(B_t),
}
\]

where the join denotes the least common fixed point reached by fair finite refinement. The general fixed-point substrate is classical. Its role here is to recover the state concept mathematically: preserve every distinction required by the declared responsibilities, discard every distinction none of them requires.

For any coalition \(S\subseteq\{H,\Theta,F\}\), let \(J_S\) be the least common fixed point of the closures in \(S\) above the same baseline. Define the coalition state debt

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

The generic non-additive debt is

\[
\boxed{
\Delta=D_{H\Theta F}-(D_H+D_\Theta+D_F).
}
\]

A nonzero \(\Delta\) means that independently measuring the burden of each temporal-position responsibility does not reconstruct the burden of satisfying them together.

To identify where this non-additivity resides, we use the exact Möbius/Harsanyi decomposition of the finite coalition game. Pairwise terms include

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

This accounting is standard. The substantive theorem is that these terms can become arbitrarily large in finite state construction at one present cut.

## 4. Theorem 1: past–future interaction is unbounded

### Statement

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
\boxed{
m(H,F)=\log_2 n-1,
}
\]

which is unbounded as \(n\to\infty\).

### Construction

Take \(n\) latent worlds with an indiscrete present-cut partition. The history closure marks one world, producing exactly two classes. The future closure is a directed cycle. Acting on the untouched present partition, the future closure costs zero because all successors remain inside one block. Once the historical mark is retained, successor stability propagates that distinction around the cycle until every world is distinct.

Thus history alone asks for one bit, future alone asks for no additional bit, yet their conjunction requires \(\log_2 n\) bits.

### Meaning

The theorem formalizes a simple but strong point:

\[
\boxed{
\text{how much of the past must survive the present depends on what future the state must support.}
}
\]

The two sides of the temporal cut cannot in general be compressed independently. This is interaction or coupling, not statistical confounding. No probability distribution, common-cause graph, or regression bias is involved.

### Numerical endpoint

At \(n=1024\), every latent world still has the same visible present. History alone requires two state classes and one bit. Future alone requires one class and zero additional bits. Together they require

\[
1024\text{ classes}=10\text{ bits}.
\]

So the past–future interaction contributes

\[
9\text{ bits},
\]

or **90% of the joint state information**.

The state-count error is equally stark: independent accounting sees at most two classes; the joint state needs 1024. The class-count underestimate is therefore

\[
\boxed{512\times.}
\]

## 5. Theorem 2: genuine history × latent-present × future interaction is unbounded

The previous theorem can still be read as a two-axis amplification. A stronger question is whether a state can be dominated by information that belongs to no temporal position alone and not even to any pair.

### Statement

For every integer \(b\ge2\), there is a finite CREST contract with one visible present class satisfying

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

and the joint partition has exactly

\[
|J_{H\Theta F}|=2^b
\]

classes.

The nontrivial lower-order coalition debt is

\[
v(H\Theta)=\log_2 3,
\]

while

\[
v(HF)=1,
\qquad
v(\Theta F)=0.
\]

Hence

\[
\boxed{m(H,\Theta)=\log_2(3/2)}
\]

and

\[
\boxed{m(H,\Theta,F)=b-\log_2 3.}
\]

Therefore

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

The genuine three-way temporal interaction can asymptotically account for the entire required state information.

### Construction

Use \(2^b+1\) latent worlds, all in one visible present-cut block.

1. **History** marks one world and produces a two-class partition.
2. **Latent present** contains a response edge from a second world into the historical seed. It is inert on the untouched cut, but after the historical distinction exists it creates a third class.
3. **Future** contains a chain of \(2^b-3\) worlds. It is inert until the latent-present split exists. Once activated, successor consistency propagates the distinction down the chain.
4. Two residual worlds remain merged, so the final partition contains exactly \(2^b\) classes.

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

No asymptotic approximation is used to obtain the interaction formula; the asymptotic statement follows from these exact finite counts.

## 6. A numerical state at one cut

Set \(b=10\). There is still only **one visible present class**, but the full adequate state requires

\[
2^{10}=1024
\]

classes and exactly 10 bits.

The decomposition is

| source of required state information | bits | share of joint debt |
|---|---:|---:|
| direct history | 1.0000000000 | 10.00% |
| history × latent present | 0.5849625007 | 5.85% |
| history × future | 0 | 0% |
| latent present × future | 0 | 0% |
| **history × latent present × future** | **8.4150374993** | **84.15%** |
| **joint** | **10.0000000000** | **100%** |

The total interaction debt is 9 bits, so 90% of the state is interaction-generated. Of those nine interaction bits, 93.50% belong to the genuine three-way term.

This example supplies the paper's central numerical endpoint. A single visible present does not imply a single scientifically adequate state. More importantly, most of the required state information need not be attributable to history, latent mechanism, or future separately. It can be created by their coupling.

## 7. Why latent present is not simply “the present”

The temporal cut deliberately prevents a symmetry problem in the conceptual framing. History and future are temporal directions relative to \(t\). Latent mechanism is not a third time direction. It is a dimension inside the fiber of the present observation.

Schematically,

```text
                         latent response structure Θ_t
                                  │
                                  │
                                  │
history H_<t  ─────────────────── O_t ───────────────────  future F_>t
                                  cut
```

The visible present is the cut itself. The latent present is transverse to that cut: two worlds can occupy the same visible point while differing in response-relevant structure.

This separation matters. If we called mechanism “the present” without qualification, the three axes would mix a temporal direction with an observational surface. If instead we treated present as a finite-width interval, the theory would inherit arbitrary choices about interval width. The cut-and-fiber formulation avoids both problems in the finite theory.

A continuous-time extension could replace the left and right sides by temporal germs and the latent fiber by a set of local generators or response kernels compatible with the same observation. CREST does not claim that theorem here.

## 8. Relation to CCOC, MLTR, and MRM

The three companion programmes remain distinct publication units.

**MLTR — history / inherited semantics.** MLTR asks when an accepted state meaning can be carried through structural replacement, when routes remain coherent, and how much historical context is minimally necessary when they do not. CREST consumes that result only as a history responsibility at the cut.

**MRM — latent contemporaneous response structure.** MRM asks when retained mechanisms that agree visibly may safely remain unresolved and when response-relevant mechanism information or active probes are required. CREST locates that ambiguity in the fiber behind the visible cut.

**CCOC — future response responsibility.** CCOC asks how a wider future grammar can expose distinctions hidden under a restricted grammar. CREST places that responsibility to the right of the cut.

The CREST contribution is not to re-prove the strongest companion theorems. It is to ask what state remains when these obligations act on one common present description and to quantify the information created by their interaction.

This gives a hierarchy:

\[
\text{companion obstruction theories}
\longrightarrow
\text{state at a common temporal cut}
\longrightarrow
\text{interaction debt and interaction anatomy}.
\]

## 9. General joint state debt

The temporal-position theorem is a structured instance of the more general CREST joint-debt result. For arbitrary responsibility closures \(C_1,\dots,C_k\) above a common baseline \(B\), define

\[
D_i=\log_2|C_i(B)|-\log_2|B|,
\]

\[
D_{\rm joint}=\log_2|J|-\log_2|B|,
\]

and

\[
\boxed{\Delta=D_{\rm joint}-\sum_iD_i.}
\]

A marked-cycle family gives

\[
D_1=1,\qquad D_2=0,\qquad D_{\rm joint}=\log_2 n,
\]

so \(\Delta=\log_2 n-1\) is unbounded. Conversely, if every standalone debt is zero, then every closure already fixes the baseline, and the joint debt is also zero.

The temporal-cut theorem sharpens the interpretation of this generic accounting. The non-additivity need not be an abstract interaction among unnamed audits. It can arise specifically because distinctions arriving from before the cut, inside its hidden fiber, and after the cut activate one another.

## 10. Evidence is downstream of required state

The current paper concerns required state information. It does not equate state with what is currently measurable.

Once \(J_t\) has been constructed, an evidence partition \(E\) licenses a deterministic full-state report only if it resolves every required state distinction. A narrower target may remain reportable even when the full state is unresolved. CREST therefore keeps three questions separate:

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

CED is the downstream companion responsible for evidence licensing and monitoring design. It is not a fourth temporal-position axis in the theorem above.

## 11. What the theorem does and does not say

The result is finite, exact, and conditional on a declared common carrier and responsibility closures.

It **does** establish that:

- the present can be treated mathematically as an observational cut rather than as the state itself;
- history, latent contemporaneous response structure, and future response can be represented as distinct responsibilities acting on the cut partition;
- past–future interaction can be unbounded;
- genuine history × latent-present × future interaction can be unbounded;
- the genuine three-way share can approach 100% of the joint state debt;
- the finite \(b=10\) witness requires 1024 state classes and assigns 8.415 bits of 10 to genuine three-way interaction.

It **does not** establish that:

- these three axes exhaust every legitimate ecological notion of state;
- every ecological system has one unique natural decomposition into history, latent present, and future;
- latent response structure is identifiable from the present observation;
- interaction here is statistical confounding;
- ecological time is fundamentally discrete;
- an infinitesimal, continuous-time, stochastic, infinite-state, or approximate analogue follows automatically;
- the activation order must follow chronological order.

The phrase “state at a temporal cut” is therefore a finite representational theorem, not a claim about the metaphysics of physical instants.

## 12. Novelty boundary

CREST does not claim novelty for closure operators, partition lattices, bisimulation-style refinement, automata minimization, marked cycles, Shapley values, Möbius inversion, Harsanyi dividends, or logarithmic class-count accounting. Those are mathematical substrate.

Nor is the broad statement that ecological history, mechanisms, or future conditions can matter for prediction new by itself.

The CREST-level contribution is their conjunction in one state-construction problem: a present observation defines a cut through possible worlds; distinct temporal-position responsibilities refine that cut; and the information they create jointly can be arbitrarily larger than the information they require separately. The stronger three-way theorem shows that the resulting state can be asymptotically dominated by interaction information that belongs to no axis alone.

## 13. Conclusion

The present need not be a state. In CREST it is a cut.

At that cut, ecological worlds can agree visibly while differing in what came before, what latent response structure exists behind the observation, and what future responses the scientific contract asks the state to support. The adequate state is the least-information quotient that preserves the distinctions those responsibilities jointly require.

The quantitative consequence is stronger than ordinary history dependence or future sensitivity. The temporal directions can interact. For history and future alone,

\[
\boxed{m(H,F)=\log_2 n-1}
\]

is unbounded. With latent contemporaneous response structure included,

\[
\boxed{m(H,\Theta,F)=b-\log_2 3}
\]

is also unbounded and can asymptotically account for the entire state burden.

At the concrete \(b=10\) endpoint, one visible present class expands to 1024 adequate-state classes. The joint state contains 10 bits; 9 are interaction-generated, and 8.415 bits—84.15% of the entire state—are genuine history × latent-present × future interaction.

The resulting state concept is therefore not “the variables measured now.” It is

\[
\boxed{
\text{the least information that must survive the temporal cut.}
}

And that information cannot, in general, be recovered by compressing past, latent present, and future independently.
