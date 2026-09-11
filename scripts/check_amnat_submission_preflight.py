#!/usr/bin/env python3
"""Report whether the AmNat submission is ready for literal upload."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.amnat_preflight import DECLARATIONS_TEMPLATE, preflight, write_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--declarations", type=Path, default=DECLARATIONS_TEMPLATE)
    parser.add_argument("--pdf-verified", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = preflight(
        args.declarations,
        pdf_visual_and_font_gate_confirmed=args.pdf_verified,
    )
    if args.output:
        print(
            write_report(
                args.output,
                args.declarations,
                pdf_visual_and_font_gate_confirmed=args.pdf_verified,
            )
        )
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))

    return 0 if result["repository_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
