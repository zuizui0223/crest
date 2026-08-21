from __future__ import annotations

from random import Random

from crest.carrier import ComponentCoverage, SynchronizedLiftProblem, maximal_common_lift
from crest.controlled_carrier import (
    ControlledSynchronizedLiftProblem,
    maximal_controlled_common_lift,
)


def _subsets(size: int):
    for mask in range(1 << size):
        yield tuple(index for index in range(size) if mask & (1 << index))


def _random_components(rng: Random, size: int) -> tuple[ComponentCoverage, ...]:
    labels = tuple(rng.randrange(3) for _ in range(size))
    represented = tuple(dict.fromkeys(labels))
    required = tuple(label for label in represented if rng.randrange(2))
    return (ComponentCoverage("component", labels, required),)


def _universal_closed_direct(problem: SynchronizedLiftProblem, subset) -> bool:
    chosen = set(subset)
    if any(not problem.compatible[index] for index in chosen):
        return False
    return all(
        successor is None or successor in chosen
        for index in chosen
        for successor in problem.successors[index]
    )


def _controlled_invariant_direct(
    problem: ControlledSynchronizedLiftProblem, subset
) -> bool:
    chosen = set(subset)
    if any(not problem.compatible[index] for index in chosen):
        return False
    for index in chosen:
        if any(
            successor is not None and successor not in chosen
            for successor in problem.uncontrollable_successors[index]
        ):
            return False
        if not any(
            successor is not None and successor in chosen
            for successor in problem.controllable_successors[index]
        ):
            return False
    return True


def _coverage_complete_direct(problem, viable_indices) -> bool:
    chosen = set(viable_indices)
    for component in problem.components:
        represented = {component.labels[index] for index in chosen}
        if any(label not in represented for label in component.required_labels):
            return False
    return True


def test_j3_matches_exhaustive_subset_oracle_across_small_problems() -> None:
    rng = Random(2026082101)

    for case in range(128):
        size = 1 + case % 4
        action_count = rng.randrange(3)
        actions = tuple(f"a{index}" for index in range(action_count))
        problem = SynchronizedLiftProblem(
            worlds=tuple(f"w{index}" for index in range(size)),
            compatible=tuple(bool(rng.randrange(2)) for _ in range(size)),
            actions=actions,
            successors=tuple(
                tuple(rng.choice((None, *range(size))) for _ in actions)
                for _ in range(size)
            ),
            components=_random_components(rng, size),
        )

        closed_subsets = [
            subset
            for subset in _subsets(size)
            if _universal_closed_direct(problem, subset)
        ]
        oracle_kernel = tuple(
            sorted({index for subset in closed_subsets for index in subset})
        )

        result = maximal_common_lift(problem)
        assert result.viable_indices == oracle_kernel
        assert result.exists == bool(oracle_kernel)
        expected_coverage = _coverage_complete_direct(problem, oracle_kernel)
        assert result.coverage_complete == expected_coverage
        assert result.admissible == (bool(oracle_kernel) and expected_coverage)
        assert all(set(subset).issubset(result.viable_indices) for subset in closed_subsets)

        for index, world in enumerate(problem.worlds):
            if index in result.viable_indices:
                continue
            chain = result.elimination_chain(world)
            assert chain[0] == world
            terminal = problem.worlds.index(chain[-1])
            assert not problem.compatible[terminal]
            assert len(chain) <= size


def test_j6_matches_exhaustive_subset_oracle_across_small_problems() -> None:
    rng = Random(2026082102)

    for case in range(128):
        size = 1 + case % 4
        uncontrollable_count = rng.randrange(3)
        controllable_count = 1 + rng.randrange(2)
        uncontrollable = tuple(f"u{index}" for index in range(uncontrollable_count))
        controllable = tuple(f"c{index}" for index in range(controllable_count))
        problem = ControlledSynchronizedLiftProblem(
            worlds=tuple(f"w{index}" for index in range(size)),
            compatible=tuple(bool(rng.randrange(2)) for _ in range(size)),
            uncontrollable_actions=uncontrollable,
            controllable_actions=controllable,
            uncontrollable_successors=tuple(
                tuple(rng.choice((None, *range(size))) for _ in uncontrollable)
                for _ in range(size)
            ),
            controllable_successors=tuple(
                tuple(rng.choice((None, *range(size))) for _ in controllable)
                for _ in range(size)
            ),
            components=_random_components(rng, size),
        )

        invariant_subsets = [
            subset
            for subset in _subsets(size)
            if _controlled_invariant_direct(problem, subset)
        ]
        oracle_kernel = tuple(
            sorted({index for subset in invariant_subsets for index in subset})
        )

        result = maximal_controlled_common_lift(problem)
        assert result.viable_indices == oracle_kernel
        assert result.exists == bool(oracle_kernel)
        expected_coverage = _coverage_complete_direct(problem, oracle_kernel)
        assert result.coverage_complete == expected_coverage
        assert result.admissible == (bool(oracle_kernel) and expected_coverage)
        assert all(
            set(subset).issubset(result.viable_indices)
            for subset in invariant_subsets
        )

        retained = set(result.viable_indices)
        for world, action, successor in result.policy:
            world_index = problem.worlds.index(world)
            action_index = problem.controllable_actions.index(action)
            successor_index = problem.worlds.index(successor)
            assert world_index in retained
            assert successor_index in retained
            assert (
                problem.controllable_successors[world_index][action_index]
                == successor_index
            )

        for index, world in enumerate(problem.worlds):
            if index in result.viable_indices:
                continue
            certificate = result.elimination_certificate(world)
            assert certificate.world == world
            assert certificate.depth <= size
