from itertools import combinations
from subprocess import run
import numpy as np
import re
lit_re = re.compile(r"-?\d+")

class zaran_cnf:
    def __init__(self, a,b, m,n):
        self.clauses = []
        self.a = a
        self.b = b
        self.m = m
        self.n = n
        self.bitfield = bitfield = np.arange(m*n).reshape((m,n)) + 1
        for rows in combinations(range(m), a):
            for cols in combinations(range(n), b):
                self.clauses.append(bitfield[np.ix_(rows, cols)].flatten())
        self.cursor = m*n+1

    def add_card_constraint_sinz(self, bits, k, comp=0):
        """Add clauses requiring exactly (comp = 0), at least (1) or at most (-1)
        k of the literals in bits to be true, where the variables should all refer
        to this instance's bitfield. Uses the version of Sinz's sequential-counter
        encoding discussed in https://arxiv.org/abs/1810.12975."""
        cursor = self.cursor
        n = len(bits)
        res = []
        for i in range(k+1):
            for j in range(n-k+1):
                bit = bits[i+j-1]
                this = cursor + k*(j-1) + (i-1)
                down = cursor + k*(j-1) + i
                right = cursor + k*j + (i-1)
                if 0 < i and 0 < j < n-k:
                    res.append([-this, right])
                if 0 < j and (comp >= 0 or i < k):
                    res.append(([-this] if 0 < i else []) + ([down] if i < k else []) + [-bit])
                if 0 < i < k and 0 < j:
                    res.append([this, -down])
                if 0 < i and (comp <= 0 or j < n-k):
                    res.append(([this] if 0 < j else []) + ([-right] if j < n-k else []) + [bit])
        self.clauses.extend(res)
        self.cursor += k*(n-k)

    def add_comparator(self, less_b, greater_b):
        """Add clauses expressing that the (MSB-first) number whose bits are
        given by less_b is less than or equal to the number given by greater_b."""
        n = len(less_b)
        res = []
        for i in range(n):
            lbi = less_b[i]
            gbi = greater_b[i]
            part = [[gbi, -lbi], [gbi, lbi], [-gbi, -lbi], [-gbi, lbi]]
            pci = self.cursor + i-1
            nci = self.cursor + i
            if 0 < i < n-1:
                res.append([-pci, nci])
            if i > 0:
                for cl in part:
                    cl.append(pci)
            if i < n-1:
                part[1].append(-nci)
                part[2].append(-nci)
                part[3].append(nci)
            else:
                part = part[:1]
            res.extend(part)
        self.clauses.extend(res)
        self.cursor += n-1

    def set_col_counts(self, counts=None):
        if counts == None:
            counts = [-1] * self.n
        for (i, count) in enumerate(counts):
            if count >= 0:
                self.add_card_constraint_sinz(self.bitfield[:,i], count)
        for i in range(self.n-1):
            if counts[i] == counts[i+1]:
                self.add_comparator(self.bitfield[:,i], self.bitfield[:,i+1])

    def set_row_counts(self, counts=None):
        # e.g. [-1, -1, -1, 3, 3, 3, -1, -1, -1, -1]
        # will be interpreted as [>=3 * 3, 3 * 3, <=3 * 4]
        if counts == None:
            counts = [-1] * self.m
        for (i, count) in enumerate(counts):
            if count >= 0:
                self.add_card_constraint_sinz(self.bitfield[i], count)
        for i in range(self.m-1):
            if counts[i] == counts[i+1]:
                self.add_comparator(self.bitfield[i], self.bitfield[i+1])

    def write(self, cnfn):
        nvars = max(abs(l) for cl in self.clauses for l in cl)
        nclauses = len(self.clauses)
        with open(cnfn, 'w') as f:
            print(f"p cnf {nvars} {nclauses}", file=f)
            for cl in self.clauses:
                print(" ".join(map(str, cl)), "0", file=f)

    def solve(cnfn, solver_path, orient=0, proof=None):
        cline = [solver_path, "-q", cnfn]
        if orient > 0:
            cline.append("--sat")
        if orient < 0:
            cline.append("--unsat")
        if proof != None:
            cline.append(proof)
        proc = run(cline, capture_output=True, encoding="utf-8")
        if proc.returncode != 10:
            return None # unsatisfiable
        return list(map(int, lit_re.findall(proc.stdout)[:-1]))

    def add_solution(self, sol):
        solbase = sol[:self.m*self.n]
        self.clauses.append([-x for x in solbase])
        return np.array([int(l > 0) for l in solbase]).reshape(self.m,self.n)

    def findallsols(self, cnfn, expected_sols=0, solver_path="./kissat", proof=None):
        found_sols = []
        while True:
            self.write(cnfn)
            res = zaran_cnf.solve(cnfn, solver_path, 1 if len(found_sols) < expected_sols else -1, proof)
            if res == None:
                return found_sols
            A = self.add_solution(res)
            print(A)
            found_sols.append(A)
