#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from crest.amnat_submission import text_word_count

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
METADATA = ROOT / "manuscript" / "amnat_submission_metadata.json"

text = MANUSCRIPT.read_text(encoding="utf-8")
old = "g_i(\\omega)=g_i(\\omega')\\ \u00a0\\text{for every }i."
new = "g_i(\\omega)=g_i(\\omega')\\quad\\text{for every }i."
if text.count(old) != 1:
    raise SystemExit(f"expected exactly one spacing cleanup site, found {text.count(old)}")
text = text.replace(old, new, 1)
MANUSCRIPT.write_text(text, encoding="utf-8")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
metadata["text_word_count"] = text_word_count(text)
METADATA.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
