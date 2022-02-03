from base64 import b64encode, b64decode
import numpy as np

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
    G[n:,:n] = B
    G[:n,n:] = B.T
    return tograph6(G)
