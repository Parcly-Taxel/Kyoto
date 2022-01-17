#!/usr/bin/env python3
from kyoto.prove import prove_val

prove_val(2,2, 2,2, 3, {(2,1): 1})

prove_val(2,2, 3,3, 6, {(2,2,2): 1})

prove_val(2,2, 4,4, 9, {(3,2,2,2): 1})

prove_val(2,2, 5,5, 12, {(3,3,2,2,2): 3, (4,2,2,2,2): 1})

prove_val(2,2, 6,6, 16, {(3,3,3,3,2,2): 3})

prove_val(2,2, 7,7, 21, {(3,)*7: 1})

prove_val(2,2, 8,8, 24, {(3,)*8: 8, (4,) + (3,)*6 + (2,): 16})
