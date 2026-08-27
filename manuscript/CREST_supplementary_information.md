# Supplementary Information
## When Conservation Capacity Outgrows Conservation Knowledge: A Contract-Relative Theory of Ecological State

This Supplementary Information provides formal definitions, proof details, finite witness constructions, and reproducibility instructions for the CREST manuscript. It is intentionally technical. The main text contains the ecological argument and the principal theorem-level consequences.

## S1. Formal setup

### S1.1 Finite ecological worlds and actions

Let \(U\) be a finite set of admissible latent ecological worlds. A partial deterministic action \(a\) has transition map

\[
\tau_a:U\rightharpoonup U.
\]

An output or current descriptor is represented by

\[
h:U\to Y.
\]

For controlled problems, the action set is partitioned into uncontrollable and controllable actions. A declared scientific contract may also carry inherited categories, candidate response mechanisms, an evidence map, and a requested target.

### S1.2 Partitions and information order

A partition \(P\) of \(U\) represents a candidate ecological state variable. We order partitions by retained information:

\[
P\preceq Q
\quad\Longleftrightarrow\quad
Q\text{ refines }P.
\]

Thus larger elements in the order retain at least as many distinctions. For \(u\in U\), \([u]_P\) denotes the block containing \(u\).

### S1.3 Exactness for a declared future grammar

A partition is exact for a declared action grammar when worlds merged by the partition have the same required present output, the same relevant legal-action structure, and successors that remain in the same state blocks under every required action. Equivalent formulations can be given through equality of all legal future traces.

### S1.4 Evidence and targets

An evidence architecture induces a reliability-qualified partition \(E_D\). Worlds in one \(E_D\)-block remain compatible with the available record after declared detection, failure, and risk assumptions are included.

A target is a map

\[
T:U\to Z.
\]

The target is deterministically reportable from the evidence exactly when it is constant on every evidence block.

## S2. Gate A: admissible carriers

State construction presupposes a world set on which the declared obligations can coexist. CREST treats this as a separate problem.

### S2.1 Universal transition-closed carrier

Let \(W_0\subseteq U\) be the statically compatible worlds. Define

\[
F(S)=\{u\in S\cap W_0:\tau_a(u)\downarrow\Rightarrow \tau_a(u)\in S
\text{ for every declared action }a\}.
\]

Starting at \(S_0=W_0\) and iterating

\[
S_{n+1}=F(S_n)
\]

produces a descending finite sequence. It therefore reaches a fixed point \(U^*\).

**Proposition S2.1.** \(U^*\) is the greatest subset of \(W_0\) closed under every declared universal action.

**Proof.** Monotonicity of \(F\) gives a descending sequence from \(W_0\), which stabilizes by finiteness. The fixed point is transition closed by definition. Any transition-closed \(C\subseteq W_0\) satisfies \(C\subseteq F(C) = C\), and induction gives \(C\subseteq S_n\) for every \(n\), hence \(C\subseteq U^*\). ∎

A nonempty universal carrier exists exactly when \(U^*\neq\varnothing\).

### S2.2 Robust controlled carrier

For a controlled contract, define \(G(S)\) as the worlds in \(S\cap W_0\) for which every uncontrollable successor remains in \(S\) and at least one legal controllable action has a successor in \(S\). Descending iteration gives a greatest robust controlled-invariant carrier \(K^*\).

**Proposition S2.2.** A nonempty robust controlled carrier exists exactly when \(K^*\neq\varnothing\). In the finite deterministic setting, every nonempty \(K^*\) admits a memoryless safe selector.

The proof is the standard greatest-fixed-point argument: a safe control can be selected independently at each world because membership in \(K^*\) guarantees at least one legal control whose successor remains inside \(K^*\).

### S2.3 Why carrier failure is not a partition failure

If the relevant common carrier is empty or fails required coverage, splitting state blocks cannot repair the problem. The declared scientific obligations are not jointly realizable on the proposed latent-world set. CREST therefore uses the dependency

\[
\text{carrier feasibility}
\longrightarrow
\text{state construction}
\longrightarrow
\text{evidence licensing}.
\]

## S3. Gate B: unique least-information state

Let \(B\) be a baseline partition that contains distinctions the analysis is already committed to preserving. Represent the implemented scientific responsibilities by refinement closures

\[
C_\Gamma,\qquad C_{\mathcal H},\qquad C_\Theta,\qquad C_{D,T}.
\]

Each closure is assumed to be monotone, inflationary, and idempotent on the finite partition lattice.

Define their common closure above \(B\) by

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B).
}
\]

### Theorem S3.1 — conditional joint-state theorem

Under these assumptions, \(J\) is the unique coarsest partition above \(B\) that satisfies all implemented requirements.

**Proof.** The partition lattice \(\Pi(U)\) is finite and complete. The join of closure operators is itself a closure operator whose fixed-point set is the intersection of the individual fixed-point sets. Hence \(J\) is a common fixed point above \(B\). If \(P\) is any other common fixed point with \(B\preceq P\), monotonicity gives

\[
J=C_*(B)\preceq C_*(P)=P.
\]

Therefore every adequate partition refines \(J\), and \(J\) is uniquely coarsest. ∎

The generic lattice and closure-operator facts are classical. The role of Theorem S3.1 is to state precisely when a least-information CREST state is well defined for a declared finite ecological problem.

### S3.2 Noncommuting refinement obligations

Pairwise commutation is not required. One refinement can create a distinction that causes another audit to expose an additional split. Fair repeated refinement still reaches the common fixed point on a finite carrier.

A finite cascade witness can be built with worlds

\[
U=\{z,a,b,c,d,r,s\}
\]

and transitions arranged so that one obligation isolates \(a\) only after \(z\) is separated, a second isolates \(b\) after \(a\), and so on. Different fair update orders take different numbers of passes but converge to the same least common fixed point. Exhaustive enumeration of all partitions in the witness confirms unique coarseness.

## S4. Gate C: evidence licensing

Let \(J\) be the required state partition and \(E_D\) the evidence partition.

### Theorem S4.1 — full-state licensing

A deterministic full-state report exists exactly when

\[
\boxed{J\preceq E_D.}
\]

**Proof.** If \(J\preceq E_D\), every evidence block lies within one required-state block, so the state is constant on each possible record. Conversely, if one evidence block intersects two distinct \(J\)-blocks, that record is compatible with at least two required states, so no deterministic full-state report is licensed. ∎

When full-state licensing fails, the sharp ambiguity-explicit report for evidence block \(e\) is

\[
\mathcal S(e)=\{[u]_J:u\in e\}.
\]

### Corollary S4.2 — target-only reportability

The requested target can remain deterministic even when the full state is unresolved. If

\[
T(u)=T(v)
\quad\text{for all }u,v\text{ in the same }E_D\text{-block},
\]

then \(T\) is reportable from the evidence whether or not \(J\preceq E_D\).

Hence the three objects

\[
\boxed{
\text{required state},\qquad
\text{identified state},\qquad
\text{reportable target}
}
\]

need not coincide.

## S5. Capability expansion and monotonicity

Let the controllable repertoires satisfy

\[
A_c\subseteq A_c',
\]

with all old transitions and uncontrollable dynamics unchanged.

### Proposition S5.1 — carrier monotonicity

\[
K^*(A_c)\subseteq K^*(A_c').
\]

Every safe policy available before expansion remains available after expansion, so the maximal robust carrier cannot shrink.

### Proposition S5.2 — required-state monotonicity

On a retained carrier, if the enlarged future responsibility \(\Gamma'\) contains every obligation in \(\Gamma\), then

\[
J_\Gamma\preceq J_{\Gamma'}.
\]

Adding response obligations cannot make a previously necessary distinction unnecessary.

These monotonicity results establish direction only. They do not determine how the size of the state refinement relates to the size of the carrier gain.

## S6. Capability–resolution divergence

### S6.1 Construction

Fix \(m\ge1\) and let

\[
X_m=\{0,1\}^m.
\]

For each address \(x=(x_1,\ldots,x_m)\), create neutral states

\[
p_{x,0},p_{x,1},\ldots,p_{x,m}
\]

and readout states

\[
q_{x,0},\ldots,q_{x,m-1}.
\]

Add two further worlds

\[
s=\texttt{safe},
\qquad
r=\texttt{fragile}.
\]

The retained present slice is

\[
U_0=\{p_{x,0}:x\in X_m\}.
\]

Use the fixed output alphabet

\[
\{\texttt{neutral},\texttt{bit0},\texttt{bit1},\texttt{done}\}.
\]

For \(j<m\), \(p_{x,j}\) outputs `neutral`; \(p_{x,m}\), \(r\), and \(s\) output `done`; and \(q_{x,j}\) outputs the \((j+1)\)-st binary coordinate of \(x\).

The old controllable repertoire is

\[
A_c^- = \{\texttt{hold}\}.
\]

Every chain state and \(s\) self-loops under `hold`; `hold` is unavailable at \(r\).

The expanded repertoire is

\[
A_c^+ = \{\texttt{hold},\texttt{probe}\}.
\]

The old transitions are unchanged and

\[
p_{x,j}\xrightarrow{\rm probe}q_{x,j}
\xrightarrow{\rm probe}p_{x,j+1}
\qquad(j<m),
\]

with terminal transitions

\[
p_{x,m}\xrightarrow{\rm probe}r
\xrightarrow{\rm probe}s,
\qquad
s\xrightarrow{\rm probe}s.
\]

The same action therefore both traverses the readout chain and rescues the previously nonviable world \(r\).

### S6.2 Carrier gain

Under the old repertoire, every chain state and \(s\) has the safe action `hold`, while \(r\) has no safe control. Hence

\[
K_m^{*-}=W_m\setminus\{r\}.
\]

After `probe` is admitted, \(r\to s\), so

\[
K_m^{*+}=W_m.
\]

Therefore

\[
\boxed{|K_m^{*+}|-|K_m^{*-}|=1.}
\]

### S6.3 Present-state refinement

Before expansion, every world in \(U_0\) has the same output and the same self-loop under the only action, so

\[
|J_m^-\restriction_{U_0}|=1.
\]

Take distinct addresses \(x,y\). Let \(j+1\) be their first differing coordinate. The word

\[
\texttt{probe}^{2j+1}
\]

reaches \(q_{x,j}\) from \(p_{x,0}\) and \(q_{y,j}\) from \(p_{y,0}\), and those states have different outputs. Thus no exact future-sensitive partition can merge the two starting worlds. Since \(|U_0|=2^m\),

\[
|J_m^+\restriction_{U_0}|=2^m.
\]

With

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|,
\]

we obtain

\[
\boxed{\Delta K_{U_0}=m.}
\]

### S6.4 Evidence and target

Fix an evidence map that assigns every world in \(U_0\) the same record. Before expansion the evidence identifies the one required present state. After expansion it merges \(2^m\) required states.

The minimum additional resolution required for full-state identification is therefore exactly \(m\) bits. A target constant on \(U_0\) remains reportable before and after.

The connected family realizes

\[
\boxed{
\Delta|K^*|=1,
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

### S6.5 No-bound corollary

There is no universal finite function \(f\) depending only on carrier-size gain such that every capability expansion in the family satisfies

\[
\Delta K_{U_0}\le f(\Delta|K^*|).
\]

The proof fixes the carrier gain at one while allowing \(m\) to be arbitrary.

The result is an impossibility statement about bounds without further structural assumptions. It is not a claim that real ecological systems generically display exponential state growth.

## S7. Monitoring-resolution debt

For evidence partition \(E\) and required state \(J\), the unique coarsest evidence refinement that preserves all existing evidence distinctions and identifies \(J\) is

\[
E\vee J.
\]

Define

\[
\boxed{
D_E(J)=\log_2|E\vee J|-\log_2|E|.
}
\]

The debt is nonnegative and vanishes exactly when the existing evidence already identifies the required state.

This quantity measures state resolution, not sampling effort. If the observation map has a structural symmetry that merges two response-relevant mechanisms, repeated observations through the same channel can leave the ambiguity unchanged. In such cases, debt is repaired by a new discriminating measurement type rather than replication alone.

## S8. Shallow-lake finite worked case

The main text uses a three-world qualitative model grounded in established shallow-lake restoration mechanisms.

Let

\[
U_{\rm lake}=\{S_w,F_w,C\},
\]

where \(S_w\) is a turbid world dominated by sediment-phosphorus legacy, \(F_w\) a turbid world dominated by food-web/macrophyte feedback, and \(C\) a recovered clear-water world.

The present output is

\[
h(S_w)=h(F_w)=\texttt{turbid},
\qquad
h(C)=\texttt{clear}.
\]

Use the illustrative action table:

| world | continued load reduction \(L\) | sediment treatment \(S\) | food-web restoration \(F\) |
|---|---|---|---|
| \(S_w\) | \(S_w\) | \(C\) | \(S_w\) |
| \(F_w\) | \(F_w\) | \(F_w\) | \(C\) |
| \(C\) | \(C\) | \(C\) | \(C\) |

For current-status reporting, the partition

\[
\{S_w,F_w\}\mid\{C\}
\]

is adequate. For the intervention-selection target under \(\{L,S,F\}\), \(S_w\) and \(F_w\) cannot be merged because their successors differ under the supplementary actions. The exact state becomes

\[
\{S_w\}\mid\{F_w\}\mid\{C\}.
\]

If routine evidence contains only the current `turbid/clear` output, its partition remains

\[
E_{\rm routine}=\{S_w,F_w\}\mid\{C\}.
\]

It therefore reports current status but does not identify which supplementary intervention-response state is present.

This is an illustrative finite mapping, not a fitted deterministic model of lake restoration. The ecological literature supports the existence of internal phosphorus legacy, biological feedback, multiple restoration channels, and delayed or failed recovery; it does not imply that the transitions in the table are universal or deterministic in real lakes.

## S9. Software reproducibility

The reference implementation is provided in the accompanying public repository. The manuscript's finite constructions are executable rather than simulated from fitted ecological data.

A clean Python environment can reproduce the automated checks with:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_crest_philosophy_submission.py --write-report
```

The automated suite includes direct construction and verification of the capability–resolution family for several finite values of \(m\), including checks that:

- the controlled-carrier gain is exactly one world;
- the retained present slice refines from one class to \(2^m\) classes;
- monitoring-resolution debt is exactly \(m\) bits under the declared fixed evidence;
- the newly viable `fragile` world lies on the same `probe` trajectories used for readout, preventing a disjoint-union interpretation of the construction;
- the coarse target remains reportable when full-state identification is lost.

The same tests are executed under multiple supported Python versions in continuous integration. The submission verifier independently checks abstract length, keyword count, blinded identifiers, required manuscript sections, and presence of the theorem headline.

No empirical dataset is needed to establish the finite theorem. The shallow-lake example in the main text is a literature-grounded worked interpretation, not an empirical calibration of the witness construction.

## S10. Relation to established mathematical results

CREST does not claim novelty for the following mathematical substrates by themselves:

- deterministic finite-state minimization and trace equivalence;
- Myhill–Nerode-style distinguishability;
- partition lattices and closure operators;
- fixed-point iteration on finite lattices;
- viability-kernel monotonicity;
- predictive state representations;
- state/action abstraction coupling;
- logarithmic state complexity.

The theorem-level claim developed in the main text is the connected cross-layer separation: one fixed-size capability expansion can add exactly one viable world while forcing arbitrarily many additional bits of least-state and evidence resolution on a retained present slice, with full-state identification lost and a coarse target preserved.

This conjunction is what supports the conservation interpretation. The mathematical witness does not establish how frequently large state-resolution changes occur in nature. It establishes that management-capability gain alone cannot provide a universal upper bound on the information an adequate ecological state may require.
