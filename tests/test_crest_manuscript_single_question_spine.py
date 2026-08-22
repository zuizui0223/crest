from pathlib import Path


MANUSCRIPT = Path("manuscript/crest_philosophy_biology_philosophy.md")


def test_manuscript_follows_single_question_three_gate_spine() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    markers = [
        "## 1. From ecosystem identity to state-representation adequacy",
        "## 2. Four obligations on one ecological sameness relation",
        "## 3. The mathematical answer: carrier, state, and evidence",
        "### 3.1 Gate A — Can the obligations share an admissible ecological world set?",
        "### 3.2 Gate B — What is the least-information joint state?",
        "### 3.3 Gate C — Does the evidence identify that state?",
        "### 3.4 Cross-gate result — when management changes what must be known",
        "## 4. From the formal state to ecological interpretation",
        "## 5. Ecological consequences: open futures, hidden mechanisms, and monitoring",
        "## 6. Position relative to existing adequacy and abstraction theories",
        "## 7. Limits",
        "## 8. Conclusion",
    ]

    positions = [text.index(marker) for marker in markers]
    assert positions == sorted(positions)


def test_temporally_thick_interpretation_is_not_mislabeled_as_proved() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")

    assert "temporally thicker interpretation" in text
    assert "not yet a general theorem for continuous or stochastic trajectories" in text
    assert "least-information scientific compression" in text
