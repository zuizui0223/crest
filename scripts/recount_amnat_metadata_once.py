#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from crest.amnat_submission import text_word_count

ROOT = Path(__file__).resolve().parents[1]
manuscript = ROOT / "manuscript" / "crest_flagship_amnat_v0.7_semantic_access.md"
metadata_path = ROOT / "manuscript" / "amnat_submission_metadata.json"

text = manuscript.read_text(encoding="utf-8")
metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
metadata["text_word_count"] = text_word_count(text)
metadata_path.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(metadata["text_word_count"])
