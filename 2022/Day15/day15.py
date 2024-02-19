#!/usr/bin/env python3
import sys
from typing import List
from math import prod
from collections import defaultdict


def prn_grid(grid: dict):
    # Determine the size of the grid
    max_row = max(key[0] for key in grid.keys())
    max_col = max(key[1] for key in grid.keys())
    
    # Iterate through each row and column, printing the grid values
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            # Print the value at the current position, default to a placeholder (e.g., '.') if not present
            print(grid.get((row, col), '.'), end=' ')
        # Move to the next line after each row
        print()

def part1(rows: List[int]) -> int:
    grid = defaultdict(lambda: '.')
    for row in rows:
        print(row)
        sx, sy, bx, by = row
        grid[(sx, sy)] = 'S'
        grid[(bx, by)] = 'B'
        manhattan = abs(sx - bx) + abs(sy - by)
        for i in range(1,manhattan+1):
            for j in range(1,manhattan+1):
                if i + j <= manhattan:
                    nx, ny = sx + i, sy + j
                    for d in [(1,1),(-1,-1),(1,-1),(-1,1)]:
                        ddx, ddy = list(prod(p) for p in list(zip(d,(nx,ny))))
                        if grid[(ddx,ddy)] == '.':
                            grid[(ddx,ddy)] = '#'
    prn_grid(grid)
    return 0

def part2(rows: List[int]) -> int:
    return 0

with open(sys.argv[1],'r') as f:
    rows = f.read().split('\n')
rows = [(r+'.').split(' ') for r in rows]
for i, row in enumerate(rows):
    test = [0,0,0,0]
    for j, n in enumerate([2,3,8,9]):
        test[j] = int(row[n][:-1].split('=')[-1])
    rows[i] = test

print(f"Part1: {part1(rows)}")