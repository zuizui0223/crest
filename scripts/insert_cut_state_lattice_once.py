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
    "The mathematical object is therefore the equivalence relation generated jointly with the cut, not a particular "
    "coordinate encoding of that relation.\n"
)
addition = (
    "\nFor a fixed cut, these representation classes exhaust the entire finite state space. Representation-equivalence "
    "classes of signature families are in one-to-one correspondence with partitions that refine \\(B_t\\): every "
    "induced cut-state refines the visible partition, and conversely any refinement of \\(B_t\\) can be realized by "
    "one signature whose kernel is that refinement. Ordering states by retained information is therefore exactly "
    "partition refinement. Adding a nonredundant signature can only move to a finer state, so \\(\\log_2|Q|\\) is "
    "monotone nondecreasing along this order.\n"
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
    "pre-state signatures; prove representation invariance and identify representation classes with the partition-"
    "refinement interval above the visible cut; then specialize retrospective carried semantics, transverse candidate-"
    "safe latent response structure, and prospective query accessibility to quantify sparse prospective access"
)
manifest["cut_state_space"] = {
    "carrier": "representation-equivalence classes of finite pre-state signature families",
    "canonical_image": "all partitions refining the visible cut partition B_t",
    "order": "more information corresponds exactly to partition refinement",
    "realizability": "every refinement of B_t is realizable by one signature whose kernel is that refinement",
    "complexity_monotonicity": "adding signatures can only refine the state, so log2(number of quotient classes) is nondecreasing",
}
manifest["submission_constraints"]["current_main_text_words"] = metadata["text_word_count"]
manifest["implementation"]["cut_state_lattice_theorem"] = "docs/crest_cut_state_partition_lattice_theorem_2026-09-09.md"
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
