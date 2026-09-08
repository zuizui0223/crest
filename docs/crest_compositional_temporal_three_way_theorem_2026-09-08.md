# CREST compositional temporal bridge — pure MLTR × MRM × CCOC three-way interaction

## Status

Exact finite **conditional-contract** bridge theorem.

This theorem repairs the remaining gap left by the strict fixed-closure no-go. It does not try to force one fixed future audit to behave differently after seeing the state partition. Instead it uses CCOC's native cross-grammar quantifier: separate closed component contracts are compared with one **jointly open composition contract** whose legal future grammar contains cross-interface queries unavailable when one component interface is absent.

The result gives a literal finite MLTR × MRM × CCOC construction with a genuine positive three-way Möbius dividend that is exactly `m` bits and therefore unbounded.

---

## 1. Three primitive ingredients

### 1.1 MLTR history interface

Use any exact two-mode MLTR history witness. The canonical path-incoherent diamond already supplies two distinct complete carried terminal maps, for example

\[
c_{p_0}=(0,1),
\qquad
c_{p_1}=(1,0).
\]

Hence the minimum history mode has two classes. Write the retained history-interface label as

\[
h\in\{0,1\}.
\]

Its cost is exactly one bit.

The raw replacement history remains immutable after the cut. Nothing below changes which path occurred.

### 1.2 MRM mechanism interface

Use the `m=1` MRM binary-signature frontier. There are two retained response types

\[
\theta\in\{0,1\},
\]

separated by one declared mechanism probe. The candidate-safe mechanism interface therefore carries one response-type bit.

The primitive candidate law remains fixed within each world. Nothing below defines the mechanism from the final CREST state.

### 1.3 CCOC open-composition exterior coordinate

Let

\[
a=(a_1,\ldots,a_m)\in\{0,1\}^m
\]

be an exterior/addressability coordinate in a finite CCOC open-composition family.

The inside interface is the already-required pair

\[
I=(h,\theta)\in\{0,1\}^2.
\]

Separate component contracts do **not** contain a legal cross-interface decoder for `a`. The jointly open contract, in which both the history and mechanism interfaces are present and the future-composition responsibility is declared, adds legal future words that decode every `a_i` while preserving the two inside labels.

This is the usual CCOC quantifier structure:

\[
\text{closed component interfaces}
\quad\longrightarrow\quad
\text{jointly open response interface}.
\]

The grammar difference is declared exogenously by the coalition contract. It is not inferred from the quotient produced afterward.

---

## 2. One common finite carrier

Take

\[
\Omega_m
=
\{0,1\}_h
\times
\{0,1\}_\theta
\times
\{0,1\}^m_a.
\]

All worlds have the same visible present-cut observation, so the baseline has one class.

The carrier contains

\[
|\Omega_m|=2^{m+2}
\]

possible worlds.

Interpret the coordinates as:

- `h`: the MLTR history-mode label already justified by carried-map incoherence;
- `theta`: the MRM response-type label already justified by candidate disagreement;
- `a`: CCOC exterior information that becomes addressable only in the jointly open future grammar.

The three coordinates are primitive before the final state quotient. Their scientific relevance changes by declared contract, but their raw values are not defined by that quotient.

---

## 3. Coalition contracts

For a coalition

\[
S\subseteq\{H,\Theta,F\},
\]

define the least exact state required by that declared contract as follows.

- If `H in S`, preserve the binary history label `h`.
- If `Theta in S`, preserve the binary mechanism response-type label `theta`.
- The exterior coordinate `a` is required **only** in the jointly open contract
  \[
  S=\{H,\Theta,F\},
  \]
  because only that contract declares the CCOC cross-interface future words that decode `a`.
- `F` without both component interfaces contains no decoder for `a` and contributes no standalone state bit in this witness family.

Therefore the exact coalition value in bits is

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

Because there are exactly three axes, the last indicator is nonzero only for the full coalition.

This is a **conditional-contract set function**. It should not be confused with the earlier fixed-closure coalition game where every audit and legal action set is held constant while only audit inclusion changes.

---

## 4. Theorem — pure genuine three-way interaction

### Statement

For every integer `m >= 1`, the construction above has coalition debts

\[
\begin{aligned}
v(H)&=1,\\
v(\Theta)&=1,\\
v(F)&=0,\\
v(H\Theta)&=2,\\
v(HF)&=1,\\
v(\Theta F)&=1,\\
v(H\Theta F)&=m+2.
\end{aligned}
\]

All pairwise Möbius dividends are zero:

\[
\boxed{
m(H,\Theta)=m(H,F)=m(\Theta,F)=0.}
\]

The genuine three-way dividend is

\[
\boxed{
m(H,\Theta,F)=m.}
\]

Hence the three-way temporal interaction is unbounded as `m -> infinity`.

### Proof

The singleton and pair values follow directly from which component labels are required. With both history and mechanism but no jointly open future grammar, the state is `(h,theta)` and has four classes, i.e. two bits. Adding `F` to only one component does not legalize a cross-interface decoder, so no additional coordinate becomes required.

In the full coalition, the jointly open CCOC grammar decodes all `m` exterior bits in addition to the two component-interface bits. Therefore the exact state is `(h,theta,a)` with

\[
2^{m+2}
\]

classes and `m+2` bits.

The pairwise dividends are

\[
m(H,\Theta)=2-1-1=0,
\]

\[
m(H,F)=1-1-0=0,
\]

and

\[
m(\Theta,F)=1-1-0=0.
\]

The three-way Möbius term is

\[
\begin{aligned}
m(H,\Theta,F)
={}&(m+2)-2-1-1+1+1+0\\
={}&m.
\end{aligned}
\]

This proves the claim. `square`

---

## 5. Interaction debt and asymptotics

The standalone sum is

\[
D_H+D_\Theta+D_F=2\text{ bits},
\]

while the joint debt is

\[
D_{H\Theta F}=m+2.
\]

Therefore

\[
\boxed{\Delta=m.}
\]

All of that non-additive debt is genuine three-way interaction; there are no pairwise interaction terms in this family.

The three-way share of the full joint state is

\[
\boxed{
\frac{m}{m+2}
\longrightarrow1.
}
\]

Thus a **literal companion-derived three-way interaction** can asymptotically dominate the state information even when the MLTR and MRM component interfaces remain one bit each.

---

## 6. Numerical endpoint

At `m=10`:

- visible present: **1 class**;
- history alone: **2 classes / 1 bit**;
- mechanism alone: **2 classes / 1 bit**;
- history + mechanism: **4 classes / 2 bits**;
- either pair with future but without the other component: unchanged;
- full history + mechanism + jointly open future: **4096 classes / 12 bits**;
- interaction debt: **10 bits**;
- genuine three-way dividend: **10 bits**;
- pairwise dividends: **0 bits**;
- three-way share of the full state: **83.33%**;
- three-way share of interaction debt: **100%**.

Relative to the history+mechanism state before joint future opening, the required class count jumps

\[
4\longrightarrow4096,
\]

an exact

\[
\boxed{1024\times}
\]

state-count amplification.

At `m=18`, the genuine three-way share reaches

\[
18/20=90\%.
\]

---

## 7. Why this does not violate the definition firewalls

### MLTR

The raw replacement path and its history-mode class are fixed before the cut. Future actions never rewrite that past. The joint state merely preserves the already-required binary history interface.

### MRM

The candidate mechanism and its response type are fixed before the CREST quotient. The joint state preserves the already-required binary response-type interface.

### CCOC

CCOC is not used to define which mechanism is true. It receives the already-declared component interfaces as the inside part of a larger open-composition problem and proves that a jointly legal future grammar can force retention of additional exterior/addressability information.

The future grammar is declared by contract. The rule

> cross-interface decoders are legal only in the jointly open H + Theta + F contract

is a premise of the cross-grammar family, not a rule inferred after seeing which state partition happens to arise.

Thus the dependency order remains acyclic:

\[
\text{MLTR history primitive},\ \text{MRM mechanism primitive},\ \text{CCOC grammar family}
\longrightarrow
\text{coalition contract}
\longrightarrow
\text{required state}.
\]

---

## 8. Relation to the older abstract closure extremum

The older fixed-closure family proves

\[
m(H,\Theta,F)=b-\log_2 3
\]

and can make the three-way share approach one. Its exact arithmetic remains valid, but the specific history-crossing activation is not a strict literal MLTR history model.

The present theorem supplies the missing positive literal bridge in a different way:

- it respects immutable history;
- it respects primitive MRM candidate laws;
- it respects CCOC's law/grammar quantifier by using a declared jointly open composition contract;
- and it obtains a pure unbounded three-way dividend
  \[
  m(H,\Theta,F)=m.
  \]

The price is conceptual precision: this is a **conditional cross-contract coalition game**, not the same fixed-audit game used for the older closure extremum.

Both are valid CREST results, but they answer different mathematical questions and should remain explicitly separated in the manuscript.
