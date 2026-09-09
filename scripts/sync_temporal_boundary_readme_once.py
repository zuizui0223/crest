#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "manuscript" / "SUBMISSION_README.md"
text = PATH.read_text(encoding="utf-8")


def rep(old: str, new: str) -> None:
    global text
    if text.count(old) != 1:
        raise SystemExit(f"expected one README match: {old!r}")
    text = text.replace(old, new, 1)


rep(
    "The paper defines ecological state as the least information that must survive an observational temporal cut under a declared scientific contract.",
    "The paper treats the present as a zero-duration observational cut and defines ecological state as the least quotient induced on that cut by retrospective, transverse latent-present, and prospective distinguishability constraints.",
)
rep(
    "- **MLTR / history H:** primitive replacement histories first, complete carried-map equivalence second;\n- **MRM / latent response Theta:** primitive candidate laws first, complete response-type equivalence second;\n- **CCOC / future F:** controlled law plus exogenously declared legal query grammar, response quotient afterward.",
    "- **MLTR / retrospective H:** primitive replacement histories first, complete carried-map equivalence second; this is the left-of-cut structure;\n- **MRM / transverse latent present Theta:** primitive candidate laws first, complete response-type equivalence second; this partitions the observation fiber without claiming full ontic mechanism identity;\n- **CCOC / prospective F:** controlled law plus exogenously declared right-of-cut query grammar, response quotient afterward.",
)
rep("It distinguishes two modeling objects:", "It distinguishes two structures controlling prospective refinement of the cut-state:")
rep(
    "The shallow-lake worked case is an executable finite decision model.",
    "The shallow-lake worked case is a worked ecological interpretation with an executable finite model.",
)
rep(
    "The contribution is the modeling architecture: non-circular companion semantics, strict realizability boundaries, target-relative interface-prerequisite identification, explicit semantic access coverage, and propagation of both objects into one exact temporal-cut state quotient.",
    "The contribution is a finite theory of state at a temporal boundary: non-circular retrospective/transverse/prospective semantics, strict realizability boundaries, sparse prospective access, and the exact cut-state quotient induced by those structures.",
)
rep(
    "possible ecological worlds Omega\n-> observational temporal cut O_t\n-> companion semantic outputs\n-> strict realizability no-go\n-> target prerequisite identification\n-> semantic access relation A_f\n-> legal semantic traces\n-> induced quotient Q_S\n-> interaction accounting\n-> evidence licensing downstream",
    "raw ecological possibilities Omega\n-> zero-duration observational cut O_t\n-> visible-cut fibers O_t^{-1}(y)\n-> retrospective / transverse / prospective pre-state structures\n-> strict realizability no-go\n-> prerequisite structure + semantic access relation A_f\n-> legal prospective traces\n-> least induced cut-state quotient Q_S\n-> interaction accounting\n-> ecological interpretation / evidence downstream",
)
rep(
    "- that history, latent response, and future are independent ontic coordinates;",
    "- that retrospective, transverse, and prospective structures are independent ontic coordinates;",
)
rep(
    "- continuous-time, stochastic, infinite-state, or approximate generality.",
    "- a proved continuous-time epsilon-to-zero or germ limit, or stochastic, infinite-state, or approximate generality.",
)

PATH.write_text(text, encoding="utf-8")
