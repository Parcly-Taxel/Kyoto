#!/usr/bin/env python3
from zcnf import zaran_cnf
from utilities import get_partitions

def prove_val(a,b, m,n, k, mode=0):
    """0 = prove no solutions, 1 = find one solution, 2 = find all solutions"""
    L = []
    for rpart in get_partitions(a,b, m,n, k):
        L.append(rpart)
    print(f"AE-admissible partitions {len(L)}")
    0 / 0
    for rpart in L:
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(rpart)
        cnf.set_row_counts()
        # cnf.findallsols(f"{body}.cnf", nsols, proof=f"{body}.drat")

prove_val(2,2, 9,9, 29)

"""
z(2,2,2,2) >= 3
AE-admissible partitions 0
[2, 1] solutions ...
[matrix code 1]
non-isomorphic witnesses 1
[matrix code 1]

z(2,2,7,7) = 21
non-isomorphic witnesses 1
[matrix code 1]

z(2,2,8,8) < 25
AE-admissible partitions 0

z(2,2,8,8) >= 24
AE-admissible partitions 1
[3, 3, 3, 3, 3, 3, 3, 3] solutions [n]
[matrix code 1]
[matrix code 2] ...
[matrix code n]
non-isomorphic witnesses 1
[matrix code 1]

z(2,2,8,10) >= 27
witness [matrix code]
"""
