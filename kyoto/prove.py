from .zcnf import zaran_cnf, solve_cnf
from .utilities import get_partitions, encode_array

def prove_solutions(a,b, m,n, k, nonzeros={}, revsort_r=False, revsort_c=False):
    """If nonzeros is a dictionary, find all Zarankiewicz solutions
    with the given parameters (which may be none). If it is the integer 1,
    find just one solution; in either case return a proof summary as a string."""
    onlyone = nonzeros == 1
    resstr = f"z({a},{b},{m},{n}) " + (">=" if nonzeros or onlyone else "<") + f" {k}\n"
    print(resstr, end="")
    for (i, rpart) in enumerate(get_partitions(a,b, m,n, k)):
        if not onlyone:
            ln = str(rpart)
            print(ln)
            resstr += ln + "\n"
        fn = f"{a}x{b}_{m}x{n}_{k}_{i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(rpart, revsort=revsort_r)
        cnf.set_row_counts(revsort=revsort_c)
        if onlyone:
            try:
                sol = next(cnf.find_all_solutions(fn, proof_path=fn, expected_sols=1))
                ln = encode_array(sol)
                print(ln)
                resstr += ln + "\n"
                break
            except StopIteration:
                continue
        else:
            for sol in cnf.find_all_solutions(fn, proof_path=fn, expected_sols=nonzeros.get(rpart, 0)):
                ln = encode_array(sol)
                print(ln)
                resstr += ln + "\n"
    return resstr.rstrip("\n")
