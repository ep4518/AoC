#!/usr/bin/env python3
import sys
from collections import defaultdict
from itertools import combinations
import numpy as np

G = open(sys.argv[1]).read().strip().split('\n')
R = len(G)
C = len(G[0])

antennas = defaultdict(list)

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch != '.':
            antennas[ch].append((i,j))

antinodes1 = set()
antinodes2 = set()
for antenna, location in antennas.items():
    location = np.array(location)
    for pair in combinations(location, 2):
        disp = pair[1] - pair[0]
        for (ant, switch) in zip(pair, [-1, 1]):
            anti = ant + switch * disp
            if (0 <= anti[0] < R) and (0 <= anti[1] < C):
                antinodes1.add(tuple(anti.tolist()))

            antinodes2.add(tuple(ant.tolist()))
            k = 1
            while (0 <= anti[0] < R) and (0 <= anti[1] < C):
                antinodes2.add(tuple(anti.tolist()))
                anti = ant + disp * k * switch
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