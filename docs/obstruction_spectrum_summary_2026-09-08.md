# Obstruction spectrum: current deliverable

The quantitative CREST structural output for one declared finite contract is now:

- standalone debt vector D_i;
- all coalition debts D(S);
- order-independent Shapley obstruction spectrum phi_i;
- interaction allocation I_i = phi_i - D_i;
- joint debt D_joint;
- non-additivity Delta = D_joint - sum_i D_i.

For the five-world CCOC -> MLTR -> MRM activation cascade:

CCOC: D=0.5849625007, phi=0.8997906153 bit
MLTR: D=0, phi=0.3148281146 bit
MRM: D=0, phi=0.1073093650 bit
joint debt=1.3219280949 bit
Delta=0.7369655942 bit

This turns the three structural obstruction labels into a numerical profile while preserving CREST's existing fixed-point semantics and non-additive joint-debt result.
