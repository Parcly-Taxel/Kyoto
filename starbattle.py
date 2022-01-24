#!/usr/bin/env python3
import numpy as np
from kyoto.zcnf import zaran_cnf

# https://puzzling.stackexchange.com/q/114592

cnf = zaran_cnf(0,0, 9,9)
cnf.clauses = []
bf = cnf.bitfield
for i in range(9):
    cnf.add_card_constraint_sinz(bf[i], 2)
    cnf.add_card_constraint_sinz(bf[:,i], 2)
for i in (0, 3, 6):
    for j in (0, 3, 6):
        cnf.add_card_constraint_sinz(bf[i:i+3,j:j+3].flatten(), 2)
for i in range(9):
    for j in range(8):
        cnf.clauses.append([-bf[i,j], -bf[i,j+1]])
        cnf.clauses.append([-bf[j,i], -bf[j+1,i]])
for i in range(8):
    for j in range(8):
        cnf.clauses.append([-bf[i,j], -bf[i+1,j+1]])
        cnf.clauses.append([-bf[i+1,j], -bf[i,j+1]])

def isomorphic(A, B):
    return any(np.all(B == np.rot90(M, k)) for M in (A, A.T) for k in range(4))

fn = "starbat"

sols = []
for (i, sol) in enumerate(cnf.find_all_solutions(fn, 1000, fn), 1):
    print(i)
    if not sols or not any(isomorphic(sol, esol) for esol in sols):
        print()
        s = "\n".join("".join("*" if c else "." for c in r) for r in sol)
        print(s)
        sols.append(sol)
