#!/usr/bin/env python3
"""Build a deterministic, identity-scrubbed review-code ZIP for the CREST paper.

The archive is whitelist-only and contains the finite implementation needed for
the v0.7 temporal-cut, strict realizability, semantic-access quotient, the
occupancy-aware Rényi access supplement, the prerequisite-support theorem and its
Shannon-uniqueness boundary, and executable shallow-lake prerequisite audit.
Repository history, provenance notes, public URLs, and submission metadata are
excluded.
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
    "crest/companion_realizability.py",
    "crest/explicit_temporal_grammar.py",
    "crest/semantic_access.py",
    "crest/semantic_temporal_quotient.py",
    "crest/renyi_access.py",
    "crest/prerequisite_access_game.py",
    "crest/prerequisite_renyi_leakage.py",
    "crest/shallow_lake_prerequisites.py",
    "tests/test_crest_temporal_cut.py",
    "tests/test_companion_realizability.py",
    "tests/test_explicit_temporal_grammar.py",
    "tests/test_semantic_access.py",
    "tests/test_semantic_temporal_quotient.py",
    "tests/test_renyi_access.py",
    "tests/test_prerequisite_access_game.py",
    "tests/test_prerequisite_renyi_leakage.py",
    "tests/test_shallow_lake_prerequisites.py",
    "tests/test_sparse_semantic_access_benchmark.py",
    "artifacts/crest_sparse_semantic_access_benchmarks_2026-09-08.json",
)

FORBIDDEN_PATTERNS = {
    "repository_owner_handle": re.compile(r"zuizui0223", re.IGNORECASE),
    "github_url": re.compile(r"https?://(?:www\.)?github\.com/", re.IGNORECASE),
    "email": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "orcid": re.compile(r"\bORCID\b", re.IGNORECASE),
}

ANONYMOUS_README = """# Anonymous review code

This archive contains the minimal finite implementation used to reproduce the
manuscript's temporal-cut, strict realizability, semantic-access quotient,
occupancy-aware Rényi access supplement, prerequisite-support theorem and its
Shannon-uniqueness boundary, and shallow-lake prerequisite results. It
intentionally excludes repository history, provenance notes, author metadata,
and external repository links.

## Reproduce the focused tests

```bash
python -m pip install -e '.[dev]'
pytest -q \\
  tests/test_crest_temporal_cut.py \\
  tests/test_companion_realizability.py \\
  tests/test_explicit_temporal_grammar.py \\
  tests/test_semantic_access.py \\
  tests/test_semantic_temporal_quotient.py \\
  tests/test_renyi_access.py \\
  tests/test_prerequisite_access_game.py \\
  tests/test_prerequisite_renyi_leakage.py \\
  tests/test_shallow_lake_prerequisites.py \\
  tests/test_sparse_semantic_access_benchmark.py
```

The v0.7 canonical semantic witness has four retained history-mode x response-type
pairs, only one of which licenses the future decoder. For an m=10 exterior
signature the induced grand quotient contains 1027 classes and the exact
three-way dividend is approximately 8.004220466 bits. The complete-access v0.6
4096-class case is retained only as the k=N boundary.

The Supplement generalizes this support-count result to nonuniform semantic-cell
occupancies. The q=0 Rényi/Hartley endpoint exactly recovers the main-text count;
at q=1 the gain is m times accessible occupancy mass. Tests also verify the
q<1/q=1/q>1 asymptotic slope law, sharp placement extrema, heterogeneous local
decoder capacity, continuous and integer decoder-budget optima, and the Shannon
prerequisite-support theorem linking declared prerequisite sets to exact Möbius
support while semantic coverage changes only the dividend weights.

A minimal two-query witness then tests the boundary of that factorization: no
query requires H and THETA jointly, yet non-Shannon Rényi orders generate a
nonzero H x THETA x F dividend. The leakage vanishes uniquely at q=1 and changes
sign across Shannon order.

The exact main-text numeric table is stored at
`artifacts/crest_sparse_semantic_access_benchmarks_2026-09-08.json` and is
cross-checked against the quotient code.

The shallow-lake code is a finite counterfactual decision model, not empirical
validation. It verifies that different declared targets can require no interface,
history only, response type only, or both retained interfaces.
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
        "schema_version": 5,
        "package_role": "anonymous_review_code",
        "scope": "finite_exact_sparse_semantic_access_renyi_spectrum_and_prerequisite_audit",
        "files": files,
        "semantic_anchor": {
            "bit_depth": 10,
            "history_modes": 2,
            "response_types": 2,
            "semantic_pairs": 4,
            "addressable_pairs": 1,
            "grand_classes": 1027,
            "grand_bits": 10.004220466,
            "three_way_bits": 8.004220466,
            "asymptotic_sparsity_penalty_bits": 2,
        },
        "renyi_access_anchor": {
            "uniform_semantic_probabilities": [0.25, 0.25, 0.25, 0.25],
            "addressable_pairs": 1,
            "bit_depth": 10,
            "q0_gain_bits": 8.004220466,
            "q1_gain_bits": 2.5,
            "asymptotic_slopes": {
                "q_below_1": 1,
                "q_equal_1": 0.25,
                "q_above_1": 0
            }
        },
        "prerequisite_support_anchor": {
            "future_label": "F",
            "canonical_prerequisites": ["H", "THETA"],
            "uniform_accessible_mass": 0.25,
            "bit_depth": 10,
            "shannon_grand_dividend_bits": 2.5,
            "claim": "prerequisite sets determine Shannon Mobius support; semantic coverage determines weights"
        },
        "shannon_uniqueness_anchor": {
            "witness_cells": 2,
            "query_prerequisites": [["H"], ["THETA"]],
            "joint_prerequisite_declared": False,
            "joint_dividend_q1_bits": 0.0,
            "leakage_sign_q_below_1": -1,
            "leakage_sign_q_above_1": 1,
            "claim": "q=1 is the unique zero-leakage Renyi order in the symmetric two-query witness"
        },
        "complete_access_boundary": {
            "semantic_pairs": 4,
            "addressable_pairs": 4,
            "bit_depth": 10,
            "grand_classes": 4096,
            "grand_bits": 12,
            "three_way_bits": 10,
        },
        "shallow_lake_prerequisites": {
            "current_status": [],
            "legacy_sensitive_recovery": ["H"],
            "mechanism_specific_intervention": ["THETA"],
            "composed_restoration_policy": ["H", "THETA"],
        },
        "claim_boundary": [
            "Mobius and Harsanyi accounting are not claimed as mathematical novelty",
            "Renyi entropy, Shannon entropy, Hill numbers, ordinary partition refinement, water-filling, and generic marginal-allocation methods are not claimed as new mathematics",
            "the supplemental contribution includes the selective semantic-access spectrum, the Shannon prerequisite-support factorization, and its non-Shannon leakage boundary",
            "semantic access coverage is distinct from syntactic interface prerequisite order",
            "the shallow-lake audit is an executable finite decision model, not empirical validation",
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
