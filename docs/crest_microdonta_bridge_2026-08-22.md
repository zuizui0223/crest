# CREST–microdonta bridge — 2026-08-22

> **Status:** cross-repository synthesis note. This imports no theorem family into CREST and makes no priority claim. It identifies which already-proved or explicitly bounded results in `zuizui0223/microdonta` can give CREST a more ecological worked interpretation, and which materials should remain outside the CREST main line.

## 0. Verdict

The strongest reusable material is not the ABM inventory itself. Two microdonta results directly sharpen CREST:

1. **channel identifiability N1/N2:** two biologically different causal channel states can be exactly identical under every observation that sees only net performance `W=FE`, yet become distinguishable when a channel-specific intervention or measurement is admitted;
2. **RACH + theorem-projection discipline:** an empirical record defines a set of still-admissible latent mechanisms, while theorem use is licensed only after the target output, factorisation, and observation map are explicitly declared and checked.

Together these supply an ecological worked bridge for CREST's state/evidence separation:

```text
same current net observation
    !=
same causal channel state
    !=
same response to a newly available intervention
```

The existing CREST `rescue` witness remains the proof of the full carrier-expansion conjunction. The microdonta channel construction supplies a less toy-like ecological realisation of the **state-refinement + fixed-evidence failure** part of that story.

---

## 1. N1 gives a concrete ecological latent-world pair

Microdonta assumes a positive two-channel performance factorisation

```text
W(z) = F(z) E(z)
```

with local reproduction/fecundity/survival channel `F` and establishment/reachability channel `E`.

Its theorem N1 compares two distinct causal programs from the same positive baseline:

```text
P_F: (F,E) -> (aF,E)
P_E: (F,E) -> (F,aE)
```

for any positive trait-dependent multiplier `a(z)`.

Both produce exactly the same net performance

```text
W_after(z) = a(z) F(z) E(z).
```

Therefore every deterministic observation `Phi(W)` is identical under the two programs, including all thresholded viable sets and their geometry. This is structural non-identifiability, not sampling noise.

### CREST interpretation

Take two latent ecological worlds

```text
u_F = local-reproduction channel loss
u_E = establishment/reachability channel loss
```

that satisfy the N1 symmetry. If the current evidence records only net performance, then

```text
E(u_F) = E(u_E).
```

If the current future grammar contains no operation that separately addresses `F` or `E`, the two worlds may legitimately share one coarse state for that contract.

Now add a channel-specific action such as

```text
restore_F
```

representing, at the declared model level, an intervention that restores the local reproductive channel while leaving establishment unchanged. Then

```text
restore_F(u_F) -> restored net performance
restore_F(u_E) -> establishment-limited net performance remains depressed.
```

The worlds were observationally and net-performance equivalent before the action was admitted, but the new action makes them future-distinct. CREST must then refine the required state even before the action is executed.

This is a direct ecological microfoundation for the current CREST thesis:

> **An intervention does not merely act on an ecological state; by becoming an admissible future operation, it can change which latent ecological differences must count as state differences.**

The accompanying executable CREST witness is `tests/test_crest_microdonta_channel_bridge.py`.

---

## 2. N2 turns the evidence gate into a measurement-design statement

Microdonta N2 proves that, in the positive two-factor model, observing net performance plus either one exact channel identifies the other:

```text
E = W/F
F = W/E.
```

So the N1 pair is not resolved by collecting more summaries that remain functions of `W`; it is resolved only by adding a channel-resolved measurement (or, under N3/N4, a proxy with a defended calibration condition).

### Why this strengthens CREST

CREST R1 says that the abstract minimum evidence refinement required to identify state `J` is the common refinement

```text
E ∨ J.
```

N1/N2 add a biological interpretation that CREST by itself does not provide:

> **monitoring-resolution debt need not be sample-size debt.**

If the ambiguity is structural under the existing observation map, arbitrarily precise or repeated `W`-only monitoring still cannot identify the channel state. The refinement must introduce a qualitatively new observation class: direct `F`, direct `E`, or a calibrated proxy satisfying the declared mapping.

This can make the CREST monitoring argument much less abstract. The practical message becomes:

```text
state requirement outruns monitoring
    -> first ask whether more of the same data can possibly resolve it
    -> if not, redesign the observation map rather than merely increase replication
```

---

## 3. RACH supplies an empirical analogue of a CREST evidence class

RACH's central object is the admissible causal region

```text
A_epsilon(y_obs, x_obs)
= { (theta,s): G(theta)=1 and d(P_sim(f(x_obs;theta,s)), P_obs(y_obs)) <= epsilon }.
```

For one observed record, this is exactly the kind of object CREST wants to keep conceptually separate from the required state: a set of latent parameter/mechanism worlds still compatible with evidence.

The mapping is not theorem-identical, because RACH is approximate/ABC-based while current CREST is finite and exact. But the roles align cleanly:

| CREST | RACH analogue |
|---|---|
| latent world `u` | `(theta,s)` causal program state |
| evidence-compatible worlds for `e` | accepted/admissible region `A_epsilon` |
| unresolved state set `S(e)` | images of admissible `(theta,s)` under the declared CREST state map |
| mechanism ambiguity | switch-state causal degeneracy `H(S | A_epsilon)` |
| strengthen evidence | observation contribution / candidate next observation |

RACH therefore gives CREST an executable route from abstract evidence ambiguity to a data-facing workflow. It should be presented as an **empirical approximation layer**, not as a proof of the CREST finite theorems.

### Important CREST correction to RACH-style information seeking

RACH's causal resolvability targets the whole retained switch vector. CREST shows that full mechanism/state resolution may be unnecessary when the declared target is constant across the surviving states.

So a future integration should distinguish:

```text
observation valuable for full causal resolution
from
observation necessary for the declared ecological target.
```

This is where CREST can turn RACH's next-observation machinery into target-conditioned monitoring design rather than information acquisition for its own sake.

---

## 4. The theorem-projection ledger is a concrete example of contract-relativity without arbitrariness

Microdonta's projection rule is:

> a theorem may be used outside its abstract model only after the target output, factorisation, and observation map have been stated and checked.

The ledger marks targets as `exact`, `requires_factorization_extension`, or `not_applicable` rather than silently transferring a theorem from an abstract model to an ABM or empirical record.

This strongly reinforces CREST's philosophical claim that contract-relativity is not free choice. A theorem/state representation becomes licensed only after a mapping preserves the structures on which the claim depends.

The closest CREST analogues are J2/J5 and the carrier/evidence gates:

```text
abstract theorem/model
    -> declare target carrier and mapping
    -> check preservation / faithful projection assumptions
    -> construct required state
    -> separately check whether empirical evidence resolves it.
```

This is especially useful for the manuscript because it provides a concrete scientific-practice example of why a state or theorem can be exact in one representation and unearned in another.

---

## 5. Patch-feedback hysteresis is useful only as a secondary history example

Microdonta's reduced feedback model proves that after patch area is restored to the same `A_high`, the long-run high/low trait state can differ depending on the current trait frequency/history. Habitat restoration alone does not force recovery; crossing the basin threshold `x_c(A)` is additionally required.

This can illustrate the MLTR/history side of CREST:

```text
same restored external environment
    !=
same dynamically adequate state
```

because state adequacy for restoration prediction may require retaining `x` or history, not just current habitat area.

However, this is not needed for the CREST main novelty line and should remain a supporting example unless the manuscript explicitly develops history-dependent state adequacy.

---

## 6. Materials that should NOT be imported as CREST evidence

Do not use the following as if they prove CREST:

- current Campanula published gradients as channel identification — microdonta itself marks them insufficient for `F` versus `E`;
- the spatial/defense/colonization ABMs as theorem-exact without a declared factorisation and observation map;
- heuristic NOV as a theorem about optimal monitoring;
- frozen legacy/demo modules listed in microdonta's post-split triage;
- a generic claim that trait-space contraction, shift, or fragmentation identifies mechanism.

Microdonta's own projection ledger is explicit that ABM richness does not earn theorem applicability automatically.

---

## 7. Recommended CREST use

### Main manuscript

Use one compact worked example after the abstract `rescue` witness or in Discussion:

```text
Two systems can have identical net trait performance W because one lost local
reproduction F while another lost establishment E. Net-only monitoring cannot
separate them. A newly available F-specific restoration action immediately makes
the two systems future-distinct, so the adequate state must split even before the
action is used. Measuring W more precisely cannot repair the ambiguity; a
channel-resolved measurement is required.
```

This makes the CREST action-availability result ecological rather than merely automata-like.

### Formal supplement / repository

Keep the executable finite witness as a regression test, but do not label it a new theorem family. It is a **microdonta-grounded witness of the existing CREST cross-gate architecture**.

### Empirical future

Use RACH admissible regions as a candidate empirical approximation to CREST evidence-compatible latent worlds, and compare two observation-design objectives:

1. reduce full causal/state ambiguity;
2. reduce only target-relevant ambiguity.

That would give CREST a genuine empirical-methodological extension rather than another abstract theorem name.
