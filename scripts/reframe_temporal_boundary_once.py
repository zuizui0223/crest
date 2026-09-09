#!/usr/bin/env python3
"""One-shot exact-string reframing of the canonical AmNat manuscript.

This script changes framing only. It deliberately leaves all sparse-access
formulae, benchmark values, and the shallow-lake executable result untouched.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"

text = MANUSCRIPT.read_text(encoding="utf-8")


def replace_once(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"expected exactly one match, got {count}: {old[:100]!r}")
    text = text.replace(old, new, 1)


replace_once(
    "Ecological state is often treated as a property measured at one moment. We instead treat the present as an observational temporal cut and define state as the least information that must survive that cut for a declared scientific contract. Retrospective history, latent response structure, and future-query grammar are defined before state through separate companion semantics. A realizability audit rules out several tempting but circular temporal interpretations. We then connect those semantics directly to the state quotient: MLTR routes collapse by carried terminal meaning, MRM candidates collapse by complete response equivalence, and future decoders are licensed only on specified semantic history-by-response pairs. This exposes a distinction hidden by complete-interface models. If N semantic pairs exist but only k are future-addressable, an m-bit decoder yields (N-k)+k2^m joint state classes and a three-way state dividend log2[((N-k)+k2^m)/N], approaching m-log2(N/k). Thus prerequisite order and semantic coverage control different aspects of state interaction. A shallow-lake restoration model makes prerequisite identification executable and target relative rather than a fixed property of the ecosystem.",
    "Ecological state is often treated as something possessed by a system at one moment. We instead idealize the present as a zero-duration temporal cut: an observational boundary, not a finite interval and not yet an adequate state. Retrospective carried history, transverse latent-present response structure, and prospective query accessibility are defined before state through separate companion semantics. Their role is not to cause the state but to constrain which distinctions may be collapsed at the cut. CREST defines ecological state as the least quotient compatible with those left, transverse, and right constraints. A realizability audit rules out several circular temporal interpretations. Sparse prospective access then changes the induced quotient: if N retrospective-by-transverse semantic pairs exist but only k are future-addressable, an m-bit decoder yields (N-k)+k2^m joint state classes and a three-way state dividend log2[((N-k)+k2^m)/N], approaching m-log2(N/k). A shallow-lake restoration model provides a worked ecological interpretation. The finite theory does not claim a continuous-time epsilon-to-zero limit theorem.",
)

replace_once(
    "Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results establish that time matters dynamically. They do not by themselves answer a representational question: when several possible ecological worlds look the same now, which distinctions must a scientific state retain?",
    "Ecological systems can remember the past. Antecedent conditions generate ecological memory (Ogle et al. 2015), hysteresis makes response depend on history (Scheffer et al. 2001), and long transients can make instantaneous conditions a poor guide to future behavior (Hastings et al. 2018). These results establish that time matters dynamically. They do not by themselves determine the structure carried by an idealized present boundary. CREST therefore begins by separating the visible observation at a time cut from the state structure that may be required on that cut.",
)

replace_once(
    "Related formal literatures construct state through predictive or decision equivalence. Computational mechanics merges histories with identical predictive consequences (Shalizi and Crutchfield 2001). Predictive state representations encode state through action-conditional predictions (Littman, Sutton, and Singh 2001). Bisimulation and state-abstraction methods merge states while preserving declared behavioral or decision properties (Givan, Dean, and Greig 2003; Li, Walsh, and Littman 2006).",
    "At a cut time t, an observation can leave several latent possibilities unresolved. These are not meant as parallel universes; mathematically they are the fiber of raw configurations compatible with the same visible cut value. Distinctions can reach that fiber from three geometrically different directions: retrospectively from histories to the left of the cut, transversely through latent response differences hidden at the cut, and prospectively through responses exposed by legal queries to the right. The theoretical problem is to determine the least quotient on the cut compatible with those distinctions.",
)

replace_once(
    "CREST addresses a composition and identification problem. We take the visible present as a baseline cut and ask what information must survive that cut when distinct scientific responsibilities meet there. The companion programmes motivating the finite theory are structurally different. MLTR begins from replacement history and inherited semantics. MRM begins from primitive candidate laws and candidate-safe response equivalence. CCOC fixes a controlled law and varies the legal future grammar. CREST does not treat these as interchangeable coordinates. It asks how their induced state obligations compose, which semantic combinations a future query can actually address, and how that access structure changes the required state.",
    "CREST studies this as a finite temporal-boundary state problem. MLTR supplies retrospective carried semantics from the left of the cut. MRM supplies candidate-safe latent response types within the observation fiber; this is the transverse latent-present direction, not an assertion of complete ontic mechanism identity. CCOC supplies prospective response distinctions under a declared right-of-cut query grammar. CREST asks how these pre-state equivalence and access structures induce a minimal cut-state and how partial prospective accessibility changes its complexity.",
)

replace_once(
    "The paper does not claim mathematical novelty for Möbius inversion or unanimity games. Those provide accounting language. The contribution is a modeling architecture with two separate identification objects:",
    "The paper does not claim mathematical novelty for Möbius inversion or unanimity games. Those provide accounting language. The finite theory isolates two distinct structures controlling the prospective refinement of the cut-state:",
)

replace_once(
    "## 2. State at an observational temporal cut",
    "## 2. State at a zero-duration temporal cut",
)

replace_once(
    "Two worlds lie in one block of \\(B_t\\) exactly when they are indistinguishable at the declared cut. The present is therefore not the ecological state. It is the observational baseline relative to which a state must be constructed.",
    "Two raw configurations lie in one block of \\(B_t\\) exactly when they are indistinguishable at the declared cut. The present is therefore not itself the ecological state. In the finite theory, `zero-duration` means that the present is represented by one indexed boundary rather than by a finite observation interval; it is not a proved limit of shrinking continuous-time windows.",
)

replace_once(
    "For a required state map \\(q_t:\\Omega\\to Q_t\\), the visible present is sufficient exactly when",
    "For one visible cut value \\(y\\), the fiber \\(L_t(y)=O_t^{-1}(y)\\) is the set of raw possibilities hidden behind that observation. The transverse latent-present structure lives inside this fiber: MRM may distinguish candidate-safe response types even when \\(O_t\\) does not.\n\nFor a required state map \\(q_t:\\Omega\\to Q_t\\), the visible present is sufficient exactly when",
)

replace_once(
    "Equivalently, \\(q_t\\) factors through \\(O_t\\). CREST defines the adequate ecological state as the least-information quotient that satisfies the declared scientific contract.",
    "Equivalently, \\(q_t\\) factors through \\(O_t\\). When this fails, the adequate cut-state is the least quotient refining \\(B_t\\) enough to preserve the declared retrospective, transverse, and prospective distinguishability constraints. State is therefore structure induced on the cut, not a synonym for the visible cut itself.",
)

replace_once(
    "## 3. Companion primitives are defined before state",
    "## 3. Retrospective, transverse, and prospective structures are pre-state",
)
replace_once("### 3.1 MLTR: retrospective carried semantics", "### 3.1 MLTR: retrospective carried semantics from the left")
replace_once(
    "The retained history context is therefore not a route identifier. It is a quotient of routes by equality of carried semantics. CREST consumes these completed carried maps rather than reimplementing MLTR's relation-composition proof machinery.",
    "The retained retrospective structure is therefore not a route identifier. It is a quotient of routes by equality of carried semantics. Geometrically it records which distinctions arrive at the cut from its left side. CREST consumes these completed carried maps rather than reimplementing MLTR's relation-composition proof machinery.",
)
replace_once("### 3.2 MRM: candidate-safe latent response", "### 3.2 MRM: transverse latent-present response structure")
replace_once(
    "Two candidates are response equivalent exactly when their complete declared response tables agree. The retained latent interface is therefore the candidate-safe quotient of primitive laws, not a mechanism label imposed from outside.",
    "Two candidates are response equivalent exactly when their complete declared response tables agree. The retained transverse structure is therefore the candidate-safe quotient of primitive laws hidden behind the visible cut. It partitions the latent-present observation fiber by response type; it is not a claim to recover complete causal or ontic mechanism identity.",
)
replace_once("### 3.3 CCOC: future query grammar", "### 3.3 CCOC: prospective query structure to the right")
replace_once(
    "The future responsibility is therefore a declared family of legal questions, not a future state variable inferred from the final quotient.",
    "The prospective structure is therefore a declared family of legal right-of-cut questions, not a future state variable inferred from the final quotient.",
)
replace_once(
    "There is no reverse dependence from the final state into these primitives.",
    "There is no reverse dependence from the final state into these primitives. The three roles are consequently not three independent state coordinates: they are retrospective, transverse, and prospective constraints that are defined before the cut-state and may be mutually dependent in the underlying ecology.",
)

replace_once("## 9. What the modeling result means", "## 9. What the cut-state result means")
replace_once(
    "CREST itself cannot infer the correct prerequisite set or semantic access relation from Möbius accounting. Those objects must come from the ecological meaning of the retained interfaces and the legal future task.",
    "CREST does not derive retrospective, transverse, or prospective semantics from Möbius accounting. Those structures are pre-state inputs. Once they are fixed, however, the induced cut quotient and its interaction accounting are mathematical consequences rather than design choices.",
)
replace_once(
    "This matters for modular state design. A modeler who constructs a history summary, a latent-response summary, and a future-response interface independently may be justified for one target and under-resolved for another. Even when both interfaces are required, assuming complete access across their Cartesian product can overstate state complexity. The relevant questions are therefore",
    "The theoretical distinction is between the order of a prospective constraint and its semantic coverage. A prospective query may require both the retrospective and transverse structures while remaining addressable on only part of their product. Complete access therefore yields a different cut-state complexity from sparse access. The corresponding structural questions are",
)

replace_once(
    "The additional modeling step is to keep several scientific responsibilities separate before quotient composition. Retrospective carried meaning, latent response equivalence, and future-query legality are defined by different companion semantics, and the realizability audit prevents the final state from being used circularly to define those inputs. The sparse-access result then distinguishes two objects that are often collapsed in a single future-equivalence relation: which interfaces a query requires, and on which semantic combinations of those interfaces that query is actually addressable.",
    "The additional theoretical step is to keep several equivalence structures separate before quotient composition. Retrospective carried meaning, transverse latent-response equivalence, and prospective query legality are defined by different companion semantics, and the realizability audit prevents the final cut-state from being used circularly to define those inputs. The sparse-access result then distinguishes two objects often collapsed in a single future-equivalence relation: which pre-state structures a prospective query requires and on which semantic combinations it is actually addressable.",
)
replace_once(
    "The resulting contribution is therefore not a new generic theory of quotient states. It is an identification discipline for ecological modeling: distinguish the visible cut from the adequate state, derive retrospective and latent interfaces from their own semantics, specify the future task independently, identify prerequisite structure and semantic coverage, and only then compute the state quotient. That placement is what connects ecological memory, historical contingency, restoration dynamics, latent-state inference, and predictive-state abstraction without treating any of them as interchangeable.",
    "The resulting contribution is therefore not a new generic theory of quotient states. It is a finite theory of state at a temporal boundary: distinguish the visible cut from its induced state, keep retrospective, transverse, and prospective equivalences pre-state, and characterize the least quotient they impose. That placement connects ecological memory, historical contingency, restoration dynamics, latent-state inference, and predictive-state abstraction without treating any of them as interchangeable.",
)

replace_once(
    "The sparse-access result should also not be oversold as difficult game theory. Once the semantic quotient and access relation are specified, its cardinality formula follows by finite counting. The modeling contribution lies in making semantic coverage an explicit state-construction object and in separating it from interface prerequisite order.",
    "The sparse-access result should also not be oversold as difficult game theory. Once the semantic quotient and access relation are specified, its cardinality formula follows by finite counting. The theoretical contribution lies in making semantic coverage an explicit part of the induced cut-state and in separating its magnitude effect from prerequisite order. The phrase `zero-duration cut` is a finite idealization: CREST has not proved that states on intervals \\( [t-\\varepsilon,t+\\varepsilon] \\) converge as \\(\\varepsilon\\to0\\), nor does it claim a continuous-time germ theorem in this manuscript.",
)

replace_once(
    "This is the practical sense in which ecological state is contract relative without being arbitrary. The scientific question is declared by the investigator, but admissible compression is constrained by semantic transport, candidate response structure, legal future queries, and the evidence required to distinguish the resulting state classes.",
    "This is the theoretical sense in which ecological state is cut- and contract-relative without being arbitrary. The pre-state semantics and query structure parameterize the problem, but once fixed they constrain a definite quotient: retrospective carriage, transverse response structure, and prospective accessibility determine which distinctions may or may not collapse at the boundary.",
)

replace_once(
    "The present need not be the ecological state. It can be the observational cut at which a state must be constructed.",
    "The present is not identified with the ecological state. In the finite theory it is a zero-duration observational cut on which state structure is induced.",
)
replace_once(
    "CREST defines retrospective history, latent response, and future-query obligations before that state, then asks which distinctions must survive their composition. The principal contribution is an identification discipline: derive history modes from carried semantics, derive latent types from candidate-safe response, identify the minimum ecological interfaces required by the future target, identify where within their semantic product that target is actually addressable, and only then compute the induced state quotient and interaction accounting.",
    "CREST defines retrospective carried history, transverse latent-present response structure, and prospective query accessibility before the state, then asks for the least quotient on the cut compatible with their distinctions. Sparse semantic access determines how much prospective structure reaches that quotient, while prerequisite structure determines where higher-order interaction appears.",
)
replace_once(
    "In this view, higher-order state interaction is not an intrinsic property of time. It is a signature of joint scientific addressability, attenuated when that addressability is semantically sparse.",
    "In this view, higher-order state interaction is not an intrinsic property of time and state is not a pre-given vector at the present. It is a property of the equivalence geometry induced across a temporal boundary, attenuated when prospective addressability is semantically sparse.",
)

replace_once(
    "Shallow-lake restoration supplies an ecology-grounded finite decision model because the same coarse current water-quality description can be compatible with different nutrient histories and different feedback structures, while restoration questions require different retained information.",
    "Shallow-lake restoration supplies a worked ecological interpretation of the abstract cut geometry because the same coarse current water-quality description can be compatible with different nutrient histories and different latent response structures, while restoration questions expose different distinctions at the boundary.",
)

MANUSCRIPT.write_text(text, encoding="utf-8")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
body = text.split("## 1. Introduction", 1)[1].split("## Literature Cited", 1)[0]
word_re = re.compile(r"\\b[A-Za-z0-9][A-Za-z0-9'’-]*\\b")
metadata["text_word_count"] = len(word_re.findall(body))
METADATA.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"reframed manuscript; inclusive main-text count={metadata['text_word_count']}")
