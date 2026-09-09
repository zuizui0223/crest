# Finite temporal-cut transport theorem

## Setup

Let \(\Omega_t\) and \(\Omega_s\) be finite world carriers at two indexed temporal cuts, with quotient states \(Q_t\) and \(Q_s\). Let

\[
\phi_{t\to s}:\Omega_t\to\Omega_s
\]

be a declared deterministic world-evolution map. No continuous-time limit is assumed.

## Theorem 1 — descent criterion

A quotient-level map

\[
\bar\phi_{t\to s}:Q_t\to Q_s,
\qquad
\bar\phi([\omega]_t)=[\phi(\omega)]_s
\]

is well defined if and only if

\[
\boxed{
\omega\sim_t\omega'
\Longrightarrow
\phi(\omega)\sim_s\phi(\omega').
}
\]

Equivalently, every source-state block is mapped entirely inside one target-state block. In partition language, \(Q_t\) refines the pullback of \(Q_s\) along \(\phi\).

### Proof

If \(\bar\phi\) is well defined and \(\omega\sim_t\omega'\), then \([\omega]_t=[\omega']_t\), so applying \(\bar\phi\) gives \([\phi(\omega)]_s=[\phi(\omega')]_s\). Thus the condition is necessary.

Conversely, assume the displayed implication. Define \(\bar\phi([\omega]_t)=[\phi(\omega)]_s\). If \([\omega]_t=[\omega']_t\), the implication gives \([\phi(\omega)]_s=[\phi(\omega')]_s\), so the definition is independent of representative. Hence \(\bar\phi\) exists.

## Corollary 1 — uniqueness

Whenever a quotient transition exists, it is unique: every source class contains a representative \(\omega\), and any commuting quotient map must send that class to \([\phi(\omega)]_s\).

## Theorem 2 — identity and composition

The identity world map descends to the identity quotient map. If

\[
\phi:\Omega_t\to\Omega_s,
\qquad
\psi:\Omega_s\to\Omega_u
\]

both descend, then \(\psi\circ\phi\) also descends and

\[
\boxed{
\overline{\psi\circ\phi}
=
\bar\psi\circ\bar\phi.
}
\]

Thus compatible finite world evolutions transport cut states functorially.

## Obstruction interpretation

Failure of the descent condition is substantive. It means that a source state class contains worlds whose evolved images occupy distinct target state classes. The source quotient therefore lacks enough distinction to support a deterministic state-level transition to that target quotient.

This is not repaired by choosing a representative of the source class: doing so would make the purported state transition representation-dependent.

## Scope firewall

This theorem does **not** claim:

- that every ecological process admits a deterministic world map;
- that state cardinality must increase or decrease with time;
- that \(\log_2|Q_t|\) is temporally monotone;
- a stochastic or multivalued quotient theorem;
- a shrinking-window or continuous-time germ limit.

It only characterizes when two already-defined finite cut states can be connected by a well-defined deterministic quotient transition.
