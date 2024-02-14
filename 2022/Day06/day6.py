#!/usr/bin/env python3
import sys
from typing import List
from collections import deque

def part1(row: str, n: int) -> int:
    lru = deque()
    for i, ch in enumerate(row):
        lru.append(ch)
        if len(set(lru)) == n and len(lru) == n:
            return i + 1
        if len(lru) == n:
            lru.popleft()
    return 0

def part2(rows: List[int]) -> int:
    return 0

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day6.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            row = list(rows[0])
            Part1 = part1(row, 4)
            Part2 = part1(row, 14)
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