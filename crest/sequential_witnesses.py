"""Executable sharp families for CREST sequential response debt.

The construction was previously embedded only in regression tests.  It is exposed
here as package API so the H*log2(r) sharpness witness can be reproduced directly
by readers and downstream scripts.
"""

from __future__ import annotations

from itertools import product

from .carrier import ComponentCoverage
from .controlled_carrier import ControlledSynchronizedLiftProblem

World = tuple[str, tuple[int, ...], int]


def sharp_sequential_problem(
    response_cardinality: int,
    horizon: int,
    include_probe: bool,
) -> tuple[
    ControlledSynchronizedLiftProblem,
    tuple[tuple[int, ...], ...],
    dict[World, int],
]:
    """Construct the connected r-ary depth-H family attaining H log2(r) bits.

    With ``include_probe=False`` only ``hold`` is available.  With
    ``include_probe=True`` the same finite world family gains one reusable probe
    action.  Repeated probes expose one r-ary response coordinate per depth until
    all ``r**horizon`` present addresses are distinguished.
    """

    if (
        not isinstance(response_cardinality, int)
        or isinstance(response_cardinality, bool)
        or response_cardinality < 2
    ):
        raise ValueError("response_cardinality must be an integer at least two")
    if (
        not isinstance(horizon, int)
        or isinstance(horizon, bool)
        or horizon < 1
    ):
        raise ValueError("horizon must be a positive integer")
    if not isinstance(include_probe, bool):
        raise ValueError("include_probe must be boolean")

    addresses = tuple(product(range(response_cardinality), repeat=horizon))
    worlds: list[World] = []
    index: dict[World, int] = {}

    for address in addresses:
        for depth in range(horizon + 1):
            world = ("path", address, depth)
            index[world] = len(worlds)
            worlds.append(world)

    safe: World = ("safe", (), 0)
    fragile: World = ("fragile", (), 0)
    index[safe] = len(worlds)
    worlds.append(safe)
    index[fragile] = len(worlds)
    worlds.append(fragile)

    actions = ("hold", "probe") if include_probe else ("hold",)
    successors: list[tuple[int | None, ...]] = []
    for world in worlds:
        kind, address, depth = world
        if kind == "path":
            hold = index[world]
            if include_probe:
                probe = (
                    index[("path", address, depth + 1)]
                    if depth < horizon
                    else index[fragile]
                )
                successors.append((hold, probe))
            else:
                successors.append((hold,))
        elif kind == "safe":
            successors.append(
                (index[safe], index[safe]) if include_probe else (index[safe],)
            )
        else:
            successors.append((None, index[safe]) if include_probe else (None,))

    problem = ControlledSynchronizedLiftProblem(
        worlds=tuple(worlds),
        compatible=(True,) * len(worlds),
        uncontrollable_actions=(),
        controllable_actions=actions,
        uncontrollable_successors=tuple(() for _ in worlds),
        controllable_successors=tuple(successors),
        components=(
            ComponentCoverage(
                "compatibility-role",
                ("live",) * len(worlds),
                ("live",),
            ),
        ),
    )
    return problem, addresses, index


__all__ = ["World", "sharp_sequential_problem"]
