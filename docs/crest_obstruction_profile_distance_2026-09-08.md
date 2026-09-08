# CREST obstruction-profile distance

## Purpose

CREST now has three quantitative layers for finite contracts:

1. a single-contract obstruction spectrum;
2. before/after signed change accounting; and
3. a symmetric distance between obstruction-accounting profiles.

The third layer answers a different question:

> How different are two contracts in the full pattern of direct and interaction-generated state debt?

It is a distance between **obstruction profiles**, not a distance between ecological systems themselves.

## Complete coordinate representation

For a fixed named responsibility set `N`, let

\[
v(S)=\log_2|J_S|-\log_2|B|
\]

be the state debt of coalition `S`. Let `m(S)` be its Möbius/Harsanyi dividend. Because Möbius inversion is bijective on the finite coalition lattice,

\[
\{v(S):S\subseteq N\}
\quad\Longleftrightarrow\quad
\{m(S):\varnothing\ne S\subseteq N\}.
\]

CREST therefore uses the nonempty dividend vector

\[
\mathbf m=(m(S))_{\varnothing\ne S\subseteq N}
\]

as the obstruction-profile coordinate system. Singleton coordinates are direct debts. Coordinates of order two or higher are interaction terms.

## Raw profile distances

For two profiles `A` and `B`, define

\[
d_1^{\rm raw}(A,B)
=
\sum_{\varnothing\ne S\subseteq N}
|m_A(S)-m_B(S)|
\]

and

\[
d_2^{\rm raw}(A,B)
=
\left(
\sum_{\varnothing\ne S\subseteq N}
[m_A(S)-m_B(S)]^2
\right)^{1/2}.
\]

These are ordinary L1 and L2 metrics on the raw dividend vectors. CREST also reports the exact L1 decomposition

\[
d_1^{\rm raw}
=
d_{1,\rm direct}^{\rm raw}
+
d_{1,\rm interaction}^{\rm raw},
\]

where direct uses singleton coordinates and interaction uses orders two and above.

## Capacity-normalized profile distances

For a carrier with `N_w` worlds and a baseline with `B` blocks, the available refinement capacity is

\[
K_{\max}=\log_2(N_w/B).
\]

When `K_max>0`, define normalized dividend coordinates

\[
\widehat m(S)=\frac{m(S)}{K_{\max}}.
\]

The normalized distances are then

\[
d_1^{\rm norm}(A,B)
=
\sum_S|\widehat m_A(S)-\widehat m_B(S)|
\]

and

\[
d_2^{\rm norm}(A,B)
=
\left(
\sum_S[\widehat m_A(S)-\widehat m_B(S)]^2
\right)^{1/2}.
\]

These are metrics on the normalized profile vectors. They are not injective metrics on underlying ecological contracts: different contracts can induce the same obstruction profile.

## Canonical CCOC/MLTR/MRM path

Use the same six-world, two-baseline-state family in three stages:

```text
inert
  ↓ activate MLTR interaction
pair-only
  ↓ activate MRM three-way interaction
full cascade
```

The only profile changes are

\[
\delta m(\mathrm{CCOC,MLTR})
=
\log_2(4/3)
=
0.4150374993\ \text{bit}
\]

and

\[
\delta m(\mathrm{CCOC,MLTR,MRM})
=
\log_2(5/4)
=
0.3219280949\ \text{bit}.
\]

Therefore inert-to-full distance is

\[
\boxed{
d_1^{\rm raw}=0.7369655942\ \text{bit}
}
\]

and

\[
\boxed{
d_2^{\rm raw}=0.5252559605\ \text{bit}.
}
\]

The available refinement capacity is

\[
K_{\max}=\log_2(6/2)=\log_2 3=1.5849625007\ \text{bit},
\]

so

\[
\boxed{d_1^{\rm norm}=0.4649735207}
\]

and

\[
\boxed{d_2^{\rm norm}=0.3313996137}.
\]

The direct component is exactly zero. The entire distance is interaction-generated, so the symmetric profile difference class is `interaction-only`. The dominant changed coordinate is the pairwise `CCOC × MLTR` term.

Along this activation path,

\[
d_1(\text{inert},\text{full})
=
d_1(\text{inert},\text{pair-only})
+
d_1(\text{pair-only},\text{full}),
\]

which is the equality case of the triangle inequality.

## Pairwise contract geometry

For a named collection of comparable contracts, CREST can build a symmetric pairwise matrix using any of

- `raw_l1_bits`;
- `raw_l2_bits`;
- `normalized_l1`; or
- `normalized_l2`.

It also reports each contract's nearest neighbor in the selected obstruction-profile geometry.

This is useful after batch ranking. Ranking answers “which contract has more burden?” Distance answers “which contracts have similar obstruction anatomy?”

## Interpretation firewall

The profile distance is deliberately narrow.

It is **not**:

- a distance between ecological worlds;
- a dynamical-system distance;
- an empirical effect size;
- evidence that two ecosystems are biologically similar; or
- a substitute for the raw bit accounting.

Mechanical comparison requires the same named responsibility set. Scientific cross-system interpretation additionally requires that responsibility meanings, carrier construction, and baseline semantics are commensurable. Capacity-normalized distances are especially sensitive to this condition because each profile is divided by its declared available refinement capacity.

The mathematical substrate—Möbius inversion and L1/L2 norms—is standard. CREST's use is to turn the complete finite joint-responsibility accounting table into a reproducible geometry of contract-relative representational burden.

## Executable surfaces

Two-contract distance:

```bash
python scripts/distance_obstruction_profiles.py before.json after.json
```

Pairwise matrix:

```bash
python scripts/matrix_obstruction_profiles.py inert.json pair.json full.json
```

The implementation is in:

- `crest/obstruction_distance.py`;
- `crest/obstruction_geometry.py`;
- `tests/test_crest_obstruction_distance.py`; and
- `tests/test_crest_obstruction_geometry.py`.
