#!/usr/bin/env python3
from math import comb
from fractions import Fraction as F
from base64 import b64encode
import numpy as np

def romanbound1(a,b, m,n):
    f = lambda p: int(F(b-1, comb(p,a-1))*comb(m,a) + F((p+1)*(a-1), a)*n)
    p = a-1
    prev = f(p)
    while True:
        nxt = f(p+1)
        if nxt >= prev:
            return prev
        prev = nxt
        p += 1

def romanbound(a,b, m,n):
    return min(romanbound1(a,b, m,n), romanbound1(b,a, n,m))

def packlimit(a,b, m):
    if (a,b) == (2,2): # OEIS A001839
        t = (m-1)//2*m//3 - (m%6 == 5)
        return comb(m,2) - 2*t - (m%6 not in (1,3)) # subtract a-1 iff the packing is not exact
    return (b-1) * comb(m,a)

def zbounds(a,b, m,n):
    """Return bounds for Zarankiewicz's function at the given arguments."""
    if m-a > n-b:
        return zbounds(b,a, n,m)
    ub = romanbound(a,b, m,n)
    if packlimit(a,b, m) <= n:
        return [ub, ub] # Roman's bound is exact in these cases
    return [0, ub]

def get_partitions(a,b, m0,n0, k0, Elims={}):
    """Return a list of all partitions of k0 into n0 parts from 0 to m0 each
    that satisfy Guy's argument A and (if provided as a dictionary) E for an a-by-b minor."""
    Alim = (b-1) * comb(m0,a)
    def P(k, m, n, partial=[]):
        completes = []
        if sum(comb(part, a) for part in partial) > Alim:
            return []
        if k == 0 and all(sum(partial[:j]) <= Elim for (j, Elim) in Elims.items()):
            return [tuple(partial)]
        if (d := k - (m-1)*n) > 0:
            completes.extend(P(k-d*m, m, n-d, partial + [m]*d))
        else:
            for part in range(-(-k//n), min(k,m)+1):
                completes.extend(P(k-part, part, n-1, partial + [part]))
        return completes
    return P(k0, m0, n0)

def encode_array(A):
    """To encode the 0-1 matrix A it is first flattened, padded to a multiple of 8 bits
    with zeros, then reshaped to an (N,8)-shape matrix. Each row is then read as a little-endian
    byte and the resulting byte sequence is base64 encoded. The final code is then
    "[height] [width] [base64]"."""
    Af = A.flatten()
    b = np.pad(Af, (0,-len(Af)%8)).reshape(-1,8) @ 2**np.arange(8)
    return f"{A.shape[0]} {A.shape[1]} {b64encode(bytes(list(b))).decode()}"
