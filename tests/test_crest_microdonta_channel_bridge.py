from __future__ import annotations

from crest.joint_state import AuditRefinement, JointCRESTContract, solve_joint_crest_state


def _empty_rows(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(() for _ in range(size))


def _contract(*, channel_action_open: bool, channel_resolved_evidence: bool = False) -> JointCRESTContract:
    worlds = ("fecundity_loss", "establishment_loss", "healthy")

    # N1 microdonta symmetry at one representative trait value:
    # baseline F0=E0=1, attenuation a=1/2.
    # (aF0)E0 = F0(aE0) = 1/2, so net-only evidence merges the two loss worlds.
    base = ("net_low", "net_low", "net_high")
    if channel_resolved_evidence:
        evidence = (
            ("W=0.5", "F=0.5"),
            ("W=0.5", "F=1.0"),
            ("W=1.0", "F=1.0"),
        )
    else:
        evidence = ("W=0.5", "W=0.5", "W=1.0")

    # The declared target is current net-performance class, not latent channel identity.
    targets = ("currently_low", "currently_low", "currently_high")

    if channel_action_open:
        future = AuditRefinement(
            "future",
            ("same", "same", "same"),
            ("restore_F",),
            (
                (2,),  # fecundity loss -> healthy after F restoration
                (1,),  # establishment loss remains establishment-limited
                (2,),  # healthy remains healthy
            ),
        )
    else:
        future = AuditRefinement(
            "future",
            ("same", "same", "same"),
            (),
            ((), (), ()),
        )

    empty = _empty_rows(len(worlds))
    same = ("same",) * len(worlds)
    return JointCRESTContract(
        worlds=worlds,
        base_labels=base,
        evidence_labels=evidence,
        target_labels=targets,
        audits=(
            future,
            AuditRefinement("semantic", same, (), empty),
            AuditRefinement("mechanism", same, (), empty),
            AuditRefinement("target", same, (), empty),
        ),
    )


def test_net_equivalent_channel_worlds_split_when_channel_specific_action_becomes_available() -> None:
    # Explicit N1 algebra: the same net performance can be produced by distinct channels.
    f0 = 1.0
    e0 = 1.0
    attenuation = 0.5
    w_fecundity_loss = (attenuation * f0) * e0
    w_establishment_loss = f0 * (attenuation * e0)
    assert w_fecundity_loss == w_establishment_loss == 0.5

    closed = solve_joint_crest_state(_contract(channel_action_open=False))
    opened = solve_joint_crest_state(_contract(channel_action_open=True))

    # With only net-performance responsibility, the two causal worlds may share one state.
    assert closed.blocks == (("fecundity_loss", "establishment_loss"), ("healthy",))
    assert closed.full_state_licensed
    assert closed.target_report_licensed

    # Merely making an F-specific restoration operation admissible makes the two worlds
    # future-distinct before the action is executed.
    assert opened.blocks == (("fecundity_loss",), ("establishment_loss",), ("healthy",))
    assert opened.state_count == 3

    # Net-only monitoring still sees both channel losses as W=0.5, so it no longer
    # identifies the required state. The declared current-performance target remains safe.
    assert not opened.full_state_licensed
    assert opened.target_report_licensed
    assert opened.sharp_state_report == ((0, 1), (2,))
    assert opened.sharp_target_report == (("currently_low",), ("currently_high",))


def test_one_channel_measurement_repairs_the_microdonta_n1_ambiguity() -> None:
    opened_net_only = solve_joint_crest_state(_contract(channel_action_open=True))
    opened_channel_resolved = solve_joint_crest_state(
        _contract(channel_action_open=True, channel_resolved_evidence=True)
    )

    assert not opened_net_only.full_state_licensed

    # Microdonta N2: W plus one exact positive factor separates the two channels.
    assert opened_channel_resolved.full_state_licensed
    assert opened_channel_resolved.target_report_licensed
