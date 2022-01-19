#!/usr/bin/env python3
import re
from math import comb
from fractions import Fraction as F
from base64 import b64encode, b64decode
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

def can_pack(a,b, m):
    """Return (t, exact) where t is (a lower bound on) the largest number of complete a-graphs
    on a+1 vertices that can be packed into the complete a-graph on m vertices duplicated b-1 times,
    and exact indicates whether this packing is exact."""
    if (a,b) == (2,2): # OEIS A001839
        return ((m-1)//2*m//3 - (m%6 == 5), m%6 in (1,3))
    return (0, True)

def packlimit(a,b, m):
    """Return the "packing limit" for n given a,b and m."""
    t, exact = can_pack(a,b, m)
    return (b-1) * comb(m,a) - a*t - (a-1)*(not exact)

def zbounds(a,b, m,n):
    """Return bounds for Zarankiewicz's function at the given arguments."""
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

def encode_array(A):
    """To encode the 0-1 matrix A it is first flattened, padded to a multiple of 8 bits
    with zeros, then reshaped to an (N,8)-shape matrix. Each row is then read as a little-endian
    byte and the resulting byte sequence is base64 encoded. The final code is then
    "[height] [width] [base64]"."""
    Af = A.flatten()
    b = np.pad(Af, (0,-len(Af)%8)).reshape(-1,8) @ 2**np.arange(8)
    return f"{A.shape[0]} {A.shape[1]} {b64encode(bytes(list(b))).decode()}"

def decode_array(ln):
    """Decode an output from encode_array() into a 0-1 matrix."""
    hs, ws, dat = ln.split()
    h, w = int(hs), int(ws)
    A = np.array([[(b&(1<<i))>>i for i in range(8)] for b in b64decode(dat)])
    return A.flatten()[:h*w].reshape(h,w)
