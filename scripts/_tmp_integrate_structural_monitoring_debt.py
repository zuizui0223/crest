from pathlib import Path

path = Path("manuscript/crest_philosophy_biology_philosophy.md")
text = path.read_text()

anchor = "These consequences do not impose a mandatory pipeline in which future sufficiency must be checked first, followed by semantics, mechanism, and evidence."
insert = r"""Eighth, **monitoring debt can be structural rather than merely quantitative**. Consider a trait-specific performance quantity that factorizes as \(W(z)=F(z)R(z)\), where \(F\) is a local reproductive channel and \(R\) is a recruitment, establishment, or reachability channel. For any positive multiplier \(a(z)\), the two causal changes \((F,R)\mapsto(aF,R)\) and \((F,R)\mapsto(F,aR)\) produce the same net performance \(W_1(z)=a(z)F(z)R(z)\). Any monitoring scheme that is only a function of \(W\) therefore leaves those causal worlds observationally equivalent, no matter how precisely or repeatedly \(W\) is measured. Yet if a newly admissible intervention acts specifically on \(F\), the two worlds can have different counterfactual successors and can no longer safely occupy one required state. The resulting monitoring deficit cannot be repaid by more observations of the same net output. A channel-resolved observation can be required: in the positive factorization, observing \(W\) together with \(F\) recovers \(R=W/F\), and symmetrically for \(R\). Thus the minimal evidence refinement \(E\vee J\) should not be read only as a demand for greater sampling effort. In some contracts, what is missing is a new discriminating measurement channel that breaks an observational symmetry.\n\n"""

if insert.strip() in text:
    raise SystemExit("structural monitoring debt paragraph already present")
if text.count(anchor) != 1:
    raise SystemExit(f"expected one consequences anchor, found {text.count(anchor)}")
text = text.replace(anchor, insert + anchor)
path.write_text(text)
