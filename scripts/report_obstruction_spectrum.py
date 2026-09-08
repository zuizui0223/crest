from __future__ import annotations

import argparse
import json
from pathlib import Path

from crest.obstruction_spectrum import three_obstruction_spectrum

REPORT = Path("artifacts/crest_obstruction_spectrum.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()

    spectrum = three_obstruction_spectrum()
    payload = {
        "audit_names": spectrum.audit_names,
        "baseline_blocks": spectrum.baseline_blocks,
        "joint_blocks": spectrum.joint_blocks,
        "standalone_debts_bits": dict(
            zip(spectrum.audit_names, spectrum.standalone_debts)
        ),
        "shapley_contributions_bits": dict(
            zip(spectrum.audit_names, spectrum.shapley_contributions)
        ),
        "shapley_shares": dict(zip(spectrum.audit_names, spectrum.shapley_shares)),
        "interaction_attributions_bits": dict(
            zip(spectrum.audit_names, spectrum.interaction_attributions)
        ),
        "joint_debt_bits": spectrum.joint_debt,
        "delta_bits": spectrum.delta,
        "coalitions": [
            {"audits": row.audits, "blocks": row.blocks, "debt_bits": row.debt}
            for row in spectrum.coalition_debts
        ],
        "interaction_dividends": [
            {"audits": row.audits, "order": row.order, "bits": row.bits}
            for row in spectrum.interaction_dividends
        ],
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if args.write_report:
        REPORT.parent.mkdir(parents=True, exist_ok=True)
        REPORT.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
