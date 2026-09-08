from __future__ import annotations

import pytest

from crest.explicit_temporal_grammar import (
    AXES,
    FUTURE,
    HISTORY,
    MECHANISM,
    DecoderRule,
    coalition_table,
    exclusive_joint_addressability,
    legal_words,
    mobius_three_way,
    quotient_size,
    worlds,
)


def fs(*items: str) -> frozenset[str]:
    return frozenset(items)


def test_world_carrier_uses_companion_primitives_not_interface_bits() -> None:
    carrier = worlds(3)
    assert len(carrier) == 32
    assert {world.history.carried_map for world in carrier} == {(0, 1), (1, 0)}
    assert {world.mechanism.response_table for world in carrier} == {(0, 0), (1, 1)}
    assert all(not isinstance(world.history, int) for world in carrier)
    assert all(not isinstance(world.mechanism, int) for world in carrier)


def test_default_typed_grammar_generates_exterior_words_only_for_grand_coalition() -> None:
    for mask in range(1 << len(AXES)):
        coalition = fs(*(AXES[i] for i in range(len(AXES)) if mask & (1 << i)))
        kinds = [word.kind for word in legal_words(4, coalition)]
        if coalition == fs(*AXES):
            assert kinds.count("exterior") == 4
        else:
            assert "exterior" not in kinds


def test_all_eight_coalition_values_are_computed_from_trace_quotients() -> None:
    m = 4
    expected_sizes = {
        fs(): 1,
        fs(HISTORY): 2,
        fs(MECHANISM): 2,
        fs(FUTURE): 1,
        fs(HISTORY, MECHANISM): 4,
        fs(HISTORY, FUTURE): 2,
        fs(MECHANISM, FUTURE): 2,
        fs(*AXES): 2 ** (m + 2),
    }
    for coalition, expected in expected_sizes.items():
        assert quotient_size(m, coalition) == expected

    table = coalition_table(m)
    assert table[fs(*AXES)] == pytest.approx(m + 2)
    assert mobius_three_way(m) == pytest.approx(m)
    assert exclusive_joint_addressability(m)


def test_interaction_order_is_determined_by_decoder_interface_requirements() -> None:
    m = 5

    no_interface = DecoderRule(frozenset())
    history_only = DecoderRule(fs(HISTORY))
    mechanism_only = DecoderRule(fs(MECHANISM))
    both = DecoderRule(fs(HISTORY, MECHANISM))

    # If F can decode without interfaces, exterior information is a main effect.
    table = coalition_table(m, no_interface)
    assert table[fs(FUTURE)] == pytest.approx(m)
    assert mobius_three_way(m, no_interface) == pytest.approx(0)
    assert not exclusive_joint_addressability(m, no_interface)

    # Requiring only one interface moves the m-bit contribution to a pairwise term.
    table_h = coalition_table(m, history_only)
    hf_dividend = table_h[fs(HISTORY, FUTURE)] - table_h[fs(HISTORY)] - table_h[fs(FUTURE)]
    assert hf_dividend == pytest.approx(m)
    assert mobius_three_way(m, history_only) == pytest.approx(0)

    table_theta = coalition_table(m, mechanism_only)
    thetaf_dividend = (
        table_theta[fs(MECHANISM, FUTURE)]
        - table_theta[fs(MECHANISM)]
        - table_theta[fs(FUTURE)]
    )
    assert thetaf_dividend == pytest.approx(m)
    assert mobius_three_way(m, mechanism_only) == pytest.approx(0)

    # Pure three-way interaction is forced exactly by two-interface completeness.
    assert mobius_three_way(m, both) == pytest.approx(m)
    assert exclusive_joint_addressability(m, both)
