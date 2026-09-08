from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_io import spectrum_from_payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute the exact CREST obstruction spectrum for one finite JSON contract."
    )
    parser.add_argument("input", type=Path, help="JSON contract path")
    parser.add_argument("--output", type=Path, help="optional output JSON path")
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    report = spectrum_from_payload(payload)
    text = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
