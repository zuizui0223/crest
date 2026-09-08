#!/usr/bin/env python3
"""Print reproducible submission metadata for the CREST AmNat manuscript."""

from __future__ import annotations

import json

from crest.amnat_submission import current_report


def main() -> int:
    print(json.dumps(current_report(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
