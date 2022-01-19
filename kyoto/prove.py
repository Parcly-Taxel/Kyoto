from itertools import product
from itertools import combinations_with_replacement as cwr
from .zcnf import zaran_cnf, solve_cnf
from .utilities import get_partitions, argd_inadmissible, encode_array

'''def prove_solutions(a,b, m,n, k, nonzeros={}, revsort_r=False, revsort_c=False):
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
    return resstr.rstrip("\n")'''

def prove_solutions2(a,b, m,n, k, nonzeros={}):
    resstr = f"z({a},{b},{m},{n}) " + (">=" if nonzeros else "<") + f" {k}\n"
    print(resstr, end="")
    if a == b and m == n:
        combos = enumerate(cwr(get_partitions(a,b, m,n, k), 2))
    else:
        combos = enumerate(product(get_partitions(a,b, m,n, k), get_partitions(b,a, n,m, k)))
    for (i, (cpart, rpart)) in combos:
        if argd_inadmissible(a,b, cpart,rpart):
            continue
        ln = f"{cpart} {rpart}"
        print(ln)
        resstr += ln + "\n"
        fn = f"{a}x{b} {m}x{n} {k} {i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(cpart)
        cnf.set_row_counts(rpart)
        for sol in cnf.find_all_solutions(fn, nonzeros.get((rpart, cpart), 0), fn):
            ln = encode_array(sol)
            print(ln)
            resstr += ln + "\n"
    return resstr.rstrip("\n")

def find_solution(a,b, m,n, k):
    resstr = f"z({a},{b},{m},{n}) >= {k}\n"
    print(resstr, end="")
    combos = enumerate(product(get_partitions(a,b, m,n, k), get_partitions(b,a, n,m, k)))
    for (i, (cpart, rpart)) in combos:
        if argd_inadmissible(a,b, cpart,rpart):
            continue
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
