#!/usr/bin/env python3
import sys
from typing import List
from collections import defaultdict

# zip(*(iter(row),)*2):

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

def gen_grid(rows: List[int]):
    grid = defaultdict(lambda: '.')
    source = (500,0)
    grid[source] = '+'
    for row in rows:
        for line_ends in zip(row, row[1:]):
            x1, y1 = line_ends[0]
            x2, y2 = line_ends[1]
            x1, x2 = sorted([x1, x2])
            y1, y2 = sorted([y1, y2])
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    grid[(x,y)] = '#'
    return grid, source

def part1(rows: List[int]) -> int:
    grid, source = gen_grid(rows=rows)
    a = '.' #air
    i=0
    primary = True
    while primary:
        i+=1
        cnt = 0
        flag = True
        x, y = source
        while flag:
            cnt += 1
            if cnt == 1000:
                primary = False
                break
            if grid[(x, y+1)] == a:
                y += 1
            else:
                if grid[(x-1,y+1)] == a:
                    y += 1
                    x -= 1
                elif grid[(x+1, y+1)] == a:
                    x += 1
                    y += 1
                else:
                    grid[(x,y)] = 'o'
                    flag = False
    # prn_grid(grid)
    return i-1

def part2(rows: List[int]) -> int:
    grid, source = gen_grid(rows=rows)
    floor_height = max(key[1] for key in grid.keys()) + 2
    # y == floor_height, grid[(x,y)] == '#'
    a = '.' #air
    i=0
    while True:
        i+=1
        flag = True
        x, y = source
        while flag:
            if y == floor_height-1:
                grid[(x,y+1)] = '#'
                grid[(x-1,y+1)] = '#'
                grid[(x+1,y+1)] = '#'
            if grid[(x, y+1)] == a:
                y += 1
            else:
                if grid[(x-1,y+1)] == a:
                    y += 1
                    x -= 1
                elif grid[(x+1, y+1)] == a:
                    x += 1
                    y += 1
                else:
                    grid[(x,y)] = 'o'
                    flag = False

        if grid[(source[0],source[1])] == 'o':
            grid[(source[0], source[1])] = '+'
            prn_grid(grid)
            return i

with open(sys.argv[1], 'r') as f:
    rows = f.read().split('\n')
    rows = [r.split('->') for r in rows]
    rows = [[tuple(int(p.strip()) for p in c.split(',') if p.strip()) for c in row] for row in rows]
    print(f"Part1: {part1(rows)}")
    print(f"Part2: {part2(rows)}")