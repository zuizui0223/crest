from pathlib import Path

path = Path("manuscript/crest_philosophy_biology_philosophy.md")
text = path.read_text()

old = """Philosophy of ecology has long examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has likewise developed explicit adequacy protocols (Getz et al., 2018), intervention-sensitive State-and-Transition Models (Stringham et al., 2003), adaptive-management and POMDP approaches to hidden state and model uncertainty (Nicol & Chadès, 2012; Fackler & Pacifici, 2014), and extensive work on model transferability under novel conditions (Yates et al., 2018). In adjacent formal fields, causal states and causal abstraction already provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling also treats adequacy as purpose-sensitive rather than reducible to one context-free notion of fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021)."""

new = """Philosophy of ecology has long examined the identity and continuity of ecological systems, including dynamical accounts of ecosystem identity and distinctions among different senses of ecological identity (Cumming & Collier, 2005; Collier & Cumming, 2011; Delettre, 2021). Ecological modelling has gone further than merely using state labels: explicit equivalence criteria for ecosystem states have been proposed (Boit & Spencer, 2019), model-adequacy protocols already scrutinize state variables, control variables, data determinacy and coarse graining (Getz et al., 2018), and State-and-Transition Models make ecological states intervention-sensitive (Stringham et al., 2003). Conservation decision theory likewise separates hidden ecological state from observation and has developed management-relevant state reduction in POMDPs, including explicit arguments for reducing state and observation variables to the smallest ensemble needed for the decision problem (Nicol & Chadès, 2012; Chadès et al., 2021), while structural and observational uncertainty can be treated jointly (Fackler & Pacifici, 2014). Monitoring itself is already understood as adaptive: long-term programmes may be redesigned as scientific and policy questions change (Lindenmayer & Likens, 2009; Lindenmayer et al., 2011). Ecological model transferability under novel conditions is also an established problem (Yates et al., 2018). In adjacent formal fields, causal states, state abstraction, and causal abstraction provide mature accounts of prediction- or intervention-preserving coarse representations (Shalizi & Crutchfield, 2001; Beckers & Halpern, 2019). General philosophy of modelling treats adequacy as purpose-sensitive rather than reducible to one context-free notion of fidelity (Giere, 2010; Parker, 2020; Bokulich & Parker, 2021), and this adequacy-for-purpose perspective has now been articulated explicitly for the environmental sciences (Parker et al., 2026)."""

if text.count(old) != 1:
    raise SystemExit(f"expected exactly one background paragraph, found {text.count(old)}")
text = text.replace(old, new)

ref_insertions = [
    (
        "Bokulich, A., & Parker, W. (2021). Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science*, 11(1), Article 31. https://doi.org/10.1007/s13194-020-00345-2\n",
        "\nBoit, A., & Spencer, M. (2019). Equivalence and dissimilarity of ecosystem states. *Ecological Modelling*, 396, 12–22. https://doi.org/10.1016/j.ecolmodel.2019.01.009\n",
    ),
    (
        "Cumming, G. S., & Collier, J. (2005). Change and identity in complex systems. *Ecology and Society*, 10(1), Article 29. https://doi.org/10.5751/ES-01252-100129\n",
        "\nChadès, I., Pascal, L. V., Nicol, S., Fletcher, C. S., & Ferrer-Mestres, J. (2021). A primer on partially observable Markov decision processes (POMDPs). *Methods in Ecology and Evolution*, 12(11), 2058–2072. https://doi.org/10.1111/2041-210X.13692\n",
    ),
    (
        "Giere, R. N. (2010). An Agent-Based Conception of Models and Scientific Representation. *Synthese*, 172(2), 269–281. https://doi.org/10.1007/s11229-009-9506-z\n",
        "\nLindenmayer, D. B., & Likens, G. E. (2009). Adaptive monitoring: a new paradigm for long-term research and monitoring. *Trends in Ecology & Evolution*, 24(9), 482–486. https://doi.org/10.1016/j.tree.2009.03.005\n\nLindenmayer, D. B., Likens, G. E., Haywood, A., & Miezis, L. (2011). Adaptive monitoring in the real world: proof of concept. *Trends in Ecology & Evolution*, 26(12), 641–646. https://doi.org/10.1016/j.tree.2011.08.002\n",
    ),
    (
        "Parker, W. S. (2020). Model Evaluation: An Adequacy-for-Purpose View. *Philosophy of Science*, 87(3), 457–477. https://doi.org/10.1086/708691\n",
        "\nParker, W. S., Carey, C. C., Olsson, F., & Thomas, R. Q. (2026). An adequacy-for-purpose perspective for the environmental sciences. *Frontiers in Ecology and the Environment*, Early View, e70058. https://doi.org/10.1002/fee.70058\n",
    ),
]
for anchor, addition in ref_insertions:
    if text.count(anchor) != 1:
        raise SystemExit(f"reference anchor count {text.count(anchor)} for {anchor[:40]!r}")
    text = text.replace(anchor, anchor + addition)

path.write_text(text)
