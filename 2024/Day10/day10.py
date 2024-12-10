#!/usr/bin/env python3
import sys

G = open(sys.argv[1], 'r').read().strip().split('\n')
R = len(G)
C = len(G[0])


trailheads = []
for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch == '0':
            trailheads.append((i, j))

def move(i, j, ch=0, seen=None):
    if seen == None:
        seen = set()

    if ch == 9:
        if (i, j) not in seen:
            seen.add((i,j))
            return 1
        
    count =  0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for d in range(4):
        di, dj = directions[d]
        ii, jj = i + di, j + dj
        if 0 <= ii < R and 0 <= jj < C:
            if G[ii][jj] == str(ch + 1):
                count += move(ii, jj, ch + 1, seen)
    
    return count

def move2(i, j, ch=0, seen=None):
    if seen == None:
        seen = set()

    if ch == 9:
        return 1
    
    seen.add((i,j))    
    count =  0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for d in range(4):
        di, dj = directions[d]
        ii, jj = i + di, j + dj
        if 0 <= ii < R and 0 <= jj < C:
            if G[ii][jj] == str(ch + 1):
                count += move2(ii, jj, ch + 1, seen.copy())
    
    return count

print(f'Part 1: {sum([move(i,j) for i, j in trailheads])}')
print(f'Part 2: {sum([move2(i,j) for i, j in trailheads])}')