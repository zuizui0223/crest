#!/usr/bin/env python3
"""Build a deterministic, identity-scrubbed review-code ZIP for the CREST paper.

The archive is whitelist-only and contains the finite implementation needed for
the v0.6 temporal-cut, companion-realizability, and explicit grammar/trace
quotient characterization theorem. Repository history, provenance notes,
empirical bridges, public URLs, and submission metadata are excluded.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "dist" / "anonymous_review_code.zip"

SOURCE_PATHS = (
    "pyproject.toml",
    "crest/__init__.py",
    "crest/joint_state.py",
    "crest/temporal_cut.py",
    "crest/temporal_interaction.py",
    "crest/companion_realizability.py",
    "crest/explicit_temporal_grammar.py",
    "tests/test_crest_temporal_cut.py",
    "tests/test_companion_realizability.py",
    "tests/test_explicit_temporal_grammar.py",
    "artifacts/crest_explicit_grammar_benchmarks_2026-09-08.json",
)

FORBIDDEN_PATTERNS = {
    "repository_owner_handle": re.compile(r"zuizui0223", re.IGNORECASE),
    "github_url": re.compile(r"https?://(?:www\.)?github\.com/", re.IGNORECASE),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "orcid": re.compile(r"\bORCID\b", re.IGNORECASE),
}

ANONYMOUS_README = """# Anonymous review code

This archive contains the minimal finite implementation used to reproduce the
manuscript's temporal-cut, strict realizability, and explicit grammar/trace
quotient results. It intentionally excludes repository history, provenance notes,
empirical material, author metadata, and external repository links.

## Reproduce the focused theorem tests

```bash
python -m pip install -e '.[dev]'
pytest -q \\
  tests/test_crest_temporal_cut.py \\
  tests/test_companion_realizability.py \\
  tests/test_explicit_temporal_grammar.py
```

The canonical benchmark is stored at
`artifacts/crest_explicit_grammar_benchmarks_2026-09-08.json`.

The focused package includes counterfactual decoder rules: allowing the future
decoder to bypass one or both component interfaces moves the exterior burden to
a lower-order term and destroys the pure three-way result. The review package
therefore tests a falsifiable interaction-order characterization rather than a
directly assigned coalition-value table.
"""


def _read_source(path: str) -> bytes:
    source = ROOT / path
    if not source.is_file():
        raise FileNotFoundError(f"required anonymous-bundle source is missing: {path}")
    return source.read_bytes()


def _scan_text(label: str, payload: bytes) -> None:
    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValueError(f"anonymous bundle accepts UTF-8 text only: {label}") from error
    for pattern_name, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            raise ValueError(
                f"identity-sensitive token {pattern_name!r} found in anonymous payload {label!r}"
            )


def _zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def _manifest(source_payloads: dict[str, bytes]) -> bytes:
    files = {
        name: {
            "sha256": hashlib.sha256(payload).hexdigest(),
            "bytes": len(payload),
        }
        for name, payload in sorted(source_payloads.items())
    }
    manifest = {
        "schema_version": 3,
        "package_role": "anonymous_review_code",
        "scope": "finite_exact_explicit_grammar_trace_quotient_theorems",
        "files": files,
        "numeric_anchor": {
            "bit_depth": 10,
            "decoder_required_interfaces": ["H", "Theta"],
            "history_mechanism_classes": 4,
            "joint_classes": 4096,
            "history_mechanism_bits": 2,
            "joint_bits": 12,
            "genuine_three_way_bits": 10,
            "state_count_amplification": 1024,
            "three_way_fraction_of_joint": 10 / 12,
        },
        "counterfactual_rules": {
            "no_required_interface_three_way_bits": 0,
            "history_only_required_three_way_bits": 0,
            "mechanism_only_required_three_way_bits": 0,
            "both_interfaces_required_three_way_bits": 10,
        },
        "claim_boundary": [
            "coalition values are induced by explicit legal grammars and trace quotients",
            "pure three-way interaction is conditional on both interfaces being decoder prerequisites",
            "alternative decoder rules move the same exterior burden to lower-order terms",
            "no empirical data are included",
            "no continuous-time or stochastic generalization is claimed",
        ],
    }
    return (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_bundle(output: Path = DEFAULT_OUTPUT) -> Path:
    """Build and return the deterministic anonymous review archive."""

    payloads = {path: _read_source(path) for path in SOURCE_PATHS}
    generated = {
        "ANONYMOUS_README.md": ANONYMOUS_README.encode("utf-8"),
        "ANONYMOUS_MANIFEST.json": _manifest(payloads),
    }
    all_payloads = {**payloads, **generated}

    for name, payload in all_payloads.items():
        _scan_text(name, payload)

    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, mode="w") as archive:
        for name in sorted(all_payloads):
            archive.writestr(_zip_info(name), all_payloads[name])
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="output ZIP path (default: dist/anonymous_review_code.zip)",
    )
    args = parser.parse_args()
    output = build_bundle(args.output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
