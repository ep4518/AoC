#!/usr/bin/env python3
import sys
from typing import List

def part1(rows: List[str]):
    max_xyz = [0, 0, 0]
    for row in rows:
        print(row)
        for i in range(3):
            tmp = max(row[0][i], row[1][i])
            max_xyz[i] = max(max_xyz[i], tmp)
    
    grid = [[['.' for x in range(max_xyz[0])] for y in range(max_xyz[1])] for z in range(max_xyz[2])]

    for row in rows:
        if row[0] != row[1]:

    for k, z in enumerate(grid):
        for j, y in enumerate(z):
            for i, x in enumerate(y):
                for block in rows:
                    pass

    print(list(grid[z][0][0] for z in range(len(grid))))
            
    return 0
def part2(rows: List[str]):
    return 0
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day22.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [r.rstrip().split('~') for r in rows]
            rows = [[tuple(int(el) for el in row[0].split(',')), tuple(int(el) for el in row[1].split(','))] for _, row in enumerate(rows)]
            Part1 = part1(rows=rows)
            Part2 = part2(rows=rows)
            print(f"Part 1: {Part1}")
            print(f"Part 2: {Part2}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()