#!/usr/bin/env python3
import sys
from typing import List

def parse(rows: List[int]):
    rows = [row.rstrip() for row in rows]
    tmp, new = [], []
    for row in rows:
        if row == '':
            continue
        if row[0] == "m":
            new.append(row)
        else:
            tmp.append(row)

    tmp = [list(r) for r in tmp]
    max_l = 0
    for r in tmp:
        max_l = max(max_l, len(r))
        for i, c in enumerate(r):
            if c in ['[', ']']:
                r[i] = " "
    for r in tmp:
        while len(r) <= max_l:
            r.append(' ') 
    stacks = [[ch for ch in row][::-1] for row in zip(*tmp)]
    stacks = [r for r in stacks if not all([ch == " " for ch in r])]
    for r in stacks:
        while r[-1] == ' ':
            r.pop()

    n = []
    for r in new:
        r = r.split(' ')
        n.append(tuple(map(int, [r[1],r[3],r[5]])))
    return stacks, n

def part1(stacks, rows: List[int]) -> int:
    for row in rows:
        for _ in range(row[0]):   
            tmp = stacks[row[1]-1].pop()
            stacks[row[2]-1].append(tmp)
    res = ('').join([s[-1] for s in stacks])
    return res

def part2(stacks, rows: List[int]) -> int:
    tmp = []
    for row in rows:
        for _ in range(row[0]):   
            tmp.append(stacks[row[1]-1].pop())
        for _ in range(row[0]):
            stacks[row[2]-1].append(tmp.pop())
    res = ('').join([s[-1] for s in stacks])
    return res

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            stacks, x = parse(rows)
            Part1 = part1(stacks, x)
            stacks, x = parse(rows)
            Part2 = part2(stacks, x)
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