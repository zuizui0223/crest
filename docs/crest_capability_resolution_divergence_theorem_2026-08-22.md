# CREST capability–resolution divergence theorem — 2026-08-22

> **Status:** sharp finite cross-gate strengthening. This extends the qualitative action-expansion theorem; it does not add a fifth audit and does not rely on empirical data.

## 1. Headline

For every integer \(m\ge 1\), there is a finite deterministic CREST family and a **single newly admitted controllable action** `probe` such that the same capability expansion:

1. enlarges the robust controlled carrier by exactly one compatible world;
2. refines the required future-sensitive state on a fixed retained present-state slice from one class to \(2^m\) classes;
3. creates exactly \(m\) bits of present-slice monitoring-resolution debt under unchanged evidence;
4. changes full required-state identification on that slice from licensed to unlicensed; while
5. a declared coarse target remains deterministically reportable.

The readout alphabet is bounded independently of \(m\). The new action is repeated and exposes one binary coordinate at a time.

Thus a constant-size change in management repertoire can create arbitrarily large representational demand even when its gain in carrier size is only one world:

\[
\boxed{\Delta |K^*|=1\qquad\text{but}\qquad \Delta K_{U_0}=m\text{ bits}.}
\]

## 2. Construction

Fix \(m\ge1\) and let \(X_m=\{0,1\}^m\). For each latent address \(x=(x_1,\ldots,x_m)\in X_m\), create neutral states

\[
p_{x,0},p_{x,1},\ldots,p_{x,m}
\]

and readout states

\[
q_{x,0},\ldots,q_{x,m-1}.
\]

The designated present-state slice is

\[
U_0=\{p_{x,0}:x\in X_m\}.
\]

Static outputs use only

\[
\{\texttt{neutral},\texttt{bit0},\texttt{bit1},\texttt{done}\}.
\]

Every \(p_{x,j}\) with \(j<m\) is `neutral`, \(p_{x,m}\) is `done`, and \(q_{x,j}\) reports `bit0` or `bit1` according to \(x_{j+1}\).

The old repertoire contains only `hold`, which self-loops. The expanded repertoire adds one action `probe` with

\[
p_{x,j}\xrightarrow{\rm probe}q_{x,j}
\xrightarrow{\rm probe}p_{x,j+1}\qquad(j<m),
\]

and \(p_{x,m}\) self-looping under `probe`.

No action name, output symbol, or local branching factor grows with \(m\).

## 3. State-complexity theorem

Let \(J_m^-\) and \(J_m^+\) be the coarsest exact future-response partitions before and after `probe` is admitted.

Under `hold` alone, every member of \(U_0\) has the same static output and same self-loop response, hence

\[
|J_m^-\restriction_{U_0}|=1.
\]

After `probe` is admitted, take distinct \(x,y\in X_m\), and let \(j\) be their first differing coordinate. Repeated `probe` reaches the corresponding readout states at that coordinate, which have different binary outputs. Therefore no exact future-sensitive partition can merge \(p_{x,0}\) and \(p_{y,0}\). Since \(|U_0|=2^m\),

\[
|J_m^+\restriction_{U_0}|=2^m.
\]

Define present-slice complexity

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|.
\]

Then

\[
K_{U_0}(J_m^-)=0,\qquad K_{U_0}(J_m^+)=m.
\]

So one newly admitted action produces an arbitrary \(m\)-bit increase in required present-state resolution.

## 4. Carrier theorem using the same action

Add ambient worlds `safe`, `fragile`, and `bad`. Mark all chain worlds, `safe`, and `fragile` compatible; mark `bad` incompatible.

Under `hold`, chain worlds and `safe` self-loop while `fragile` goes to `bad`. Under `probe`, the chain follows the readout dynamics above, `safe` stays safe, and `fragile` goes to `safe`.

Before expansion, `fragile` is excluded from the greatest robust controlled-invariant carrier. After expansion, `probe` is a safe control from `fragile`, while every previously viable world remains viable by choosing `hold`. Hence

\[
K_m^{*+}=K_m^{*-}\cup\{\texttt{fragile}\}
\]

and therefore

\[
\boxed{|K_m^{*+}|-|K_m^{*-}|=1.}
\]

The same single action `probe` causes both the one-world carrier gain and the \(m\)-bit state refinement.

## 5. Evidence and monitoring debt

Fix evidence on \(U_0\) that merges all present worlds into one record class. Before `probe`, that evidence identifies the required present state because \(J_m^-\restriction_{U_0}\) also has one class.

After `probe`, the required state has \(2^m\) present classes while evidence is unchanged, so full-state identification fails. The coarsest evidence refinement that identifies the new present state has \(2^m\) classes. Thus the present-slice monitoring debt is exactly

\[
D_{U_0}=\log_2(2^m)-\log_2(1)=m.
\]

## 6. Target-only reportability

Let the requested target be constant on \(U_0\), for example a coarse present viability label. Then the unchanged one-block evidence still licenses the target both before and after action expansion even though it ceases to license the full required state.

Therefore, for arbitrary finite \(m\), one added action realizes

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

The family rules out any universal finite bound of the form

\[
\Delta K_{U_0}\le f(\Delta|K^*|)
\]

where \(f\) depends only on carrier-size gain. Here \(\Delta|K^*|=1\) for every \(m\), while \(\Delta K_{U_0}=m\) is arbitrary.

Hence **viability gain alone cannot upper-bound the representational burden created by a capability expansion** without additional structural assumptions.

## 8. Relation to the existing CREST spine

The previous four-world action-expansion witness proved only simultaneous strictness. This family establishes an unbounded separation of scales: viability benefit remains constant while required-state complexity and monitoring debt grow without bound.

J1 still supplies the meaning of the least-information state; J6 supplies the robust controlled carrier; the evidence gate supplies the licensing criterion. This theorem couples those existing gates quantitatively rather than creating a new audit.

## 9. Claim boundary

Not claimed as new by itself: deterministic automaton minimization, sequential binary readout, viability-kernel monotonicity, partition refinement, observability, or logarithmic state complexity.

The CREST-level candidate contribution is the **cross-gate scaling conjunction and no-bound result**: one fixed-size capability expansion can have a constant viability gain but arbitrarily large consequences for the least-information state and the monitoring resolution required to identify it.