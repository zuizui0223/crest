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

## S6. Capability–resolution divergence and sharp response-depth law

### S6.1 Carrier-gain no-bound result

The earlier connected family establishes that for every \(m\ge1\), one newly admitted controllable action can realize

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m.
}
\]

Consequently no universal finite function depending only on carrier-size gain can upper-bound added state information. This is an impossibility result about the explanatory variable \(\Delta|K^*|\); it does not imply that state debt lacks other finite bounds.

### S6.2 Sequential response-capacity upper bound

Fix one old state class \(C\). Suppose a newly relevant sequential intervention has response-relevant depth \(H\), and stage \(h\) can produce at most \(r_h\) distinguishable retained response types within \(C\).

For \(u\in C\), let

\[
\Sigma_H(u)=(Y_1(u),\ldots,Y_H(u))
\]

be the complete sequential response record. The strengthened state can split \(C\) only according to distinctions in \(\Sigma_H\).

**Theorem S6.1 — sequential state-debt bound.** The class \(C\) can split into at most

\[
\boxed{
\prod_{h=1}^{H}r_h
}
\]

strengthened classes, and therefore

\[
\boxed{
\Delta K_C
\le
\sum_{h=1}^{H}\log_2r_h.
}
\]

**Proof.** The strengthened classes inject into the response-vector space \(R_1\times\cdots\times R_H\), whose cardinality is at most \(\prod_h r_h\). Taking \(\log_2\) yields the bit bound. ∎

For a homogeneous \(r\)-ary response path,

\[
\boxed{
|J_H^+|/|J_H^-|\le r^H,
\qquad
\Delta K\le H\log_2r.
}
\]

The inverse necessary condition is

\[
\boxed{
H\ge\left\lceil\frac{k}{\log_2r}\right\rceil
}
\]

for generating \(k\) added bits through an \(r\)-ary sequential channel.

### S6.3 Sharp connected construction

Fix integers \(r\ge2\) and \(H\ge1\), and let

\[
X_{r,H}=\{0,1,\ldots,r-1\}^{H}.
\]

For every address

\[
x=(x_1,\ldots,x_H)\in X_{r,H},
\]

create states

\[
p_{x,0},p_{x,1},\ldots,p_{x,H}.
\]

All \(p_{x,0}\) output `neutral`. For \(h\ge1\), state \(p_{x,h}\) outputs `response-\(x_h\)`. Add two common compatible worlds

\[
s=\texttt{safe},
\qquad
f=\texttt{fragile},
\]

both with output `done`.

The old controllable repertoire is

\[
A_c^-=\{\texttt{hold}\}.
\]

Every path state and \(s\) self-loops under `hold`, while `hold` is unavailable at \(f\).

The expanded repertoire is

\[
A_c^+=\{\texttt{hold},\texttt{probe}\}.
\]

Old transitions are unchanged and

\[
p_{x,h}\xrightarrow{\rm probe}p_{x,h+1}
\qquad(0\le h<H),
\]

followed by

\[
p_{x,H}\xrightarrow{\rm probe}f
\xrightarrow{\rm probe}s,
\qquad
s\xrightarrow{\rm probe}s.
\]

Thus the same new action exposes the sequential response address and rescues the unique previously nonviable world.

### S6.4 Exact carrier gain

Under the old repertoire, every path state and \(s\) has the safe action `hold`, while \(f\) has no safe control. Therefore \(f\) is excluded from the old maximal controlled carrier. After `probe` is admitted, \(f\to s\), so it becomes viable and every old viable world remains viable.

Hence

\[
\boxed{
\Delta|K^*|=1.
}
\]

### S6.5 Exact present-state refinement

Let

\[
U_0=\{p_{x,0}:x\in X_{r,H}\}.
\]

Before expansion, every world in \(U_0\) has the same output and self-loops under the only action, so

\[
\boxed{|J^-\restriction_{U_0}|=1.}
\]

After expansion, applying `probe` \(h\) times reaches \(p_{x,h}\), whose output is `response-\(x_h\)`. The H-stage response record is therefore exactly

\[
(\texttt{response-}x_1,\ldots,\texttt{response-}x_H).
\]

All \(r^H\) addresses are realized and distinct addresses differ at at least one stage. Hence

\[
\boxed{|J^+\restriction_{U_0}|=r^H.}
\]

Therefore

\[
\boxed{
\Delta K_{U_0}=H\log_2r.
}
\]

At every prefix depth \(d\le H\), exactly the first \(d\) address coordinates have been exposed, so

\[
\boxed{
|J_d\restriction_{U_0}|=r^d,
\qquad
K_d(U_0)=d\log_2r.
}
\]

The upper bound is attained at every prefix depth.

### S6.6 Exact evidence debt and target

Fix one evidence record on all worlds in \(U_0\). Before expansion the evidence identifies the single old required state. After expansion it merges all \(r^H\) required states.

The minimum additional resolution required for full-state identification is therefore

\[
\boxed{
D_E=H\log_2r.
}
\]

A target constant on \(U_0\) remains reportable before and after. The sharp family realizes

\[
\boxed{
\Delta|K^*|=1,
\quad
|J_H^+|/|J_H^-|=r^H,
\quad
\Delta K=D_E=H\log_2r,
\quad
\text{full state: yes}\to\text{no},
\quad
\text{target: yes}\to\text{yes}.
}
\]

For binary response stages,

\[
\boxed{
\Delta|K^*|=1,
\qquad
|J_H^+|/|J_H^-|=2^H,
\qquad
\Delta K=D_E=H\text{ bits}.
}
\]

This is the preferred sharp construction. The older \(m\)-bit / \(2m-1\)-depth readout remains repository provenance for the no-bound result.

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

The debt is nonnegative and vanishes exactly when the existing evidence already identifies the required state. In the sharp sequential family with one-block present evidence,

\[
\boxed{D_E=H\log_2r.}
\]

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

The automated suite includes direct construction and verification of the sharp sequential family across binary and multi-outcome examples, including checks that:

- the controlled-carrier gain is exactly one world;
- one old present state refines to exactly \(r^H\) states;
- each partial response depth \(d\) yields exactly \(r^d\) present response signatures;
- state information and monitoring-resolution debt are exactly \(H\log_2r\) bits;
- the newly viable `fragile` world lies on the same `probe` trajectories used for sequential readout;
- the coarse target remains reportable when full-state identification is lost;
- the inverse minimum-depth calculations agree with the analytic bound.

The older arbitrary-\(m\) connected witness remains tested as provenance for the carrier-gain no-bound result. The same tests are executed under multiple supported Python versions in continuous integration. The submission verifier independently checks abstract length, keyword count, blinded identifiers, required manuscript sections, and presence of the theorem headline.

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
- finite-state distinguishing sequences and response trees;
- the product/information capacity of finite \(r\)-ary response vectors;
- logarithmic state complexity.

The theorem-level CREST claim is the matched cross-layer result. Carrier-size gain alone cannot upper-bound added state burden, finite counterfactual response capacity can, and a connected family attains the sharp sequential equality while carrier gain remains exactly one world, full-state licensing is lost under fixed evidence, and a coarse target is preserved.

The mathematical witness does not establish how frequently large state-resolution changes occur in nature. It identifies a precise structural quantity for future empirical work: response-relevant depth and the number of independently distinguishable retained outcomes exposed at each stage.