from pathlib import Path
import re

path = Path("manuscript/crest_philosophy_biology_philosophy.md")
text = path.read_text()

# 1) Replace the abstract with the single-question / three-gate narrative.
abstract_start = text.index("## Abstract\n") + len("## Abstract\n")
abstract_end = text.index("\n**Keywords:**", abstract_start)
new_abstract = r'''

Ecology routinely compresses heterogeneous configurations into shared states for prediction, comparison, and management. We ask a single question: when are two ecological configurations scientifically allowed to count as the same state? CREST treats that judgment as a contract-relative commitment constrained by four currently formalized obligations: future sufficiency under declared operations, semantic coherence after structural change, robustness across retained response mechanisms, and evidential licensing. The mathematics then separates three gates. First, the obligations must admit a common ecological carrier. Second, on an admissible finite carrier they induce a unique coarsest joint partition \(J=(C_\Gamma\vee C_\mathcal H\vee C_\Theta\vee C_{D,T})(B)\); the CREST state of configuration \(u\) is its least-information block \([u]_J\). Third, the evidence must be fine enough to identify that block, although a requested target can remain reportable when the full state is unresolved. A strict control-enrichment witness shows why these gates cannot be collapsed: adding one management action can enlarge the viable carrier while forcing a finer state that unchanged monitoring no longer identifies. The minimum evidence refinement is \(E\vee J\), and a channel-factorization example shows that the resulting monitoring deficit can be structural, requiring a new measurement type rather than more replication of the same output. CREST therefore makes ecological sameness a testable scientific commitment while rejecting both a nature-given universal state partition and the claim that its four obligations exhaust ecological adequacy.
'''
text = text[:abstract_start] + new_abstract + text[abstract_end:]

# 2) Tighten Section 2 around four obligations on one state.
text = text.replace(
    "## 2. One state label, four different obligations",
    "## 2. Four obligations on one ecological sameness relation",
)
text = text.replace(
    "The four obligations can interact under refinement, so independently minimizing each row once need not recover the joint state. Their common resolution is constructed later through the J1 least common fixed point, after the common-carrier gate.",
    "The four obligations can interact under refinement, so independently minimizing each row once need not recover the joint state. They therefore feed into one mathematical question with three distinct gates: can the obligations share an admissible carrier, what is the least-information state on that carrier, and does the evidence identify it?",
)

# 3) Rebuild Section 3 in the mathematical dependency order.
sec3_start = text.index("## 3. ")
sec4_start = text.index("## 4. ", sec3_start)
sec3 = text[sec3_start:sec4_start]

matches = list(re.finditer(r"^### 3\.\d+ .*?$", sec3, flags=re.M))
if len(matches) != 4:
    raise SystemExit(f"expected exactly four Section 3 subsections, found {len(matches)}")

parts = []
for i, m in enumerate(matches):
    end = matches[i + 1].start() if i + 1 < len(matches) else len(sec3)
    parts.append(sec3[m.start():end].strip())

def classify(part: str) -> str:
    heading = part.splitlines()[0].lower()
    low = part.lower()

    # Prefer the existing subsection heading: it expresses the manuscript's present
    # organization more reliably than incidental cross-references inside the prose.
    if "carrier" in heading or "common lift" in heading:
        return "carrier"
    if "one ecological state" in heading or "joint state" in heading:
        return "state"
    if "evidence" in heading or "evidential" in heading:
        return "evidence"
    if "frontier" in heading:
        return "cross"

    # Fallbacks use distinctive mathematical content and are deliberately ordered
    # from the most specific cross-gate/evidence markers to the more general J1 text.
    if "management-induced information debt" in low or "`rescue`" in low or "adequacy frontier" in low:
        return "cross"
    if "reliability-qualified evidence partition" in low or "sharp state report" in low:
        return "evidence"
    if ("j3" in low or "j6" in low) and ("common carrier" in low or "common lift" in low):
        return "carrier"
    if "operatorname{state}" in low or ("j1" in low and "unique coarsest" in low):
        return "state"
    raise SystemExit("could not classify subsection: " + part.splitlines()[0])

classified = {}
for part in parts:
    key = classify(part)
    if key in classified:
        raise SystemExit(
            f"duplicate Section 3 classification: {key}; headings were "
            + " | ".join(p.splitlines()[0] for p in parts)
        )
    classified[key] = part

if set(classified) != {"carrier", "state", "evidence", "cross"}:
    raise SystemExit(
        f"missing Section 3 classifications: {set(classified)}; headings were "
        + " | ".join(p.splitlines()[0] for p in parts)
    )

def rehead(part: str, heading: str) -> str:
    return re.sub(r"^### 3\.\d+ .*?$", heading, part, count=1, flags=re.M)

carrier = rehead(classified["carrier"], "### 3.1 Gate A — Can the obligations share an admissible ecological world set?")
state = rehead(classified["state"], "### 3.2 Gate B — What is the least-information joint state?")
evidence = rehead(classified["evidence"], "### 3.3 Gate C — Does the evidence identify that state?")
cross = rehead(classified["cross"], "### 3.4 Cross-gate result — when management changes what must be known")

cross = cross.replace(
    "We call changes among these regimes the **ecological state adequacy frontier**.",
    "For bookkeeping, these changes can be displayed as an **ecological state adequacy frontier**. The frontier is descriptive terminology for the three gate outputs, not a fourth mathematical gate.",
)
cross = cross.replace(
    "We call this **management-induced information debt**: expanding what managers can do can expand what they must know.",
    "This strict witness motivates the descriptive phrase **management-induced information debt**: expanding what managers can do can expand what they must know.",
)

new_sec3 = r'''## 3. The mathematical answer: carrier, state, and evidence

The four obligations remain scientifically distinct, but the synthesis question asks for one state. CREST answers that question in dependency order rather than by treating its individual theorem labels as parallel results. The first issue is whether the obligations can even be synchronized on one admissible set of ecological worlds. Only then does it make sense to construct the least-information joint state. Only after that state exists can one ask whether the observation system identifies it.

This separation is essential. A carrier failure is not a bad partition, a state-refinement requirement is not an observation, and an evidence failure does not imply that the requested target is unreportable. The three gates therefore distinguish existence, representation, and identification before any cross-gate ecological consequence is considered.

''' + carrier + "\n\n" + state + "\n\n" + evidence + "\n\n" + cross + "\n\n"
text = text[:sec3_start] + new_sec3 + text[sec4_start:]

# 4) Turn Section 4 into the bridge from the finite theorem to ecology while retaining
# the important anti-relativist argument as a subsection.
old4 = "## 4. Contract-relative does not mean arbitrary\n\n"
if text.count(old4) != 1:
    raise SystemExit(f"expected one Section 4 heading, found {text.count(old4)}")
new4 = r'''## 4. From the formal state to ecological interpretation

The proved results are finite and exact, but the ecological object represented by one latent world need not be a present-time snapshot. A declared world may carry relevant history, current population or community configuration, latent response structure, and responses to future actions. CREST therefore permits a temporally thicker interpretation of ecological state: a state can compress distinctions inherited from the past and distinctions that matter only under counterfactual futures. This is an interpretation of the current latent-world formalism, not yet a general theorem for continuous or stochastic trajectories.

The ecological point is consequently narrower than saying that the observer creates the ecosystem. Underlying dynamics remain mind-independent. What changes with the scientific viewpoint or contract is the quotient through which those dynamics are represented and the obligations that quotient must satisfy.

### 4.1 Contract-relative does not mean arbitrary

'''
text = text.replace(old4, new4)

# 5) Make the ecological exit explicit.
text = text.replace(
    "## 5. Consequences for ecological explanation and measurement",
    "## 5. Ecological consequences: open futures, hidden mechanisms, and monitoring",
)
needle5 = "## 5. Ecological consequences: open futures, hidden mechanisms, and monitoring\n\nThe joint-state account changes how ecological state variables should be discussed."
repl5 = r'''## 5. Ecological consequences: open futures, hidden mechanisms, and monitoring

Ecological systems make the three-gate distinction especially consequential because state variables sit inside open, interacting, evolving, and only partially observed systems. CREST does not assume deterministic trajectories or monotonic maximization of one global fitness function. Its narrower claim is that history, interaction structure, latent response mechanisms, and accessible futures become state-relevant exactly when forgetting them violates a declared scientific obligation.

The joint-state account therefore changes how ecological state variables should be discussed.'''
if text.count(needle5) != 1:
    raise SystemExit(f"expected one Section 5 lead, found {text.count(needle5)}")
text = text.replace(needle5, repl5)

# 6) Add the temporally thick interpretation to the conclusion without promoting it to theorem status.
conclusion_anchor = "This does not turn CREST into a universal theory of ecological ontology. The framework remains conditional on declared futures, meanings, mechanisms, evidence, targets, and synchronization. Its philosophical proposal is instead that ecological sameness is a defeasible scientific commitment whose burden can change as scientific responsibilities change. What counts as the same ecological state is therefore not only contract-relative; it has a structured, testable response to changes in the contract."
if text.count(conclusion_anchor) != 1:
    raise SystemExit(f"expected one conclusion anchor, found {text.count(conclusion_anchor)}")
conclusion_repl = conclusion_anchor + "\n\n" + (
    "Ecologically, this also supports a temporally thicker interpretation without yet proving a trajectory-level theory: a present state can legitimately encode distinctions inherited from history and distinctions exposed only by possible futures when the declared scientific work makes those distinctions consequential. The resulting state is not the whole ecosystem and not merely a snapshot. It is the least-information scientific compression that the declared obligations permit."
)
text = text.replace(conclusion_anchor, conclusion_repl)

path.write_text(text)
