from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROV = (ROOT / "docs" / "glue_white_clover_upstream_provenance_2026-08-24.md").read_text(encoding="utf-8")


def test_provenance_names_source_repo_and_tables() -> None:
    assert "James-S-Santangelo/glue_pc" in PROV
    for path in (
        "allCities_logisticReg_coefs.csv",
        "eniroMeansSlopes.csv",
        "elasticNet_coefSummary.csv",
        "elasticNet_obs_result.csv",
    ):
        assert path in PROV
    assert "10.1126/science.abk0989" in PROV
