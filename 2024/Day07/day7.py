#!/usr/bin/env python3
import sys
from typing import List

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]

def recurse(rem: List[int], tot):
    if not rem:
        return [tot]

    n = rem.pop()

    if tot == 0:
        return recurse(rem.copy(), n)

    return recurse(rem.copy(), tot * n) + recurse(rem.copy(), tot + n) 
    
def recurse2(rem: List[int], tot):
    if not rem:
        return [tot]

    n = rem.pop()

    if tot == 0:
        return recurse2(rem.copy(), n)

    cat = int(str(tot) + str(n))

    return recurse2(rem.copy(), tot * n) + recurse2(rem.copy(), tot + n) + recurse2(rem.copy(), cat)

cnt1, cnt2 = 0, 0 
for row in rows:
    flag = False
    test, remaining = row.split(':')
    remaining = list(map(int, remaining.strip().split(' ')))
    test = int(test) 
    if test in recurse(remaining[::-1], 0):
        cnt1 += test
    if test in recurse2(remaining[::-1], 0):
        cnt2 += test


print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')