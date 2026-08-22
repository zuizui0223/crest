from pathlib import Path

path = Path("manuscript/crest_philosophy_biology_philosophy.md")
text = path.read_text()

needle = "observational symmetry.\\n\\nThese consequences do not impose a mandatory pipeline"
replacement = "observational symmetry.\n\nThese consequences do not impose a mandatory pipeline"

if text.count(needle) != 1:
    raise SystemExit(f"expected one escaped-newline target, found {text.count(needle)}")
text = text.replace(needle, replacement)
path.write_text(text)
