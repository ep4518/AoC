#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

input = [tuple(map(int, x.split(','))) for x in open(sys.argv[1]).read().strip().split('\n')]

R = 71 if sys.argv[1] == 'input.txt' else 7
C = 71 if sys.argv[1] == 'input.txt' else 7
bytes = 1024 if sys.argv[1] == 'input.txt' else 12 

def inbounds(i, j):
    return 0 <= i < R and 0 <= j < C

def prn(path=set()):
    for i in range(R):
        for j in range(C):
            if (i,j) in path:
                print('O',end='')
            else:
                print(G[(i,j)], end='')
        print('')

def dte(i, j):
    """ Manhattan Distance to Exit """
    return R - 1 - i + C - 1 - j

for bytes in range(len(input)):
    G = defaultdict(lambda: '.')

    for y, x in input[:bytes]:
        if inbounds(y, x):
            G[(x, y)] = '#'

    i, j = 0, 0
    SEEN = set()
    Q = deque([(0, i, j)])

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    flag = True
    while Q:
        
        d, i, j = Q.popleft()

        if dte(i, j) == 0:
            if bytes == 1024:
                print(f'Part 1: {d}')


            flag = False
            break

        if (i, j) in SEEN:
            continue

        SEEN.add((i, j))
        
        for di, dj in dirs:
            ii, jj = i + di, j + dj
            if inbounds(ii, jj) and (ii, jj) and G[(ii, jj)] != '#':
                Q.append((d + 1, ii, jj))

    if flag:
        print(f'Part 2: {input[bytes-1]}')
        break
