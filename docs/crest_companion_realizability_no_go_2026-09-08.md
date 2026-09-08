# CREST companion-realizability audit — strict temporal semantics and no-go results

## Status

Exact finite claim-control theorem for the temporal-cut flagship.

This note does **not** retract the CREST closure theorems. The existing formulas

\[
m(H,F)=\log_2 n-1
\]

and

\[
m(H,\Theta,F)=b-\log_2 3
\]

remain exact for the declared refinement-closure families. The question here is stricter:

> Can those same sharp cascades already be interpreted literally as canonical MLTR history, canonical fixed-grammar MRM response type, and canonical law-fixed CCOC future responsibility on one common temporal carrier?

The answer for the current cascades is **no**. Two finite no-go theorems identify why and therefore locate the actual bridge theorem still required.

---

## 1. Primitive companion semantics

The companion definition firewalls fix the following dependency order before CREST constructs the final state.

### MLTR

A raw history is a declared root-to-terminal replacement path `p`. A fixed root law and the composed replacement relation give the carried terminal map `c_p`. The minimum history mode is the equality class of the complete carried map.

Once the terminal cut is reached, this path/history mode is retrospective information. Right-of-cut interventions do not rewrite which replacement route occurred.

### MRM

A primitive candidate mechanism `theta` induces declared transition maps

\[
G_a^\theta:Q\to Q.
\]

Response types are the quotient of candidate mechanisms by equality of the complete transition table under the fixed declared action set. Typed MRM dynamics preserve the response-type coordinate.

### CCOC

A controlled law `M=(S,A,T,h)` is fixed and the future grammar `L` is declared. CCOC compares raw configurations under that one law through their legal future response profiles. The future grammar is a query responsibility, not a mechanism coordinate.

These definitions are individually non-circular. The issue below is simultaneous realization of the **sharp activation pattern**.

---

## 2. Fixed quotients cannot produce positive interaction on a one-class cut

Suppose one visible cut block contains all worlds and every responsibility contributes only a fixed precomputed partition

\[
P_1,\ldots,P_k.
\]

Their joint state is the common refinement. If `n_i=|P_i|`, then every joint block is identified by one tuple of individual block labels, so

\[
|P_{\rm joint}|\le \prod_i n_i.
\]

Therefore

\[
\log_2|P_{\rm joint}|-\sum_i\log_2|P_i|\le0.
\]

Hence:

\[
\boxed{\text{positive one-cut interaction requires state-dependent obligations, not merely intersecting fixed companion quotients.}}
\]

This explains why CREST uses closure operators rather than only precomputed partitions. It also means that a literal companion bridge must specify how each companion obligation acts **relative to distinctions already retained by the joint state**.

---

## 3. The immutable-history no-activation theorem

Let `B` be the indiscrete present-cut partition. Let `H` be a retrospective history label on the world carrier. Let `C_F` be a post-cut deterministic refinement audit.

Assume:

1. `C_F(B)=B`; that is, the future audit has zero standalone debt on the visible cut;
2. every legal post-cut transition preserves raw history:
   \[
   H(\tau_a(w))=H(w);
   \]
3. the audit's static labels and legal-action rows are already compatible with the one-block baseline, as forced by condition 1.

### Theorem

The history partition `P_H` is fixed by the future audit:

\[
\boxed{C_F(P_H)=P_H.}
\]

### Proof

Take two worlds in the same `H` block. Condition 1 implies that the future audit cannot distinguish them on the indiscrete baseline through static labels or action legality. For every legal action, condition 2 sends both successors into the same history block as their respective source block. Because the two sources share the same history label, their successors also share one `P_H` block. Their complete refinement signatures relative to `P_H` therefore agree. No pair inside one history block is split, so `P_H` is already a fixed point. `square`

### Consequence

A zero-debt post-cut future audit cannot be **activated by immutable history alone**.

The current CREST marked-cycle `H x F` witness violates exactly this strict temporal premise: the closing future transition enters the singled-out history-marked world from an unmarked world. The abstract closure witness is valid, but its mark is not a literal immutable MLTR replacement-history mode.

Thus the statement

> how much of the past must survive can depend on the future

still motivates a bridge theorem, but the present marked-cycle proof does not yet establish it under strict MLTR history semantics.

---

## 4. Fixed-grammar MRM zero-debt no-go

Let `R` be the MRM response-type set for a fixed observable state set `Q` and fixed declared action set `A`. The typed dynamics are

\[
T_a(q,r)=(G_a^r(q),r).
\]

Let `P_Q` be the partition of `Q x R` by the visible `q` coordinate.

### Theorem

If `P_Q` is already candidate-safe, then

\[
\boxed{|R|=1.}
\]

### Proof

Candidate safety of `P_Q` means that for every visible state `q`, action `a`, and pair of retained response types `r,r'`, the successors remain in the same visible block. Therefore

\[
G_a^r(q)=G_a^{r'}(q)
\]

for all `q,a,r,r'`. All complete response tables are identical. By the MRM definition of response type, all candidates belong to one response type. `square`

### Consequence

Under a **fixed intervention grammar**, a nontrivial MRM response-type family cannot have zero standalone candidate-safe debt and later become nontrivial merely because another state partition was added.

The current CREST three-way sharp family has an abstract latent-present audit with zero standalone debt but a positive later activation. That closure is therefore not yet a literal fixed-grammar MRM candidate-safe quotient.

A literal MRM x future bridge can instead arise when the **declared intervention grammar changes**, because the response-type equivalence itself is grammar conditioned. That is a different construction and is the correct direction for the next positive bridge theorem.

---

## 5. Audit of the current sharp families

### Pairwise family

The abstract family has

\[
D_H=1,\qquad D_F=0,\qquad D_{HF}=\log_2 n.
\]

Its future cycle is inert on the one-block baseline, but the cycle does not preserve the static history mark: one legal future transition crosses from the unmarked class into the marked seed. Therefore it fails the immutable-history premise above.

### Three-way family

The abstract family has

\[
D_H=1,\qquad D_\Theta=D_F=0,
\]

and

\[
m(H,\Theta,F)=b-\log_2 3.
\]

Its latent activation edge similarly enters the history seed from a differently history-labelled world. In addition, the zero-standalone/nontrivial-later latent audit cannot be identified with a canonical fixed-grammar MRM response-type family by the MRM theorem above.

Therefore:

\[
\boxed{\text{the current sharp temporal cascades are exact CREST closure witnesses, but not yet strict simultaneous MLTR x MRM x CCOC realizations.}}
\]

---

## 6. What remains proved

The following results remain untouched:

1. the finite least-common-fixed-point CREST state theorem;
2. the generic non-additive debt `Delta`;
3. the exact marked-cycle closure extremum `log2(n)-1`;
4. the exact three-audit closure extremum `b-log2(3)`;
5. the 1024-class / 10-bit / 8.415-bit numerical calculations;
6. the non-circular primitive dependency DAG for the companion definitions.

What changes is the **interpretation boundary**. The numerical sharp families may be called `history-role`, `latent-response-role`, and `future-role` closure families. They must not yet be described as a literal simultaneous execution of the canonical MLTR, MRM, and CCOC models.

---

## 7. The actual bridge problem

There are two mathematically clean routes forward.

### Route A — contract-conditioned relevance

Let the future grammar condition which historical carried-map differences and which mechanism response-table differences are scientifically relevant. Examples include:

- a CCOC grammar-conditioned quotient of MLTR carried maps restricted to future-reachable tests;
- an MRM response-type equivalence indexed by the declared intervention grammar.

This preserves the immutability of raw history while allowing the **relevance equivalence** on histories or mechanisms to change when the future contract changes.

### Route B — scoped/fibered common-lift closures

A common carrier may contain different mechanism-law fibers. CCOC must compare configurations **within one fixed-law fiber**, whereas MRM compares **across law fibers** at fixed visible configuration. A correct lifted closure must preserve this quantifier scoping rather than treating the mechanism index as an ordinary CCOC raw-state coordinate.

The existing CREST-J3 maximal-common-lift theorem begins after an ambient synchronization has been declared and explicitly lists construction of that synchronization from arbitrary CCOC/MLTR/MRM objects as an open problem. The present no-go explains why that construction cannot be a naive product partition.

---

## 8. Publication firewall

Until a positive bridge theorem is proved, the flagship should distinguish:

- **proved:** unbounded interaction among abstract state-dependent temporal-role closures;
- **proved:** MLTR, MRM, and CCOC primitive definitions are individually non-circular;
- **proved:** strict immutable-history and fixed-grammar MRM conditions rule out the current literal cascade interpretation;
- **open:** a simultaneous canonical companion realization with an unbounded genuine three-way interaction.

This boundary is stronger than leaving the relation implicit: it identifies the exact premise that a future positive theorem must relax or enrich.
