from pathlib import Path


MANUSCRIPT = Path('manuscript/crest_philosophy_biology_philosophy.md')


def test_cross_gate_result_is_part_of_the_target_manuscript() -> None:
    text = MANUSCRIPT.read_text()
    assert '### 4.4 Cross-gate result — when management changes what must be known' in text
    assert 'The future does not have to happen to change the present scientific state' in text
    assert 'monitoring-resolution debt' in text
    assert 'full-state identification is lost' in text
    assert 'requested target remains constant and reportable' in text
    assert 'representational claim' in text


def test_cross_gate_section_keeps_the_priority_and_scope_firewall() -> None:
    text = MANUSCRIPT.read_text()
    assert 'The common-refinement calculation itself is classical' in text
    assert 'CREST should therefore not be judged by whether any one ingredient is new.' in text
    assert 'No claim of historical priority for the generic equivalence-class idea is needed.' in text
    assert 'not backward causation' in text
