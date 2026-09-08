from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_distance import distance_contract_payloads


def _load(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Measure distance between two finite CREST obstruction profiles."
    )
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    args = parser.parse_args()

    result = distance_contract_payloads(_load(args.before), _load(args.after))
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
