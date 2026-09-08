from __future__ import annotations

from itertools import combinations

from crest.compositional_temporal_game import compositional_contract_bits
from crest.explicit_temporal_grammar import AXES, DecoderRule, HISTORY, MECHANISM, quotient_bits


def all_coalitions():
    for size in range(len(AXES) + 1):
        for subset in combinations(AXES, size):
            yield subset


def test_direct_value_module_is_exact_closed_form_corollary_of_explicit_grammar() -> None:
    rule = DecoderRule(frozenset((HISTORY, MECHANISM)))
    for bit_depth in (1, 2, 4, 7):
        for coalition in all_coalitions():
            assert compositional_contract_bits(bit_depth, coalition) == quotient_bits(
                bit_depth, coalition, rule
            )
