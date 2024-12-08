#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import combinations

G = open(sys.argv[1]).read().strip().split('\n')
R = len(G)
C = len(G[0])

antennas = defaultdict(list)

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch != '.':
            antennas[ch].append((i,j))

def displacement(X: tuple, Y: tuple) -> tuple:
    x1, y1 = X
    x2, y2 = Y
    return (x2 - x1, y2 - y1)

def add(X: tuple, Y: tuple, negate: int) -> tuple:
    x1, y1 = X
    x2, y2 = Y
    return (x1 + negate * x2, y1 + negate * y2)

def times(X: tuple, inn: int) -> tuple:
    return (X[0]*inn, X[1]*inn)

antinodes1 = set()
antinodes2 = set()
for antenna, location in antennas.items():
    for pair in combinations(location, 2):
        disp = displacement(*pair)
        for (ant, switch) in zip(pair, [-1, 1]):
            anti = add(ant, disp, switch)
            if (0 <= anti[0] < R) and (0 <= anti[1] < C):
                antinodes1.add(anti)

            antinodes2.add(ant)
            k = 1
            while (0 <= anti[0] < R) and (0 <= anti[1] < C):
                antinodes2.add(anti)
                anti = add(ant, times(disp, k), switch)
                k += 1

for i in range(R):
    for j in range(C):
        if G[i][j] != ".":
            print(G[i][j], end="")
        elif (i, j) in antinodes1:
            print("#", end="")
        else:
            print(".",end="")
    print("")

print(f"Part 1: {len(antinodes1)}")
print(f"Part 1: {len(antinodes2)}")