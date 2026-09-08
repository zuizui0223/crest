# CREST mathematical spine

> **Purpose:** identify the smallest mathematical chain needed to answer the central CREST question, and separate classical substrate from the nontrivial cross-gate result.

## 1. One question, three gates, one cross-gate headline

The mathematical task is:

> Given a declared scientific contract, when can one ecological state exist, what is the least-information such state, how much joint resolution does it require, how does that burden change across contracts, when does evidence identify it, and how can those requirements change when the future/management repertoire changes?

The canonical proof chain is

```text
Gate A: admissible common carrier?
        ↓
Gate B: unique least-information joint state?
        ↓
Joint-debt layer: how many bits are required jointly,
                  and which responsibilities/interactions generate them?
        ↓
Change layer: when the contract changes, did burden move directly,
              through interaction, or both—and at what order?
        ↓
Gate C: evidence identifies that state?
        ↓
Cross-gate: how can one capability expansion move viability,
            state complexity, evidence adequacy, and target reportability
            in different directions and at different scales?
        ↓
Capacity law: what response resource actually bounds the added state debt?
```

The first three gates define feasibility, state, and evidence. The debt layers quantify the state constructed at Gate B and make representational change diagnosable before Gate C is evaluated. The cross-gate results then rule out carrier gain as a sufficient complexity parameter and identify counterfactual response capacity as one relevant finite bound.

## 2. Gate A — carrier feasibility

The companion obligations do not automatically live on the same latent world set. CREST therefore separates state construction from carrier existence.

### Universal carrier — J3

For static-compatible worlds `W0` and partial deterministic actions, define

\[
F(S)=\{w\in S\cap W_0:\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S\text{ for every declared }a\}.
\]

Descending iteration yields the greatest universally transition-closed carrier \(U^*\), with

\[
\boxed{
\text{nonempty universal common carrier exists}
\iff
U^*\neq\varnothing.
}
\]

### Controlled carrier — J6

When uncontrollable moves must all be survived but one controllable move may be selected, define

\[
G(S)=\{w\in S\cap W_0:\text{all uncontrollable successors stay in }S\text{ and some legal control stays in }S\}.
\]

Descending iteration yields the greatest robustly controlled-invariant carrier \(K^*\), with

\[
\boxed{
\text{nonempty controlled common carrier exists}
\iff
K^*\neq\varnothing.
}
\]

Every nonempty \(K^*\) admits a memoryless safe selector in the finite deterministic setting.

### Why Gate A is separate

An empty or coverage-incomplete carrier is not a failure to find the right partition. It says the declared obligations cannot all be represented on one admissible world set without changing the contract.

Detailed proofs:

- `crest_maximal_common_lift_theorem_2026-08-17.md`
- `crest_controlled_common_lift_theorem_2026-08-18.md`

## 3. Gate B — unique least-information state

On one admissible finite carrier \(U\), let \(\Pi(U)\) be the partition lattice ordered by information:

\[
P\preceq Q
\iff
Q\text{ refines }P.
\]

Let baseline \(B\) preserve distinctions that must already be retained. Represent the declared companion obligations by monotone, inflationary, idempotent refinement closures

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}.
\]

Define

\[
\boxed{
J=C_*(B)
=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

### J1 — conditional joint-state theorem

\(J\) is the unique coarsest partition above \(B\) fixed by all declared closures.

Proof skeleton:

1. \(\Pi(U)\) is finite and complete;
2. the join of the closure operators is a closure operator whose fixed points are the intersection of their fixed-point sets;
3. inflationarity gives \(B\preceq J\);
4. idempotence gives that \(J\) is a common fixed point;
5. any other common fixed point \(P\) above \(B\) satisfies
   \[
   J=C_*(B)\preceq C_*(P)=P.
   \]

Thus no coarser adequate state exists. For a finite world \(u\in U\),

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

### Constructive consequence

Pairwise commutation is unnecessary. Any fair repeated schedule of the closures converges to \(J\). A one-pass combination can fail because one split can expose a distinction required by another audit. The seven-world cascade witness and exhaustive partition oracle verify this explicitly.

### Claim ceiling

The generic closure/fixed-point substrate is classical. J1 is important because it tells CREST exactly when the phrase **one least-information state** is mathematically meaningful, not because least common fixed points themselves are new.

Detailed proof: `crest_joint_state_theorem_2026-08-17.md`.

### Quantitative joint-debt layer

Once \(J\) exists, CREST measures its information burden relative to the baseline:

\[
D_{\rm joint}=\log_2|J|-\log_2|B|.
\]

For each responsibility acting alone,

\[
D_i=\log_2|C_i(B)|-\log_2|B|,
\]

and

\[
\boxed{
\Delta=D_{\rm joint}-\sum_iD_i.
}
\]

A positive \(\Delta\) means that separately budgeting the responsibilities against the untouched baseline understates the state resolution needed after joint closure. The marked-cycle family gives

\[
D_1=1,
\qquad D_2=0,
\qquad D_{\rm joint}=\log_2n,
\qquad
\boxed{\Delta=\log_2n-1},
\]

so positive non-additive excess is unbounded. Conversely,

\[
D_i=0\ \forall i
\Longrightarrow
D_{\rm joint}=\Delta=0.
\]

Detailed proof and implementation:

- `docs/flagship_integration/joint_debt_delta_section.md`
- `crest/joint_debt.py`
- `tests/test_crest_joint_debt.py`

### Obstruction spectrum — direct and interaction anatomy

For every audit coalition \(S\), let \(J_S\) be its least common fixed point and define

\[
v(S)=\log_2|J_S|-\log_2|B|,
\qquad v(\varnothing)=0.
\]

Exact coalition enumeration provides the full finite obstruction spectrum. CREST reports:

- singleton debts \(D_i=v(\{i\})\);
- joint debt \(v(N)\);
- Shapley attribution of joint debt to named responsibilities; and
- Möbius/Harsanyi dividends \(m(S)\) that decompose debt by exact coalition.

Thus

\[
\boxed{
D_{\rm joint}
=
\sum_{\varnothing\ne S\subseteq N}m(S)
}
\]

and

\[
\boxed{
\Delta
=
\sum_{|S|\ge2}m(S).
}
\]

In the canonical CCOC/MLTR/MRM witness,

\[
D_{\rm joint}=1.3219280949\ \text{bit},
\]

with exact nonzero components

\[
0.5849625007_{\rm\ CCOC}
+
0.4150374993_{\rm\ CCOC\times MLTR}
+
0.3219280949_{\rm\ CCOC\times MLTR\times MRM}.
\]

So the three obstruction theories are not merely labels on parallel equations: the implemented common closure produces a measurable direct/pairwise/three-way anatomy in bits.

Detailed surface:

- `docs/crest_obstruction_spectrum_2026-09-08.md`
- `crest/obstruction_spectrum.py`
- `artifacts/crest_obstruction_spectrum.json`

### Before/after obstruction-change accounting

For two contracts on the same named responsibility set,

\[
\boxed{
\delta D_{\rm joint}
=
\sum_i\delta D_i+\delta\Delta.
}
\]

If every standalone debt is unchanged,

\[
\delta D_i=0\ \forall i,
\]

then any nonzero change in joint burden is entirely interaction-generated:

\[
\boxed{
\delta D_{\rm joint}=\delta\Delta
=
\sum_{|S|\ge2}\delta m(S).
}
\]

The comparison engine classifies change as `direct-only`, `interaction-only`, `mixed`, or `null`. It also reports `increase/decrease/unchanged` directions for joint, direct, and interaction components.

For interaction order \(k\), define

\[
M_k=\sum_{|S|=k}\delta m(S).
\]

Then

\[
\boxed{
\delta D_{\rm joint}=\sum_{k\ge1}M_k,
\qquad
M_1=\sum_i\delta D_i,
\qquad
\delta\Delta=\sum_{k\ge2}M_k.
}
\]

The canonical CCOC/MLTR/MRM activation change has

```text
source class               interaction-only
joint direction            increase
direct direction           unchanged
interaction direction      increase
active interaction orders  [2, 3]
dominant order             2
```

with

\[
M_2=+0.4150374993\ \text{bit},
\qquad
M_3=+0.3219280949\ \text{bit},
\]

and

\[
\delta D_{\rm joint}=+0.7369655942\ \text{bit}.
\]

The reverse comparison has the same source class and active orders with signs reversed. This is the finite quantitative diagnostic of representational change used by the current CREST program.

Detailed proof and implementation:

- `docs/crest_obstruction_change_accounting_2026-09-08.md`
- `docs/crest_obstruction_comparison_2026-09-08.md`
- `crest/obstruction_compare.py`
- `scripts/compare_obstruction_spectra.py`

## 4. Gate C — evidence licensing

Let \(E\) be the reliability-qualified evidence partition.

### Full-state licensing

\[
\boxed{
\text{full deterministic state report exists}
\iff
J\preceq E.
}
\]

If the condition fails, the sharp honest report is the set of \(J\)-blocks intersecting the observed evidence class.

### Target-only corollary

A requested target \(T\) can remain deterministic even if the full state is unresolved:

\[
J\not\preceq E
\quad\text{but}\quad
T\text{ factors through }E.
\]

Hence CREST keeps separate

\[
\boxed{
\text{required state},\qquad
\text{identified state},\qquad
\text{reportable target}.
}
\]

They need not coincide.

## 5. Cross-gate monotonicity — qualitative action expansion

Let controllable repertoires satisfy

\[
A_c\subseteq A_c',
\]

with old and uncontrollable dynamics preserved. Then

\[
\boxed{K^*(A_c)\subseteq K^*(A_c').}
\]

On a fixed retained carrier, if \(\Gamma'\) is an order-compatible strengthening of future responsibility \(\Gamma\), then

\[
\boxed{J_\Gamma\preceq J_{\Gamma'}.}
\]

For fixed evidence \(E\), full-state identifiability is antitone under required-state refinement:

\[
J_\Gamma\not\preceq E
\Rightarrow
J_{\Gamma'}\not\preceq E.
\]

The original strict `rescue` witness realizes

\[
\boxed{
|K^*|\uparrow,
\quad |J|\uparrow,
\quad \text{full-state identification: yes}\to\text{no},
\quad \text{target reportability: yes}\to\text{yes}.
\]

This establishes direction: more management capability can make more worlds viable while making fewer worlds scientifically interchangeable.

Detailed proof: `crest_action_expansion_cross_gate_theorem_2026-08-22.md`.

## 6. Cross-gate scale separation and the resource that controls it

### 6.1 Carrier gain alone does not bound state burden

The original connected capability–resolution family shows that for every integer \(m\ge1\), adding the single controllable action `probe` can give

\[
\boxed{
\Delta |K^*|=1,
\qquad
\Delta K_{U_0}=m\text{ bits}.
}
\]

On the retained present slice \(U_0\), the old least exact state has one class, the new least exact state has \(2^m\) classes, unchanged one-block evidence loses full-state adequacy, the monitoring-resolution debt becomes exactly \(m\) bits, and a constant coarse target remains reportable.

Hence there is no universal finite function \(f\) depending only on carrier-size gain such that

\[
\Delta K_{U_0}\le f(\Delta|K^*|).
\]

Therefore

\[
\boxed{
\text{viability gain alone cannot upper-bound representational burden.}
\]

Detailed proof: `crest_capability_resolution_divergence_theorem_2026-08-22.md`.

### 6.2 Finite counterfactual response capacity does bound state burden

For a finite response alphabet of size \(q\), action alphabet size \(a\), and counterfactual horizon \(H\), the number of complete response signatures is finite. With

\[
N_H(a)=\sum_{d=0}^{H}a^d,
\]

we have

\[
\boxed{
|J_H|\le(q+1)^{N_H(a)},
\qquad
K_H\le N_H(a)\log_2(q+1).
}
\]

The extra symbol accounts for illegality of a word. More generally, if only a finite response-test basis \(w_1,\ldots,w_r\) is needed and test \(i\) realizes \(r_i\) outcomes within an old state class, then

\[
\boxed{
\Delta K\le\sum_i\log_2r_i.
}
\]

Thus the arbitrary burden in the no-bound theorem is not free: some source of counterfactual distinguishing capacity must grow.

Detailed proof: `crest_counterfactual_response_capacity_bound_2026-09-06.md`.

### 6.3 Sharp sequential state-debt law

The response-capacity result becomes directly ecological when the new responsibility is one sequential intervention path of response-relevant depth \(H\). If stage \(h\) has at most \(r_h\) distinguishable retained outcomes, then

\[
\boxed{
\Delta K
\le
\sum_{h=1}^{H}\log_2r_h.
}
\]

For a homogeneous \(r\)-ary path,

\[
\boxed{
|J_H^+|/|J_H^-|\le r^H,
\qquad
\Delta K\le H\log_2r.
}
\]

Equivalently, generating \(k\) additional bits through an \(r\)-ary sequential channel requires at least

\[
\boxed{
H\ge\left\lceil\frac{k}{\log_2r}\right\rceil.
}
\]

This bound is sharp in one connected CREST family. The same single new action `probe`:

- rescues exactly one previously nonviable world, so \(\Delta|K^*|=1\);
- exposes one \(r\)-ary response coordinate at each of \(H\) stages;
- splits one old present state into exactly \(r^H\) present states;
- creates exactly \(H\log_2r\) bits of state information and monitoring-resolution debt;
- changes full-state licensing from yes to no under fixed one-block evidence;
- leaves a constant coarse target reportable.

Hence the full equality package is

\[
\boxed{
\Delta|K^*|=1,
\qquad
|J_H^+|/|J_H^-|=r^H,
\qquad
\Delta K=D_E=H\log_2r.
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

At every prefix depth \(d\le H\), the sharp family has exactly \(r^d\) present classes and \(d\log_2r\) bits. The operative resource is therefore **response-relevant depth × response information per stage**, not the number of new actions or newly viable worlds.

Detailed proof: `crest_sharp_sequential_state_debt_law_2026-09-06.md`.

Executable witness: `tests/test_crest_sharp_sequential_debt.py`.

## 7. Minimum monitoring refinement

For fixed evidence \(E\) and required state \(J\), define

\[
E_J^*=E\vee J.
\]

Then \(E\vee J\) is the unique coarsest evidence refinement that preserves all existing evidence distinctions and identifies \(J\). The finite monitoring-resolution debt is

\[
\boxed{
D_E(J)=\log_2|E\vee J|-\log_2|E|.
}
\]

It is nonnegative, vanishes exactly when evidence already identifies \(J\), and is monotone under required-state refinement.

The sharp sequential family gives the explicit equality

\[
\boxed{D_E=H\log_2r}
\]

under fixed one-block evidence.

Detailed proof: `crest_monitoring_resolution_debt_2026-08-21.md`.

## 8. Structural rather than merely quantitative monitoring debt

A complementary witness shows that an evidence deficit can be about measurement **type**, not only resolution. Suppose

\[
W(z)=F(z)R(z).
\]

For any positive multiplier \(a(z)\),

\[
(aF)R=F(aR).
\]

Observations depending only on net performance \(W\) cannot distinguish a change in the \(F\)-channel from a compensating change in \(R\), regardless of replication. If a newly relevant intervention acts specifically on \(F\), the latent worlds can require different state labels. The deficit is repaired by a symmetry-breaking channel, not merely by more repeated measurements of \(W\).

This remains a witness of the state/evidence architecture, not a fifth audit.

## 9. Supporting theorem infrastructure

The following remain proved and useful but are not separate philosophical headlines.

### Lift comparison

- **J2:** faithful-lift invariance.
- **J5:** one-sided refinement bounds for non-identical lifts.

### Carrier repair

- **J4:** exact universal-carrier repair characterization; NP-complete global selection.
- **J7:** exact controlled-carrier repair characterization; NP-complete global selection.

### Cross-gate obstruction

- **O1:** cheapest structural repair need not be cheapest fully evidence-licensed repair.

These protect the separation among carrier feasibility, state adequacy, and evidence licensing and belong in the full proof ledger / appendices.

## 10. Derived concepts retained as descriptions

Useful terms retained without promoting new theorem families:

- Monitoring Adequacy Envelope;
- Counterfactual Obsolescence;
- Ecological State Shadow / anticipatory state;
- Decision-Safe Ignorance;
- Monitoring Resolution Debt.

## 11. Current proof boundary

Still open:

- a canonical common carrier supplied by nature;
- infinite/continuous/stochastic trajectory analogues of the finite joint-state theorem;
- a general relation between dynamical, evolutionary, and representational stability outside the finite obstruction comparison;
- a general observation-symmetry theorem for arbitrary measurement families;
- empirical calibration of response-relevant depth \(H\), stage response cardinalities \(r_h\), and obstruction-spectrum terms in real ecological systems.

Not required for the current finite mathematical claims:

- empirical validation of a particular ecological contract;
- raw-data benchmarking against predictive-state algorithms.

The next mathematical result should enter the canonical spine only if it strengthens the carrier/state/evidence/target coupling, proves a new necessary-and-sufficient boundary, or establishes another sharp impossibility/bound that cannot be reduced to the existing theorems.
