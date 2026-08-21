from pathlib import Path

path = Path('manuscript/crest_philosophy_biology_philosophy.md')
text = path.read_text()

abstract = '''Ecology routinely compresses heterogeneous configurations into shared states for prediction, comparison, and management. We ask when that compression remains scientifically adequate as the work assigned to a state changes. CREST distinguishes four currently formalized obligations: future sufficiency under declared operations, semantic coherence after structural change, robustness across retained response mechanisms, and evidence-relative target resolution. On one admissible finite common carrier, these obligations induce a unique coarsest joint partition \\(J\\); the CREST state of configuration \\(u\\) is its block \\([u]_J\\), the least-information equivalence class preserving every distinction forced by the declared contract. A separate evidence gate asks whether the required block is actually identified. This yields an ecological state adequacy frontier rather than a single context-free state: changes in scientific obligations can alter carrier feasibility, required state resolution, and evidential identifiability in different directions. A finite control-enrichment witness shows that adding one management action can enlarge the viable carrier while increasing the least-information state resolution beyond fixed monitoring, even though a requested target remains reportable. We call this management-induced information debt. CREST therefore treats ecological state equivalence as a testable scientific commitment and shows why increased management capability can increase, rather than reduce, what must be known about the system. The account is contract-relative but not arbitrary, and it does not claim that the four obligations are exhaustive or that nature supplies one intrinsic state partition.'''

start = text.index('## Abstract\n\n') + len('## Abstract\n\n')
end = text.index('\n\n**Keywords:**', start)
text = text[:start] + abstract + text[end:]

section34 = r'''### 3.4 The ecological state adequacy frontier

The preceding results suggest that one ecological state should not be viewed only as the output of a fixed modelling contract. A second question is how the required state changes when the scientific contract itself changes. Let \(\mathcal C\) denote a declared contract and let \(J_{\mathcal C}\) be its J1 state whenever the relevant carrier gate is admissible. For an evidence record \(e\), let

\[
\mathcal S_{\mathcal C}(e)
=
\{[u]_{J_{\mathcal C}}:u\text{ remains compatible with }e\}.
\]

CREST therefore associates a contract not only with a state partition but with three separable quantities: whether a coherent carrier exists, how fine the least-information adequate state must be, and how many such state blocks remain compatible with the evidence. We call changes among these regimes the **ecological state adequacy frontier**.

The frontier has an order-theoretic asymmetry. Along a comparison in which a stronger contract requires a refinement of the earlier state while the evidence is held fixed, the required state-information burden cannot decrease. If that fixed evidence already fails to identify the coarser state, refining the state cannot restore identification. Conversely, evidence that identifies a finer state necessarily identifies its coarsenings. Scientific requirements can therefore outrun an unchanged monitoring programme.

This effect need not be gradual. The CCOC extremal family shows that adding one previously illegal primitive future action can increase exact state memory by an arbitrary number of bits across a finite family. The point is not a generic priority claim about representation phase transitions. It is that a small change in the ecological future or intervention contract can make a previously adequate ecological classification severely under-resolved even before the physical configuration has changed.

A finite cross-gate witness makes the management implication sharper. Before enrichment, a controlled contract admits a two-world viable carrier whose two required states are identified by the declared evidence. Adding one controllable `rescue` action makes a third world viable. Yet the same action gives two candidate worlds different future behavior, so J1 must split them. The viable carrier therefore expands while the required state count increases from two to three. Because the original monitoring record still merges those two worlds, full-state identification is lost. The requested target remains constant across them and is still reportable.

We call this **management-induced information debt**: expanding what managers can do can expand what they must know. The claim is existential, not universal. New actions need not always increase state resolution. The witness establishes only that greater control authority and easier state identification are not generally aligned.

'''
marker4 = '## 4. Contract-relative does not mean arbitrary'
if '### 3.4 The ecological state adequacy frontier' not in text:
    text = text.replace(marker4, section34 + marker4, 1)

extra_consequences = '''Sixth, **monitoring adequacy can fail before the ecosystem changes state physically**. A monitoring programme may correctly identify the least-information state required under one intervention repertoire. If restoration, reconnection, colonization, invasion, or management innovation makes new futures scientifically relevant, the required state can refine while the observations remain unchanged. The monitoring programme can therefore become inadequate because the counterfactual responsibilities assigned to the state expanded, not because sensor quality deteriorated or because the ecosystem already crossed a physical regime threshold.

Seventh, **more management capacity can create an epistemic burden**. Additional management options can make previously irrelevant differences consequential. In that regime, increasing control authority and increasing knowledge requirements occur together. This suggests that the design of a new intervention should be coupled to an audit of whether existing monitoring resolves the state distinctions that the intervention makes consequential.

'''
consequence_marker = 'These consequences do not impose a mandatory pipeline'
if 'monitoring adequacy can fail before the ecosystem changes state physically' not in text:
    text = text.replace(consequence_marker, extra_consequences + consequence_marker, 1)

old_contribution = '''The ecology-specific contribution is the mapping between distinct scientific obligations and one contract-relative state representation, together with explicit carrier and evidence gates. The four companion programmes provide differently structured failure conditions; J1 shows how their state-resolution requirements can be combined on one carrier; J3/J6 show that the carrier itself can fail; and the evidence gate prevents a required state resolution from being mistaken for an observed state.'''
new_contribution = '''The ecology-specific contribution is therefore not generic purpose-relativity, minimal abstraction, partial observability, or representation phase transitions. Those have established antecedents. CREST's narrower contribution is to couple three questions that ecological state practice often treats separately: whether the declared scientific obligations share any coherent carrier, what the unique least-information state is when they do, and whether existing evidence identifies that state. The ecological state adequacy frontier studies how those three quantities move as the contract changes. The management-enrichment witness then supplies a counterexample to a tempting intuition: increasing management capability need not simplify the epistemic problem. One additional control can enlarge the viable domain while simultaneously making the adequate state finer than the monitoring system can identify.'''
if old_contribution not in text:
    raise SystemExit('contribution paragraph marker not found')
text = text.replace(old_contribution, new_contribution, 1)

new_conclusion = r'''## 8. Conclusion

CREST makes a stronger claim than that ecological states are purpose-relative. For a fixed coherent contract, the adequate state is the unique coarsest equivalence that preserves the distinctions required for the declared scientific work:

\[
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B),
\qquad
\operatorname{State}_{\mathcal C}(u)=[u]_J.
\]

Across changing contracts, however, state adequacy has a frontier: the coherent carrier, the minimum required state resolution, and the evidence-compatible state set can move differently. A state may remain mathematically well defined after it ceases to be observationally identifiable; a target may remain reportable after full-state identification is lost; and a strengthened contract may eventually cease to admit any fully adequate joint state.

The finite management-enrichment witness exposes an ecological consequence. Adding an available intervention can make more configurations viable while simultaneously increasing the distinctions that a usable state must encode. Existing monitoring may then become inadequate before the ecosystem has undergone any physical regime shift. In this sense, management capability can create information debt: expanding what can be done can expand what must be known.

This does not turn CREST into a universal theory of ecological ontology. The framework remains conditional on declared futures, meanings, mechanisms, evidence, targets, and synchronization. Its philosophical proposal is instead that ecological sameness is a defeasible scientific commitment whose burden can change as scientific responsibilities change. What counts as the same ecological state is therefore not only contract-relative; it has a structured, testable response to changes in the contract.

'''
conclusion_start = text.index('## 8. Conclusion')
declarations = text.index('## Statements and Declarations', conclusion_start)
text = text[:conclusion_start] + new_conclusion + text[declarations:]

note_marker = '- The manuscript now distinguishes unconditional/cross-contract global minimality (not claimed) from J1 conditional unique coarseness on a declared admissible finite common carrier (proved).'
replacement_note = note_marker + '\n- The manuscript now foregrounds the ecological state adequacy frontier and the finite management-induced information-debt witness; neither is presented as a historical-firstness claim.'
if note_marker not in text:
    raise SystemExit('submission note marker not found')
text = text.replace(note_marker, replacement_note, 1)

path.write_text(text)
