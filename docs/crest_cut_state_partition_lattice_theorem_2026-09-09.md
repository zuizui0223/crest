# CREST cut-state partition-lattice theorem

## Setup

Fix a finite carrier \(\Omega\) and one observational cut

\[
O_t:\Omega\to Y_t,
\]

with visible partition

\[
B_t=\ker O_t.
\]

For any finite pre-state signature family \(\mathcal G\), let

\[
Q_{\mathcal G}=Q(O_t,\mathcal G)
\]

be the unique coarsest cut-state quotient preserving the cut and every signature in \(\mathcal G\).

Two families are representation equivalent when they induce the same quotient partition. Write \([\mathcal G]\) for such an equivalence class.

Let

\[
\operatorname{Ref}(B_t)
=
\{P:\ P\text{ is a partition of }\Omega\text{ and }P\text{ refines }B_t\}.
\]

## Theorem — state-space representation

The map

\[
\Phi:[\mathcal G]\mapsto Q_{\mathcal G}
\]

is a bijection from representation-equivalence classes of finite signature families onto \(\operatorname{Ref}(B_t)\).

### Proof

**Well defined.** Representation-equivalent families induce the same quotient by definition.

**Injective.** If \(\Phi([\mathcal G])=\Phi([\mathcal H])\), then \(Q_{\mathcal G}=Q_{\mathcal H}\), so \(\mathcal G\) and \(\mathcal H\) are representation equivalent.

**Image lies in \(\operatorname{Ref}(B_t)\).** Every induced state preserves the cut observation, so every state block lies within one cut block. Hence \(Q_{\mathcal G}\) refines \(B_t\).

**Surjective.** Let \(P\in\operatorname{Ref}(B_t)\). Label every world by the block of \(P\) containing it, producing one signature \(g_P\). Then \(\ker g_P=P\). Because \(P\) already refines \(B_t\), the common refinement of \(B_t\) and \(P\) is exactly \(P\). Therefore

\[
Q(O_t,\{g_P\})=P.
\]

Thus every admissible cut refinement is realizable by a finite signature family.

## Order isomorphism

Put the information order on representation classes by

\[
[\mathcal G]\preceq[\mathcal H]
\iff
Q_{\mathcal H}\text{ refines }Q_{\mathcal G}.
\]

Use the same orientation on \(\operatorname{Ref}(B_t)\): finer partitions carry weakly more distinctions. Then \(\Phi\) preserves and reflects the order. Hence the quotient space of signature representations is not merely in bijection with the cut-refinement interval; it has the same partial-order structure.

## Corollary — monotonicity under added distinctions

If \(\mathcal G\subseteq\mathcal H\), then

\[
Q_{\mathcal H}\text{ refines }Q_{\mathcal G}.
\]

Therefore the finite state complexity

\[
K(Q)=\log_2|Q|
\]

is monotone:

\[
K(Q_{\mathcal H})\ge K(Q_{\mathcal G}).
\]

Equality holds exactly when the added signatures are redundant in the sense of the signature-family invariance theorem.

## Interpretation

This gives a representation-free description of the finite CREST state space. Once the observational cut is fixed, possible cut states are exactly the refinements of the visible partition. Signature families are coordinates or generators for those states, not the states themselves.

Accordingly:

- the **visible cut** fixes the bottom of the admissible interval;
- adding scientifically retained distinctions moves upward by partition refinement;
- representation-equivalent signature families identify the same lattice element;
- redundant signatures do not move the state;
- genuinely new distinctions move to a strictly finer partition;
- state complexity is monotone along this refinement order.

The theorem does not decide which refinement is ecologically correct. It characterizes the complete finite mathematical space in which such a choice can live.

## Relation to sparse semantic access

The MLTR/MRM/CCOC construction selects one structured path through this cut-refinement space. Sparse prospective access determines how strongly the prospective component refines the retrospective-by-transverse base, yielding the existing finite formula

\[
|Q|=(N-k)+k2^m.
\]

Thus sparse semantic access is a structured cardinality result inside the more general cut-state partition lattice.
