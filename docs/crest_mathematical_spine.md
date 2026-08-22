# CREST mathematical spine

> **Purpose:** distinguish the mathematics needed to answer the central philosophical question from supporting theorem infrastructure.

## 1. One question, three gates

The mathematical task is not to maximize theorem count. It is to answer:

> Given a declared scientific contract, when can one ecological state exist, what is the least-information such state, and when does evidence identify it?

The main proof chain is:

```text
Gate A: admissible common carrier?
        ↓
Gate B: unique least-information joint state?
        ↓
Gate C: evidence identifies that state?
        ↓
Cross-gate: how do those answers change when management/future contracts expand?
```

## 2. Gate A — carrier feasibility

The four companion obligations do not automatically live on the same latent world set. CREST therefore separates state construction from carrier existence.

### Universal carrier — J3

For static-compatible worlds `W0` and partial deterministic actions, define the universal predecessor operator

\[
F(S)=\{w\in S\cap W_0:\tau_a(w)\downarrow\Rightarrow\tau_a(w)\in S\text{ for every declared }a\}.
\]

Descending iteration yields the greatest universally transition-closed carrier \(U^*\).

Core statement:

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

Descending iteration yields the greatest robustly controlled-invariant carrier \(K^*\).

Core statement:

\[
\boxed{
\text{nonempty controlled common carrier exists}
\iff
K^*\neq\varnothing.
}
\]

Every nonempty \(K^*\) admits a memoryless safe selector in the finite deterministic setting.

### Why Gate A is conceptually necessary

An empty or coverage-incomplete carrier is not a failure to find the right partition. It says the declared scientific obligations cannot all be represented on one admissible world set without changing the contract.

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

Let baseline \(B\) preserve distinctions that must be retained before the four audits. Assume each companion obligation is represented by a monotone, inflationary, idempotent refinement closure:

\[
C_\Gamma,\ C_\mathcal H,\ C_\Theta,\ C_{D,T}.
\]

Define their closure join \(C_*\) and

\[
\boxed{
J=C_*(B)
=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

### J1 theorem

\(J\) is the unique coarsest partition above \(B\) fixed by all four closures.

Proof skeleton:

1. the partition lattice is finite and complete;
2. the join of closure operators is a closure operator whose fixed points are the intersection of their fixed-point sets;
3. inflationarity gives \(B\preceq J\);
4. idempotence gives that \(J\) is a common fixed point;
5. if \(P\) is any common fixed point above \(B\), monotonicity yields
   \[
   J=C_*(B)\preceq C_*(P)=P.
   \]

Thus no coarser adequate state exists.

### Constructive consequence

Pairwise commutation is unnecessary. Any fair repeated schedule of the four closures converges to \(J\) on the finite carrier. A one-pass combination can fail because one audit's split can expose a distinction required by another audit.

The seven-world cascade witness and exhaustive partition oracle verify this interaction explicitly.

Detailed proof: `crest_joint_state_theorem_2026-08-17.md`.

## 4. Gate C — evidence licensing

Let \(E\) be the reliability-qualified evidence partition: two worlds share one evidence block when the declared observation/experiment cannot distinguish them.

### Full-state licensing theorem

\[
\boxed{
\text{full deterministic state report exists}
\iff
J\preceq E.
}
\]

Proof skeleton:

- if \(J\preceq E\), each evidence block lies within one \(J\)-block, so the state label factors through evidence;
- conversely, any evidence-measurable adequate state \(P\) must satisfy
  \[
  J\preceq P\preceq E,
  \]
  hence \(J\preceq E\).

If the condition fails, the sharp honest report is the set of \(J\)-blocks intersecting the observed evidence class.

### Target-only corollary

A target \(T\) can still be deterministic when the full state is unresolved:

\[
J\not\preceq E
\quad\text{but}\quad
T\text{ factors through }E.
\]

This is why CREST distinguishes state identification from decision/report sufficiency.

## 5. Cross-gate theorem — action expansion

This is the main non-obvious ecological result currently derived from the spine.

Let controllable repertoires satisfy

\[
A_c\subseteq A_c',
\]

with old and uncontrollable dynamics preserved. Then controlled-carrier monotonicity gives

\[
\boxed{K^*(A_c)\subseteq K^*(A_c').}
\]

On a fixed retained carrier, let \(\Gamma'\) be an order-compatible strengthening of future responsibility \(\Gamma\). Then

\[
\boxed{J_\Gamma\preceq J_{\Gamma'}.}
\]

For fixed evidence \(E\), full-state identifiability is antitone under required-state refinement:

\[
J_\Gamma\not\preceq E
\Rightarrow
J_{\Gamma'}\not\preceq E.
\]

The strict `rescue` witness realizes

\[
\boxed{
|K^*|\uparrow,
\quad |J|\uparrow,
\quad \text{full-state identification: yes}\to\text{no},
\quad \text{target reportability: yes}\to\text{yes}.
}
\]

So management capability can expand the domain that becomes viable while shrinking the equivalence relation that is scientifically safe.

Detailed proof: `crest_action_expansion_cross_gate_theorem_2026-08-22.md`.

## 6. Minimum monitoring refinement

For fixed evidence \(E\) and required state \(J\), define the common refinement

\[
E_J^*=E\vee J.
\]

### R1

\(E\vee J\) is the unique coarsest evidence refinement that:

1. preserves all distinctions already present in \(E\); and
2. identifies \(J\).

Therefore the finite monitoring-resolution debt is

\[
\boxed{
D_E(J)=\log_2|E\vee J|-\log_2|E|.
}
\]

It is nonnegative, vanishes exactly when evidence already identifies \(J\), and is monotone when the required state refines.

Detailed proof: `crest_monitoring_resolution_debt_2026-08-21.md`.

## 7. Structural rather than merely quantitative monitoring debt

A useful ecological witness comes from a positive channel factorization

\[
W(z)=F(z)R(z).
\]

For any positive multiplier \(a(z)\),

\[
(aF)R=F(aR).
\]

Thus observations depending only on net performance \(W\) cannot distinguish a change in the \(F\)-channel from the corresponding change in the \(R\)-channel, no matter how often \(W\) is remeasured.

If a newly admissible intervention acts specifically on \(F\), the two latent worlds can have different future successors and must split in the required state. The evidence deficit is then repaired by a symmetry-breaking measurement channel, such as observing \(W\) together with \(F\), not by additional net-only replication.

The CREST repository tests this as an ecology-grounded witness of the existing state/evidence architecture; it is not a new fifth audit.

## 8. Supporting theorem infrastructure

The following results remain proved and important but are **supporting**, not headline answers to the philosophical question.

### Lift comparison

- **J2:** faithful-lift invariance.
- **J5:** one-sided refinement bounds for non-identical lifts.

Role: verify that scientifically invisible latent duplication does not create fake state complexity and describe one-sided changes when a lift is stronger or weaker.

### Carrier repair

- **J4:** exact universal-carrier repair characterization; NP-complete global selection.
- **J7:** exact controlled-carrier repair characterization; NP-complete global selection.

Role: characterize what must be changed when Gate A fails under a declared repair language.

### Cross-gate obstruction

- **O1:** cheapest structural repair need not be cheapest fully evidence-licensed repair.

Role: prevent collapse of carrier feasibility, state adequacy, and evidence licensing into one optimization problem.

These results belong in the full proof ledger and appendices, not in the conceptual headline.

## 9. Derived concepts retained as descriptions, not theorem families

The repository retains the following useful derived language:

- Monitoring Adequacy Envelope;
- Counterfactual Obsolescence;
- Ecological State Shadow / anticipatory state;
- Decision-Safe Ignorance;
- Monitoring Resolution Debt.

Their underlying order/refinement facts are proved, but they should not be presented as independent discoveries unless a future result adds a genuinely new coupling or impossibility.

## 10. Current proof boundary

Not yet proved:

- a canonical common carrier supplied by nature;
- an infinite/continuous/stochastic trajectory version of J1;
- a general theorem that a present snapshot is insufficient;
- a general relation between dynamical, evolutionary, and representational stability;
- an observation-symmetry theorem for arbitrary measurement families;
- empirical validity of any declared ecological contract.

The next mathematical result should be added only if it strengthens the one-question spine rather than creating another parallel vocabulary family.
