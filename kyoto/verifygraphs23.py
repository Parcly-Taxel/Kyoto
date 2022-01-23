#!/usr/bin/env python3
import numpy as np
from kyoto.graphs import encode_array, decode_array, Btog6
rng = np.random.default_rng()

# A 2.5-hour sharpSAT (https://github.com/marcthurley/sharpSAT) run shows that
# the CNF corresponding to the z(2,2, 23,23) = 115, 5^23/5^23 case has 46656 = 6^6 solutions.
# This program generates 46656 distinct solutions from one graph, showing that the CNF's solutions
# are all isomorphic.

A = decode_array("23 23 C0EAC0EAC0EAC0EAC0EAC0EAC0EAC0EAC8EAC4EAC4EAC4EAC4EAC4EAC4MAC4IAC4IAC4IAC4IAG4IAE4IAF4IAAQ==")
powers = (2**np.arange(23))[::-1]

def lsort1(X):
    return X[np.argsort(X @ powers)[::-1]]

def lsort(X):
    while True:
        Y = lsort1(lsort1(X).T).T
        if np.all(X == Y):
            return Y
        X = Y

def randsorted():
    perm1 = rng.permutation(np.arange(23))
    perm2 = rng.permutation(np.arange(23))
    return lsort(A[np.ix_(perm1,perm2)])

seen = set()
while len(seen) < 6**6:
    A = randsorted()
    new = encode_array(A)
    if new not in seen:
        newT = encode_array(A.T)
        if newT not in seen:
            print(new)
            print(newT)
            seen.add(new)
            seen.add(newT)
        else:
            print(new, "*")
            seen.add(new)
