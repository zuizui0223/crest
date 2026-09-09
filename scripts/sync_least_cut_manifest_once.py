#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "flagship_integration" / "flagship_integration_manifest.json"

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
if manifest.get("schema_version") != 11:
    raise SystemExit("expected flagship integration schema 11")
manifest["submission_constraints"]["current_main_text_words"] = 3618
manifest["implementation"]["least_cut_quotient_module"] = "crest/cut_state_quotient.py"
manifest["implementation"]["least_cut_quotient_theorem"] = "docs/crest_least_temporal_cut_quotient_theorem_2026-09-09.md"
manifest["theory_contribution"] = (
    "characterize ecological state as the unique coarsest quotient preserving the cut observation and declared pre-state signatures, "
    "then specialize retrospective carried semantics, transverse candidate-safe latent response structure, and prospective query accessibility to quantify sparse prospective access"
)
MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
