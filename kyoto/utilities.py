#!/usr/bin/env python3
import re
from math import comb
from itertools import product, combinations_with_replacement
from fractions import Fraction as F
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

def packable_simplices(a,b, m):
    """Return (a lower bound on) the largest number of complete a-graphs on a+1 vertices
    that can be packed into the complete a-graph on m vertices duplicated b-1 times."""
    if a+1 > m:
        return 0
    if a+1 == m:
        return b-1
    if (a,b) == (2,2): # OEIS A001839
        return (m-1)//2*m//3 - (m%6 == 5)
    if (a,b) == (2,3): # twice OEIS A001840
        return (m-1)*m // 3
    if (a,b) == (3,2): # OEIS A001843
        return ((m-2)//2*(m-1)//3 - (m%6 == 0))*m//4
    if (a,b) == (3,3): # OEIS A351100
        if m%6 in (2,4):
            return comb(m,3)//2 # perfect, by Hanani
        # These values were verified by Gurobi and some casework
        d = {5: 5, 6: 9, 7: 15, 9: 40, 11: 80, 12: 108, 13: 143, 15: 225, 17: 340, 18: 405}
        if m in d:
            return d[m]
        return packable_simplices(a,b, m-1)
    if (a,b) == (4,4):
        d = {6: 7, 7: 21, 8: 36}
        if m in d:
            return d[m]
        return packable_simplices(a,b, m-1)
    return None

def packlimit(a,b, m):
    """Return the "packing limit" for n given a,b and m."""
    if (t := packable_simplices(a,b, m)) != None:
        exact = (b-1)*comb(m,a) == t*(a+1)
    else:
        t = 0
        exact = True
    return (b-1)*comb(m,a) - a*t - (a-1)*(not exact)

def zbounds(a,b, m,n):
    """Return bounds for Zarankiewicz's function at the given arguments."""
    if a > m or b > n:
        return [m*n, m*n]
    if m-a > n-b:
        return zbounds(b,a, n,m)
    rbound = romanbound(a,b, m,n)
    lbs = [0]
    if packlimit(a,b, m) <= n:
        lbs.append(rbound) # Roman's bound is exact in these cases
    ubs = [rbound]
    # Search the relevant data file for any tighter bounds
    zbound_re = re.compile(rf"z\({a},{b},{m},{n}\) (>=|<) (\d+)")
    with open(f"{__file__.rpartition('/')[0]}/data/{a}x{b}", 'r') as f:
        for match in zbound_re.finditer(f.read()):
            if match[1] == ">=":
                lbs.append(int(match[2]))
            else:
                ubs.append(int(match[2]) - 1)
    return [max(lbs), min(ubs)]

def get_partitions(a,b, m0,n0, k0):
    """Return a list of all partitions of k0 into n0 parts from 0 to m0 each
    that satisfy Guy's arguments A and E for an a-by-b minor."""
    Alim = (b-1) * comb(m0,a)
    Elims = {n: zbounds(a,b, m0,n)[1] for n in range(b, n0)}
    def P(k, m, n, partial=[]):
        completes = []
        if sum(comb(part, a) for part in partial) > Alim or \
                any(sum(partial[:j]) > Elim for (j, Elim) in Elims.items() if j <= len(partial)):
            return []
        if k == 0:
            return [tuple(partial)] if all(sum(partial[:j]) <= Elim for (j, Elim) in Elims.items()) else []
        if (d := k - (m-1)*n) > 0:
            completes.extend(P(k-d*m, m, n-d, partial + [m]*d))
        else:
            for part in range(-(-k//n), min(k,m)+1):
                completes.extend(P(k-part, part, n-1, partial + [part]))
        return completes
    return P(k0, m0, n0)

def argd_inadmissible1(a,b, cpart,rpart):
    """Determine whether Guy's argument D prohibits a Zarankiewicz matrix with the
    given column and row partitions from existing."""
    return sum(comb(c-1,a-1) for c in cpart[-rpart[0]:]) > (b-1)*comb(len(rpart)-1,a-1)

def argd_inadmissible(a,b, cpart,rpart):
    """Determine whether Guy's argument D or D' ("transpose argument")
    prohibits a Zarankiewicz matrix with the given column and row partitions from existing."""
    return argd_inadmissible1(a,b, cpart,rpart) or argd_inadmissible1(b,a, rpart,cpart)

def get_bipartitions(a,b, m,n, k):
    """Assuming k ones are on the board, return all possible pairs (column partition, row partition)
    compatible with Guy's arguments A, D and E."""
    if a == b and m == n:
        combos = combinations_with_replacement(get_partitions(a,b, m,n, k), 2)
    else:
        combos = product(get_partitions(a,b, m,n, k), get_partitions(b,a, n,m, k))
    return list(filter(lambda ps: not argd_inadmissible(a,b, ps[0],ps[1]), combos))

def sort_icdv(part):
    """Return this partition sorted by Increasing Count of occurences, then Decreasing part Value."""
    return tuple(-v for (c, v) in sorted([(part.count(p), -p) for p in set(part)]) for _ in range(c))
