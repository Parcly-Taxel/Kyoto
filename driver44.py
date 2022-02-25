#!/usr/bin/env python3
import numpy as np
np.set_printoptions(linewidth=400, threshold=2000)
from kyoto.prove import prove_solutions, find_solution
from kyoto.utilities import zbounds
from kyoto.graphs import decode_array

A = np.array([[zbounds(4,4, m,n) for n in range(1,15)] for m in range(1,15)])
print(A[:,:,0])
print(A[:,:,1])

"""prove_solutions(4,4, 4,4, 15, {((4,4,4,3),)*2: 1})

prove_solutions(4,4, 5,5, 22, {((5,5,4,4,4),)*2: 1})

prove_solutions(4,4, 6,6, 31, {((6,5,5,5,5,5),)*2: 1})
prove_solutions(4,4, 6,6, 32)
for (n, z) in enumerate([36, 39, 43, 47, 51, 55, 59], 7):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 6,n, z+1)
        lb = find_solution(4,4, 6,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 7,7, 42, {((6,)*7,)*2: 1})
prove_solutions(4,4, 7,7, 43)
for (n, z) in enumerate([45, 49, 54, 58, 63, 68, 72], 8):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 7,n, z+1)
        lb = find_solution(4,4, 7,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 8,8, 51, {((7,)*3+(6,)*5,)*2: 2})
prove_solutions(4,4, 8,8, 52)
for (n, z) in enumerate([55, 60, 65, 70, 75, 80], 9):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 8,n, z+1)
        lb = find_solution(4,4, 8,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 9,9, 61, {((8,)*2+(7,)*3+(6,)*4,)*2: 13,
                               ((8,)+(7,)*5+(6,)*3,)*2: 225})
prove_solutions(4,4, 9,9, 62)
for (n, z) in enumerate([67, 72, 78, 84, 88], 10):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 9,n, z+1)
        lb = find_solution(4,4, 9,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 10,10, 74, {((9,)*2+(7,)*8,)*2: 8})
prove_solutions(4,4, 10,10, 75)
for (n, z) in enumerate([79, 86, 93, 97], 11):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 10,n, z+1)
        lb = find_solution(4,4, 10,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 11,11, 86, {((7,)*2+(8,)*9,)*2: 66,
                                 ((10,)+(7,)*4+(8,)*6,)*2: 1,
                                 ((10,)+(7,)*4+(8,)*6, (10,9)+(8,)*4+(7,)*5): 3}, True)
prove_solutions(4,4, 11,11, 87)
for (n, z) in enumerate([93, 100], 12):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 11,n, z+1)
        lb = find_solution(4,4, 11,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 12,12, 100, {((9,)*4+(8,)*8,)*2: 1,
                                  ((11,)+(9,)*3+(8,)*6+(7,)*2,)*2: 1})
prove_solutions(4,4, 12,12, 101)
for (n, z) in enumerate([108], 13):
    with open("kyoto/data/4x4", 'a') as df:
        ub = prove_solutions(4,4, 12,n, z+1)
        lb = find_solution(4,4, 12,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(4,4, 13,13, 117, {((9,)*13,)*2: 8})
prove_solutions(4,4, 13,13, 118)
"""
