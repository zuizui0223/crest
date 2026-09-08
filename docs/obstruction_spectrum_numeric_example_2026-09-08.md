# Five-world quantitative obstruction witness

Worlds are ordered as z, a, b, c, r. The baseline partition is

B = {z} | {a,b,c,r},

so |B|=2.

The three structural audits form an activation cascade:

1. CCOC marks a, giving 3 states.
2. MLTR maps b -> a while a,c,r map to r, so once CCOC separates a, MLTR separates b, giving 4 states.
3. MRM maps c -> b while r -> r, so once MLTR separates b, MRM separates c, giving 5 states.

Coalition debts in bits are:

| coalition | blocks | debt |
|---|---:|---:|
| none | 2 | 0 |
| CCOC | 3 | 0.5849625007 |
| MLTR | 2 | 0 |
| MRM | 2 | 0 |
| CCOC+MLTR | 4 | 1.0000000000 |
| CCOC+MRM | 3 | 0.5849625007 |
| MLTR+MRM | 2 | 0 |
| CCOC+MLTR+MRM | 5 | 1.3219280949 |

Therefore

Delta = 1.3219280949 - 0.5849625007 = 0.7369655942 bit.

The order-independent Shapley obstruction spectrum is

| obstruction | standalone D_i | Shapley phi_i | interaction allocation phi_i-D_i |
|---|---:|---:|---:|
| CCOC | 0.5849625007 | 0.8997906153 | 0.3148281146 |
| MLTR | 0 | 0.3148281146 | 0.3148281146 |
| MRM | 0 | 0.1073093650 | 0.1073093650 |
| total | 0.5849625007 | 1.3219280949 | 0.7369655942 |

The key point is numerical rather than terminological: MLTR and MRM have zero standalone debt at the baseline but nonzero joint attribution after upstream distinctions activate them. A list of three definitions cannot show this activation structure; the obstruction spectrum does.
