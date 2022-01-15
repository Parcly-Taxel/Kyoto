from math import comb

def cdiv(a, b):
    """Return ceil(a/b) for a and b positive integers."""
    return -(-a//b)

def get_partitions(k0, m0, n0, a, b, Elims={}):
    """Yield all partitions of k0 into n0 parts from 0 to m0 each
    that satisfy Guy's argument A and (if provided as a dictionary) E for an a-by-b minor."""
    parts = [0] * n0
    Alim = (b-1) * comb(m0,a)
    def P(k, m, n): # n is the number of parts remaining
        i = n0-n
        if sum(comb(parts[j], a) for j in range(i)) > Alim or sum(parts[:i]) > Elims.get(i, m*i):
            return
        if k == 0:
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
