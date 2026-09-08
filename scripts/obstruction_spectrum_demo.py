"""Print the quantitative CCOC/MLTR/MRM obstruction spectrum witness."""

from crest.joint_state import AuditRefinement
from crest.obstruction_spectrum_v1 import obstruction_spectrum


baseline = (0, 1, 1, 1, 1)
audits = (
    AuditRefinement(
        "CCOC",
        ("ordinary", "future-mark", "ordinary", "ordinary", "ordinary"),
        (),
        ((), (), (), (), ()),
    ),
    AuditRefinement(
        "MLTR",
        ("same",) * 5,
        ("history",),
        ((0,), (4,), (1,), (4,), (4,)),
    ),
    AuditRefinement(
        "MRM",
        ("same",) * 5,
        ("mechanism",),
        ((0,), (4,), (4,), (2,), (4,)),
    ),
)

report = obstruction_spectrum(audits, baseline)
print("baseline blocks:", report.baseline_blocks)
print("joint blocks:", report.joint_blocks)
print("standalone debt:")
for name, value in zip(report.audit_names, report.standalone_debts):
    print(f"  {name}: {value:.6f} bit")
print("Shapley obstruction spectrum:")
for name, value, interaction in zip(
    report.audit_names,
    report.shapley_contributions,
    report.interaction_allocations,
):
    print(f"  {name}: phi={value:.6f} bit, interaction allocation={interaction:.6f} bit")
print(f"joint debt: {report.joint_debt:.6f} bit")
print(f"Delta: {report.delta:.6f} bit")
