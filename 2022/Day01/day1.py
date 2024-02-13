#!/usr/bin/env python3
import sys
from typing import List

def e(rows: List[int]) -> List[int]:
    rows = [row.rstrip() for row in rows]
    elves = [0]
    for row in rows:
        if row == '':
            elves.append(0)
        else:
            elves[-1] += int(row)
    return elves

def part1(rows: List[int]) -> int:
    elves = e(rows)
    return max(enumerate(elves),key=lambda x: x[1])[1]

def part2(rows: List[int]) -> int:
    elves = e(rows)
    elves = sorted(elves, reverse=True)[0:3]
    return sum(elves)
    

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day1.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
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