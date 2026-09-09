# CREST pure-theory spine — temporal boundary formulation

## Core object

CREST studies a finite state-representation problem at a temporal boundary.

The present is not itself a state variable. It is an observation cut

\[
O_t:\Omega\to Y_t,
\]

with baseline equivalence

\[
B_t=\ker O_t.
\]

The theory asks how much additional structure must live on that cut once three kinds of distinguishability are imposed.

## Three directions at the cut

### Retrospective / left

MLTR supplies distinctions inherited from histories before the cut. Raw paths are not retained directly; they are quotiented by carried semantics.

### Transverse / latent present

MRM supplies distinctions within one visible cut fiber. These are not later times and not additional observed coordinates. They are candidate-safe response distinctions hidden behind the same visible present. Geometrically, they are transverse to the time axis.

### Prospective / right

CCOC supplies distinctions exposed by legal future queries after the cut. Prospective access can be sparse over the retrospective-by-transverse semantic product.

## State comes after the three structures

The three directions do not cause the state and are not assumed independent. They impose constraints on which raw worlds may remain equivalent at the cut.

The adequate state is the least cut quotient compatible with those constraints. In the existing closure notation,

\[
J_t=(C_H\vee C_\Theta\vee C_F)(B_t).
\]

Under sparse semantic access, the prospective constraint is active only on

\[
A_f\subseteq H_{\min}\times\Theta.
\]

If the semantic product has `N` pairs, `k` are addressable, and each addressable pair exposes `2^m` exterior signatures, then

\[
|Q|=(N-k)+k2^m.
\]

Thus the pure-theory question is not how an ecologist should design a state vector. It is:

> Given a temporal cut and left, transverse, and right distinguishability/access structures, what minimal quotient is induced on the cut, which abstract closures are realizable by those structures, and how does quotient complexity vary with sparse prospective access?

## Zero-width language

The finite theory treats the cut as having no temporal duration. This is an idealization encoded directly in the primitive `O_t`; it is not yet a theorem obtained as

\[
[t-\varepsilon,t+\varepsilon]\to\{t\}
\]

when `epsilon -> 0`.

A future continuous-time extension could study left germs, transverse generator/fiber structure, and right germs. The present paper must not claim that extension has already been proved.

## Ecological interpretation

Ecology enters as an interpretation domain for the abstract equivalence structures:

- ecological memory and historical contingency instantiate retrospective distinctions;
- hidden feedback or response regimes instantiate transverse distinctions;
- intervention or prediction questions instantiate prospective distinctions.

The shallow-lake construction is therefore a worked interpretation showing that all three roles can occur in a recognizable ecological setting. It is not the source of the mathematics and not a prescriptive design recipe.
