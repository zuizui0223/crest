from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "artifacts" / "temporal_cut_definition_dependency_dag_2026-09-08.json"


def _load() -> dict:
    return json.loads(PATH.read_text(encoding="utf-8"))


def _assert_acyclic(nodes: dict[str, list[str]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visited:
            return
        if node in visiting:
            raise AssertionError(f"dependency cycle detected at {node}")
        visiting.add(node)
        for dep in nodes[node]:
            assert dep in nodes, f"unknown dependency {dep!r} of {node!r}"
            visit(dep)
        visiting.remove(node)
        visited.add(node)

    for node in nodes:
        visit(node)


def _ancestors(nodes: dict[str, list[str]], node: str) -> set[str]:
    result: set[str] = set()
    stack = list(nodes[node])
    while stack:
        current = stack.pop()
        if current in result:
            continue
        result.add(current)
        stack.extend(nodes[current])
    return result


def test_temporal_cut_definition_graph_is_acyclic() -> None:
    payload = _load()
    _assert_acyclic(payload["nodes"])


def test_final_state_is_downstream_of_all_three_responsibilities() -> None:
    payload = _load()
    nodes = payload["nodes"]
    final_state = payload["final_state_node"]
    ancestors = _ancestors(nodes, final_state)

    assert "history_type_H" in ancestors
    assert "mechanism_type_Theta" in ancestors
    assert "future_type_F" in ancestors


def test_final_state_does_not_define_pre_state_responsibilities() -> None:
    payload = _load()
    nodes = payload["nodes"]
    final_state = payload["final_state_node"]

    for node in payload["pre_state_responsibility_nodes"]:
        assert final_state not in _ancestors(nodes, node), (
            f"pre-state responsibility {node} depends on final state {final_state}"
        )


def test_final_state_is_a_sink() -> None:
    payload = _load()
    nodes = payload["nodes"]
    final_state = payload["final_state_node"]

    dependents = {node for node, deps in nodes.items() if final_state in deps}
    assert dependents == set()


def test_companion_quantifier_firewall_is_encoded() -> None:
    payload = _load()
    nodes = payload["nodes"]

    assert nodes["history_type_H"] == ["history_carried_map_c_p"]
    assert "candidate_family_C" in nodes["mechanism_type_Theta"]
    assert "future_grammar_L" in nodes["future_trace_profile_rho"]
    assert "M_ccoc" in nodes["future_trace_profile_rho"]

    # The MRM mechanism type and CCOC future type have different primitive parents.
    mechanism_ancestors = _ancestors(nodes, "mechanism_type_Theta")
    future_ancestors = _ancestors(nodes, "future_type_F")
    assert "candidate_family_C" in mechanism_ancestors
    assert "future_grammar_L" not in mechanism_ancestors
    assert "future_grammar_L" in future_ancestors
    assert "candidate_family_C" not in future_ancestors
