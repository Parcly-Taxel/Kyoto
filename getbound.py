#!/usr/bin/env python3
from math import comb
from fractions import Fraction as F

def romanbound1(a, b, m, n):
    f = lambda p: int(F(b-1, comb(p,a-1))*comb(m,a) + F((p+1)*(a-1), a)*n)
    p = a-1
    prev = f(p)
    while True:
        nxt = f(p+1)
        if nxt >= prev:
            return prev
        prev = nxt
        p += 1

def romanbound(a, b, m, n):
    return min(romanbound1(a, b, m, n), romanbound1(b, a, n, m))

def packlimit(a, b, m):
    if (a, b) == (2, 2): # OEIS A001839
        t = (m-1)//2*m//3 - (m%6 == 5)
        return comb(m,2) - 2*t - (m%6 not in (1,3)) # subtract a-1 iff the packing is not exact
    return (b-1) * comb(m,a)

def zbounds(a, b, m, n):
    """Return bounds for Zarankiewicz's function at the given arguments."""
    if m-a > n-b:
        return zbounds(b, a, n, m)
    ub = romanbound(a, b, m, n)
    if packlimit(a, b, m) <= n:
        return [ub, ub] # Roman's bound is exact in these cases
    return [0, ub]
