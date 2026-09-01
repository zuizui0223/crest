from __future__ import annotations

from itertools import combinations
from random import Random

from crest.carrier import ComponentCoverage
from crest.controlled_carrier import ControlledSynchronizedLiftProblem
from crest.controlled_repair import (
    ControlledLiftRelaxationCosts,
    minimum_controlled_lift_relaxation,
)


def _brute_force_cover(sets, costs, universe):
    best_cost = None
    best_subsets = []
    for width in range(1, len(sets) + 1):
        for chosen in combinations(range(len(sets)), width):
            covered = frozenset().union(*(sets[index] for index in chosen))
            if covered != universe:
                continue
            cost = sum(costs[index] for index in chosen)
            if best_cost is None or cost < best_cost:
                best_cost = cost
                best_subsets = [chosen]
            elif cost == best_cost:
                best_subsets.append(chosen)
    return best_cost, tuple(best_subsets)


def _j7_set_cover_instance(sets, costs, universe):
    worlds = tuple(f"set-{index}" for index in range(len(sets)))
    components = tuple(
        ComponentCoverage(
            name=f"element-{element}",
            labels=tuple(1 if element in members else 0 for members in sets),
            required_labels=(1,),
        )
        for element in sorted(universe)
    )
    problem = ControlledSynchronizedLiftProblem(
        worlds=worlds,
        compatible=(False,) * len(worlds),
        uncontrollable_actions=(),
        controllable_actions=("stay",),
        uncontrollable_successors=tuple(() for _ in worlds),
        controllable_successors=tuple((index,) for index in range(len(worlds))),
        components=components,
    )
    waiver_penalty = sum(costs) + 1
    return ControlledLiftRelaxationCosts(
        problem=problem,
        enable_world_costs=tuple(costs),
        disable_uncontrollable_costs=tuple(() for _ in worlds),
        fallback_action="fallback",
        fallback_successors=(None,) * len(worlds),
        install_fallback_costs=(None,) * len(worlds),
        drop_coverage_costs=tuple((waiver_penalty,) for _ in universe),
    )


def _random_coverable_instances():
    rng = Random(2026090101)
    for universe_size in (1, 2, 3):
        universe = frozenset(range(universe_size))
        possible = tuple(
            frozenset(element for element in universe if mask & (1 << element))
            for mask in range(1, 1 << universe_size)
        )
        for _case in range(16):
            width = rng.randint(1, min(5, len(possible) + 2))
            sets = tuple(rng.choice(possible) for _ in range(width))
            if frozenset().union(*sets) != universe:
                sets = sets + (universe,)
            costs = tuple(rng.randint(1, 5) for _ in sets)
            yield sets, costs, universe


def test_j7_reduction_matches_weighted_set_cover_over_small_instance_family():
    for sets, costs, universe in _random_coverable_instances():
        cover_cost, optimal_covers = _brute_force_cover(sets, costs, universe)
        assert cover_cost is not None

        result = minimum_controlled_lift_relaxation(
            _j7_set_cover_instance(sets, costs, universe)
        )

        assert result.feasible
        assert result.minimum_cost == cover_cost
        returned = tuple(plan.retained_indices for plan in result.optimal_plans)
        assert set(returned) == set(optimal_covers)
        for plan in result.optimal_plans:
            assert plan.dropped_coverage == ()
            assert plan.disabled_uncontrollable == ()
            assert plan.installed_fallbacks == ()
            assert plan.verified_kernel().admissible


def test_j7_hardness_family_uses_only_the_restricted_theorem_language():
    sets = (frozenset({0}), frozenset({1}), frozenset({0, 1}))
    costs = (1, 1, 3)
    costs_contract = _j7_set_cover_instance(sets, costs, frozenset({0, 1}))
    problem = costs_contract.problem

    assert problem.uncontrollable_actions == ()
    assert problem.controllable_actions == ("stay",)
    assert all(row == (index,) for index, row in enumerate(problem.controllable_successors))
    assert costs_contract.fallback_successors == (None,) * len(problem.worlds)
    assert costs_contract.install_fallback_costs == (None,) * len(problem.worlds)
