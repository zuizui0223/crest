# Least temporal-cut quotient theorem

## Setup

Let \(\Omega\) be a nonempty finite carrier and let

\[
O_t:\Omega\to Y
\]

be the observation map at one temporal cut. Let

\[
g_i:\Omega\to Z_i,\qquad i\in I,
\]

be any finite family of pre-state signatures. A signature may represent retrospective carried meaning, transverse latent-present response type, a context-conditioned prospective trace, or any other distinction declared independently of the final state.

Define

\[
\omega\sim_*\omega'
\iff
O_t(\omega)=O_t(\omega')
\quad\text{and}\quad
g_i(\omega)=g_i(\omega')\ \text{for every }i\in I.
\]

Let \(q_*:\Omega\to Q_*:=\Omega/{\sim_*}\) be the quotient map.

## Theorem — least cut-state quotient

The quotient \(q_*\) has three properties.

1. **Preservation.** The visible observation and every declared signature factor through \(q_*\). Thus there exist maps \(\bar O_t\) and \(\bar g_i\) such that

   \[
   O_t=\bar O_t\circ q_*,
   \qquad
   g_i=\bar g_i\circ q_*.
   \]

2. **Leastness.** If another quotient \(r:\Omega\to R\) also preserves \(O_t\) and every \(g_i\), then \(r\) refines \(q_*\). Equivalently, there is a unique map \(h:R\to Q_*\) satisfying

   \[
   q_*=h\circ r.
   \]

3. **Uniqueness up to relabeling.** Any quotient satisfying preservation and the leastness property has exactly the same blocks as \(q_*\), differing at most by names assigned to quotient classes.

Hence \(Q_*\) is the unique least-information state compatible with the declared cut observation and pre-state signatures.

## Proof

For preservation, if two worlds lie in the same \(q_*\)-class, the definition of \(\sim_*\) gives equality of \(O_t\) and of every \(g_i\). Each of those maps is therefore constant on every quotient class, which is exactly the finite factorization criterion.

For leastness, suppose \(r(\omega)=r(\omega')\). Because \(O_t\) and all \(g_i\) factor through \(r\), equality under \(r\) implies

\[
O_t(\omega)=O_t(\omega')
\]

and

\[
g_i(\omega)=g_i(\omega')\quad\forall i.
\]

Therefore \(\omega\sim_*\omega'\), so every \(r\)-class lies inside one \(q_*\)-class. Thus \(r\) refines \(q_*\), and the map \(h\) sending each \(r\)-class to its containing \(q_*\)-class is well defined and unique.

If \(q'\) also satisfies the same universal property, leastness of \(q_*\) implies \(q'\) refines \(q_*\), while leastness of \(q'\) implies \(q_*\) refines \(q'\). Their partitions are therefore identical.

## Why this removes circularity

The final state does not define the signatures. The dependency direction is

\[
(O_t,\{g_i\}_{i\in I})
\longrightarrow
\sim_*
\longrightarrow
Q_*.
\]

The investigator may choose which scientific signatures enter the theorem, but after those signatures are fixed the quotient is not freely chosen. It is forced by the universal property above.

This separates two questions that should not be conflated:

- **semantic/model validity:** whether the chosen \(g_i\) are justified representations of the scientific distinctions of interest;
- **quotient mathematics:** given those \(g_i\), which cut-state is minimally sufficient.

CREST can prove the second exactly. The first requires companion theory, ecological interpretation, or empirical evidence outside this finite set-theoretic theorem.

## Specialization to v0.7 sparse semantic access

For the current canonical finite witness, take the visible cut to be one coarse observation class and choose three signatures:

- \(g_H\): MLTR carried-semantic history mode;
- \(g_\Theta\): MRM candidate-safe response type;
- \(g_F\): the context-conditioned prospective trace, equal to the exterior response signature on addressable history-by-response pairs and to one `INACCESSIBLE` symbol otherwise.

The least common refinement of these three kernels is exactly the semantic trace quotient computed in `crest.semantic_temporal_quotient`.

If there are \(N\) history-by-response semantic pairs, \(k\) are prospectively addressable, and each addressable pair exposes \(2^m\) exterior signatures, this specialization has

\[
|Q_*|=(N-k)+k2^m.
\]

Thus the sparse-access formula is not the definition of state. It is a closed-form cardinality theorem for one structured specialization of the general least cut-state quotient.

## Scope

This theorem is finite and exact. It proves neither that a chosen companion signature is ecologically correct nor that a continuous-time shrinking-window limit exists. The zero-duration cut is a primitive finite idealization in the present theory.
