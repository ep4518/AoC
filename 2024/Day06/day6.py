#!/usr/bin/env python3
import sys

p1 = 0
p2 = 0

rows = open(sys.argv[1]).read().strip().split('\n')
for i, R in enumerate(rows):
    t = R.rfind('^')
    if t != -1:
        start = (i, t)

R = len(rows)
C = len(rows[0])
for r in range(R):
    for c in range(C):
        if rows[r][c] == '^':
            sr,sc = r,c

for o_r in range(R):
    for o_c in range(C):
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        SEENWDIR = set()
        SEEN = set()
        while True:
            if (r,c,d) in SEENWDIR:
                p2 += 1
                break
            SEENWDIR.add((r,c,d))
            SEEN.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                if rows[o_r][o_c]=='#':
                    p1 = len(SEEN)
                break
            if rows[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")