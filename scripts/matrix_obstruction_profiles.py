from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_geometry import pairwise_obstruction_distances


def _load(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a pairwise CREST obstruction-profile distance matrix."
    )
    parser.add_argument(
        "contracts",
        nargs="+",
        type=Path,
        help="JSON contract files; file stem is used as the contract name",
    )
    parser.add_argument(
        "--metric",
        default="normalized_l1",
        choices=("raw_l1_bits", "raw_l2_bits", "normalized_l1", "normalized_l2"),
    )
    args = parser.parse_args()

    named = {path.stem: _load(path) for path in args.contracts}
    result = pairwise_obstruction_distances(named, metric=args.metric)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
