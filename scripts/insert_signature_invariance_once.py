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
    "The investigator therefore chooses which pre-state signatures define the scientific problem, "
    "but once those signatures are fixed the least compatible state is not freely chosen.\n"
)
addition = (
    "\nThis conclusion is representation invariant. Two different pre-state signature families induce the same cut-state "
    "exactly when every signature in each family factors through the state induced by the other. Thus relabeling, "
    "reordering, duplicating, packing, or splitting signatures cannot alter the state when the generated distinction "
    "structure is unchanged. Equivalently, adding any signature already determined by the existing cut-state is "
    "redundant. The mathematical object is therefore the equivalence relation generated jointly with the cut, not a "
    "particular coordinate encoding of that relation.\n"
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
    "pre-state signatures; prove representation invariance under mutually factorizing signature families; then "
    "specialize retrospective carried semantics, transverse candidate-safe latent response structure, and prospective "
    "query accessibility to quantify sparse prospective access"
)
manifest["representation_invariance"] = {
    "criterion": "two signature families induce the same cut state iff each family mutually factors through the state induced by the other",
    "redundancy_corollary": "adding signatures already determined by the induced state leaves the quotient unchanged",
    "interpretation": "the generated equivalence relation, not signature names or coordinate encoding, determines the cut state",
}
manifest["submission_constraints"]["current_main_text_words"] = metadata["text_word_count"]
manifest["implementation"]["signature_invariance_theorem"] = "docs/crest_signature_family_invariance_theorem_2026-09-09.md"
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
