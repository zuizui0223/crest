#!/usr/bin/env python3
"""Generate the exact anonymous AmNat review manuscript from frozen sources."""

from __future__ import annotations

import argparse
from pathlib import Path

from crest.amnat_submission import DEFAULT_REVIEW_MANUSCRIPT, build_review_manuscript


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_REVIEW_MANUSCRIPT)
    args = parser.parse_args()
    print(build_review_manuscript(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
