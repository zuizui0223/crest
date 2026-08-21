# CREST state trichotomy validation — 2026-08-21

> **Status:** validation note. No new theorem. This note checks the end-to-end meaning of
> “state absent / state exists / state exists but is unresolved” against J3/J6, J1,
> and the evidence gate.

## 1. Exact claim being validated

CREST does **not** claim that the empty set of admissible worlds implies that no
mathematical partition can be written down. The no-go is contract-relative:

> there is no **fully adequate joint ecological state representation satisfying the
> declared synchronization, action, coverage, and four-audit obligations**.

The distinction matters when the maximal carrier is nonempty but coverage-incomplete.
A partition can be formed on the surviving worlds, but it is not a solution to the
full declared contract because one or more required component labels have been lost.

## 2. Gate A — carrier existence and coverage

For the universal-action contract, J3 returns the greatest compatible
transition-closed kernel `U*`. Every other compatible transition-closed subset is
contained in `U*`.

Therefore:

- if `U*` is empty, no nonempty common lift exists;
- if `U*` is nonempty but misses a required component label, no smaller closed lift
  can restore that missing label, so no coverage-complete common lift exists;
- only `U*.admissible == True` authorizes the full declared synchronization to pass
  to the J1 state-construction gate.

The controlled J6 gate has the same logical form with the greatest robustly
controlled-invariant kernel `K*` and its declared coverage obligations.

## 3. Gate B — joint-state construction

On one admitted nonempty common carrier, J1 constructs the unique coarsest common
fixed point

\[
J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B).
\]

For a world `u` in that carrier, the required CREST state is `[u]_J`.

This is an existence-and-minimality result **conditional on having already passed
Gate A**. J1 should not be interpreted as repairing an empty or coverage-incomplete
carrier.

## 4. Gate C — evidence resolution

Even when J exists, the current evidence may not identify its block. Full state
reporting is licensed iff the evidence partition refines J (`J <= E_D` in the
manuscript's information order). Otherwise the honest full-state report is the set
of J-blocks compatible with the evidence class.

A requested target can nevertheless remain deterministic when it is constant on
each evidence class.

## 5. Validated trichotomy

The correct end-to-end classification is therefore:

1. **No fully adequate CREST state under the declared contract.**
   Gate A fails because the maximal carrier is empty or coverage-incomplete. A
   finite elimination/no-go certificate explains the failure.
2. **CREST state exists and is identified.**
   Gate A passes, J1 returns J, and the evidence resolves the J-block.
3. **CREST state exists but is unresolved.**
   Gate A passes and J1 returns J, but the evidence class intersects multiple
   J-blocks. Target-only reporting may still be licensed.

This trichotomy is contract-relative. Changing the synchronization, action roles,
coverage obligations, four audit definitions, target, or evidence contract can
change which branch applies.

## 6. Validation boundary

This note does not establish:

- a nature-given canonical carrier;
- one state across all scientific contracts;
- empirical truth of a declared carrier or evidence model;
- stochastic/continuous/infinite-state generalization.

It only verifies that the finite CREST theorem surfaces support the three-way
existence/resolution interpretation without collapsing carrier feasibility, state
construction, and evidence licensing.
