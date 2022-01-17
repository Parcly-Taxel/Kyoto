from .zcnf import zaran_cnf, solve_cnf
from .utilities import get_partitions, encode_array

def prove_solutions(a,b, m,n, k, nonzeros={}, onlyone=False):
    print(f"z({a},{b},{m},{n})", ">=" if nonzeros or onlyone else "<", k)
    for (i, rpart) in enumerate(get_partitions(a,b, m,n, k)):
        print(rpart)
        fn = f"{a}x{b}_{m}x{n}_{k}_{i}"
        cnf = zaran_cnf(a,b, m,n)
        cnf.set_col_counts(rpart)
        cnf.set_row_counts()
        for sol in cnf.find_all_solutions(fn, proof_path=fn, expected_sols=nonzeros.get(rpart, 0)):
            print(encode_array(sol))
            print()
            if onlyone:
                return
