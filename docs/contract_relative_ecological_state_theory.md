# Contract-Relative Ecological State Theory (CREST)

> **Canonical philosophical statement.** Technical theorem details live in
> [`crest_mathematical_spine.md`](crest_mathematical_spine.md) and the proof ledger.

## 1. The question

CREST is organized around one question:

> **What counts as the same ecological state?**

A state label is useful only because it treats many different ecological configurations as equivalent. Calling two configurations the same state therefore makes a scientific commitment:

\[
\boxed{
\text{the differences erased by the state will not matter for the work assigned to it.}
}
\]

CREST asks when that commitment is justified.

The scientific contract is written schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where:

- \(\Gamma\): future interactions, operations, or interventions the state must survive;
- \(\mathcal H\): inherited meanings or historical structure that must remain coherent;
- \(\Theta\): retained response mechanisms or causal alternatives;
- \(D\): experiment, observation, reliability, and evidence contract;
- \(T\): the report or decision target.

State identity is therefore **contract-relative but not arbitrary**. Scientists declare the work; dynamics, causal structure, and evidence can refute a proposed merge.

## 2. Four obligations on one ecological state

The four companion programs identify four distinct ways that ecological sameness can fail.

### Future sufficiency — CCOC

Two configurations may be indistinguishable under every currently legal future yet behave differently after colonization, reconnection, a newly available interaction, or a new intervention.

\[
\boxed{
\text{present functional equivalence}
\not\Rightarrow
\text{open-future causal equivalence}
}
\]

CCOC asks which distinctions must be retained so that a state remains exact under the declared future grammar.

### Semantic coherence — MLTR

An ecological category may remain syntactically available after structural turnover while no longer preserving its old operational meaning. Pollinator replacement, species turnover, network rewiring, or restoration can make an inherited state label too coarse.

MLTR asks how much an inherited classification must be refined to remain exact while preserving as much carried meaning as possible.

### Mechanism robustness — MRM

The same visible state can remain compatible with multiple latent mechanisms. Those mechanism differences need not always be represented. They become state-relevant exactly where retained mechanisms disagree about a future response that the state is required to support.

Thus CREST does not equate ecological state with full mechanism identity. It preserves **response-relevant latent distinctions**.

### Evidential licensing — CED

A distinction can be required by the scientific model without being identified by the current field evidence. Finite observation, detection failure, common-mode error, or an observation map that collapses causal channels can leave several required states compatible with one record.

CED separates:

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

## 3. The CREST answer

Conditional on one admissible finite common carrier \(U\), let the four obligations induce monotone, inflationary, idempotent refinement closures on the partition lattice of \(U\):

\[
C_\Gamma,\quad C_\mathcal H,\quad C_\Theta,\quad C_{D,T}.
\]

From a baseline partition \(B\), CREST-J1 defines

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
}
\]

Then \(J\) is the unique coarsest / least-information partition satisfying all four obligations. For a latent world \(u\),

\[
\boxed{
\operatorname{State}_{\mathcal C}(u)=[u]_J.
}
\]

So the CREST answer is:

> **Two ecological configurations count as the same state exactly to the extent that the declared scientific contract permits all differences between them to be ignored.**

The generic lattice machinery is classical. CREST's content is the ecology-specific mapping of future, inherited meaning, mechanism uncertainty, and evidence onto one state-adequacy problem.

## 4. Three gates, not one ontology

The mathematical program separates three questions that ecological practice often collapses.

### Gate A — carrier feasibility

Can the four obligations even be synchronized on one admissible world set?

J3/J6 answer this under universal and controlled action semantics. Failure here means that a fully adequate common state does not exist under the declared contract.

### Gate B — representational adequacy

If an admissible carrier exists, what is the least-information state that preserves every required distinction?

That state is \(J\).

### Gate C — evidential licensing

Does the observation contract identify which \(J\)-block is occupied?

For evidence partition \(E\),

\[
\boxed{
\text{full-state report exists}
\iff
J\preceq E.
}
\]

A target can still be reportable when this condition fails.

## 5. The non-obvious ecological consequence

The strongest current CREST result is not merely that state depends on purpose.

A newly available management action can make **more ecological worlds viable** while simultaneously making **fewer worlds scientifically interchangeable**.

Under the assumptions of the action-expansion result,

\[
A_c\uparrow
\Rightarrow
K^*\uparrow,
\]

while a strengthened future contract can force

\[
J\text{ to refine}.
\]

A strict finite witness realizes

\[
\boxed{
|K^*|\uparrow,
\qquad
|J|\uparrow,
\qquad
\text{full-state identifiability}\downarrow,
\qquad
\text{target reportability unchanged}.
}
\]

The intervention need not yet have been executed. Its availability can already change which latent differences the present state must preserve.

This is the core of **management-induced information debt**.

## 6. Monitoring debt can be structural

For fixed evidence partition \(E\) and required state \(J\), the unique coarsest evidence refinement that preserves existing evidence distinctions and identifies \(J\) is

\[
E\vee J.
\]

The finite resolution debt is

\[
D_E(J)=\log_2|E\vee J|-\log_2|E|.
\]

But this debt should not be read only as "collect more samples."

Suppose a net ecological performance factorizes as

\[
W(z)=F(z)R(z),
\]

where \(F\) is a reproductive channel and \(R\) a recruitment/reachability channel. The changes

\[
(F,R)\mapsto(aF,R)
\quad\text{and}\quad
(F,R)\mapsto(F,aR)
\]

produce identical net output \(aFR\). Repeatedly measuring only \(W\) cannot distinguish the two latent worlds. If a future intervention acts specifically on \(F\), however, those worlds may need different states.

The missing evidence is then **a different measurement channel**, not merely more measurements of the old one.

## 7. A temporally thick interpretation

The present finite theory is formulated on latent worlds, not on a continuous ontology of time. Nevertheless, a latent world can contain relevant history and future-response structure as coordinates.

This supports the following philosophical interpretation:

> **An ecological state is not necessarily a property of an instant. It can be a scientifically licensed compression of a temporally extended possible world.**

A latent world may encode:

- relevant history or inherited state meaning;
- current ecological configuration;
- latent mechanism or fitness-relevant structure;
- possible responses to declared future interactions and interventions;
- the observation record through which science accesses that world.

Under this interpretation, a present snapshot \(X\) is sufficient only when all latent worlds sharing that snapshot also share the required CREST state. Formally, a future theorem could study the criterion

\[
X(u)=X(v)
\Rightarrow
[u]_J=[v]_J.
\]

The current repository treats this as a **research direction**, not as an already proved trajectory theorem.

## 8. Two kinds of stability

CREST also motivates separating:

1. **dynamical stability** — whether the ecological system resists or recovers from perturbation; and
2. **representational stability** — whether a state representation remains adequate when the scientific contract, observation view, or intervention repertoire changes.

The action-expansion witness already proves that the second can fail without a prior physical regime shift. A system can be dynamically unchanged while its scientifically adequate state becomes finer.

A general theory connecting dynamical, evolutionary, and representational stability remains future work.

## 9. What CREST does not claim

CREST does not establish:

- a nature-given canonical state partition;
- a unique common carrier for every scientific description;
- that all biological evolution monotonically maximizes one global fitness function;
- that stochasticity disappears at the ecological level;
- that every present snapshot is insufficient;
- that the four obligations are exhaustive;
- that monitoring bits equal money, sensors, or person-hours;
- an infinite, continuous, fully stochastic, or approximate trajectory theorem.

The theory is deliberately conditional: its value is to make the conditions under which ecological sameness is scientifically defensible explicit and testable.

## 10. Where to go next

The canonical progression is now:

```text
philosophical question
    What counts as the same ecological state?
        ↓
four obligations
    future / semantics / mechanisms / evidence
        ↓
three mathematical gates
    carrier → least-information state → evidence
        ↓
cross-gate consequences
    action expansion / monitoring debt / target-only reporting
        ↓
ecological projection
    open systems / turnover / latent causality / monitoring / stability
```

See:

- [`crest_mathematical_spine.md`](crest_mathematical_spine.md) for the proved theorem hierarchy;
- [`crest_ecological_projection.md`](crest_ecological_projection.md) for the ecology-facing interpretation; and
- [`README.md`](README.md) for supporting and archived documents.
