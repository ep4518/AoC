#!/usr/bin/env python3
from sys import argv
from collections import deque

pipe_map = {
    "S": [(1, 0), (-1, 0),(0, 1), (0, -1)],
    "|": [(1, 0), (-1, 0)], # up and down
    "-": [(0, 1), (0, -1)], # right and left
    "L": [(-1, 0), (0, 1)], # up and right
    "J": [(-1, 0), (0, -1)],# up and left
    "F": [(1, 0), (0, 1)],  # down and right
    "7": [(1, 0), (0, -1)], # down and left
    ".": [],
}

def get_valid_moves(r,c):
    res = []
    for dr, dc in pipe_map[grid[r][c]]:
        for drr, dcc in pipe_map[grid[r + dr][c + dc]]:
            if dr == -drr and dc == -dcc:
                res.append((r + dr, c + dc))
    return [r for r in res]

def start_type(r,c):
    res = []
    for dr, dc in pipe_map[grid[r][c]]:
        for drr, dcc in pipe_map[grid[r + dr][c + dc]]:
            if dr == -drr and dc == -dcc:
                res.append((dr, dc))
    return ('').join(move for move in pipe_map if set(pipe_map[move]) == set(res))

def find_start(rows:list[str]) -> (int, int):
    for i, row in enumerate(rows):
        for j, ch in enumerate(row):
            if ch == "S":
                return (i, j)

with open(argv[1], "r") as f:
    grid = [l.strip() for l in f.readlines()]

startr, startc = find_start(grid)
dq = deque([(startr, startc)])
seen = set()
while dq:
    r, c = dq.popleft()
    if (r, c) in seen:
        continue
    seen.add((r, c))

    for rr, cc in get_valid_moves(r,c):
        dq.append((rr, cc))

part1 = int(len(seen) / 2)
print(f"Part1 = {part1}")

grid2 = [
    ''.join("." if (i,j) not in seen else ch for j, ch in enumerate(line))
    for i, line in enumerate(grid)
]
grid2[startr] = grid2[startr].replace("S", start_type(startr, startc))

part2 = 0 
for line in grid2:
    # print(line)
    outside = True
    startF = None
    for ch in line:
        match ch:
            case ".":
                if not outside:
                    part2 += 1
            case "|":
                outside = not outside
            case "F":
                startF = True
            case "L":
                startF = False
            case "-":
                assert not startF is None
            case "7":
                assert not startF is None
                if not startF:
                    outside = not outside
                startF = None
            case "J":
                assert not startF is None
                if startF:
                    outside = not outside
                startF = None

print(f"Part2 = {part2}")