# Positive temporal-cut bridge theorems — future-conditioned history and mechanism relevance

## Status

Exact finite bridge results following the strict companion-realizability no-go audit.

The no-go results show that the old marked-cycle activation cannot literally use an immutable MLTR history mode, and that a nontrivial fixed-grammar MRM response-type family cannot have zero standalone candidate-safe debt. The correct repair is not to make raw history or raw mechanism mutable. It is to let the **relevance equivalence** depend on the declared future/intervention grammar.

This note proves two sharp pairwise bridges:

1. MLTR x future grammar: future-conditioned history relevance can increase by exactly `m` bits;
2. MRM x future grammar: grammar-conditioned mechanism response-type relevance can increase by exactly `m` bits.

These are literal positive bridges. A genuine three-way MLTR x MRM x CCOC interaction remains open.

---

## 1. Future-conditioned history relevance

### 1.1 MLTR primitive construction

Fix a root state set

\[
S_r=\{u_0,u_1\},
\qquad
q_r(u_b)=b.
\]

Fix terminal states

\[
S_v=\{z_0,z_1,x_1,\ldots,x_m\}.
\]

For every binary word

\[
r=(r_1,\ldots,r_m)\in\{0,1\}^m,
\]

declare one root-to-terminal replacement history `p_r` whose composed relation is

\[
R_r=
\{(u_0,z_0),(u_1,z_1)\}
\cup
\{(u_{r_i},x_i):1\le i\le m\}.
\]

The two anchor pairs make every `R_r` source-total, while every terminal state is covered, so the MLTR total-relation requirement is satisfied.

The carried terminal map is

\[
c_r(z_0)=0,
\qquad
c_r(z_1)=1,
\qquad
c_r(x_i)=r_i.
\]

The complete carried maps are pairwise distinct. Therefore the full MLTR minimum-history theorem gives

\[
|H_{\min}|=2^m.
\]

That is the **full semantic preservation** requirement. CREST may ask a narrower target-specific question at one cut: which of those carried-map differences are relevant to the future tests the state is actually required to support?

### 1.2 Future grammar

Take `z_0` as the current terminal configuration. Let `probe_i` deterministically move the terminal system to `x_i`. The raw history `p_r` remains fixed; only the terminal configuration changes under a post-cut action.

For the grammar containing the first `k` probes, define the future-conditioned history profile

\[
\rho^{H}_{k}(p_r)
=
\bigl(c_r(x_1),\ldots,c_r(x_k)\bigr)
=
(r_1,\ldots,r_k).
\]

Define

\[
p_r\equiv_{H\mid k}p_s
\iff
\rho^{H}_{k}(p_r)=\rho^{H}_{k}(p_s).
\]

This is a quotient of **immutable raw histories** by the semantic distinctions reachable under the declared future contract. It is not a redefinition of the histories themselves.

### Theorem 1 — exact future-conditioned history frontier

After `k` declared binary probes,

\[
\boxed{
|H_{\min}(k)|=2^k,
\qquad
K_H(k)=k\text{ bits}.
}
\]

Hence opening the grammar from `k=0` to `k=m` forces exactly

\[
\boxed{m\text{ additional bits of history relevance}.}
\]

### Proof

Two histories are equivalent exactly when their first `k` signature bits agree. There are `2^k` possible prefixes, each realized by `2^{m-k}` histories. Therefore there are exactly `2^k` equivalence classes. Taking base-two logarithms gives `k` bits. `square`

### Relation to MLTR Paper A

For `k=m`, every addressable coordinate has been queried. Equality of the full profile is then equality of the complete carried maps in this family, so the bridge recovers the MLTR minimum-history quotient.

For `k<m`, this is intentionally **weaker** than unconditional MLTR complete-map preservation. It is a CREST target-specific quotient: histories that differ only on currently irrelevant/unreachable carried labels may be merged for the declared future task.

Thus the correct literal statement is

\[
\boxed{
\text{how much past semantic information must survive the cut can depend on the future grammar.}
}
\]

The past does not change. Its relevance equivalence does.

---

## 2. Grammar-conditioned MRM response types

### 2.1 MRM primitive construction

Let

\[
Q=\{0,1\},
\qquad
C_m=\{\theta_r:r\in\{0,1\}^m\}.
\]

Every candidate shares one `hold` action with

\[
G^{\theta_r}_{\rm hold}(q)=q.
\]

For each `i`, define

\[
G^{\theta_r}_{\mathrm{probe}_i}(q)=r_i
\qquad(q\in Q).
\]

The candidate mechanism is primitive. The MRM response type is derived only after the declared action grammar is fixed.

For the grammar with `hold` plus the first `k` probes, write

\[
\theta_r\equiv_{\Theta\mid k}\theta_s
\]

when the complete transition tables agree for all currently declared actions.

### Theorem 2 — exact grammar-conditioned mechanism frontier

After `k` probes are included in the declared intervention grammar,

\[
\boxed{
|R(k)|=2^k,
\qquad
K_\Theta(k)=k\text{ response-type bits}.
}
\]

Relative to the common fixed-candidate visible law, the mechanism ambiguity surcharge therefore rises by exactly one bit per newly declared binary probe and reaches

\[
\boxed{m\text{ bits}}
\]

when all `m` probes are legal.

### Proof

The `hold` table is identical for every candidate. The first `k` probe tables expose exactly the first `k` signature bits. Two candidates are response-equivalent under that grammar exactly when those `k` bits agree. There are `2^k` such prefixes. `square`

This is a literal MRM x future-grammar bridge and avoids the fixed-grammar no-go: the response-type equivalence is allowed to refine because the declared action set itself has changed.

---

## 3. Shared exact numerical frontier

The two bridges have the same class-count law for different reasons:

| declared binary queries `k` | relevant history classes | MRM response types | information bits |
|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 |
| 1 | 2 | 2 | 1 |
| 2 | 4 | 4 | 2 |
| 4 | 16 | 16 | 4 |
| 8 | 256 | 256 | 8 |
| 10 | 1024 | 1024 | 10 |

At `m=10`, opening the declared future/intervention grammar can therefore turn a zero-bit target-specific history or mechanism distinction into a 1024-class, 10-bit responsibility.

The arithmetic is shared; the quantifiers are not:

- history bridge: fixed raw replacement histories and carried maps, wider future reachability/query set;
- mechanism bridge: fixed candidate laws, wider intervention grammar.

---

## 4. What this repairs in the temporal-cut story

The previous abstract closure cascade used a future/latent transition that crossed an MLTR history mark. That is not needed for these pairwise bridges.

Here:

- raw history `p_r` is immutable under all post-cut queries;
- primitive mechanism candidate `theta_r` is fixed;
- only the scientific equivalence relation induced by the declared future grammar changes.

So the pairwise temporal claim now has a literal companion basis without backward causation or definitional circularity.

---

## 5. Remaining three-way problem

These two sharp pairwise bridges do **not** yet prove a genuine positive

\[
m(H,\Theta,F)
\]

for canonical MLTR, MRM, and CCOC simultaneously.

A strict simultaneous three-way theorem must specify a coupling in which:

1. MLTR histories remain immutable;
2. MRM candidate laws remain primitive and its response equivalence is grammar conditioned;
3. CCOC keeps its law-fixed quantifier rather than silently absorbing the mechanism index into raw state;
4. the common-lift compatibility/scoping is explicit; and
5. the resulting coalition value has a positive, preferably unbounded, genuine three-way Möbius dividend.

That is now the precise open theorem. The old abstract `b-log2(3)` family remains an exact CREST closure extremum, but it is not used as a substitute for this missing literal bridge.
