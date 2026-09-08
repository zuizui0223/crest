"""Temporal-cut formulation of CREST state.

The present is not modeled here as a finite-width temporal interval or as a third
time axis.  A declared observation map at time t induces a cut partition.  Past
and future responsibilities act from the two temporal sides of that cut, while
latent contemporaneous mechanism structure lives inside fibers of the cut.

This is a finite exact formulation.  It does not introduce an infinitesimal or
continuous-time limit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable

from .joint_state import AuditRefinement
from .obstruction_spectrum import ObstructionSpectrumReport, obstruction_spectrum

HISTORY = "HISTORY"
LATENT_PRESENT = "LATENT_PRESENT"
FUTURE = "FUTURE"


@dataclass(frozen=True)
class TemporalCutContract:
    """One finite CREST contract centered on an observational temporal cut.

    ``cut_observations`` are the values returned by the observation map O_t on an
    ordered finite latent-world carrier.  Equal values define the visible-present
    fiber at the cut.  The three audits then encode distinctions required by:

    - retrospective history to the left of the cut;
    - latent contemporaneous response structure inside a cut fiber; and
    - prospective/counterfactual response responsibility to the right of the cut.

    The object deliberately does not define a finite-duration ``present`` state.
    """

    worlds: tuple[Hashable, ...]
    cut_observations: tuple[Hashable, ...]
    history: AuditRefinement
    latent_present: AuditRefinement
    future: AuditRefinement

    def __post_init__(self) -> None:
        if not self.worlds:
            raise ValueError("temporal cut requires a nonempty finite carrier")
        if len(set(self.worlds)) != len(self.worlds):
            raise ValueError("temporal-cut worlds must be unique")
        if len(self.cut_observations) != len(self.worlds):
            raise ValueError("cut observations must align with worlds")
        for value in (*self.worlds, *self.cut_observations):
            try:
                hash(value)
            except TypeError as error:
                raise ValueError("worlds and cut observations must be hashable") from error
        audits = (self.history, self.latent_present, self.future)
        if any(audit.world_count != len(self.worlds) for audit in audits):
            raise ValueError("all temporal audits must share the cut carrier")
        names = tuple(audit.name for audit in audits)
        if names != (HISTORY, LATENT_PRESENT, FUTURE):
            raise ValueError(
                "temporal audits must be named HISTORY, LATENT_PRESENT, FUTURE"
            )

    @property
    def audits(self) -> tuple[AuditRefinement, AuditRefinement, AuditRefinement]:
        return (self.history, self.latent_present, self.future)

    @property
    def baseline(self) -> tuple[Hashable, ...]:
        """Kernel partition labels induced by the observation cut O_t."""

        return self.cut_observations

    def fiber(self, observation: Hashable) -> tuple[Hashable, ...]:
        """Return the latent worlds lying behind one visible cut value."""

        return tuple(
            world
            for world, value in zip(self.worlds, self.cut_observations)
            if value == observation
        )

    def spectrum(self) -> ObstructionSpectrumReport:
        """Compute H / latent-present / F joint debt above the cut partition."""

        return obstruction_spectrum(self.audits, self.baseline)


__all__ = [
    "FUTURE",
    "HISTORY",
    "LATENT_PRESENT",
    "TemporalCutContract",
]
