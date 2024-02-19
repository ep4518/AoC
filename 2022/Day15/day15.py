#!/usr/bin/env python3
# import sys
# from typing import List
# from math import prod
# from collections import defaultdict
# from tqdm import tqdm


# def prn_grid(grid: dict):
#     # Determine the size of the grid
#     max_row = max(key[0] for key in grid.keys())
#     max_col = max(key[1] for key in grid.keys())
    
#     # Iterate through each row and column, printing the grid values
#     for row in range(-10, max_row + 1):
#         for col in range(-10, max_col + 1):
#             # Print the value at the current position, default to a placeholder (e.g., '.') if not present
#             print(grid.get((row, col), '.'), end=' ')
#         # Move to the next line after each row
#         print()

# def part1(rows: List[int]) -> int:
#     grid = defaultdict(lambda: '.')
#     target_row = set()
#     target_row_beacons = set()
#     Row = 10
#     for row in tqdm(rows):
#         sx, sy, bx, by = row
#         grid[(sx, sy)] = 'S'
#         grid[(bx, by)] = 'B'
#         manhattan = abs(sx - bx) + abs(sy - by)
#         y_dist = abs(Row - sy)
#         x_dist = manhattan - y_dist
#         for x in range(sx - x_dist,sx + x_dist+1):
#             target_row.add(x)
#         if by == target_row:
#             target_row_beacons.add(bx)
#         # for i in range(0,manhattan+1):
#         #     for j in range(0,manhattan+1):
#         #         if i + j <= manhattan:
#         #             for d in [(1,1),(-1,-1),(1,-1),(-1,1)]:
#         #                 ddx, ddy = list(prod(p) for p in list(zip(d,(i,j))))
#         #                 nx, ny = sx + ddx, sy + ddy
#         #                 if grid[(nx,ny)] == '.':
#         #                     grid[(nx,ny)] = '#'

#     # prn_grid(grid)
#     # t = sum(r == Row and val in ['#','B'] for (r,_), val in grid.items())
#     return len(target_row)- len(target_row_beacons)

# def part2(rows: List[int]) -> int:
#     return 0

# with open(sys.argv[1],'r') as f:
#     rows = f.read().split('\n')
# rows = [(r+'.').split(' ') for r in rows]
# for i, row in enumerate(rows):
#     test = [0,0,0,0]
#     for j, n in enumerate([2,3,8,9]):
#         test[j] = int(row[n][:-1].split('=')[-1])
#     rows[i] = test

# print(f"Part1: {part1(rows)}")



import sys


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def find_tuning_freq(sensors):
    for sx, sy, d in sensors:
        for dx in range(d + 2):
            dy = d + 1 - dx
            for x, y in [
                (sx + dx, sy + dy),
                (sx + dx, sy - dy),
                (sx - dx, sy + dy),
                (sx - dx, sy - dy),
            ]:
                if not (0 <= x <= 4_000_000 and 0 <= y <= 4_000_000):
                    continue
                if check_point(x, y, sensors):
                    return 4_000_000 * x + y


def check_point(x, y, sensors):
    for sx, sy, d in sensors:
        if dist(x, y, sx, sy) <= d:
            return False
    return True


target_row = 2_000_000
target_row_empty = set()
target_row_beacons = set()
sensors = set()

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

for line in lines:
    # Sensor at x=3844106, y=3888618: closest beacon is at x=3225436, y=4052707
    toks = line.split(" ")
    sx = int(toks[2][2:-1])
    sy = int(toks[3][2:-1])
    bx = int(toks[8][2:-1])
    by = int(toks[9][2:])
    d = dist(sx, sy, bx, by)
    sensors.add((sx, sy, d))

    y_dist = abs(sy - target_row)
    x_dist = d - y_dist
    for x in range(sx - x_dist, sx + x_dist + 1):
        target_row_empty.add(x)
    if by == target_row:
        target_row_beacons.add(bx)

part1 = len(target_row_empty) - len(target_row_beacons)
print(f"Part 1: {part1}")

print(f"Part 2: {find_tuning_freq(sensors)}")
