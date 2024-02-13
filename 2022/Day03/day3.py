#!/usr/bin/env python3
import sys
from typing import List

def ordish(cc: List[str]):
    counts = map(ord, cc)
    counts = [ch - 96 for ch in counts]
    counts = [ch + 58 if ch < 0 else ch for ch in counts]
    return counts

def part1(rows: List[int]) -> int:
    cnt = 0
    for row in rows:
        f, s = row[:len(row)//2], row[len(row)//2:]
        seen = set()
        shared = set()
        for ch in f:
            seen.add(ch)
        for ch in s:
            if ch in seen:
                shared.add(ch)
        counts = ordish(shared)
        cnt += sum(counts)
    return cnt

def find_common(grp: List[List[str]]) -> str:
    common_1 = set()
    seen = list(set(r) for _, r in enumerate(grp))
    for ch in seen[0]:
        if ch in seen[1]:
            common_1.add(ch)
    for ch in common_1:
        if ch in seen[2]:
            return ch

def part2(rows: List[int]) -> int:
    c = 0
    cnt = []
    grps, grp = [], []
    for row in rows:
        if c % 3 == 0 and c != 0:
            grps.append(grp)
            grp = []
        grp.append(row)
        c += 1
    grps.append(grp)
    for grp in grps:
        cnt.append(find_common(grp))
    counts = ordish(cnt)
    return sum(counts)

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day3.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [row.rstrip() for row in rows]
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