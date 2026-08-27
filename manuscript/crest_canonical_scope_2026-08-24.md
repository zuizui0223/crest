# CREST canonical manuscript scope — revised 2026-08-27

## Status

This is the canonical scope contract for the CREST Biology & Philosophy submission.

The manuscript is an **ecological problem → philosophical/formal analysis → finite theorem → conservation consequence** paper.

It is **not an empirical validation paper**. However, it now contains one **ecology-grounded worked case** in shallow-lake restoration so that the formal distinctions do real ecological work in the main text. The worked case is a finite illustrative mapping grounded in established lake-restoration mechanisms; it is not a fitted empirical test of CREST and does not claim that the extremal theorem has been observed in real lakes.

## 1. Organizing claim

The paper is organized around:

\[
\boxed{
\textbf{conservation capacity can outgrow conservation knowledge.}
}
\]

A newly available intervention can enlarge what can be managed while simultaneously making a previously adequate ecological-state description too coarse for the new responsibility.

The operational state question remains:

> **When should different ecological worlds count as the same ecological state?**

## 2. Philosophical state problem

CREST treats an ecological state as a scientifically licensed quotient of temporally extended ecological worlds.

Relative to a present time, write

\[
\omega=(h_t,x_t,\mathcal F_t),
\]

where \(h_t\) is relevant history, \(x_t\) present configuration, and \(\mathcal F_t\) future-response structure under relevant interactions and interventions.

For scientific access \(V\) and contract \(\mathcal C\),

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V},
\qquad
\operatorname{State}_{\mathcal C,V}(\omega)=[\omega]_{\sim_{\mathcal C,V}}.
\]

The manuscript connects this to established philosophical work on:

- abstraction and idealization in ecology;
- diverse scientific aims and purpose-relative adequacy;
- multiple realization and levels of description;
- predictive and interventional state abstractions.

CREST does not claim novelty for any of those themes by themselves.

## 3. Well-posed scientific contracts

Contract-relativity must not collapse into arbitrary relabelling. The manuscript therefore distinguishes normative value from formal well-posedness.

A CREST contract is well posed only when:

1. response, action repertoire, and target are specified independently of the candidate quotient;
2. the declared obligations share a nonempty admissible domain covering the intended systems;
3. proposed state merges have a failure condition—response disagreement, semantic failure, or target disagreement;
4. the state required by the task is kept distinct from the state identified by evidence.

CREST does not rank the moral or institutional value of scientific aims. It constrains what counts as an adequate state once an aim has been declared.

## 4. Worked ecological case — shallow-lake restoration

The main text contains one finite ecology-grounded example.

Two currently turbid worlds are considered:

- sediment-phosphorus legacy;
- food-web/macrophyte feedback.

For current-status reporting they can share one coarse state. Once sediment-focused and food-web-focused restoration actions become part of the management repertoire, they require different response states because the interventions have different successors.

The worked case follows the CREST gates:

```text
Gate A — one admissible management world set
Gate B — coarse turbid state splits under mechanism-specific actions
Gate C — routine water-quality evidence can still merge the required states
```

The resulting current-status target can remain reportable even when the intervention-response state is unresolved.

This case is a **worked ecological interpretation**, not empirical validation of the capability–resolution theorem.

## 5. Finite mathematical spine

### Gate A — admissible carrier

Ask whether the declared obligations can be represented on one finite latent-world carrier.

### Gate B — least-information required state

On an admissible finite carrier and baseline partition \(B\), refinement closures yield

\[
\boxed{
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B),
}
\]

which is the unique coarsest common fixed point under the stated assumptions.

The generic lattice, closure, and finite-state minimization machinery is classical and is not the novelty claim.

### Gate C — evidence licensing

For evidence partition \(E_D\),

\[
\boxed{
\text{full deterministic state report exists}
\iff J\preceq E_D.
}
\]

A coarser target may remain reportable when the full state is not.

Hence preserve

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}
}
\]

in general.

## 6. Main theorem — capability–resolution divergence

For every integer \(m\ge1\), one connected finite construction gives

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m.
}
\]

On the retained present slice:

- required state refines from \(1\) class to \(2^m\) classes;
- monitoring-resolution debt grows from \(0\) to \(m\) bits;
- full-state licensing changes from yes to no under fixed evidence;
- a coarse target remains reportable.

Therefore no finite function of carrier-size gain alone universally upper-bounds the increase in required state complexity.

This is an extremal impossibility result. It does not claim that real ecosystems typically show exponential state growth.

## 7. Conservation consequence

The manuscript's main ecological conclusion is not simply “monitor more” or “management response can differ.” It is the asymmetry:

> **A new conservation capability can make the system more manageable while making the old state description less adequate.**

The intervention need not be executed. Once the scientific responsibility includes predicting its effect, previously hidden distinctions can become state-relevant.

This yields four consequences:

1. conservation-state categories that include intervention response are partly indexed to feasible management space;
2. successful target reporting does not imply full state identification;
3. monitoring deficits can be structural and require a new measurement channel rather than more replication;
4. whenever the management repertoire changes, state adequacy should be re-audited.

## 8. Relation to prior theory

The manuscript explicitly credits prior work on:

- purpose-relative model adequacy;
- idealization and abstraction;
- multiple realization and levels of description;
- predictive state representations;
- POMDPs;
- causal abstraction;
- state/action abstraction coupling;
- ecological state-and-transition modelling;
- ecological model transferability.

The defended CREST contribution is the ecology-specific state-sameness architecture

\[
\boxed{
\text{admissible worlds}
\to
\text{required state}
\to
\text{evidence-identified state}
\to
\text{reportable target}
\to
\text{quotient-level law}
}
\]

plus the connected cross-layer no-bound construction.

## 9. Explicit exclusions

Do not reintroduce any of the following as empirical validation arcs:

- Izu/Campanula field validation;
- prospective CREST field testing;
- restoration/conservation cross-domain validation registries;
- urban/island validation series;
- claims that published case studies test the finite theorem end to end.

A single ecology-grounded worked example is allowed and required for readability. Its role is conceptual demonstration, not empirical confirmation.

## 10. Submission structure

The main manuscript should read in this order:

```text
1. conservation-capacity paradox
2. ecological state as justified equivalence
3. shallow-lake worked case
4. finite carrier/state/evidence architecture
5. capability–resolution divergence theorem
6. conservation consequences
7. philosophical and formal positioning
8. limits and conclusion
```

Detailed proof machinery and software reproducibility belong in Supplementary Information.
