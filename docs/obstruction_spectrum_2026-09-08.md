# Quantitative obstruction spectrum

This note defines a numerical accounting layer for the three structural CREST obstructions (CCOC, MLTR, MRM) on a declared finite common carrier.

For a coalition S of structural audits, let J_S be the least common fixed point above baseline partition B and define

D(S) = log2 |J_S| - log2 |B|.

The standalone debt of audit i is D({i}). The joint debt is D(N). Existing CREST interaction debt is

Delta = D(N) - sum_i D({i}).

To assign the joint debt to named obstruction axes without choosing an audit order, define the Shapley obstruction contribution

phi_i = sum_{S subseteq N\\{i}} |S|!(n-|S|-1)!/n! * [D(S union {i}) - D(S)].

Then sum_i phi_i = D(N). Define the interaction allocation on axis i by

I_i = phi_i - D({i}),

so sum_i I_i = Delta.

Interpretation:

- D({i}) is what obstruction i costs when inspected alone from the baseline.
- phi_i is its order-independent share of the fully activated joint state debt.
- I_i is how much its attributed burden changes because other responsibilities activate or overlap with it.
- positive I_i means net interaction amplification on that axis; negative I_i means net overlap/redundancy.

This is an accounting theorem relative to the declared finite structural audits. It does not imply statistical independence, causal independence, or universal exhaustiveness of CCOC/MLTR/MRM.
