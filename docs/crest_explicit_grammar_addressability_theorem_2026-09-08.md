# CREST explicit grammar theorem: interface requirements determine interaction order

## Status

Finite exact theorem derived from an explicit grammar, trace semantics, and induced quotients. This replaces direct coalition-value assignment as the mathematical support for higher-order temporal interaction.

## 1. Primitive carrier

Let

\[
\Omega_m=P_H\times P_\Theta\times\{0,1\}^m,
\]

where `P_H` contains two MLTR replacement-history primitives with distinct complete carried maps and `P_Theta` contains two MRM primitive candidate laws with distinct complete response tables. Thus the history and mechanism interfaces are derived from companion primitives rather than inserted as anonymous bits.

Let the final coordinate be an exterior signature

\[
a=(a_1,\ldots,a_m).
\]

All worlds have one visible cut value before responsibilities are declared.

## 2. Compositional grammar

Each responsibility contributes primitive grammar resources:

- `H` makes the carried-map interface observable;
- `Theta` makes the response-table interface observable;
- `F` contributes exterior decoder primitives.

Fix a decoder prerequisite set

\[
R\subseteq\{H,\Theta\}.
\]

An exterior word `decode_i` is well typed in coalition `S` exactly when

\[
F\in S
\quad\text{and}\quad
R\subseteq S.
\]

The grammar is generated from these typing rules. No coalition is assigned a bit cost directly.

The trace of a world under a legal word is its carried map, response table, or requested exterior bit. Two worlds are state equivalent under coalition `S` iff all legal traces agree.

## 3. Lemma — generated-word criterion

For every coalition

\[
S\subseteq\{H,\Theta,F\},
\]

an exterior decoder exists in the generated grammar iff

\[
F\in S\ \text{and}\ R\subseteq S.
\]

### Proof

`F` is the only responsibility that supplies a decoder primitive. The typed decoder consumes every interface in `R`. Hence absence of `F` or of any required interface makes the composite word ill typed. Conversely, when `F` and all interfaces in `R` are present, the grammar generator produces `decode_i` for each `i=1,...,m`. QED.

## 4. Lemma — quotient cardinality

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

Then the exact trace quotient has

\[
\boxed{
|Q_S|=2^{\delta_H(S)+\delta_\Theta(S)+m\delta_R(S)}.
}
\]

Therefore

\[
\boxed{
v_R(S)=\log_2|Q_S|
=\delta_H(S)+\delta_\Theta(S)+m\delta_R(S).
}
\]

### Proof

The two carried maps are distinct, so an `H` word separates exactly two history classes. The two response tables are distinct, so a `Theta` word separates exactly two mechanism classes. When decoder words are absent, changing `a` leaves every legal trace unchanged. When they are present, the `m` decoder words recover the complete binary signature and therefore separate all `2^m` exterior values. The carrier is a direct product and the three trace components are independent, so the class counts multiply. QED.

The key point is that this value formula is now a theorem about an explicit trace quotient. It is not the definition used by the implementation.

## 5. Characterization theorem — decoder prerequisites determine interaction order

The exterior contribution is the unanimity game

\[
u_{R\cup\{F\}}(S)=m\,\mathbf 1_{R\cup\{F\}\subseteq S}.
\]

Its Möbius transform has exactly one nonzero dividend: `m` bits on coalition

\[
R\cup\{F\}.
\]

Hence:

1. if `R = empty`, exterior information is an `F` main effect of `m` bits;
2. if `R = {H}`, exterior information is a pure `H x F` pairwise dividend of `m` bits;
3. if `R = {Theta}`, exterior information is a pure `Theta x F` pairwise dividend of `m` bits;
4. if
   \[
   \boxed{R=\{H,\Theta\}},
   \]
   exterior information is a pure genuine three-way dividend
   \[
   \boxed{m(H,\Theta,F)=m}.
   \]

Thus pure three-way interaction is not an arbitrary consequence of naming three responsibilities. It occurs exactly in this family when the future decoder is **interface complete with respect to both companion interfaces**.

## 6. Falsifiability and boundary

This theorem explicitly answers the objection that one could instead let `F` decode the exterior coordinate alone. One can: changing the decoder rule to `R=empty` moves all `m` bits into the `F` main effect and the three-way dividend becomes zero. Requiring only one interface moves the same information into the corresponding pairwise interaction.

Therefore CREST does **not** claim that all future grammars force pure three-way interaction. The claim is conditional and structural:

> the interaction order of addressability debt is determined by the minimal interface prerequisite set of the decoder.

The remaining scientific question for an application is whether its legal response grammar genuinely has a two-interface completeness requirement. That cannot be inferred from the accounting theorem alone.

## 7. Implementation

- `crest/explicit_temporal_grammar.py` — companion primitives, grammar generation, traces, quotients, and Möbius calculation;
- `tests/test_explicit_temporal_grammar.py` — all eight coalition quotients plus counterfactual decoder-rule tests.

The tests intentionally include alternative grammars that destroy the three-way term. This makes the result refutable rather than self-confirming.
