"""Explicit finite grammar/trace construction for CREST temporal interaction.

This module replaces direct coalition-bit assignment with a falsifiable pipeline:

primitive companion objects -> generated legal grammar -> traces -> quotient.

MLTR history is represented by replacement-history primitives carrying terminal
maps. MRM mechanism is represented by primitive candidate laws carrying response
tables. CCOC future responsibility contributes decoder primitives. Exterior
queries are well-typed compositions that require both companion interfaces before
an F decoder can be applied.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import log2
from typing import Iterable

HISTORY = "H"
MECHANISM = "THETA"
FUTURE = "F"
AXES = (HISTORY, MECHANISM, FUTURE)


@dataclass(frozen=True)
class HistoryPrimitive:
    """MLTR-like raw replacement history with a complete carried terminal map."""

    name: str
    carried_map: tuple[int, ...]


@dataclass(frozen=True)
class MechanismPrimitive:
    """MRM-like primitive candidate law represented by a complete response table."""

    name: str
    response_table: tuple[int, ...]


@dataclass(frozen=True)
class World:
    history: HistoryPrimitive
    mechanism: MechanismPrimitive
    exterior: tuple[int, ...]


@dataclass(frozen=True)
class Word:
    """A well-typed observable word generated from responsibility primitives."""

    kind: str
    index: int | None = None


@dataclass(frozen=True)
class DecoderRule:
    """Typing rule for an exterior decoder.

    By default the decoder consumes both the MLTR-derived history interface and
    MRM-derived mechanism interface. Changing this rule is an explicit model
    perturbation and can destroy pure three-way interaction; tests use that fact
    as a falsifiability check.
    """

    required_interfaces: frozenset[str] = frozenset((HISTORY, MECHANISM))

    def __post_init__(self) -> None:
        if not self.required_interfaces.issubset((HISTORY, MECHANISM)):
            raise ValueError("decoder prerequisites may only use H and THETA")


HISTORY_PRIMITIVES = (
    HistoryPrimitive("p0", (0, 1)),
    HistoryPrimitive("p1", (1, 0)),
)

MECHANISM_PRIMITIVES = (
    MechanismPrimitive("theta0", (0, 0)),
    MechanismPrimitive("theta1", (1, 1)),
)


def history_interface(history: HistoryPrimitive) -> tuple[int, ...]:
    """Retained MLTR interface derived from complete carried-map semantics."""

    return history.carried_map


def mechanism_interface(mechanism: MechanismPrimitive) -> tuple[int, ...]:
    """Retained MRM interface derived from the primitive response table."""

    return mechanism.response_table


def worlds(bit_depth: int) -> tuple[World, ...]:
    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")
    return tuple(
        World(history, mechanism, exterior)
        for history in HISTORY_PRIMITIVES
        for mechanism in MECHANISM_PRIMITIVES
        for exterior in product((0, 1), repeat=bit_depth)
    )


def normalize_coalition(coalition: Iterable[str]) -> frozenset[str]:
    members = frozenset(coalition)
    if not members.issubset(AXES):
        raise ValueError("coalition contains an unknown responsibility")
    return members


def legal_words(
    bit_depth: int,
    coalition: Iterable[str],
    decoder_rule: DecoderRule = DecoderRule(),
) -> tuple[Word, ...]:
    """Generate legal observable words by compositional typing.

    H supplies access to a carried-map interface; THETA supplies access to a
    response-table interface; F supplies decoder primitives. An exterior word is
    generated only when F is present and every interface required by the decoder
    typing rule is available. No coalition bit value is assigned here.
    """

    if not isinstance(bit_depth, int) or isinstance(bit_depth, bool) or bit_depth < 1:
        raise ValueError("bit_depth must be a positive integer")
    members = normalize_coalition(coalition)
    words: list[Word] = []

    if HISTORY in members:
        words.append(Word("history"))
    if MECHANISM in members:
        words.append(Word("mechanism"))

    interfaces_available = decoder_rule.required_interfaces.issubset(members)
    if FUTURE in members and interfaces_available:
        words.extend(Word("exterior", i) for i in range(bit_depth))
    return tuple(words)


def trace(world: World, word: Word) -> tuple[int, ...] | int:
    if word.kind == "history":
        return history_interface(world.history)
    if word.kind == "mechanism":
        return mechanism_interface(world.mechanism)
    if word.kind == "exterior":
        if word.index is None or not 0 <= word.index < len(world.exterior):
            raise ValueError("invalid exterior decoder index")
        return world.exterior[word.index]
    raise ValueError(f"unknown word kind: {word.kind}")


def trace_profile(
    world: World, grammar: tuple[Word, ...]
) -> tuple[tuple[int, ...] | int, ...]:
    return tuple(trace(world, word) for word in grammar)


def induced_classes(
    bit_depth: int,
    coalition: Iterable[str],
    decoder_rule: DecoderRule = DecoderRule(),
) -> tuple[tuple[World, ...], ...]:
    """Exact quotient induced by equality of every legal trace."""

    grammar = legal_words(bit_depth, coalition, decoder_rule)
    buckets: dict[tuple[tuple[int, ...] | int, ...], list[World]] = {}
    for world in worlds(bit_depth):
        buckets.setdefault(trace_profile(world, grammar), []).append(world)
    return tuple(tuple(bucket) for bucket in buckets.values())


def quotient_size(
    bit_depth: int,
    coalition: Iterable[str],
    decoder_rule: DecoderRule = DecoderRule(),
) -> int:
    return len(induced_classes(bit_depth, coalition, decoder_rule))


def quotient_bits(
    bit_depth: int,
    coalition: Iterable[str],
    decoder_rule: DecoderRule = DecoderRule(),
) -> float:
    return log2(quotient_size(bit_depth, coalition, decoder_rule))


def coalition_table(
    bit_depth: int, decoder_rule: DecoderRule = DecoderRule()
) -> dict[frozenset[str], float]:
    table: dict[frozenset[str], float] = {}
    for mask in range(1 << len(AXES)):
        coalition = frozenset(AXES[i] for i in range(len(AXES)) if mask & (1 << i))
        table[coalition] = quotient_bits(bit_depth, coalition, decoder_rule)
    return table


def mobius_three_way(
    bit_depth: int, decoder_rule: DecoderRule = DecoderRule()
) -> float:
    v = coalition_table(bit_depth, decoder_rule)
    h = frozenset((HISTORY,))
    theta = frozenset((MECHANISM,))
    future = frozenset((FUTURE,))
    htheta = h | theta
    hf = h | future
    thetaf = theta | future
    grand = frozenset(AXES)
    empty = frozenset()
    return (
        v[grand]
        - v[htheta]
        - v[hf]
        - v[thetaf]
        + v[h]
        + v[theta]
        + v[future]
        - v[empty]
    )


def exclusive_joint_addressability(
    bit_depth: int, decoder_rule: DecoderRule = DecoderRule()
) -> bool:
    """Check exterior invisibility for proper coalitions from generated grammars."""

    grand = frozenset(AXES)
    grand_grammar = legal_words(bit_depth, grand, decoder_rule)
    if not any(word.kind == "exterior" for word in grand_grammar):
        return False

    for mask in range(1 << len(AXES)):
        coalition = frozenset(AXES[i] for i in range(len(AXES)) if mask & (1 << i))
        grammar = legal_words(bit_depth, coalition, decoder_rule)
        if coalition != grand and any(word.kind == "exterior" for word in grammar):
            return False
    return True


__all__ = [
    "AXES",
    "DecoderRule",
    "FUTURE",
    "HISTORY",
    "HISTORY_PRIMITIVES",
    "HistoryPrimitive",
    "MECHANISM",
    "MECHANISM_PRIMITIVES",
    "MechanismPrimitive",
    "World",
    "Word",
    "coalition_table",
    "exclusive_joint_addressability",
    "history_interface",
    "induced_classes",
    "legal_words",
    "mechanism_interface",
    "mobius_three_way",
    "quotient_bits",
    "quotient_size",
    "trace",
    "trace_profile",
    "worlds",
]
