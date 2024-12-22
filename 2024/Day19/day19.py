#!/usr/bin/env python3
import sys
from functools import cache

f = open(sys.argv[1])

patterns = [p.strip() for p in f.readline().split(',')]
f.readline()
designs = f.read().strip().split('\n')

def constructLps(pat, lps):
    len_ = 0
    m = len(pat)

    lps[0] = 0

    i = 1
    while i < m:

        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1

        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            
            else:
                lps[i] = 0
                i += 1

def kmp_search(pat, txt):
    n = len(txt)
    m = len(pat)

    lps = [0] * m
    res = []

    constructLps(pat, lps)

    i = 0
    j = 0

    while i < n:

        if txt[i] == pat[j]:
            i += 1
            j += 1

            if j == m:
                res.append((i - j, i - j + len(pat)))
                j = lps[j - 1]
        
        else:
            if j != 0:
                j = lps[j - 1]

            else:
                i += 1

    return res

# etxt = 'abababcababc'
# epat = 'ababc'
# res = kmp_search(epat, etxt)

res = 0
for design in designs:

    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    matches = []
    for pattern in patterns:
        matches.extend(kmp_search(pattern, design))
    
    matches.sort()

    for start, end in matches:
        if dp[start]:
            dp[end] = True
    
    if dp[n]:
        res += 1
    
print(f'Part 1: {res}')

@cache
def _count(design):
    if design == "":
        return 1
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += _count(design[len(pattern):])

    return count

print(f'Part 2: {sum([_count(d) for d in designs])}')