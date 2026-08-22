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
        "### 4.4 Cross-gate result — when management changes what must be known",
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


def test_predictive_state_prior_art_boundary_is_explicit() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    assert "Predictive State Representations" in text
    assert "does not claim novelty for predictive equivalence" in text
    assert "does not claim to be more expressive than a sufficiently rich PSR" in text
    assert "Littman, M. L., Sutton, R. S., & Singh, S. (2002)" in text
    assert "Singh, S., James, M. R., & Rudary, M. R. (2004)" in text
