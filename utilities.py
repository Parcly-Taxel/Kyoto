#!/usr/bin/env python3
from math import comb
from fractions import Fraction as F

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

def cdiv(a, b):
    """Return ceil(a/b) for a and b positive integers."""
    return -(-a//b)

def get_partitions(a,b, m0,n0, k0, Elims={}):
    """Yield all partitions of k0 into n0 parts from 0 to m0 each
    that satisfy Guy's argument A and (if provided as a dictionary) E for an a-by-b minor."""
    parts = [0] * n0
    Alim = (b-1) * comb(m0,a)
    def P(k, m, n):
        i = n0-n
        if sum(comb(parts[j], a) for j in range(i)) > Alim:
            return
        if k == 0 and all(sum(parts[:j]) <= Elim for (j, Elim) in Elims.items()):
            yield parts
        elif (d := k - (m-1)*n) > 0:
            for j in range(d):
                parts[i+j] = m
            yield from P(k-d*m, m, n-d)
            for j in range(d):
                parts[i+j] = 0
        else:
            for part in range(cdiv(k,n), min(k,m)+1):
                parts[i] = part
                yield from P(k-part, part, n-1)
            parts[i] = 0
    yield from P(k0, m0, n0)
