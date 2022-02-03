#!/usr/bin/env python3
import numpy as np
np.set_printoptions(linewidth=400, threshold=2000)
from kyoto.prove import prove_solutions, find_solution
from kyoto.utilities import zbounds
from kyoto.graphs import decode_array

A = np.array([[zbounds(3,3, m,n) for n in range(1,19)] for m in range(1,19)])
print(A[:,:,0])
print(A[:,:,1])

"""prove_solutions(3,3, 3,3, 8, {((3,3,2),)*2: 1})
prove_solutions(3,3, 4,4, 13, {((4,3,3,3),)*2: 1})
prove_solutions(3,3, 5,5, 20, {((4,4,4,4,4),)*2: 1})
prove_solutions(3,3, 6,6, 26, {((5,5,4,4,4,4),)*2: 1})
prove_solutions(3,3, 6,6, 27)
for (n, z) in enumerate([29, 32, 36, 39], 7):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 6,n, z+1)
        lb = find_solution(3,3, 6,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 7,7, 33, {((6,5,5,5,4,4,4),)*2: 1})
prove_solutions(3,3, 7,7, 34)

for (n, z) in enumerate([37, 40, 44, 47, 50, 53, 56, 60, 63, 66, 69, 72, 75, 78, 81], 8):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 7,n, z+1)
        lb = find_solution(3,3, 7,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 8,8, 42, {((7,)+(5,)*7,)*2: 1})
prove_solutions(3,3, 8,8, 43)

for (n, z) in enumerate([45, 50, 53, 57, 60, 64, 67, 70, 74, 77], 9):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 8,n, z+1)
        lb = find_solution(3,3, 8,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 9,9, 49, {((6,)*4+(5,)*5,)*2: 14,
                               ((6,)*4+(5,)*5, (7,)+(6,)*3+(5,)*4+(4,)): 1,
                               ((7,)+(6,6)+(5,)*6,)*2: 1,
                               ((7,)+(6,)*3+(5,)*4+(4,),)*2: 1})
prove_solutions(3,3, 9,9, 50)

for (n, z) in enumerate([54, 59, 64, 67, 70, 73, 77, 81, 85], 10):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 9,n, z+1)
        lb = find_solution(3,3, 9,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 10,10, 60, {((6,)*10,)*2: 16})
prove_solutions(3,3, 10,10, 61)

for (n, z) in enumerate([64, 68, 73, 77, 81, 85, 90, 94], 11):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 10,n, z+1)
        lb = find_solution(3,3, 10,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 11,11, 69, {((7,)*4+(6,)*6+(5,),)*2: 3})
prove_solutions(3,3, 11,11, 70)

for (n, z) in enumerate([74, 80, 84, 88, 92, 96, 101], 12):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 11,n, z+1)
        lb = find_solution(3,3, 11,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 12,12, 80, {((8,)+(7,)*6+(6,)*5,)*2: 1,
                                 ((7,)*8+(6,)*4,)*2: 1})
prove_solutions(3,3, 12,12, 81)

for (n, z) in enumerate([86, 91, 96, 99], 13):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 12,n, z+1)
        lb = find_solution(3,3, 12,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 13,13, 92, {((8,)*3+(7,)*8+(6,)*2,)*2: 1})
prove_solutions(3,3, 13,13, 93)

for (n, z) in enumerate([98, 104, 107], 14):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 13,n, z+1)
        lb = find_solution(3,3, 13,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 14,14, 105, {((8,)*7+(7,)*7,)*2: 1})
prove_solutions(3,3, 14,14, 106)

for (n, z) in enumerate([112, 115], 15):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 14,n, z+1)
        lb = find_solution(3,3, 14,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(3,3, 15,15, 120, {((8,)*15,)*2: 1})
prove_solutions(3,3, 15,15, 121)

for (n, z) in enumerate([123], 16):
    with open("kyoto/data/3x3", 'a') as df:
        ub = prove_solutions(3,3, 15,n, z+1)
        lb = find_solution(3,3, 15,n, z)
        print()
        print(lb + "\n" + ub + "\n", file=df)"""
