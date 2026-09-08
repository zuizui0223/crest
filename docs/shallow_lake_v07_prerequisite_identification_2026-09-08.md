# Shallow-lake v0.7 prerequisite identification

## Status

This is a **literature-grounded finite decision model**, not an empirical fit and not a claim that a universal shallow-lake policy has been discovered.

Its purpose is narrower: justify the ecological ingredients used in the CREST shallow-lake example, make the target functions explicit, and separate what the restoration literature supports from what is introduced as a deliberately minimal formal witness of interface dependence.

## 1. Literature-supported ecological ingredients

Three claims used by the finite model are independently supported by the shallow-lake restoration literature.

### 1.1 Historical nutrient loading can remain operationally relevant after external-load reduction

Søndergaard, Jensen, and Jeppesen (2003) review the role of shallow-lake sediments and show that phosphorus accumulated during high external loading can sustain substantial internal loading after external inputs are reduced. This supports treating a retained nutrient/sediment legacy as a retrospective variable that can matter for recovery questions.

### 1.2 Similar coarse turbid states can involve different response-relevant resistance channels

Shallow-lake restoration reviews distinguish chemical inertia associated with sediment phosphorus from biological inertia associated with fish communities and delayed macrophyte recovery. Jeppesen et al. (2012) explicitly discuss both sources of within-lake resilience after nutrient-load reduction. This supports representing at least two latent response types in the finite model: a sediment/internal-P channel and a biological feedback channel.

### 1.3 Restoration choice can require more than one management channel

Søndergaard et al. (2007) show that long-term restoration success and failure depend on multiple factors, including insufficient external-load reduction, internal phosphorus loading, fish-community dynamics, and the absence of stable submerged macrophytes. Jeppesen et al. (2012) likewise discuss combined physico-chemical and biological restoration. This supports using a composed restoration target rather than assuming that one universal intervention channel is sufficient.

These papers support the **ingredients and distinction among channels**. They do not specify the exact finite target maps below.

## 2. Finite world carrier

All four finite worlds share the same visible coarse status:

`visible_status = turbid_eutrophic`.

They cross two retrospective modes

- `no_retained_legacy`
- `retained_nutrient_legacy`

with two latent response types

- `sediment_internal_p`
- `biological_feedback`.

This 2 x 2 carrier is a modeling device for prerequisite identification. It does not assert that real shallow lakes fall into exactly four natural classes.

## 3. Target-specific prerequisite audit

CREST asks whether each target factors through no retained interface, history only, latent response only, or both.

### 3.1 Current-status target

`current_status_target` returns the coarse visible status only.

Therefore

\[
R_{\mathrm{status}}=\varnothing.
\]

This target is descriptive rather than restorative.

### 3.2 Legacy-sensitive recovery target

`legacy_sensitive_recovery_target` asks whether a retained nutrient/sediment legacy constraint is present.

Therefore

\[
R_{\mathrm{legacy}}=\{H\}.
\]

The literature supports the relevance of this retrospective distinction through persistent internal phosphorus loading after external-load reduction (Søndergaard et al. 2003).

### 3.3 Mechanism-specific intervention target

`mechanism_specific_intervention_target` distinguishes a sediment-focused channel from a food-web/macrophyte channel.

Therefore

\[
R_{\mathrm{mechanism}}=\{\Theta\}.
\]

The literature supports the existence of these distinct response-relevant restoration channels, but not this exact two-label coding.

### 3.4 Binary composed target

Earlier versions assigned a different output label to all four history-response combinations. That was sufficient to force

\[
R=\{H,\Theta\},
\]

but it was an unnecessarily strong witness because four inputs were mapped to four outputs.

The current model uses only **two outputs**:

- `standard_pathway`
- `cross_interface_review`.

Define two binary semantic signals:

\[
L(h)=1
\iff
h=\texttt{retained\_nutrient\_legacy},
\]

and

\[
S(\theta)=1
\iff
\theta=\texttt{sediment\_internal\_p}.
\]

The composed target is the concordance diagnostic

\[
T_{\mathrm{composed}}(h,\theta)
=
\mathbf 1\{L(h)=S(\theta)\}.
\]

Equivalently, the complementary label is XOR-like mismatch. The output cardinality is two, not four.

For every fixed history mode, changing response type changes the target. For every fixed response type, changing history mode changes the target. Therefore neither interface alone is sufficient, while the pair is sufficient:

\[
\boxed{R_{\mathrm{composed}}=\{H,\Theta\}.}
\]

This demonstrates genuine joint dependence without relying on one unique output label per semantic pair.

## 4. Interpretation boundary of the binary target

The concordance/mismatch rule is a **minimal finite formalization**, not a published restoration rule.

The restoration literature supports:

1. persistent historical sediment-P legacy;
2. distinct sediment/internal-P and biological feedback response channels;
3. the need for target- and system-specific combinations of restoration measures.

The literature does **not** establish that shallow-lake managers literally use the parity rule above, nor that `cross_interface_review` is a measured treatment category. That binary map is introduced only to show that a target can require both retained interfaces even when its output has two levels.

Accordingly, the shallow-lake case licenses the statement:

> a restoration target can be modeled so that both retrospective legacy and latent response structure are individually necessary for exact target recovery.

It does not license the stronger statement:

> real shallow-lake restoration policy universally follows the specific XOR/XNOR diagnostic encoded here.

## 5. Executable validation

`crest/shallow_lake_prerequisites.py` computes prerequisite sets by exact factorization over all four finite worlds.

`tests/test_shallow_lake_prerequisites.py` additionally verifies that:

- the composed target has exactly two outputs for four semantic pairs;
- conditioning on history alone leaves both outputs possible;
- conditioning on response type alone leaves both outputs possible;
- counterfactual substitution of either interface changes the composed target while the other interface and visible cut are held fixed.

Thus the two-interface requirement is an executable property of the declared finite map rather than a markdown assertion.

## 6. References

Jeppesen, E., M. Søndergaard, T. L. Lauridsen, T. A. Davidson, Z. Liu, N. Mazzeo, C. Trochine, K. Özkan, H. S. Jensen, D. Trolle, F. Starling, X. Lazzaro, L. S. Johansson, R. Bjerring, L. Liboriussen, S. E. Larsen, F. Landkildehus, S. Egemose, and M. Meerhoff. 2012. Biomanipulation as a restoration tool to combat eutrophication: recent advances and future challenges. *Advances in Ecological Research* 47:411–488. https://doi.org/10.1016/B978-0-12-398315-2.00006-5.

Søndergaard, M., J. P. Jensen, and E. Jeppesen. 2003. Role of sediment and internal loading of phosphorus in shallow lakes. *Hydrobiologia* 506:135–145. https://doi.org/10.1023/B:HYDR.0000008611.12704.dd.

Søndergaard, M., E. Jeppesen, T. L. Lauridsen, C. Skov, E. H. Van Nes, R. Roijackers, E. Lammens, and R. Portielje. 2007. Lake restoration: successes, failures and long-term effects. *Journal of Applied Ecology* 44:1095–1105. https://doi.org/10.1111/j.1365-2664.2007.01363.x.
