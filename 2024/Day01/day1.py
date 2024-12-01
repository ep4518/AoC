#!/usr/bin/env python3
import sys

def part1(rows):
    left = []
    right = []
    for row in rows:
        t = row.split(' ')
        left.append(int(t[0]))
        right.append(int(t[-1]))

    tot = 0
    for (l, r) in zip(sorted(left), sorted(right)):
        tot += abs(l - r)
    
    return tot

def part2(rows):
    left = []
    right = []

    for row in rows:
        t = row.split(' ')
        left.append(int(t[0]))
        right.append(int(t[-1]))

    d = {num: 0 for num in left}
    for num in d.keys():
        for n in right:
            if num == n:
                d[num] += 1

    return sum([key * value for key, value in d.items()])

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]
    Part1 = part1(rows=rows)
    Part2 = part2(rows=rows)
    print(f"Part 1: {Part1}")
    print(f"Part 2: {Part2}")