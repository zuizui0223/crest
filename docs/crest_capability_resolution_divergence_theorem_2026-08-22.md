# CREST capability–resolution divergence theorem — 2026-08-22

> **Status:** sharp finite cross-gate strengthening. This extends the qualitative action-expansion theorem; it does not add a fifth audit and does not rely on empirical data.

## 1. Headline

For every integer \(m\ge 1\), there is one finite deterministic CREST system and a **single newly admitted controllable action** `probe` such that the same capability expansion:

1. enlarges the greatest robust controlled carrier by exactly one compatible world;
2. refines the least exact future-sensitive state on a retained present slice from one class to \(2^m\) classes;
3. creates exactly \(m\) bits of present-slice monitoring-resolution debt under unchanged evidence;
4. changes full required-state identification on that slice from licensed to unlicensed; while
5. a declared coarse target remains deterministically reportable.

The output alphabet has four symbols, the action alphabet changes from one symbol to two, and neither grows with \(m\). Repeated use of the one new action exposes one latent binary coordinate at a time.

Thus

\[
\boxed{
\Delta |K^*|=1
\qquad\text{while}\qquad
\Delta K_{U_0}=m\ \text{bits}
}
\]

for arbitrary \(m\).

The construction is connected in the relevant sense: the same `probe` trajectories that reveal the latent address terminate in the unique world that `probe` newly makes viable. The result is therefore not a disjoint union of an independent readout gadget and an independent rescue gadget.

## 2. Construction

Fix \(m\ge1\) and let

\[
X_m=\{0,1\}^m.
\]

For each address \(x=(x_1,\ldots,x_m)\in X_m\), create neutral states

\[
p_{x,0},p_{x,1},\ldots,p_{x,m}
\]

and readout states

\[
q_{x,0},\ldots,q_{x,m-1}.
\]

Add two further compatible worlds

\[
s=\texttt{safe},
\qquad
r=\texttt{fragile}.
\]

The retained present slice is

\[
U_0=\{p_{x,0}:x\in X_m\},
\]

which is contained in the controlled carrier both before and after action expansion.

### Outputs

Use only the four static output symbols

\[
\{\texttt{neutral},\texttt{bit0},\texttt{bit1},\texttt{done}\}.
\]

For \(j<m\), every \(p_{x,j}\) is `neutral`; every \(p_{x,m}\), \(s\), and \(r\) is `done`; and \(q_{x,j}\) reports `bit0` or `bit1` according to \(x_{j+1}\).

### Old repertoire

The old controllable repertoire is

\[
A_c^- = \{\texttt{hold}\}.
\]

Every chain world and \(s\) self-loops under `hold`. At \(r\), `hold` is unavailable. Hence \(r\) has no safe control under the old contract.

### Expanded repertoire

The new repertoire is

\[
A_c^+ = \{\texttt{hold},\texttt{probe}\}.
\]

The old `hold` transitions are unchanged. The one new action satisfies

\[
p_{x,j}\xrightarrow{\rm probe}q_{x,j}
\xrightarrow{\rm probe}p_{x,j+1}
\qquad(j<m),
\]

and the terminal chain transition is

\[
p_{x,m}\xrightarrow{\rm probe}r
\xrightarrow{\rm probe}s,
\qquad
s\xrightarrow{\rm probe}s.
\]

Thus every address-readout path enters the newly rescued world \(r\) and then the safe sink \(s\).

No action name, output symbol, or local branching factor grows with \(m\).

## 3. Carrier theorem

Let \(K_m^{*-}\) and \(K_m^{*+}\) denote the greatest robust controlled-invariant carriers under \(A_c^-\) and \(A_c^+\).

Under the old repertoire, every chain world and \(s\) has the safe control `hold`, while \(r\) has no legal safe control. Therefore

\[
K_m^{*-}=W_m\setminus\{r\},
\]

where \(W_m\) is the full compatible ambient world set.

After `probe` is admitted, \(r\xrightarrow{\rm probe}s\), so \(r\) becomes viable. Every previously viable world remains viable because `hold` is unchanged and remains safe there. Hence

\[
K_m^{*+}=W_m=K_m^{*-}\cup\{r\}.
\]

Therefore

\[
\boxed{|K_m^{*+}|-|K_m^{*-}|=1.}
\]

The same transition graph that yields this one-world carrier gain also contains the address-readout paths used below.

## 4. State-complexity theorem

Let \(J_m^-\) be the coarsest exact future-response partition on \(K_m^{*-}\) under `hold`, and let \(J_m^+\) be the coarsest exact future-response partition on \(K_m^{*+}\) under `hold` and `probe`.

### Before expansion

Every world in \(U_0\) has output `neutral` and self-loops under the only legal action `hold`. Hence all worlds in \(U_0\) have the same complete legal future trace:

\[
|J_m^-\restriction_{U_0}|=1.
\]

### After expansion

Take distinct \(x,y\in X_m\), and let \(j+1\) be their first differing coordinate. Starting from \(p_{x,0}\), the word

\[
\texttt{probe}^{\,2j+1}
\]

reaches \(q_{x,j}\); starting from \(p_{y,0}\), the same word reaches \(q_{y,j}\). Those states have different binary outputs because \(x_{j+1}\ne y_{j+1}\). Therefore no exact future-sensitive partition can merge \(p_{x,0}\) and \(p_{y,0}\).

Since \(|U_0|=2^m\),

\[
|J_m^+\restriction_{U_0}|=2^m.
\]

Define present-slice state complexity

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|.
\]

Then

\[
K_{U_0}(J_m^-)=0,
\qquad
K_{U_0}(J_m^+)=m,
\]

so

\[
\boxed{\Delta K_{U_0}=m.}
\]

A one-action expansion can therefore create arbitrarily large required present-state information while changing carrier size by only one world.

## 5. Evidence and monitoring debt

Fix an unchanged evidence map on \(U_0\) that assigns every present world the same record. Before `probe`, this one-block evidence identifies \(J_m^-\restriction_{U_0}\). After `probe`, it does not identify \(J_m^+\restriction_{U_0}\).

For this retained slice define

\[
D_{U_0}(E,J)
=
\log_2 |(E\vee J)\restriction_{U_0}|
-
\log_2 |E\restriction_{U_0}|.
\]

Because \(E\restriction_{U_0}\) has one block and the new required state has \(2^m\) blocks,

\[
D_{U_0}(E,J_m^-)=0,
\qquad
D_{U_0}(E,J_m^+)=m.
\]

Thus fixed monitoring can move from full-state adequacy to an exact \(m\)-bit resolution deficit even though the management capability gain is only one newly viable world.

## 6. Target-only reportability

Let the requested target \(T\) be constant on \(U_0\), for example a coarse `presently viable` label. Then the unchanged one-block evidence licenses \(T\) before and after action expansion even though it ceases to license the full required state.

For arbitrary finite \(m\), the connected family therefore realizes

\[
\boxed{
\Delta |K^*|=1,
\quad
\Delta K_{U_0}=m,
\quad
D_{U_0}:0\to m,
\quad
\text{full state: yes}\to\text{no},
\quad
\text{target: yes}\to\text{yes}.
}
\]

## 7. No-bound corollary

There is no universal finite function \(f\) depending only on carrier-size gain such that every CREST capability expansion satisfies

\[
\Delta K_{U_0}\le f(\Delta|K^*|).
\]

Indeed, this family has

\[
\Delta|K^*|=1
\]

for every \(m\), while

\[
\Delta K_{U_0}=m
\]

is arbitrary.

Hence

\[
\boxed{
\text{viability gain alone does not upper-bound representational burden.}
}
\]

Any such upper bound requires additional structural assumptions beyond the number of newly viable worlds.

## 8. Why the connected construction matters

A weaker proof could place an arbitrary response-memory gadget beside an unrelated one-world rescue gadget and let the same action name appear in both. That would establish logical conjunction but little structural coupling.

The present construction removes that objection. Under `probe`, every address chain terminates at the same rescued world \(r\), and \(r\) is viable only because that very `probe` action reaches \(s\). Thus the capability-changing transition is part of the same future-response graph whose repeated action traces force the \(m\)-bit present-state refinement.

The theorem still does not claim that carrier gain *causes* the state-complexity increase. It proves a sharper statement: one fixed-size capability expansion can simultaneously have a constant effect at the viability gate and an unbounded effect at the state/evidence gates within one connected finite system.

## 9. Relation to the existing CREST spine

J1 supplies the least-information state on a declared carrier. J6 supplies the greatest robust controlled carrier. The evidence gate supplies full-state licensing, and target factorization supplies target-only reportability.

The earlier four-world action-expansion witness established only simultaneous strictness. The connected family above strengthens it to an arbitrary scaling separation and a no-bound corollary.

This result belongs in the canonical mathematical spine because it couples existing CREST gates quantitatively rather than introducing another audit or another vocabulary family.

## 10. Claim boundary

Not claimed as new by itself:

- deterministic automaton minimization;
- sequential binary readout;
- viability kernels or their monotonicity;
- partition refinement;
- observability;
- logarithmic state complexity.

The CREST-level candidate contribution is the **connected cross-gate scaling conjunction and its no-bound consequence**: one fixed-size capability expansion can add exactly one viable world while forcing arbitrarily many bits of additional least-information state and monitoring resolution, with full-state identification lost but a coarse target still reportable.
