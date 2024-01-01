Output.txt contains the first n cycles and the corresponding loadings on the north beam.

Looking for a pattern (inspired by the test.txt input which is 6 mod 7), the value 96505

occurs 3 times at iteration 158, 236 and 314. The difference is indeed 78 for both differences

and we find that 10 ** 9 % 78 is 64. Looking at iteration 64 + 78 + 78 = 220 (first mod after cycle

158 where we first begin to observe pattern in 96505's) we find a loading of 96447. 