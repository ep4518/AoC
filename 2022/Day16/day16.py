#!/usr/bin/env python3
import sys
from typing import List
from functools import cache


with open(sys.argv[1], 'r') as f:
    rows = f.read().split('\n')
    rows = [(r+',').split(' ') for r in rows]
    rows = [(row[1], int(row[4].split('=')[1][:-1]), [r.rstrip(',') for r in row[9:]]) for row in rows]

nodes = {}
for row in rows:
    node, value, next_nodes = row
    nodes[node] = (next_nodes, value)

@cache
def recursive(node, time):
    next_nodes, val = nodes[node]
    score = max(n for n in x)


    
def part1(rows: List[int]) -> int:
    return recursive('AA', 30)

def part2(rows: List[int]) -> int:
    return 0


print(f"Part 1: {part1(rows)}")

""" 

"""