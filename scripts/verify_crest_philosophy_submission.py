from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TARGET = Path("manuscript/crest_biology_philosophy_blinded_submission.md")
REPORT = Path("artifacts/crest_philosophy_submission_report.json")


def visible_text(markdown: str) -> str:
    text = re.sub(r"<!--.*?-->", " ", markdown, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", re.sub(r"[*_>#|]", " ", text)).strip()


def word_count(markdown: str) -> int:
    return len(re.findall(r"\b[\w’'-]+\b", visible_text(markdown), flags=re.UNICODE))


def between(text: str, start: str, end: str) -> str:
    if start not in text or end not in text.split(start, 1)[1]:
        raise ValueError(f"missing section boundary: {start!r} -> {end!r}")
    return text.split(start, 1)[1].split(end, 1)[0].strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    text = TARGET.read_text(encoding="utf-8")
    abstract = between(text, "## Abstract", "**Keywords:**")
    keyword_line = between(text, "**Keywords:**", "## 1.").splitlines()[0]
    keywords = [x.strip() for x in keyword_line.split(";") if x.strip()]
    pre_references = text.split("## References", 1)[0]

    blind_patterns = {
        "github": r"github(?:\.com)?",
        "owner_handle": r"zuizui0223",
        "email": r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        "pull_request": r"\b(?:PR|pull request)\s*#?\d+\b",
        "author_metadata": r"AUTHOR INPUT REQUIRED|Corresponding author",
    }
    blind_hits = {
        name: sorted(set(re.findall(pattern, pre_references, flags=re.I)))
        for name, pattern in blind_patterns.items()
        if re.search(pattern, pre_references, flags=re.I)
    }

    required = [
        "## 1. The ecological state problem begins with a conservation paradox",
        "## 2. Ecological state as scientifically constrained equivalence",
        "## 3. A worked ecological case: shallow-lake restoration",
        "## 4. The finite CREST architecture",
        "## 5. Main result: capability–resolution divergence",
        "## 6. Conservation capacity can outgrow conservation knowledge",
        "## 7. Relation to abstraction, adequacy, and multiple realization",
        "## 8. Limits and conclusion",
        "\\Delta|K^*|=1",
        "\\Delta K_{U_0}=m",
        "conservation capacity can outgrow conservation knowledge",
        "required state",
        "identified state",
        "reportable target",
        "Potochnik",
        "Odenbaugh",
        "Batterman",
        "Wimsatt",
        "Yates et al. 2018",
    ]
    missing = [item for item in required if item not in text]
    abstract_words = word_count(abstract)
    body_words = word_count(pre_references)

    blockers = []
    if not 150 <= abstract_words <= 250:
        blockers.append(f"abstract word count {abstract_words} is outside 150-250")
    if not 4 <= len(keywords) <= 6:
        blockers.append(f"keyword count {len(keywords)} is outside 4-6")
    if body_words > 10_000:
        blockers.append(f"main-text word count {body_words} exceeds 10,000")
    if blind_hits:
        blockers.append(f"potential blinded identifiers found: {sorted(blind_hits)}")
    if missing:
        blockers.append("missing canonical claims/sections: " + ", ".join(missing))

    report = {
        "target": str(TARGET),
        "abstract_words": abstract_words,
        "main_text_words_before_references": body_words,
        "keyword_count": len(keywords),
        "blind_hits": blind_hits,
        "missing_canonical_items": missing,
        "blockers": blockers,
        "status": "pass" if not blockers else "fail",
    }
    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if not blockers else 1


if __name__ == "__main__":
    raise SystemExit(main())
