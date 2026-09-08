from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_io import spectrum_payload
from crest.obstruction_spectrum import three_obstruction_spectrum

REPORT = Path("artifacts/crest_obstruction_spectrum.json")
CANONICAL_CARRIER_WORLDS = 6


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    spectrum = three_obstruction_spectrum()
    payload = spectrum_payload(
        spectrum, carrier_worlds=CANONICAL_CARRIER_WORLDS
    )
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
