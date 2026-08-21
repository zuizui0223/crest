from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Hashable, Iterable, Mapping, Sequence

State = Hashable
Action = Hashable
Block = frozenset[State]
Partition = tuple[Block, ...]


def _stable_key(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=repr)


def canonical_partition(blocks: Iterable[Iterable[State]]) -> Partition:
    """Return a deterministic, duplicate-free partition representation."""
    normalized: list[Block] = []
    seen: set[State] = set()
    for raw in blocks:
        block = frozenset(raw)
        if not block:
            continue
        overlap = seen.intersection(block)
        if overlap:
            raise ValueError(f"partition blocks overlap: {sorted(map(repr, overlap))}")
        seen.update(block)
        normalized.append(block)
    normalized.sort(key=lambda b: tuple(sorted((_stable_key(x) for x in b))))
    return tuple(normalized)


def block_index(partition: Partition) -> dict[State, int]:
    index: dict[State, int] = {}
    for i, block in enumerate(partition):
        for state in block:
            if state in index:
                raise ValueError(f"state appears in multiple blocks: {state!r}")
            index[state] = i
    return index


@dataclass(frozen=True)
class FiniteActionSystem:
    """Neutral deterministic finite-state/action contract.

    This object intentionally contains no CCOC, MLTR, MRM, CED, or CREST theorem
    semantics. It is only a shared substrate for declared finite states, legal
    actions, outputs, and deterministic successors.
    """

    states: tuple[State, ...]
    actions: tuple[Action, ...]
    transitions: Mapping[tuple[State, Action], State]
    outputs: Mapping[State, Hashable] | None = None

    def legal_actions(self, state: State) -> tuple[Action, ...]:
        return tuple(a for a in self.actions if (state, a) in self.transitions)

    def successor(self, state: State, action: Action) -> State:
        try:
            return self.transitions[(state, action)]
        except KeyError as exc:
            raise KeyError(f"illegal transition: {state!r} --{action!r}--> ?") from exc

    def validate(self) -> None:
        state_set = set(self.states)
        if len(state_set) != len(self.states):
            raise ValueError("states must be unique")
        if len(set(self.actions)) != len(self.actions):
            raise ValueError("actions must be unique")
        for (state, _action), nxt in self.transitions.items():
            if state not in state_set or nxt not in state_set:
                raise ValueError("all transition endpoints must belong to states")
        if self.outputs is not None and not set(self.outputs).issubset(state_set):
            raise ValueError("outputs contain unknown states")


def refine_partition(
    system: FiniteActionSystem,
    partition: Partition,
    *,
    preserve_outputs: bool = True,
) -> Partition:
    """Compute the coarsest stable refinement below a supplied partition.

    States remain together only when they have the same declared output (when
    requested), the same legal-action row, and successors landing in the same
    current blocks. This is generic partition refinement, not a scientific claim.
    """
    system.validate()
    current = canonical_partition(partition)
    if set(block_index(current)) != set(system.states):
        raise ValueError("partition must cover exactly the system states")

    while True:
        idx = block_index(current)
        next_blocks: list[Block] = []
        for block in current:
            groups: dict[tuple[object, ...], set[State]] = {}
            for state in block:
                legal = system.legal_actions(state)
                signature: tuple[object, ...] = (
                    system.outputs.get(state) if preserve_outputs and system.outputs else None,
                    tuple(_stable_key(a) for a in legal),
                    tuple(idx[system.successor(state, a)] for a in legal),
                )
                groups.setdefault(signature, set()).add(state)
            next_blocks.extend(frozenset(group) for group in groups.values())
        refined = canonical_partition(next_blocks)
        if refined == current:
            return refined
        current = refined


def deterministic_fingerprint(value: object) -> str:
    """SHA-256 fingerprint of a canonically JSON-encoded value."""
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), default=repr)
    return sha256(payload.encode("utf-8")).hexdigest()


def replay(
    system: FiniteActionSystem,
    start: State,
    actions: Sequence[Action],
) -> tuple[State, ...]:
    """Deterministically replay an action sequence and return visited states."""
    if start not in set(system.states):
        raise ValueError(f"unknown start state: {start!r}")
    visited = [start]
    state = start
    for action in actions:
        state = system.successor(state, action)
        visited.append(state)
    return tuple(visited)
