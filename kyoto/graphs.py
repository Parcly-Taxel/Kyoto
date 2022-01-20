import numpy as np

def tograph6(A):
    """Convert the given adjacency matrix to graph6 format."""
    n = len(A)
    bits = [A[i,j] for j in range(1, n) for i in range(j)]
    bits.extend([0] * ((-len(bits)) % 6))
    Nx = chr(n+63)
    Rx = "".join(chr(63+sum(b * 2**(5-k) for (k, b) in enumerate(tup))) for tup in zip(*[iter(bits)]*6))
    return Nx + Rx

def Btog6(B):
    """Convert a biadjacency matrix to a graph6 string."""
    m, n = B.shape
    G = np.zeros((m+n, m+n), dtype=int)
    G[n:,:m] = B
    G[:m,n:] = B.T
    return tograph6(G)
