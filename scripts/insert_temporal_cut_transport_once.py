#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from crest.amnat_submission import text_word_count

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"

anchor = (
    "For a fixed cut, these representation classes exhaust the entire finite state space. Representation-equivalence "
    "classes of signature families are in one-to-one correspondence with partitions that refine \\(B_t\\): every "
    "induced cut-state refines the visible partition, and conversely any refinement of \\(B_t\\) can be realized by one "
    "signature whose kernel is that refinement. Ordering states by retained information is therefore exactly partition "
    "refinement. Adding a nonredundant signature can only move to a finer state, so \\(\\log_2|Q|\\) is monotone "
    "nondecreasing along this order.\n"
)
addition = (
    "\nStates at different cuts can be connected only when the underlying world evolution respects their quotient "
    "equivalences. For a declared deterministic map \\(\\phi_{t\\to s}:\\Omega_t\\to\\Omega_s\\), a state-level map "
    "\\(\\bar\\phi:Q_t\\to Q_s\\) exists exactly when \\(\\omega\\sim_t\\omega'\\) implies "
    "\\(\\phi(\\omega)\\sim_s\\phi(\\omega')\\). When this descent condition holds, "
    "\\(\\bar\\phi([\\omega]_t)=[\\phi(\\omega)]_s\\) is unique; identity and composition descend. Failure is a "
    "state-sufficiency obstruction: one source state class evolves into multiple target state classes, so no deterministic "
    "quotient transition is well defined. This finite transport result does not imply temporal monotonicity of "
    "\\(|Q_t|\\) or a continuous-time limit.\n"
)
text = MANUSCRIPT.read_text(encoding="utf-8")
if addition.strip() not in text:
    if text.count(anchor) != 1:
        raise SystemExit(f"expected exactly one manuscript anchor, found {text.count(anchor)}")
    text = text.replace(anchor, anchor + addition, 1)
    MANUSCRIPT.write_text(text, encoding="utf-8")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
metadata["text_word_count"] = text_word_count(text)
METADATA.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
manifest["theory_contribution"] = (
    "characterize ecological state as the unique coarsest quotient preserving the cut observation and declared "
    "pre-state signatures; prove representation invariance, identify the fixed-cut state space with the partition-"
    "refinement interval, and characterize deterministic transport between cuts by quotient descent; then specialize "
    "retrospective carried semantics, transverse candidate-safe latent response structure, and prospective query "
    "accessibility to quantify sparse prospective access"
)
manifest["temporal_cut_transport"] = {
    "criterion": "a deterministic world map descends iff source-equivalent worlds always map to target-equivalent worlds",
    "uniqueness": "the induced quotient transition is unique whenever it exists",
    "composition": "identity and composition descend for compatible finite world evolutions",
    "obstruction": "failure means one source state class reaches multiple target state classes",
    "scope": "no stochastic or multivalued transport theorem, no temporal monotonicity of state cardinality, and no continuous-time limit",
}
manifest["submission_constraints"]["current_main_text_words"] = metadata["text_word_count"]
manifest["implementation"]["temporal_cut_transport_module"] = "crest/temporal_cut_transport.py"
manifest["implementation"]["temporal_cut_transport_theorem"] = "docs/crest_temporal_cut_transport_theorem_2026-09-09.md"
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
