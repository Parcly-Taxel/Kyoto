#!/usr/bin/env python3
import numpy as np
np.set_printoptions(linewidth=300)
from kyoto.prove import prove_solutions
from kyoto.utilities import zbounds, decode_array

A = np.array([[zbounds(2,2, m,n) for n in range(2,32)] for m in range(2,32)])
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
        print(lb + "\n" + ub + "\n", file=df)"""

for arr_s in ("14 24 xwAAGQMAAXwAAYAPKoQAEggRAhFiDCAkNEACBIrASEBYkASoYCGBoBIU", "14 25 xwAAMgYABPABCAB8oEAIUQYhgECEGBYIAhQgggkUcCABhYIEogImCgS0ABE=",
        "14 26 DwAAxAcAEOADQADwARJCGIgQgiGEEBiRgIiEEEkQFFCCAiERIhgoCIkIQoAQDQ==", "14 27 +QAACPgAQAD4AAIA+KAQQggJIYSIEEJICCGEDEhAooCBIImAKAgJCgIECRzAAAUD",
        "14 28 +QAAEPABAAHgAxAAwAcKIYQgIYQQIoQQIoQQQgwCIkIBEQkkQUBEiEgQQDBAC0igyA=="):
    A = decode_array(arr_s)
    print("\n".join("".join("1" if c else "." for c in r) for r in A))
    print()
