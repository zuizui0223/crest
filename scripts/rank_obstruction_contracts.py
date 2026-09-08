from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_batch import rank_obstruction_contracts


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "contracts",
        nargs="+",
        help="JSON files containing finite CREST obstruction contracts",
    )
    parser.add_argument(
        "--rank-by",
        default="normalized_joint_burden",
        choices=(
            "normalized_joint_burden",
            "joint_debt_bits",
            "interaction_fraction_of_joint",
            "delta_bits",
        ),
    )
    args = parser.parse_args()

    payloads = {
        Path(path).stem: json.loads(Path(path).read_text(encoding="utf-8"))
        for path in args.contracts
    }
    result = rank_obstruction_contracts(payloads, rank_by=args.rank_by)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
