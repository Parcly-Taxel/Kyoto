from .zcnf import zaran_cnf, solve_cnf
from .utilities import get_bipartitions, encode_array

def prove_solutions(a,b, m,n, k, nonzeros={}):
    resstr = f"z({a},{b},{m},{n}) " + (">=" if nonzeros else "<") + f" {k}\n"
    print(resstr, end="")
    for (i, (cpart, rpart)) in enumerate(get_bipartitions(a,b, m,n, k)[::-1]):
        ln = f"{cpart} {rpart}"
        print(ln)
        resstr += ln + "\n"
        fn = f"{a}x{b} {m}x{n} {k} {i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(cpart)
        cnf.set_row_counts(rpart)
        for sol in cnf.find_all_solutions(fn, nonzeros.get((cpart, rpart), 0), fn):
            ln = encode_array(sol)
            print(ln)
            resstr += ln + "\n"
    return resstr.rstrip("\n")

def find_solution(a,b, m,n, k):
    resstr = f"z({a},{b},{m},{n}) >= {k}\n"
    print(resstr, end="")
    for (i, (cpart, rpart)) in enumerate(get_bipartitions(a,b, m,n, k)):
        #if cpart != (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 2, 2):
        #    continue
        print(cpart, rpart)
        fn = f"{a}x{b} {m}x{n} {k} {i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(cpart)
        cnf.set_row_counts(rpart)
        # XXX a hack
        #for x in (0, 1, 11, 12, 13):
        #    cnf.clauses.append([cnf.bitfield[x,0]])
        try:
            sol = next(cnf.find_all_solutions(fn, 1, fn))
            ln = encode_array(sol)
            print(ln)
            resstr += ln
            break
        except StopIteration:
            continue
    return resstr

def prove_small():
    fn = "test"
    cnf = zaran_cnf(2,2, 19,2)
    cnf.set_col_counts((5,5))
    cnf.set_row_counts((-6,)*6+(-5,)*13)
    for sol in cnf.find_all_solutions(fn, 10000, fn):
        ln = encode_array(sol)
        print(ln)
