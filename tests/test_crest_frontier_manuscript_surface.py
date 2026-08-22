from pathlib import Path


MANUSCRIPT = Path('manuscript/crest_philosophy_biology_philosophy.md')


def test_cross_gate_result_is_part_of_the_target_manuscript() -> None:
    text = MANUSCRIPT.read_text()
    assert '### 3.4 Cross-gate result — when management changes what must be known' in text
    # The frontier term may remain as descriptive bookkeeping, but it is no longer
    # required to be the manuscript's mathematical headline.
    assert 'ecological state adequacy frontier' in text
    assert '**management-induced information debt**' in text
    assert 'monitoring adequacy can fail before the ecosystem changes state physically' in text
    assert 'more management capacity can create an epistemic burden' in text
    assert 'The claim is existential, not universal.' in text


def test_cross_gate_section_keeps_the_priority_firewall() -> None:
    text = MANUSCRIPT.read_text()
    assert 'The point is not a generic priority claim about representation phase transitions.' in text
    assert 'Whether this exact ecology-specific synthesis warrants any historical-priority claim remains open' in text
