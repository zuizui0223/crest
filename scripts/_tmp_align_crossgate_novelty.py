from pathlib import Path

manuscript_path = Path("manuscript/crest_philosophy_biology_philosophy.md")
review_path = Path("docs/crest_prior_art_review_protocol_and_evidence_matrix_2026-08-21.md")
text = manuscript_path.read_text()

old_abstract = "This yields an ecological state adequacy frontier rather than a single context-free state: changes in scientific obligations can alter carrier feasibility, required state resolution, and evidential identifiability in different directions. A finite control-enrichment witness shows that adding one management action can enlarge the viable carrier while increasing the least-information state resolution beyond fixed monitoring, even though a requested target remains reportable. We call this management-induced information debt."
new_abstract = "Within CREST, these three quantities define what we call an ecological state adequacy frontier: changes in scientific obligations can alter carrier feasibility, required state resolution, and evidential identifiability in different directions. A finite control-enrichment witness shows that adding one management action can enlarge the viable carrier while increasing the least-information state resolution beyond fixed monitoring, even though a requested target remains reportable. We use management-induced information debt for this specific cross-gate pattern rather than as a claim to a new generic theory of representational obsolescence."
if text.count(old_abstract) != 1:
    raise SystemExit(f"abstract target count={text.count(old_abstract)}")
text = text.replace(old_abstract, new_abstract)

old_debt = "We call this **management-induced information debt**: expanding what managers can do can expand what they must know. The claim is existential, not universal. New actions need not always increase state resolution. The witness establishes only that greater control authority and easier state identification are not generally aligned."
new_debt = "We call this **management-induced information debt**: expanding what managers can do can expand what they must know. The claim is existential, not universal. New actions need not always increase state resolution. The witness establishes only that greater control authority and easier state identification are not generally aligned.\n\nThe associated monitoring burden can be stated exactly. For a fixed evidence partition \\(E\\) and required state partition \\(J\\), the unique coarsest refinement of the existing evidence that both preserves its distinctions and licenses deterministic full-state reporting is the common refinement \\(E\\vee J\\). CREST therefore defines the finite monitoring-resolution debt\n\n\\[\nD_E(J)=\\log_2|E\\vee J|-\\log_2|E|.\n\\]\n\nIn the `rescue` witness, full-state debt becomes \\(\\log_2(3/2)>0\\) while target debt remains zero. Across the existing CCOC extremal family, one newly relevant future action can induce \\(m\\) bits of such debt for arbitrary finite \\(m\\). The common-refinement construction is classical; the point here is its coupling to the CREST carrier/state/evidence gates."
if text.count(old_debt) != 1:
    raise SystemExit(f"debt target count={text.count(old_debt)}")
text = text.replace(old_debt, new_debt)

old_position = "The ecology-specific contribution is therefore not generic purpose-relativity, minimal abstraction, partial observability, or representation phase transitions. Those have established antecedents. CREST's narrower contribution is to couple three questions that ecological state practice often treats separately: whether the declared scientific obligations share any coherent carrier, what the unique least-information state is when they do, and whether existing evidence identifies that state. The ecological state adequacy frontier studies how those three quantities move as the contract changes. The management-enrichment witness then supplies a counterexample to a tempting intuition: increasing management capability need not simplify the epistemic problem. One additional control can enlarge the viable domain while simultaneously making the adequate state finer than the monitoring system can identify."
new_position = "The ecology-specific contribution is therefore not generic purpose-relativity, minimal abstraction, partial observability, representation phase transitions, viability analysis, or a generic link between viability and observability. Viability kernels are established tools in ecosystem management (Cury et al., 2005), and control theory has explicitly connected observability to viability-kernel constructions (Kassara, 2012). CREST's narrower contribution is the architecture produced when four separately owned obligations—future sufficiency, inherited-semantic coherence, retained-mechanism robustness, and evidence/target licensing—are imposed on one coarse ecological state equivalence and passed through an explicit carrier/state/evidence sequence. The ecological state adequacy frontier is the CREST bookkeeping of how those three gate outputs move as the contract changes, not a priority claim for generic adequacy regions. The management-enrichment witness then supplies the stronger cross-gate result: one additional control can enlarge the viable domain, force a finer adequate state, make that state unidentifiable under fixed monitoring, and still leave the declared target reportable. The exact state-versus-target monitoring debt makes that coupling quantitative."
if text.count(old_position) != 1:
    raise SystemExit(f"position target count={text.count(old_position)}")
text = text.replace(old_position, new_position)

old_conclusion = "CREST makes a stronger claim than that ecological states are purpose-relative. For a fixed coherent contract, the adequate state is the unique coarsest equivalence that preserves the distinctions required for the declared scientific work:"
new_conclusion = "CREST makes a more specific claim than the already established point that ecological representations can be purpose-relative. For a fixed coherent contract, the adequate state is the unique coarsest equivalence that preserves the distinctions required for the declared scientific work:"
if text.count(old_conclusion) != 1:
    raise SystemExit(f"conclusion target count={text.count(old_conclusion)}")
text = text.replace(old_conclusion, new_conclusion)

refs = {
    "cury": "Cury, P. M., Mullon, C., Garcia, S. M., & Shannon, L. J. (2005). Viability theory for an ecosystem approach to fisheries. *ICES Journal of Marine Science*, 62(3), 577–584. https://doi.org/10.1016/j.icesjms.2004.10.007",
    "kassara": "Kassara, K. (2012). Observability by using viability kernels. *Journal of Control Theory and Applications*, 10(3), 303–308. https://doi.org/10.1007/s11768-012-1022-x",
}
if refs["cury"] not in text:
    anchor = "Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129"
    if text.count(anchor) != 1:
        raise SystemExit("Cury reference anchor not unique")
    text = text.replace(anchor, anchor + "\n\n" + refs["cury"])
if refs["kassara"] not in text:
    anchor = "Giere, R. N. (2010). An Agent-Based Conception of Models and Scientific Representation. *Synthese*, 172(2), 269–281. https://doi.org/10.1007/s11229-009-9506-z"
    if text.count(anchor) != 1:
        raise SystemExit("Kassara reference anchor not unique")
    text = text.replace(anchor, anchor + "\n\n" + refs["kassara"])

manuscript_path.write_text(text)

review = review_path.read_text()
marker = "## 13. Targeted cross-gate exact-match check — control, viability and observability"
if marker not in review:
    review += """

---

## 13. Targeted cross-gate exact-match check — control, viability and observability

A final targeted search asked whether the strongest surviving CREST result is already explicit in control theory or ecological management: **expanding an admissible management-action repertoire enlarges the viable domain while simultaneously forcing a finer adequate state, making that state unidentifiable under fixed evidence, yet leaving a declared target reportable.**

Additional query families included combinations of `action set`, `control authority`, `viability kernel`, `observability`, `state distinguishability`, `monitoring`, `partial observability`, `state abstraction`, and `ecosystem management`.

### Closest prior art found

- Cury et al. (2005), *Viability theory for an ecosystem approach to fisheries*, establishes viability kernels as ecological-management objects whose size depends on admissible controls and constraints.
- Ecosystem-management viability work more generally shows that regulation through available controls can enlarge the set of states from which ecological constraints can be maintained.
- Kassara (2012), *Observability by using viability kernels*, and Kassara (2013), *A Set-Valued Approach to Observability*, explicitly connect observability and viability-kernel constructions in control theory.
- POMDP and adaptive-management literature already combines actions, partial observability, monitoring and decision value.
- Automata/state-learning literature already uses richer input alphabets to expose otherwise indistinguishable states.

### Novelty consequence

These findings block any claim that CREST first links **viability and observability**, first shows that admissible controls change a viable set, or first shows that richer inputs can expose latent state distinctions.

No direct match was located in this audit for the full CREST cross-gate conjunction:

\[
\text{action repertoire expansion}
\Rightarrow
\text{viable carrier}\uparrow,
\quad |J|\uparrow,
\quad \text{fixed-evidence full-state identification}\downarrow,
\quad \text{target reportability preserved},
\]

with the required monitoring repair characterized by the unique common refinement `E ∨ J` and with the CCOC family yielding arbitrarily large finite monitoring-resolution debt from one newly relevant future action.

This remains a **no-direct-match result from the present audit**, not evidence of historical firstness.

### Final priority rule

The manuscript should sell the **cross-gate conjunction and theorem-backed architecture**, not any of its generic ingredients. If future literature supplies the same conjunction, CREST remains defensible as an ecology-specific theorem-grounded synthesis, but the novelty language must be reduced again.
"""
    review_path.write_text(review)
