#!/usr/bin/env python3
import sys
from typing import List

def part1(rows: List[int]) -> int:
    cnt = 0
    for row in rows:
        e1, e2 = row
        x1, y1 = e1
        x2, y2 = e2
        if (x1 <= x2 and y2 <= y1) or (x2 <= x1 and y1 <= y2) :
            cnt += 1

    return cnt

def part2(rows: List[int]) -> int:
    cnt = 0
    for row in rows:
        e1, e2 = sorted(row, key=lambda x : x[0])
        x1, y1 = sorted(e1)
        x2, y2 = sorted(e2)
        if (y1 >= x2 and x1 <= y2) or (x1 <= y2 and x2 <= y1):
            cnt += 1
        # (x1,y1) (x2,y2)
        # x1 ... x2 y1 ... y2
        # x2 ... x1 y2 ... y1

    return cnt

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day4.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [tuple(tuple(map(int, element.split('-'))) for element in row.rstrip().split(',')) for row in rows]
            Part1 = part1(rows)
            Part2 = part2(rows)
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