#!/usr/bin/env python3
"""Generate the anonymous AmNat review title page from canonical metadata."""

from __future__ import annotations

import argparse
from pathlib import Path

from crest.amnat_submission import DEFAULT_TITLE_PAGE, build_title_page


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_TITLE_PAGE)
    args = parser.parse_args()
    print(build_title_page(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
