# CREST counterfactual response-capacity bound — 2026-09-06

> **Status:** candidate canonical strengthening of the capability–resolution result. The finite counting and distinguishing-test substrate is classical finite-state reasoning; the CREST contribution is the matched interpretation: carrier-size gain does not bound representational burden, whereas counterfactual response capacity does.

## 1. Why this result is needed

The existing connected CREST family proves that one newly admitted controllable action can give

\[
\Delta |K^*|=1
\qquad\text{and}\qquad
\Delta K_{U_0}=m
\]

for arbitrary \(m\). That theorem is a sharp no-bound result against **carrier-size gain** as the explanatory variable.

But the construction repeatedly reuses `probe` to expose successive latent bits. Therefore the arbitrary \(m\)-bit burden is not created from nothing. The missing question is:

> **What finite resource does upper-bound the number of ecological distinctions that a declared counterfactual repertoire can expose?**

The answer is the response capacity of the admitted future tests.

The resulting pair of conclusions is:

\[
\boxed{
\text{capability gain does not bound state burden,}
}
\]

but

\[
\boxed{
\text{counterfactual response capacity does.}
}
\]

This changes the explanatory target of the paper. The number of new management options is not by itself the relevant complexity parameter. What matters is how many distinguishable response records the admitted future grammar can extract from currently merged worlds.

---

## 2. Finite partial deterministic response system

Let

\[
\mathcal M=(S,A,\delta,z)
\]

be a finite partial deterministic response system.

- \(S\) is the finite world set;
- \(A\) is the action alphabet, \(|A|=a\);
- \(\delta:S\times A\rightharpoonup S\) is a partial deterministic transition map;
- \(z:S\to Z\) is the retained static/base response label, with \(|Z|=q\).

If a baseline partition must also be preserved, absorb it into the response label by replacing \(z(s)\) with the pair

\[
(B(s),z(s)).
\]

Thus \(q\) means the number of distinct labels that must be retained before future-response refinement.

For a word

\[
w=a_1\cdots a_d\in A^*,
\]

define the terminal response

\[
R_s(w)=
\begin{cases}
z(\delta_w(s)),&\text{if every transition in }w\text{ is legal from }s,\\
\bot,&\text{otherwise.}
\end{cases}
\]

The illegal symbol \(\bot\) is distinct from every element of \(Z\).

For horizon \(H\), let

\[
W_H(A)=\{w\in A^*:|w|\le H\}.
\]

Two worlds are \(H\)-response equivalent when

\[
s\equiv_H t
\iff
R_s(w)=R_t(w)
\quad\forall w\in W_H(A).
\]

Because every intermediate prefix is itself a word in \(W_H(A)\), the terminal-response vector contains the complete finite output/legal-response tree through depth \(H\).

Let \(J_H\) be the induced partition and

\[
K_H=\log_2|J_H|.
\]

---

## 3. Finite-horizon response-volume upper bound

The number of action words through horizon \(H\) is

\[
N_H(a)=\sum_{d=0}^{H}a^d.
\]

Each word can return at most one of \(q\) retained labels or \(\bot\). Therefore each state has a response signature in

\[
(Z\cup\{\bot\})^{N_H(a)}.
\]

Hence:

## Theorem 1 — finite response-volume bound

For every finite partial deterministic response system,

\[
\boxed{
|J_H|
\le
(q+1)^{N_H(a)}
}
\]

and therefore

\[
\boxed{
K_H
\le
N_H(a)\log_2(q+1).
}
\]

### Proof

Map each world \(s\) to its complete finite response vector

\[
\sigma_H(s)
=
\bigl(R_s(w)\bigr)_{w\in W_H(A)}.
\]

Two worlds are in the same \(J_H\)-block exactly when their response vectors agree. Thus the number of blocks is the size of the image of \(\sigma_H\), which cannot exceed the cardinality of its codomain:

\[
|\operatorname{im}\sigma_H|
\le
(q+1)^{|W_H(A)|}.
\]

Taking \(\log_2\) gives the bit bound. \(\square\)

### Interpretation

Arbitrarily many finite state distinctions cannot be created while simultaneously holding fixed:

1. the response alphabet;
2. the admitted counterfactual word set;
3. the test horizon.

At least one source of response capacity must grow.

This is a generic finite-state counting fact, not a CREST novelty claim by itself.

---

## 4. Relative bound for an action expansion

The CREST use case is relative rather than absolute.

Let

\[
A^-\subseteq A^+
\]

with old action dynamics and labels preserved, and let the retained present slice be common to the two contracts.

Let

\[
W_H^-=W_H(A^-),
\qquad
W_H^+=W_H(A^+).
\]

Within an old \(H\)-response state, all coordinates indexed by \(W_H^-\) are already fixed. Only newly admitted words can split that old state.

Define

\[
M_H
=
|W_H^+\setminus W_H^-|.
\]

For full free-word grammars with

\[
|A^-|=a,
\qquad
|A^+|=a+k,
\]

this is

\[
M_H
=
\sum_{d=1}^{H}
\left[(a+k)^d-a^d\right].
\]

## Theorem 2 — relative action-expansion bound

Every old \(H\)-response class can split into at most

\[
(q+1)^{M_H}
\]

new classes. Consequently, on any retained slice on which old response semantics are preserved,

\[
\boxed{
|J_H^+|
\le
|J_H^-|(q+1)^{M_H}
}
\]

and

\[
\boxed{
K_H^+-K_H^-
\le
M_H\log_2(q+1).
}
\]

### Proof

Fix one old block \(C\). All old-word response coordinates are constant on \(C\). Therefore a new response signature can vary inside \(C\) only on the \(M_H\) newly admitted word coordinates. Each coordinate has at most \(q+1\) outcomes. Hence \(C\) splits into at most \((q+1)^{M_H}\) new blocks. Summing this multiplicative split bound over old blocks yields the global class-count inequality. Taking logarithms gives the bit bound. \(\square\)

### Grammar-aware form

The same proof does not require the full free monoid. For declared finite test languages

\[
\mathcal L^-\subseteq\mathcal L^+,
\]

replace \(M_H\) by

\[
|\mathcal L^+\setminus\mathcal L^-|.
\]

This is the ecologically relevant formulation when many syntactically different action words are operationally redundant.

---

## 5. Response-basis capacity

Raw word count can be very loose. A more informative contract-specific bound uses a response-test basis.

Fix one old state class \(C\). Let

\[
\mathcal B=\{w_1,\ldots,w_r\}
\]

be a finite test family such that equality of the response vector on \(\mathcal B\), together with old-state identity, is sufficient to determine the strengthened state inside \(C\).

For test \(w_i\), let

\[
r_i
=
|\{R_s(w_i):s\in C\}|
\]

be the number of outcomes that the test actually realizes inside that old class.

## Theorem 3 — response-basis capacity bound

The number of strengthened state classes inside \(C\) is at most

\[
\boxed{
\prod_{i=1}^{r} r_i
}
\]

and the added information is at most

\[
\boxed{
\sum_{i=1}^{r}\log_2 r_i.
}
\]

If every outcome combination is realized and the response vector on \(\mathcal B\) exactly characterizes the strengthened classes, equality holds.

### Proof

The strengthened blocks inject into the realized response vectors

\[
C
\longrightarrow
\prod_i R_i,
\qquad
s\mapsto(R_s(w_1),\ldots,R_s(w_r)).
\]

The codomain has size \(\prod_i r_i\). Equality holds exactly when the induced response vectors realize the full product and distinguish all strengthened blocks. \(\square\)

This is the quantity that the existing CREST family saturates.

---

## 6. Exact recovery of the existing connected CREST family

In the capability–resolution construction, the retained present worlds are

\[
U_0=\{p_{x,0}:x\in\{0,1\}^m\}.
\]

Before `probe`, they form one state.

After `probe`, use the response basis

\[
\mathcal B_m
=
\{\texttt{probe}^{1},
\texttt{probe}^{3},
\ldots,
\texttt{probe}^{2m-1}\}.
\]

For address

\[
x=(x_1,\ldots,x_m),
\]

the \(j\)-th basis test returns

\[
R_{p_{x,0}}
(\texttt{probe}^{2j-1})
=
\texttt{bit}_{x_j}.
\]

Therefore every basis coordinate has exactly two outcomes and the joint response vector is exactly the binary address:

\[
\bigl(
\texttt{bit}_{x_1},\ldots,\texttt{bit}_{x_m}
\bigr).
\]

All \(2^m\) combinations are realized. Hence Theorem 3 is sharp:

\[
\boxed{
|J^+|/|J^-|
=2^m
=
\prod_{j=1}^{m}2
}
\]

and

\[
\boxed{
\Delta K=m
=
\sum_{j=1}^{m}\log_2 2.
}
\]

So the arbitrary \(m\)-bit burden in the existing theorem is exactly the capacity of \(m\) independent binary counterfactual response coordinates.

This resolves a possible objection to the current headline. The result is not that one action name somehow contains unbounded information for free. Repeated use of the one action creates an unbounded family of sequentially addressable response tests.

---

## 7. Exact depth law for the connected witness

The same construction gives a stronger family-specific statement.

Restrict attention to pure `probe` prefixes

\[
\epsilon,
\texttt{probe},
\texttt{probe}^2,
\ldots,
\texttt{probe}^H.
\]

On \(U_0\), the informative outputs occur after odd probe depths:

\[
1,3,5,\ldots,2m-1.
\]

Therefore the number of present classes visible through horizon \(H\) is exactly

\[
\boxed{
|J_H\restriction_{U_0}|
=2^{\min(m,\lceil H/2\rceil)}
}
\]

and

\[
\boxed{
K_H(U_0)
=
\min(m,\lceil H/2\rceil).
}
\]

Thus this witness accumulates exactly one additional bit of required present-state information every two probe steps until all \(m\) latent coordinates have been exposed.

This makes the hidden resource in the existing no-bound theorem explicit: increasing \(m\) also increases the required counterfactual depth to \(2m-1\).

---

## 8. New CREST conclusion

The mathematical story should no longer stop at

\[
\text{one new capability}
\Rightarrow
\text{arbitrarily large state debt}.
\]

The stronger and less misleading result is the pair:

\[
\boxed{
\text{carrier-size gain alone cannot upper-bound representational burden,}
}
\]

while

\[
\boxed{
\text{finite counterfactual response capacity does upper-bound it.}
}
\]

Therefore the operative complexity parameter is not simply the number of management actions or newly viable worlds. It is the **distinguishing capacity of the future-response grammar**.

In ecological language, large representational debt requires one or more of:

- more intervention branches;
- deeper sequential response horizons;
- richer observable response alphabets;
- more independent latent response channels.

This supplies a new ecological prediction from the mathematics:

> **Management innovation should generate the largest state/monitoring debt in systems whose intervention responses have deep memory, branching pathways, or multiple independently distinguishable latent channels.**

Examples such as hysteresis, delayed internal loading, seed-bank legacies, dormant interaction partners, and sequential recovery pathways become relevant for a precise reason: they enlarge counterfactual response capacity.

The claim is structural, not empirical frequency. CREST does not yet show that any particular real ecosystem saturates this bound.

---

## 9. Prior-art and novelty firewall

The following generic ingredients are not claimed as new:

- finite-state distinguishing sequences or characterization sets;
- finite response trees;
- counting response signatures;
- automaton minimization;
- predictive tests in predictive-state representations.

Classical finite-state-machine testing already studies separating / distinguishing sequences and characterization sets, and predictive-state representations characterize hidden state by predictions of action-observation tests.

The CREST-level contribution of this note is narrower:

1. match a finite response-capacity upper bound to the existing CREST no-bound theorem;
2. show that the connected capability–resolution witness exactly saturates an \(m\)-binary-test capacity budget;
3. expose the growing sequential counterfactual depth that powers its arbitrary \(m\)-bit burden; and
4. replace `number of new interventions` with `distinguishable counterfactual response capacity` as the proposed explanatory quantity for representational debt.

This note should enter the manuscript spine only after the executable regressions pass and the claim is reviewed against the finite-state testing / predictive-state literature.
