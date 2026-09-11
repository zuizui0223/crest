from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_amnat_anonymous_bundle.py"


def _load_builder():
    spec = importlib.util.spec_from_file_location("amnat_anonymous_bundle", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _archive_bytes(path: Path) -> bytes:
    return path.read_bytes()


def test_anonymous_bundle_is_whitelist_only_and_identity_scrubbed(tmp_path: Path) -> None:
    builder = _load_builder()
    output = builder.build_bundle(tmp_path / "review.zip")

    expected = set(builder.SOURCE_PATHS) | {
        "ANONYMOUS_README.md",
        "ANONYMOUS_MANIFEST.json",
    }
    with zipfile.ZipFile(output) as archive:
        assert set(archive.namelist()) == expected
        assert all(not name.startswith(".git") for name in archive.namelist())
        combined = b"\n".join(archive.read(name) for name in archive.namelist()).decode("utf-8")

    forbidden = (
        r"zuizui0223",
        r"https?://(?:www\.)?github\.com/",
        r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",
        r"\bORCID\b",
    )
    for pattern in forbidden:
        assert re.search(pattern, combined, re.IGNORECASE) is None


def test_anonymous_bundle_is_byte_deterministic(tmp_path: Path) -> None:
    builder = _load_builder()
    first = builder.build_bundle(tmp_path / "first.zip")
    second = builder.build_bundle(tmp_path / "second.zip")
    assert _archive_bytes(first) == _archive_bytes(second)


def test_anonymous_manifest_hashes_every_whitelisted_source(tmp_path: Path) -> None:
    builder = _load_builder()
    output = builder.build_bundle(tmp_path / "review.zip")

    with zipfile.ZipFile(output) as archive:
        manifest = json.loads(archive.read("ANONYMOUS_MANIFEST.json"))
        assert manifest["schema_version"] == 5
        assert set(manifest["files"]) == set(builder.SOURCE_PATHS)
        assert "crest/renyi_access.py" in manifest["files"]
        assert "tests/test_renyi_access.py" in manifest["files"]
        assert "crest/prerequisite_access_game.py" in manifest["files"]
        assert "tests/test_prerequisite_access_game.py" in manifest["files"]
        assert "crest/prerequisite_renyi_leakage.py" in manifest["files"]
        assert "tests/test_prerequisite_renyi_leakage.py" in manifest["files"]
        for name, metadata in manifest["files"].items():
            payload = archive.read(name)
            assert hashlib.sha256(payload).hexdigest() == metadata["sha256"]
            assert len(payload) == metadata["bytes"]

        anchor = manifest["semantic_anchor"]
        assert anchor["semantic_pairs"] == 4
        assert anchor["addressable_pairs"] == 1
        assert anchor["grand_classes"] == 1027
        assert abs(anchor["grand_bits"] - 10.004220466) < 1e-9
        assert abs(anchor["three_way_bits"] - 8.004220466) < 1e-9
        assert anchor["asymptotic_sparsity_penalty_bits"] == 2

        renyi = manifest["renyi_access_anchor"]
        assert renyi["addressable_pairs"] == 1
        assert renyi["bit_depth"] == 10
        assert abs(renyi["q0_gain_bits"] - 8.004220466) < 1e-9
        assert renyi["q1_gain_bits"] == 2.5
        assert renyi["asymptotic_slopes"] == {
            "q_below_1": 1,
            "q_equal_1": 0.25,
            "q_above_1": 0,
        }

        support = manifest["prerequisite_support_anchor"]
        assert support["future_label"] == "F"
        assert support["canonical_prerequisites"] == ["H", "THETA"]
        assert support["uniform_accessible_mass"] == 0.25
        assert support["bit_depth"] == 10
        assert support["shannon_grand_dividend_bits"] == 2.5

        uniqueness = manifest["shannon_uniqueness_anchor"]
        assert uniqueness["witness_cells"] == 2
        assert uniqueness["query_prerequisites"] == [["H"], ["THETA"]]
        assert uniqueness["joint_prerequisite_declared"] is False
        assert uniqueness["joint_dividend_q1_bits"] == 0.0
        assert uniqueness["leakage_sign_q_below_1"] == -1
        assert uniqueness["leakage_sign_q_above_1"] == 1

        boundary = manifest["complete_access_boundary"]
        assert boundary["addressable_pairs"] == 4
        assert boundary["grand_classes"] == 4096
        assert boundary["three_way_bits"] == 10

        lake = manifest["shallow_lake_prerequisites"]
        assert lake["current_status"] == []
        assert lake["legacy_sensitive_recovery"] == ["H"]
        assert lake["mechanism_specific_intervention"] == ["THETA"]
        assert lake["composed_restoration_policy"] == ["H", "THETA"]


def test_anonymous_bundle_runs_focused_theorem_tests(tmp_path: Path) -> None:
    builder = _load_builder()
    output = builder.build_bundle(tmp_path / "review.zip")
    extracted = tmp_path / "extracted"
    with zipfile.ZipFile(output) as archive:
        archive.extractall(extracted)

    completed = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "-q",
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
        ],
        cwd=extracted,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
