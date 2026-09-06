"""Finite counterfactual response-capacity bounds for CREST.

The generic counting bounds in this module are finite-state / finite-test
substrate, not an independent novelty claim.  Their CREST role is to identify a
quantity that *does* upper-bound representational burden, in contrast to the
capability-resolution theorem showing that carrier-size gain alone does not.
"""

from __future__ import annotations

from itertools import product
from math import log2, prod
from typing import Hashable, Iterable

from .joint_state import AuditRefinement

Word = tuple[Hashable, ...]
Response = tuple[bool, Hashable | None]


def _require_nonnegative_integer(name: str, value: int) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _require_positive_integer(name: str, value: int) -> int:
    _require_nonnegative_integer(name, value)
    if value == 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def words_through_horizon(
    actions: Iterable[Hashable], horizon: int
) -> tuple[Word, ...]:
    """Enumerate all action words of length at most ``horizon``.

    The empty word is always included.  This helper is intended for finite
    theorem witnesses and tests; its output grows exponentially with horizon.
    """

    horizon = _require_nonnegative_integer("horizon", horizon)
    action_tuple = tuple(actions)
    if len(set(action_tuple)) != len(action_tuple):
        raise ValueError("actions must be unique")
    for action in action_tuple:
        try:
            hash(action)
        except TypeError as error:
            raise ValueError("actions must be hashable") from error

    words: list[Word] = [()]
    for depth in range(1, horizon + 1):
        words.extend(product(action_tuple, repeat=depth))
    return tuple(words)


def horizon_word_count(action_count: int, horizon: int) -> int:
    """Return ``sum(action_count**d, d=0..horizon)`` exactly."""

    action_count = _require_nonnegative_integer("action_count", action_count)
    horizon = _require_nonnegative_integer("horizon", horizon)
    return sum(action_count**depth for depth in range(horizon + 1))


def newly_admitted_word_count(
    old_action_count: int,
    new_action_count: int,
    horizon: int,
) -> int:
    """Count new words through a horizon after an action-alphabet expansion."""

    old_action_count = _require_nonnegative_integer(
        "old_action_count", old_action_count
    )
    new_action_count = _require_nonnegative_integer(
        "new_action_count", new_action_count
    )
    horizon = _require_nonnegative_integer("horizon", horizon)
    if new_action_count < old_action_count:
        raise ValueError("new_action_count must be at least old_action_count")
    return sum(
        new_action_count**depth - old_action_count**depth
        for depth in range(1, horizon + 1)
    )


def horizon_state_class_bound(
    observation_count: int,
    action_count: int,
    horizon: int,
) -> int:
    """Upper-bound finite-horizon response classes by raw response volume.

    ``observation_count`` is the number of possible retained static/base labels.
    One additional response symbol is reserved for an illegal word.
    """

    observation_count = _require_positive_integer(
        "observation_count", observation_count
    )
    return (observation_count + 1) ** horizon_word_count(action_count, horizon)


def horizon_state_bit_bound(
    observation_count: int,
    action_count: int,
    horizon: int,
) -> float:
    """Log2 version of :func:`horizon_state_class_bound`."""

    observation_count = _require_positive_integer(
        "observation_count", observation_count
    )
    return horizon_word_count(action_count, horizon) * log2(
        observation_count + 1
    )


def action_expansion_split_factor_bound(
    observation_count: int,
    old_action_count: int,
    new_action_count: int,
    horizon: int,
) -> int:
    """Bound how much an old finite-horizon class can split after expansion."""

    observation_count = _require_positive_integer(
        "observation_count", observation_count
    )
    new_words = newly_admitted_word_count(
        old_action_count, new_action_count, horizon
    )
    return (observation_count + 1) ** new_words


def action_expansion_bit_bound(
    observation_count: int,
    old_action_count: int,
    new_action_count: int,
    horizon: int,
) -> float:
    """Upper bound on added log2 state classes from newly admitted words."""

    observation_count = _require_positive_integer(
        "observation_count", observation_count
    )
    return newly_admitted_word_count(
        old_action_count, new_action_count, horizon
    ) * log2(observation_count + 1)


def terminal_response(
    audit: AuditRefinement,
    start: int,
    word: Iterable[Hashable],
) -> Response:
    """Return terminal retained label, or an explicit illegal response.

    Equality of these terminal responses for every prefix/word through a finite
    horizon is equivalent to equality of the corresponding finite response tree,
    because intermediate labels are terminal labels of shorter prefixes.
    """

    if not isinstance(start, int) or isinstance(start, bool) or not 0 <= start < audit.world_count:
        raise ValueError("start must be a valid world index")
    action_columns = {action: index for index, action in enumerate(audit.actions)}
    state = start
    for action in tuple(word):
        if action not in action_columns:
            raise ValueError(f"word contains undeclared action: {action!r}")
        successor = audit.successors[state][action_columns[action]]
        if successor is None:
            return (False, None)
        state = successor
    return (True, audit.static_labels[state])


def response_signature(
    audit: AuditRefinement,
    start: int,
    words: Iterable[Iterable[Hashable]],
) -> tuple[Response, ...]:
    """Return the response vector of one world on a declared finite test set."""

    word_tuple = tuple(tuple(word) for word in words)
    return tuple(terminal_response(audit, start, word) for word in word_tuple)


def signature_class_count(
    audit: AuditRefinement,
    starts: Iterable[int],
    words: Iterable[Iterable[Hashable]],
) -> int:
    """Count distinct finite response signatures on selected start worlds."""

    start_tuple = tuple(starts)
    word_tuple = tuple(tuple(word) for word in words)
    return len(
        {
            response_signature(audit, start, word_tuple)
            for start in start_tuple
        }
    )


def response_basis_split_bound(outcome_cardinalities: Iterable[int]) -> int:
    """Product upper bound for a complete finite response-test basis."""

    cardinalities = tuple(outcome_cardinalities)
    for cardinality in cardinalities:
        _require_positive_integer("outcome cardinality", cardinality)
    return prod(cardinalities, start=1)


def response_basis_bit_bound(outcome_cardinalities: Iterable[int]) -> float:
    """Information-capacity form of :func:`response_basis_split_bound`."""

    cardinalities = tuple(outcome_cardinalities)
    for cardinality in cardinalities:
        _require_positive_integer("outcome cardinality", cardinality)
    return sum(log2(cardinality) for cardinality in cardinalities)
