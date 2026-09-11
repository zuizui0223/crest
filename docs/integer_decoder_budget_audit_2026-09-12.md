# Integer decoder-budget audit

The continuous decoder-allocation result in the AmNat Supplement has been extended to an exact whole-bit allocation rule.

## Claim

For an integer total budget B and semantic occupancies p_i:

- for 0 <= q <= 1, an optimum assigns all B bits to a most-occupied cell (q=0: any vertex is optimal);
- for finite q > 1, each next bit is assigned to the cell maximizing p_i^q 2^{-(q-1)x_i};
- at q = infinity, each next bit is assigned to the cell maximizing p_i 2^{-x_i}.

The q>1 rule is globally optimal because each cell contributes a geometrically decreasing chain of marginal reductions, so the optimum selects the B largest feasible marginals. This is a specialization of standard separable discrete resource-allocation / marginal-allocation machinery, not a claim that the greedy method itself is new.

## Verification contract

`tests/test_renyi_access.py` exhaustively enumerates all integer compositions of a small budget across three cells for q in {0, 0.5, 1, 1.5, 2, 4, infinity} and requires the proposed allocation to attain the global maximum. A separate test verifies that no one-bit exchange improves the q>1 solution.
