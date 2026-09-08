"""Temporal-position interaction witnesses for CREST state construction.

The visible present is treated as the baseline state description. Three declared
responsibility axes may then retain information from:

- HISTORY: retrospective distinctions carried from before the present;
- LATENT_PRESENT: contemporaneous response structure hidden by the visible snapshot;
- FUTURE: prospective distinctions exposed by declared future responses.

The constructions below are finite exact witnesses. They do not claim that these
three axes exhaust all legitimate ecological state responsibilities.
"""

from __future__ import annotations

from math import log2

from .joint_state import AuditRefinement
from .obstruction_spectrum import ObstructionSpectrumReport, obstruction_spectrum

HISTORY = "HISTORY"
LATENT_PRESENT = "LATENT_PRESENT"
FUTURE = "FUTURE"


def past_future_cycle(
    state_count: int,
) -> tuple[tuple[int, ...], tuple[AuditRefinement, AuditRefinement]]:
    """Two-axis family with unbounded past-by-future interaction.

    All latent worlds share one visible-present baseline class. HISTORY marks one
    retrospective class and therefore costs one bit alone. FUTURE is a directed
    cycle that costs zero on the untouched baseline, but once the historical mark
    is retained it propagates the distinction around the cycle until all states
    are distinct.
    """

    if not isinstance(state_count, int) or isinstance(state_count, bool) or state_count < 2:
        raise ValueError("state_count must be an integer at least two")

    baseline = (0,) * state_count
    history = AuditRefinement(
        HISTORY,
        tuple("history-mark" if index == 0 else "history-unmarked" for index in range(state_count)),
        (),
        tuple(() for _ in range(state_count)),
    )
    future = AuditRefinement(
        FUTURE,
        ("same-visible-present",) * state_count,
        ("future-step",),
        tuple((((index + 1) % state_count),) for index in range(state_count)),
    )
    return baseline, (history, future)


def past_future_report(state_count: int) -> ObstructionSpectrumReport:
    baseline, audits = past_future_cycle(state_count)
    return obstruction_spectrum(audits, baseline)


def temporal_three_way_cascade(
    bit_depth: int,
) -> tuple[
    tuple[int, ...],
    tuple[AuditRefinement, AuditRefinement, AuditRefinement],
]:
    """History -> latent-present -> future cascade with unbounded 3-way debt.

    ``bit_depth=m`` creates ``2**m + 1`` latent worlds with one visible-present
    baseline class. The joint fixed point has exactly ``2**m`` classes.

    HISTORY marks one world. LATENT_PRESENT can distinguish a second world only
    after the history mark exists. FUTURE contains a chain of ``2**m - 3`` worlds
    that remains dormant until the latent-present split exists; it then propagates
    that distinction down the chain. Two residual worlds remain merged.
    """

    if (
        not isinstance(bit_depth, int)
        or isinstance(bit_depth, bool)
        or bit_depth < 2
    ):
        raise ValueError("bit_depth must be an integer at least two")

    future_chain_length = 2**bit_depth - 3
    world_count = future_chain_length + 4
    history_seed = 0
    latent_seed = 1
    future_chain = tuple(range(2, 2 + future_chain_length))
    residual = 2 + future_chain_length
    shadow = residual + 1

    baseline = (0,) * world_count

    history = AuditRefinement(
        HISTORY,
        tuple(
            "history-mark" if index == history_seed else "history-unmarked"
            for index in range(world_count)
        ),
        (),
        tuple(() for _ in range(world_count)),
    )

    latent_successors = [residual] * world_count
    latent_successors[latent_seed] = history_seed
    latent_present = AuditRefinement(
        LATENT_PRESENT,
        ("same-visible-present",) * world_count,
        ("latent-response",),
        tuple((successor,) for successor in latent_successors),
    )

    future_successors = [residual] * world_count
    previous = latent_seed
    for world in future_chain:
        future_successors[world] = previous
        previous = world
    future_successors[residual] = residual
    future_successors[shadow] = residual
    future = AuditRefinement(
        FUTURE,
        ("same-visible-present",) * world_count,
        ("future-step",),
        tuple((successor,) for successor in future_successors),
    )

    return baseline, (history, latent_present, future)


def temporal_three_way_report(bit_depth: int) -> ObstructionSpectrumReport:
    baseline, audits = temporal_three_way_cascade(bit_depth)
    return obstruction_spectrum(audits, baseline)


def temporal_three_way_closed_form(bit_depth: int) -> dict[str, float | int]:
    """Closed-form quantities for the temporal three-way cascade."""

    if (
        not isinstance(bit_depth, int)
        or isinstance(bit_depth, bool)
        or bit_depth < 2
    ):
        raise ValueError("bit_depth must be an integer at least two")

    pair = log2(3.0 / 2.0)
    triple = bit_depth - log2(3.0)
    return {
        "joint_blocks": 2**bit_depth,
        "joint_debt_bits": float(bit_depth),
        "standalone_history_bits": 1.0,
        "standalone_latent_present_bits": 0.0,
        "standalone_future_bits": 0.0,
        "history_latent_pair_bits": pair,
        "history_future_pair_bits": 0.0,
        "latent_future_pair_bits": 0.0,
        "three_way_bits": triple,
        "interaction_bits": float(bit_depth - 1),
        "interaction_fraction_of_joint": (bit_depth - 1) / bit_depth,
        "three_way_fraction_of_joint": triple / bit_depth,
        "three_way_fraction_of_interaction": triple / (bit_depth - 1),
    }


__all__ = [
    "FUTURE",
    "HISTORY",
    "LATENT_PRESENT",
    "past_future_cycle",
    "past_future_report",
    "temporal_three_way_cascade",
    "temporal_three_way_closed_form",
    "temporal_three_way_report",
]
