from .zcnf import zaran_cnf, solve_cnf
from .utilities import get_bipartitions, sort_icdv
from .graphs import encode_array

def prove_solutions(a,b, m,n, k, nonzeros={}, icdv=False):
    resstr = f"z({a},{b},{m},{n}) " + (">=" if nonzeros else "<") + f" {k}\n"
    print(resstr, end="")
    for (i, (cpart, rpart)) in enumerate(get_bipartitions(a,b, m,n, k)):
        if icdv:
            cpart = sort_icdv(cpart)
            rpart = sort_icdv(rpart)
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
        print(cpart, rpart)
        fn = f"{a}x{b} {m}x{n} {k} {i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(cpart)
        cnf.set_row_counts(rpart)
        try:
            sol = next(cnf.find_all_solutions(fn, 1, fn))
            ln = encode_array(sol)
            print(ln)
            resstr += ln
            break
        except StopIteration:
            continue
    return resstr

def extend_solution(a,b, m,n, B, k):
    """Use B as a starting point to find solutions with k extra 1s."""
    fn = f"{a}x{b} {m}x{n} +{k}"
    cnf = zaran_cnf(a,b, m,n)
    cnf.add_card_constraint_sinz(cnf.set_cubes(B), k)
    yield from cnf.find_all_solutions(fn, 1000, fn)
