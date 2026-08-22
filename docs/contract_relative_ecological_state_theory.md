# Contract-Relative Ecological State Theory (CREST)

> **Canonical philosophical statement.** CREST is organized from ecological worlds to state representations, not from four companion audits upward. Technical finite theorem details live in [`crest_mathematical_spine.md`](crest_mathematical_spine.md) and the proof ledger.

## 1. The starting point: world before state

CREST begins from the fact that an ecological system need not be well represented as a point moving under one fixed, context-free rule. Ecological interaction, environmental change, stochasticity, and evolution can alter the response structure that determines what happens next.

The theory therefore treats a possible ecological world schematically as

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where:

- \(h_t\) is relevant history;
- \(x_t\) is present configuration;
- \(\mathcal F_t\) is the future-response structure under the interactions and interventions relevant to the scientific problem.

For stochastic systems, \(\mathcal F_t\) can be a conditional distribution over possible future paths rather than one predetermined future.

This framing does not assert a block-universe ontology, determinism, or one globally increasing fitness function. Its purpose is narrower: **a scientific state may need to summarize temporally extended distinctions even when the researcher observes only a present snapshot.**

## 2. The central question

CREST asks:

> **Which differences among possible ecological worlds may science safely ignore when those worlds are assigned the same ecological state?**

A state is therefore a compression. Calling two worlds the same state makes the commitment

\[
\boxed{
\text{every difference erased by the state is irrelevant to the work assigned to it.}
}
\]

The central working definition is:

\[
\boxed{
\text{ecological state}
=\text{ scientifically licensed equivalence class of ecological worlds.}
}
\]

Equivalently, under context \(V\) and contract \(\mathcal C\),

\[
\operatorname{State}_{\mathcal C,V}(\omega)
=[\omega]_{\sim_{\mathcal C,V}}.
\]

The current finite implementation realizes this idea on declared finite latent-world sets. A general continuous/stochastic trajectory theorem is not yet claimed.

## 3. Scientific access is not the world itself

Science does not observe \(\omega\) directly. An observation/intervention context \(V\) determines what is accessible, schematically

\[
O_V:\Omega\to Y_V.
\]

Changing \(V\) can change which worlds are observationally or experimentally distinguishable without changing the underlying ecological dynamics.

The scientific contract is written

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where:

- \(\Gamma\): future interactions, operations, or interventions the state must survive;
- \(\mathcal H\): inherited meanings or historical structure that must remain coherent;
- \(\Theta\): retained response mechanisms or causal alternatives;
- \(D\): experiment, observation, reliability, and evidence contract;
- \(T\): requested report or decision target.

State identity is **context- and contract-relative but not arbitrary**. The researcher declares the task; dynamics, causal structure, and evidence determine whether a proposed merge survives it.

## 4. Snapshot sufficiency

Let \(X(\omega)\) denote the present ecological snapshot. The snapshot is sufficient for a declared CREST state exactly when the required state factors through \(X\):

\[
\boxed{
X(\omega)=X(\omega')
\Longrightarrow
q_{\mathcal C,V}(\omega)=q_{\mathcal C,V}(\omega').
}
\]

If there exist \(\omega,\omega'\) with

\[
X(\omega)=X(\omega')
\quad\text{but}\quad
q_{\mathcal C,V}(\omega)\neq q_{\mathcal C,V}(\omega'),
\]

then the present snapshot is not a sufficient state for that contract.

This criterion is deliberately conditional. CREST does not claim that snapshots are always insufficient; it makes snapshot sufficiency something to demonstrate rather than assume.

## 5. Three structural ways snapshot sufficiency can fail

The companion theorem programs are best read as obstruction theories below the world-level definition.

### 5.1 Future insufficiency — CCOC

Two worlds can share one present description yet differ in a distinction exposed only when a future interaction, connection, colonization route, or intervention becomes relevant.

\[
\boxed{
\text{present functional equivalence}
\not\Rightarrow
\text{open-future causal equivalence}
}
\]

CCOC quantifies how opening the future grammar can force a finer causal interface.

### 5.2 Historical / semantic insufficiency — MLTR

An inherited category can remain syntactically available after turnover or replacement while losing exact operational meaning. Different histories or structural replacements can require the old macrostate to split.

MLTR asks for the least exact repair of an inherited classification while preserving as much carried meaning as possible.

### 5.3 Mechanistic insufficiency — MRM

The same visible state can remain compatible with several latent response mechanisms. CREST does not preserve full mechanism identity. A mechanism difference becomes state-relevant only when it changes a required future response or report.

Thus CCOC, MLTR, and MRM explain three different reasons why equal present snapshots can fail to imply equal required states.

## 6. Evidence licensing is a second-stage problem — CED

A required distinction can exist in the ecological model without being identified by current evidence.

CED therefore sits after representational adequacy and separates

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{target report}
}
\]

in general.

Finite observation, detection failure, common-mode error, or an observation map that collapses causal channels can leave several required states compatible with one record.

This distinction is important: CED does not create the underlying world difference. It audits whether the scientific record licenses a claim about distinctions required elsewhere in CREST.

## 7. The finite CREST construction

Conditional on one admissible finite common carrier \(U\), let the declared requirements induce monotone, inflationary, idempotent refinement closures on the partition lattice of \(U\). In the current implementation these are represented as

\[
C_\Gamma,\quad C_\mathcal H,\quad C_\Theta,\quad C_{D,T}.
\]

From baseline partition \(B\), CREST-J1 constructs

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

Then \(J\) is the unique coarsest / least-information partition satisfying the declared finite requirements. For latent world \(u\),

\[
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

The generic lattice machinery is classical. The CREST content is the ecological interpretation of which world distinctions must survive the quotient and the explicit separation of required state from evidential identification.

## 8. Three finite gates

The current theorem package separates three questions.

### Gate A — carrier feasibility

Can the declared world descriptions and requirements be synchronized on one admissible finite carrier?

J3/J6 address this under universal and controlled action semantics. Failure means that no fully adequate common finite state exists under the declared contract.

### Gate B — representational adequacy

If a carrier exists, what is the least-information partition preserving all required distinctions?

That state is \(J\).

### Gate C — evidential licensing

Does the observation contract identify which \(J\)-block is occupied?

For evidence partition \(E\),

\[
\boxed{
\text{full deterministic state report exists}
\iff
J\preceq E.
}
\]

A target can remain reportable even when this condition fails.

## 9. Ecological rules as quotient laws

CREST also reframes what an ecological rule is doing.

Suppose a state quotient merges worlds according to \(\sim_{\mathcal C,V}\). A rule is well-defined on that quotient only if worlds in the same block agree on every response the rule is required to return.

Therefore:

\[
\boxed{
\text{many ecological rules are effective laws of an adequate quotient,
not necessarily laws of the full latent world.}
}
\]

Changing scale, observation channel, intervention repertoire, or structural context can invalidate the old quotient for a new task without making the original rule false in its original domain.

This is not epistemic relativism. The dynamics constrain whether the proposed coarse law is well-defined.

## 10. Counterfactual futures can change the present scientific state

A newly available management action can expose a response distinction between worlds previously treated as equivalent.

The action need not yet be executed. Its inclusion in the scientific contract can already force \(J\) to refine.

Under the existing finite action-expansion result, one can have

\[
|K^*|\uparrow,
\qquad
|J|\uparrow,
\qquad
\text{full-state identifiability}\downarrow,
\]

while target reportability remains unchanged.

Thus:

> **The future does not have to happen to change the present scientific state; a counterfactual future need only become relevant to what the state is required to support.**

This is representational, not backward, causation.

## 11. Dynamical, evolutionary, and representational stability

CREST distinguishes three questions that should not be collapsed.

1. **Dynamical stability:** does the ecological system resist or recover from perturbation?
2. **Evolutionary stability:** does a strategy or trait resist invasion under the relevant evolutionary model?
3. **Representational stability:** does the same state quotient remain adequate when the scientific context changes?

The existing action-expansion witness proves one strict separation: the ecological system can remain physically unchanged while the scientifically adequate state becomes finer.

A general theory connecting all three forms of stability remains future work.

## 12. Monitoring debt can be structural

For fixed evidence partition \(E\) and required state \(J\), the unique coarsest evidence refinement that preserves existing evidence distinctions and identifies \(J\) is

\[
E\vee J.
\]

The finite resolution debt is

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

But this does not mean only "collect more samples." If two latent mechanisms produce the same observed net channel, repeated measurement of that same channel may preserve the observational symmetry. A new discriminating measurement type can be necessary.

## 13. What CREST does not claim

CREST does not establish:

- a nature-given canonical ecological partition;
- a unique common carrier for every scientific description;
- that every present snapshot is insufficient;
- that all biological evolution maximizes one global fitness function;
- that stochasticity disappears at the ecological level;
- that ecosystems are generically mathematically chaotic;
- that CCOC, MLTR, MRM, and CED exhaust every possible source of state inadequacy;
- that finite state-memory bits equal money, sensors, or field effort;
- a general infinite, continuous, stochastic, approximate, or delayed-observation trajectory theorem.

The trajectory-first framing is the organizing interpretation of the current finite latent-world theory, not a silent upgrade of interpretation into an unproved theorem.

## 14. Canonical progression

```text
self-modifying ecological world
        ↓
temporally extended possible worlds
        ↓
observation / intervention context
        ↓
snapshot sufficiency question
        ↓
structural obstructions
    CCOC / MLTR / MRM
        ↓
least-information adequate state
        ↓
evidence licensing
    CED
        ↓
quotient laws, reportability, and representational stability
```

See:

- [`crest_ecological_projection.md`](crest_ecological_projection.md) for the ecology-facing interpretation;
- [`crest_mathematical_spine.md`](crest_mathematical_spine.md) for the proved finite theorem hierarchy; and
- [`README.md`](../README.md) for the canonical repository entry point.
