#!/usr/bin/env python3
import sys
from collections import defaultdict

G = open(sys.argv[1]).read().strip().split('\n')
G = [list(row) for row in G]
R, C = len(G), len(G[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def inbounds(i, j):
    return 0 <= i < R and 0 <= j < C

track = []

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch == 'S':
            start = (i, j)

i, j = start
while G[i][j] != 'E':
    track.append((i, j))
    for di, dj in directions:
        ii = i + di
        jj = j + dj

        if inbounds(i, j):
            if G[ii][jj] == '.' and (ii, jj) not in track:
                i, j = ii, jj
                break

            if G[ii][jj] == 'E':
                i, j = ii, jj
                end = (i, j)
                track.append(end)

jumps = []
jumps_dict = defaultdict(lambda: 0)
for i, j in track:
    for di, dj in directions:
        ii, jj = i + di, j + dj
        ii2, jj2 = i + 2 * di, j + 2 * dj

        if inbounds(ii2, jj2):
            if G[ii][jj] == '#':
                if G[ii2][jj2] == 'E' or G[ii2][jj2] == '.':
                    _len = track.index((ii2,jj2)) - track.index((i, j)) - 2
                    if _len > 0:
                        jumps.append(((i, j), (ii2, jj2), _len))
                        jumps_dict[_len] += 1


jumps = sorted(jumps, key=lambda x: x[2])
print("\n".join("".join("O" if (y, x) in track else "." for x in range(C)) for y in range(R)))
print(f'Part 1: {sum([item for key, item in jumps_dict.items() if key >= 100])}')

def find_shortcuts(max_cheat, min_shortcut):
    shortcuts = defaultdict(int)
    for r, c in track:
        for len_cheat in range(2, max_cheat + 1):
            for dr in range(len_cheat + 1):
                dc = len_cheat - dr
                for r2, c2 in set(
                    [
                        (r + dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c + dc),
                        (r - dr, c - dc),
                    ]
                ):
                    if (r2, c2) not in track: continue
                    savings = track[(r2, c2)] - track[(r, c)] - len_cheat
                    if savings >= min_shortcut:
                        shortcuts[savings] += 1
    
    return dict(sorted(shortcuts.items()))

track = {a: i+1 for i, a in enumerate(track)}

print(f'Part 2: {sum(c for c in find_shortcuts(20, 100).values())}')