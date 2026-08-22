from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TARGET = Path("manuscript/crest_philosophy_biology_philosophy.md")
REPORT = Path("artifacts/crest_philosophy_submission_report.json")


def section(text: str, start: str, end: str | None = None) -> str:
    try:
        body = text.split(start, 1)[1]
    except IndexError as exc:
        raise ValueError(f"missing section marker: {start}") from exc
    if end is not None:
        try:
            body = body.split(end, 1)[0]
        except IndexError as exc:
            raise ValueError(f"missing section marker: {end}") from exc
    return body.strip()


def visible_text(markdown: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", markdown, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_>#|]", " ", text)
    text = re.sub(r"^\s*[-+]\s+", " ", text, flags=re.M)
    text = re.sub(r"^\s*\d+[.)]\s+", " ", text, flags=re.M)
    return re.sub(r"\s+", " ", text).strip()


def word_count(markdown: str) -> int:
    text = visible_text(markdown)
    return len(re.findall(r"\b[\w’'-]+\b", text, flags=re.UNICODE))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    text = TARGET.read_text(encoding="utf-8")
    lower_text = text.lower()

    abstract = section(text, "## Abstract", "**Keywords:**")
    keywords_line = section(text, "**Keywords:**", "## 1.").splitlines()[0].strip()
    keywords = [part.strip() for part in keywords_line.split(";") if part.strip()]
    pre_reference = text.split("## References", 1)[0]

    abstract_words = word_count(abstract)
    manuscript_words_before_references = word_count(pre_reference)

    identifying_patterns = {
        "github": r"github(?:\.com)?",
        "owner_handle": r"zuizui0223",
        "email": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "pull_request": r"\b(?:PR|pull request)\s*#?\d+\b",
        "repository_phrase": r"\bour repository\b",
    }
    blind_hits = {
        name: sorted(set(re.findall(pattern, pre_reference, flags=re.I)))
        for name, pattern in identifying_patterns.items()
    }
    blind_hits = {name: hits for name, hits in blind_hits.items() if hits}

    reference_text = section(text, "## References", "## Submission-control note")
    excluded_unpublished = [
        name
        for name in ("Swanson", "Huang", "PhilArchive", "arXiv")
        if re.search(re.escape(name), reference_text, flags=re.I)
    ]

    carrier_gate_present = bool(
        re.search(r"###\s+\d+\.1\s+Gate A", text, flags=re.I)
        and re.search(r"common carrier|common ecological world set", text, flags=re.I)
    ) or "Carrier existence comes before state construction" in text

    joint_state_checks = {
        "defines_joint_partition": bool(
            re.search(
                r"J=\(C_\\Gamma\\vee C_\{\\mathcal H\}\\vee C_\\Theta\\vee C_\{D,T\}\)\(B\)",
                text,
            )
        ),
        "defines_state_block": "\\operatorname{State}_{\\mathcal C}(u)=[u]_J" in text,
        "states_unique_coarseness": "unique coarsest" in text,
        "states_carrier_gate": carrier_gate_present,
        "states_evidence_gate": "J\\preceq E_D" in text,
        "rejects_global_intrinsic_state": (
            "does **not** establish one universal joint state independent of scientific contract" in text
            and "not one intrinsic partition of nature" in text
        ),
    }

    trajectory_first_checks = {
        "defines_temporally_extended_state": (
            "scientifically licensed compression of a temporally extended ecological world" in text
        ),
        "states_snapshot_factorization_criterion": (
            "Snapshot sufficiency is a factorization criterion" in text
            and "not a novelty-bearing theorem" in text
        ),
        "separates_ced_as_evidence_gate": "CED is deliberately downstream" in text,
        "states_trajectory_theorem_firewall": (
            "not yet a general theorem for continuous or stochastic trajectories" in text
        ),
        "states_psr_prior_art_boundary": (
            "Predictive State Representations" in text
            and "does not claim novelty for predictive equivalence" in text
            and "does not claim to be more expressive than a sufficiently rich PSR" in text
        ),
    }

    capability_resolution_checks = {
        "states_scaling_section": "### 4.5 Cross-gate scale separation — capability–resolution divergence" in text,
        "states_unit_carrier_gain": bool(
            re.search(r"\\Delta\s*\|K\^\*\|=1", text)
        ),
        "states_arbitrary_m_bit_growth": bool(
            re.search(r"\\Delta K_\{U_0\}=m", text)
            and "For every integer \\(m\\ge1\\)" in text
        ),
        "states_no_carrier_gain_only_bound": (
            "no universal finite function" in lower_text
            and "viability gain alone therefore cannot upper-bound" in lower_text
        ),
        "states_full_state_loss_target_retention": (
            "full-state licensing changes from yes to no" in lower_text
            and "coarse target" in lower_text
            and "remains reportable" in lower_text
        ),
        "states_connected_witness": (
            "connected future-response graph" in text
            and "fragile" in text
            and "safe" in text
        ),
        "states_action_abstraction_prior_art_boundary": (
            "Konidaris (2019)" in text
            and "state and action abstraction as coupled problems" in text
            and "The CREST result is therefore **not** the qualitative proposition" in text
        ),
        "references_konidaris": (
            "Konidaris, G. (2019). On the necessity of abstraction." in reference_text
            and "10.1016/j.cobeha.2018.11.005" in reference_text
        ),
    }

    stale_joint_state_phrases = [
        "no claim is made that these four audits are exhaustive, commuting, jointly minimal",
        "share a joint minimum is an open mathematical question",
        "does not establish a universal joint state, an audit order",
    ]
    stale_joint_state_hits = [phrase for phrase in stale_joint_state_phrases if phrase in text]

    stale_action_headline_phrases = [
        "The action-expansion witness adds a specifically ecological consequence.",
        "The action-expansion witness proves one strict finite separation of this kind.",
    ]
    stale_action_headline_hits = [
        phrase for phrase in stale_action_headline_phrases if phrase in text
    ]

    blockers: list[str] = []
    if not 150 <= abstract_words <= 250:
        blockers.append(f"abstract word count {abstract_words} is outside 150-250")
    if not 4 <= len(keywords) <= 6:
        blockers.append(f"keyword count {len(keywords)} is outside 4-6")
    if manuscript_words_before_references > 10_000:
        blockers.append(
            f"repository word count before references {manuscript_words_before_references} exceeds 10,000"
        )
    if blind_hits:
        blockers.append(f"potential double-blind identifiers found: {sorted(blind_hits)}")
    if excluded_unpublished:
        blockers.append(
            "submission reference list contains unpublished/preprint audit sources: "
            + ", ".join(excluded_unpublished)
        )
    missing_joint_state = [name for name, ok in joint_state_checks.items() if not ok]
    if missing_joint_state:
        blockers.append(
            "post-J1 joint-state synchronization checks failed: " + ", ".join(missing_joint_state)
        )
    missing_trajectory_first = [name for name, ok in trajectory_first_checks.items() if not ok]
    if missing_trajectory_first:
        blockers.append(
            "trajectory-first manuscript checks failed: " + ", ".join(missing_trajectory_first)
        )
    missing_capability_resolution = [
        name for name, ok in capability_resolution_checks.items() if not ok
    ]
    if missing_capability_resolution:
        blockers.append(
            "capability-resolution manuscript checks failed: "
            + ", ".join(missing_capability_resolution)
        )
    if stale_joint_state_hits:
        blockers.append(
            "obsolete pre-J1 joint-state wording remains: " + " | ".join(stale_joint_state_hits)
        )
    if stale_action_headline_hits:
        blockers.append(
            "obsolete qualitative-only action headline remains: "
            + " | ".join(stale_action_headline_hits)
        )

    author_controlled = {
        "competing_interests_placeholder": "AUTHOR INPUT REQUIRED BEFORE SUBMISSION" in text,
        "funding_placeholder": text.count("AUTHOR INPUT REQUIRED BEFORE SUBMISSION") >= 2,
        "ai_disclosure_requires_final_human_review": "FINAL HUMAN REVIEW REQUIRED BEFORE SUBMISSION" in text,
        "title_page_metadata_required": True,
    }

    report = {
        "target": str(TARGET),
        "repository_word_count_definition": "visible markdown tokens before References; publisher count may differ slightly",
        "abstract_words": abstract_words,
        "keyword_count": len(keywords),
        "keywords": keywords,
        "manuscript_words_before_references": manuscript_words_before_references,
        "development_target_5500_7500_met": 5500 <= manuscript_words_before_references <= 7500,
        "hard_cap_10000_met": manuscript_words_before_references <= 10_000,
        "blind_hits": blind_hits,
        "excluded_unpublished_reference_hits": excluded_unpublished,
        "post_j1_joint_state_checks": joint_state_checks,
        "trajectory_first_checks": trajectory_first_checks,
        "capability_resolution_checks": capability_resolution_checks,
        "stale_joint_state_hits": stale_joint_state_hits,
        "stale_action_headline_hits": stale_action_headline_hits,
        "automated_blockers": blockers,
        "author_controlled_blockers": author_controlled,
        "automated_checks_pass": not blockers,
        "submission_ready": False,
        "submission_ready_reason": "author-controlled metadata, final human source/claim/text review, and final policy recheck remain required",
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return 1 if blockers else 0


if __name__ == "__main__":
    raise SystemExit(main())
