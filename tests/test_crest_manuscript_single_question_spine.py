from pathlib import Path


MANUSCRIPT = Path("manuscript/crest_philosophy_biology_philosophy.md")


def test_manuscript_follows_trajectory_first_state_spine() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    markers = [
        "## 1. Why ecological state is a compression problem",
        "## 2. From temporally extended worlds to scientific states",
        "### 2.2 Snapshot sufficiency is a factorization criterion, not an assumption",
        "## 3. Three structural obstructions and one evidence gate",
        "### 3.1 Future insufficiency — CCOC",
        "### 3.2 Historical and semantic insufficiency — MLTR",
        "### 3.3 Mechanistic insufficiency — MRM",
        "### 3.4 Evidence licensing — CED",
        "## 4. The finite mathematical answer: carrier, state, and evidence",
        "### 4.1 Gate A — Can the requirements share an admissible ecological world set?",
        "### 4.2 Gate B — What is the least-information adequate state?",
        "### 4.3 Gate C — Does the evidence identify that state?",
        "### 4.4 Cross-gate direction — capability can enlarge the carrier and refine the state",
        "### 4.5 Cross-gate scale separation — capability–resolution divergence",
        "### 4.6 Monitoring-resolution debt",
        "## 5. Quotient laws and representational stability",
        "## 6. Position relative to existing theories",
        "## 7. Limits",
        "## 8. Conclusion",
    ]

    positions = [text.index(marker) for marker in markers]
    assert positions == sorted(positions)


def test_temporally_extended_interpretation_is_not_mislabeled_as_proved() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    assert "scientifically licensed compression of a temporally extended ecological world" in text
    assert "not yet a general theorem for continuous or stochastic trajectories" in text
    assert "Snapshot sufficiency is a factorization criterion" in text
    assert "CED is deliberately downstream" in text
    assert "representational stability" in text
    assert "not backward causation" in text


def test_predictive_and_action_abstraction_prior_art_boundaries_are_explicit() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    assert "Predictive State Representations" in text
    assert "does not claim novelty for predictive equivalence" in text
    assert "does not claim to be more expressive than a sufficiently rich PSR" in text
    assert "Littman, M. L., Sutton, R. S., & Singh, S. (2002)" in text
    assert "Singh, S., James, M. R., & Rudary, M. R. (2004)" in text

    assert "Konidaris (2019)" in text
    assert "state and action abstraction as coupled problems" in text
    assert "The CREST result is therefore **not** the qualitative proposition" in text
    assert "Konidaris, G. (2019). On the necessity of abstraction." in text


def test_scaling_theorem_is_the_quantitative_headline() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    assert "\\Delta |K^*|=1" in text
    assert "\\Delta K_{U_0}=m" in text
    assert "no universal finite function" in text
    assert "full-state licensing changes from yes to no" in text
    assert "Viability gain alone therefore cannot upper-bound" in text
