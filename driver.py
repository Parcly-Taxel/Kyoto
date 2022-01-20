#!/usr/bin/env python3
import numpy as np
np.set_printoptions(linewidth=400, threshold=2000)
from kyoto.prove import prove_solutions, find_solution
from kyoto.utilities import zbounds, decode_array

A = np.array([[zbounds(2,2, m,n) for n in range(1,32)] for m in range(1,32)])
print(A[:,:,0])
print(A[:,:,1])

"""prove_solutions(2,2, 2,2, 3, {(2,1): 1})
prove_solutions(2,2, 3,3, 6, {(2,2,2): 1})
prove_solutions(2,2, 4,4, 9, {(3,2,2,2): 1})
prove_solutions(2,2, 5,5, 12, {(3,3,2,2,2): 3, (4,2,2,2,2): 1})
prove_solutions(2,2, 6,6, 16, {(3,3,3,3,2,2): 3})
prove_solutions(2,2, 7,7, 21, {(3,)*7: 1})
prove_solutions(2,2, 8,8, 24, {(3,)*8: 8, (4,) + (3,)*6 + (2,): 16})
prove_solutions(2,2, 8,8, 25)
prove_solutions(2,2, 8,9, 26, 1)
prove_solutions(2,2, 8,9, 27)
prove_solutions(2,2, 8,10, 28, 1)
prove_solutions(2,2, 8,10, 29)
prove_solutions(2,2, 9,9, 29, {(4,)*2 + (3,)*7: 2})
prove_solutions(2,2, 9,9, 30)
prove_solutions(2,2, 9,10, 31, 1)
prove_solutions(2,2, 9,10, 32)
prove_solutions(2,2, 9,11, 33, 1)
prove_solutions(2,2, 9,11, 34)
prove_solutions(2,2, 10,10, 34, {(4,)*4 + (3,)*6: 1})
prove_solutions(2,2, 10,10, 35)
with open("kyoto/data/2x2", 'a') as df:
    for (n, z) in enumerate([36, 39, 40, 42, 44, 46, 47], 11):
        lb = prove_solutions(2,2, 10,n, z, 1)
        print(lb)
        ub = prove_solutions(2,2, 10,n, z+1)
        print(ub)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(2,2, 11,11, 39, {(4,)*6 + (3,)*5: 24})
prove_solutions(2,2, 11,11, 40)
with open("kyoto/data/2x2", 'a') as df:
    for (n, z) in enumerate([42, 44, 45, 47, 50, 51, 53, 55], 12):
        lb = prove_solutions(2,2, 11,n, z, 1)
        ub = prove_solutions(2,2, 11,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(2,2, 12,12, 45, {(4,)*9 + (3,)*3: 32})
prove_solutions(2,2, 12,12, 46)
with open("kyoto/data/2x2", 'a') as df:
    for (n, z) in enumerate([48, 49, 51, 53, 55, 57, 60, 61, 63, 65, 66, 68], 13):
        lb = prove_solutions(2,2, 12,n, z, 1)
        ub = prove_solutions(2,2, 12,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(2,2, 13,13, 52, {(4,)*13: 8})
prove_solutions(2,2, 13,13, 53)
for (n, z) in enumerate([53, 55, 57, 59, 61, 64, 66, 67, 69, 71, 73, 75], 14):
    with open("kyoto/data/2x2", 'a') as df:
        lb = prove_solutions(2,2, 13,n, z, 1)
        ub = prove_solutions(2,2, 13,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(2,2, 14,14, 56, {(4,)*14: 28}, True, True)
prove_solutions(2,2, 14,14, 57)
for (n, z) in enumerate([58, 60, 63, 65, 68, 70, 72], 15):
    with open("kyoto/data/2x2", 'a') as df:
        lb = prove_solutions(2,2, 14,n, z, 1, True, True)
        ub = prove_solutions(2,2, 14,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

for (n, z) in enumerate([73, 75], 22):
    with open("kyoto/data/2x2", 'a') as df:
        lb = prove_solutions(2,2, 14,n, z, 1, True, True)
        ub = prove_solutions(2,2, 14,n, z+1, {}, True, True)
        print()
        print(lb + "\n" + ub + "\n", file=df)"""

# XXX GUY'S VALUE FOR z(2,2, 14,24) IS WRONG!!!
# XXX ALL VALUES FOR m = 14 AFTER THIS ARE LIKELY HIGHER!!!

"""for (n, z) in enumerate([78, 80, 82, 84, 86], 24):
    with open("kyoto/data/2x2", 'a') as df:
        lb = prove_solutions(2,2, 14,n, z, 1, True, True)
        ub = prove_solutions(2,2, 14,n, z+1, {}, True, True)
        print()
        print(lb + "\n" + ub + "\n", file=df)

# (4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2) (7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6) is quite a hard case

for (n, z) in enumerate([87, 89, 91, 92, 94], 29):
    with open("kyoto/data/2x2", 'a') as df:
        lb = find_solution(2,2, 14,n, z)
        ub = prove_solutions2(2,2, 14,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions2(2,2, 15,15, 61, {((5,5)+(4,)*12+(3,),)*2: 6})
prove_solutions2(2,2, 15,15, 62)"""

# XXX Guy's values for z(2,2, 15,15) to z(2,2, 15,17) are also too low by 1

"""for (n, z) in enumerate([64, 67, 69, 72, 75, 77, 78, 80, 82, 85, 86, 88, 91, 93, 95, 96, 98, 100, 102], 16):
    with open("kyoto/data/2x2", 'a') as df:
        lb = find_solution(2,2, 15,n, z)
        ub = prove_solutions2(2,2, 15,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions2(2,2, 16,16, 67, {((5,)*3+(4,)*13,)*2: 68, ((5,)*4+(4,)*11+(3,),)*2: 2})
prove_solutions2(2,2, 16,16, 68)

for (n, z) in enumerate([70, 73, 76, 80, 81, 83, 85, 87, 90, 91, 93, 96, 98, 100, 102], 17):
    with open("kyoto/data/2x2", 'a') as df:
        lb = find_solution(2,2, 16,n, z)
        ub = prove_solutions2(2,2, 16,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)
# There is only one case for the upper bound below, but it takes quite a while to prove UNSAT
for (n, z) in enumerate([103], 32):
    with open("kyoto/data/2x2", 'a') as df:
        # lb = find_solution(2,2, 16,n, z)
        ub = prove_solutions2(2,2, 16,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)

prove_solutions(2,2, 17,17, 74, {((5,)*6+(4,)*11,)*2: 20})
prove_solutions(2,2, 17,17, 75)

for (n, z) in enumerate([77, 80, 84, 85, 87, 89, 91, 94, 96, 98, 101, 102], 18):
    with open("kyoto/data/2x2", 'a') as df:
        lb = find_solution(2,2, 17,n, z)
        ub = prove_solutions(2,2, 17,n, z+1)
        print()
        print(lb + "\n" + ub + "\n", file=df)"""
