#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from crest.amnat_submission import text_word_count

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"

text = MANUSCRIPT.read_text(encoding="utf-8")
old = "Equivalently, \\(q_t\\) factors through \\(O_t\\). When this fails, the adequate cut-state is the least quotient refining \\(B_t\\) enough to preserve the declared retrospective, transverse, and prospective distinguishability constraints. State is therefore structure induced on the cut, not a synonym for the visible cut itself."
new = """Equivalently, \\(q_t\\) factors through \\(O_t\\). When this fails, the adequate cut-state is the least quotient refining \\(B_t\\) enough to preserve the declared retrospective, transverse, and prospective distinguishability constraints. State is therefore structure induced on the cut, not a synonym for the visible cut itself.\n\nThis leastness has a companion-independent finite form. Let \\(g_i:\\Omega\\to Z_i\\) be any finite family of pre-state signatures defined independently of the final state. Define\n\n\\[\n\\omega\\sim_*\\omega'\n\\iff\nO_t(\\omega)=O_t(\\omega')\n\\quad\\text{and}\\quad\ng_i(\\omega)=g_i(\\omega')\\ \u00a0\\text{for every }i.\n\\]\n\nThen \\(Q_* = \\Omega/{\\sim_*}\\) preserves the cut observation and every declared signature. Moreover, if another quotient \\(r:\\Omega\\to R\\) preserves the same objects, every \\(r\\)-class lies inside one \\(Q_*\\)-class. Hence \\(r\\) refines \\(Q_*\\): the induced cut-state is the unique coarsest admissible quotient, up to relabeling of its classes. The investigator therefore chooses which pre-state signatures define the scientific problem, but once those signatures are fixed the least compatible state is not freely chosen."""

if text.count(old) != 1:
    raise SystemExit(f"expected exactly one insertion site, found {text.count(old)}")
text = text.replace(old, new, 1)
MANUSCRIPT.write_text(text, encoding="utf-8")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
metadata["text_word_count"] = text_word_count(text)
METADATA.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
