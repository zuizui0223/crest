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
        assert manifest["schema_version"] == 3
        assert set(manifest["files"]) == set(builder.SOURCE_PATHS)
        for name, metadata in manifest["files"].items():
            payload = archive.read(name)
            assert hashlib.sha256(payload).hexdigest() == metadata["sha256"]
            assert len(payload) == metadata["bytes"]

        anchor = manifest["numeric_anchor"]
        assert anchor["decoder_required_interfaces"] == ["H", "Theta"]
        assert anchor["history_mechanism_classes"] == 4
        assert anchor["joint_classes"] == 4096
        assert anchor["joint_bits"] == 12
        assert anchor["genuine_three_way_bits"] == 10
        assert anchor["state_count_amplification"] == 1024

        counterfactual = manifest["counterfactual_rules"]
        assert counterfactual["no_required_interface_three_way_bits"] == 0
        assert counterfactual["history_only_required_three_way_bits"] == 0
        assert counterfactual["mechanism_only_required_three_way_bits"] == 0
        assert counterfactual["both_interfaces_required_three_way_bits"] == 10


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
        ],
        cwd=extracted,
        text=True,
        capture_output=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
