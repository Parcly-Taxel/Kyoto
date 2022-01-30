![Kyoto's logo is the conjectured unique solution to z_3(16)](/logo.svg)

This repository began with a bad but passable [question](https://math.stackexchange.com/q/4335395) on the Mathematics Stack Exchange about the minimum number of 1s needed in a 7×7 binary matrix to eliminate all zero 3×3 minors. Having some experience with SAT solving I did my own work on the problem, unaware of the literature. When I emerged with an apparently new number sequence I was encouraged to add it to the OEIS – which I did as [A350237](https://oeis.org/A350237) – at which point I realised that (1) the original question was a particular case of Zarankiewicz's problem and (2) I had indirectly found the first new term of A001198 in over 50 years. Eventually I applied to change the topic of my final-year project to this problem.

My initial research was confined to 3×3 minors in square matrices, formatted as a gist. I soon realised that a full-fledged repository would both allow generalisation across all parameters and fewer cases to consider (from Guy's argument E capturing the dependence of larger Zarankiewicz numbers on smaller ones); keeping with my tradition of naming all my repositories after real locations I chose Kyoto, one of the few Japanese cities with a grid layout, in this case over a thousand years old.

----

The Zarankiewicz number z(a,b, m,n) is the maximum number of 1s in an m×n binary matrix with no all-1 a×b minor. To prove such a number in the general case requires both showing that there is an admissible matrix with k 1s and no such matrix with k+1 1s; files in the `data` subfolder record both maximal matrices in a base64 format and proofs of impossibility as the cases considered.

The default arguments to the functions proving Zarankiewicz numbers in `prove.py` assume a compiled [Kissat](https://github.com/arminbiere/kissat) executable in the top-level directory.
