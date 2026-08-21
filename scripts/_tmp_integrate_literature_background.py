from pathlib import Path

path = Path("manuscript/crest_philosophy_biology_philosophy.md")
text = path.read_text()

old = """Philosophy of ecology has long examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has likewise developed explicit adequacy protocols (Getz et al., 2018), intervention-sensitive State-and-Transition Models (Stringham et al., 2003), adaptive-management and POMDP approaches to hidden state and model uncertainty (Nicol & Chadès, 2012; Fackler & Pacifici, 2014), and extensive work on model transferability under novel conditions (Yates et al., 2018). In adjacent formal fields, causal states and causal abstraction already provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling also treats adequacy as purpose-sensitive rather than reducible to one context-free notion of fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021)."""

new = """Philosophy of ecology has long examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has gone further than merely using state labels: explicit equivalence criteria for ecosystem states have been proposed (Boit & Spencer, 2019), model-adequacy protocols already scrutinize state variables, control variables, data determinacy and coarse graining (Getz et al., 2018), and State-and-Transition Models make ecological states intervention-sensitive (Stringham et al., 2003). Conservation decision theory likewise separates hidden ecological state from observation and has developed management-relevant state reduction in POMDPs, including explicit arguments for reducing state and observation variables to the smallest ensemble needed for the decision problem (Nicol & Chadès, 2012; Chadès et al., 2021), while structural and observational uncertainty can be treated jointly (Fackler & Pacifici, 2014). Monitoring itself is already understood as adaptive: long-term programmes may be redesigned as scientific and policy questions change (Lindenmayer & Likens, 2009; Lindenmayer et al., 2011). Ecological model transferability under novel conditions is also an established problem (Yates et al., 2018). In adjacent formal fields, causal states, state abstraction, and causal abstraction provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling treats adequacy as purpose-sensitive rather than reducible to one context-free notion of fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021), and this adequacy-for-purpose perspective has now been articulated explicitly for the environmental sciences (Parker et al., 2026)."""

if old in text:
    if text.count(old) != 1:
        raise SystemExit("background paragraph unexpectedly duplicated")
    text = text.replace(old, new)
elif text.count(new) != 1:
    raise SystemExit("neither old nor integrated background paragraph found exactly once")

references = {
    "boit": "Boit, A., & Spencer, M. (2019). Equivalence and dissimilarity of ecosystem states. *Ecological Modelling*, 396, 12–22. https://doi.org/10.1016/j.ecolmodel.2019.01.009",
    "chades": "Chadès, I., Pascal, L. V., Nicol, S., Fletcher, C. S., & Ferrer-Mestres, J. (2021). A primer on partially observable Markov decision processes (POMDPs). *Methods in Ecology and Evolution*, 12(11), 2058–2072. https://doi.org/10.1111/2041-210X.13692",
    "linden2009": "Lindenmayer, D. B., & Likens, G. E. (2009). Adaptive monitoring: a new paradigm for long-term research and monitoring. *Trends in Ecology & Evolution*, 24(9), 482–486. https://doi.org/10.1016/j.tree.2009.03.005",
    "linden2011": "Lindenmayer, D. B., Likens, G. E., Haywood, A., & Miezis, L. (2011). Adaptive monitoring in the real world: proof of concept. *Trends in Ecology & Evolution*, 26(12), 641–646. https://doi.org/10.1016/j.tree.2011.08.002",
    "parker2026": "Parker, W. S., Carey, C. C., Olsson, F., & Thomas, R. Q. (2026). An adequacy-for-purpose perspective for the environmental sciences. *Frontiers in Ecology and the Environment*, Early View, e70058. https://doi.org/10.1002/fee.70058",
}

# Insert missing audited references. Anchors are stable published references already in the manuscript.
insert_specs = [
    (references["boit"], "Bokulich, A., & Parker, W. (2021). Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science*, 11(1), Article 31. https://doi.org/10.1007/s13194-020-00345-2"),
    (references["chades"], "Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129"),
    (references["linden2009"] + "\n\n" + references["linden2011"], "Giere, R. N. (2010). An Agent-Based Conception of Models and Scientific Representation. *Synthese*, 172(2), 269–281. https://doi.org/10.1007/s11229-009-9506-z"),
    (references["parker2026"], "Parker, W. S. (2020). Model Evaluation: An Adequacy-for-Purpose View. *Philosophy of Science*, 87(3), 457–477. https://doi.org/10.1086/708691"),
]
for addition, anchor in insert_specs:
    first_line = addition.splitlines()[0]
    if first_line not in text:
        if text.count(anchor) != 1:
            raise SystemExit(f"reference anchor not unique: {anchor[:50]}")
        text = text.replace(anchor, anchor + "\n\n" + addition)

# Keep the local B/C reference block alphabetic after the insertions.
items = {
    "Beckers": "Beckers, S., & Halpern, J. Y. (2019). Abstracting Causal Models. *Proceedings of the AAAI Conference on Artificial Intelligence*, 33(01), 2678–2685. https://doi.org/10.1609/aaai.v33i01.33012678",
    "Boit": references["boit"],
    "Bokulich": "Bokulich, A., & Parker, W. (2021). Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science*, 11(1), Article 31. https://doi.org/10.1007/s13194-020-00345-2",
    "Chadès": references["chades"],
    "Collier": "Collier, J., & Cumming, G. S. (2011). A Dynamical Approach to Ecosystem Identity. In *Philosophy of Ecology*, Handbook of the Philosophy of Science, Vol. 11, pp. 201–218. Elsevier. https://doi.org/10.1016/B978-0-444-51673-2.50008-X",
    "Cumming": "Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129",
    "Delettre": "Delettre, O. (2021). Identity of ecological systems and the meaning of resilience. *Journal of Ecology*, 109, 3147–3156. https://doi.org/10.1111/1365-2745.13655",
}
start = text.index(items["Beckers"])
end = text.index(items["Delettre"]) + len(items["Delettre"])
current_block = text[start:end]
for item in items.values():
    if current_block.count(item) != 1:
        raise SystemExit(f"reference block item missing/duplicated: {item[:45]}")
sorted_block = "\n\n".join(items[name] for name in ("Beckers", "Boit", "Bokulich", "Chadès", "Collier", "Cumming", "Delettre"))
text = text[:start] + sorted_block + text[end:]

path.write_text(text)
