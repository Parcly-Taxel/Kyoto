#!/usr/bin/env python3
import numpy as np
from kyoto.zcnf import zaran_cnf
from kyoto.graphs import encode_array

# For the 23×23 [5^23, 5^23] case the first five rows and columns are completely forced
# by the existing constraints. These generate a 4×4 grid of 4×4 boxes; we split on the sums
# of these boxes, the whole grid of which may be freely permuted boxwise and then lex-sorted
# normally *while preserving the box sums*. A combinatorial argument shows that the non-isomorphic
# sum configurations are in bijection with disjoint unions of even cycles (including the 2-cycle)
# optionally minus an edge, 12 in all. These cases form the secondary split and are enough to
# generate all solutions in a reasonable time - 310 solutions which happen to be all isomorphic.

boxsums = [[2,4,4,4,4,2,4,4,4,4,2,4,4,4,4,2],
[3,4,4,4,4,2,4,4,4,4,2,4,4,4,4,2],
[2,4,4,4,4,2,4,4,4,4,3,3,4,4,3,3],
[3,4,4,4,4,2,4,4,4,4,3,3,4,4,3,3],
[2,4,4,4,4,2,4,4,4,4,3,3,4,4,3,4],
[2,4,4,4,4,3,3,4,4,3,4,3,4,4,3,3],
[3,4,4,4,4,3,3,4,4,3,4,3,4,4,3,3],
[2,4,4,4,4,3,3,4,4,3,4,3,4,4,3,4],
[3,3,4,4,3,3,4,4,4,4,3,3,4,4,3,3],
[3,3,4,4,3,3,4,4,4,4,3,3,4,4,3,4],
[3,3,4,4,3,4,3,4,4,3,4,3,4,4,3,4],
[3,3,4,4,3,4,3,4,4,3,4,3,4,4,3,3]]
boxsums = [np.array(l).reshape(4,4) for l in boxsums]
solcounts = [0, 0, 0, 0, 16, 48, 0, 0, 192, 0, 6, 48]

for (n, bs) in enumerate(boxsums):
    cnf = zaran_cnf(2,2, 23,23)
    cnf.set_col_counts((5,)*23)
    cnf.set_row_counts((5,)*23)
    for i in range(4):
        for j in range(4):
            cnf.add_card_constraint_sinz(cnf.bitfield[5+4*i:9+4*i,5+4*j:9+4*j].flatten(), bs[i,j])
    print(f"{n}:")
    print(bs)
    for sol in cnf.find_all_solutions(f"23-{n}", solcounts[n], f"23-{n}"):
        print(encode_array(sol))
