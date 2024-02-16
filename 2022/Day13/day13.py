#!/usr/bin/env python3
import sys
from typing import List
from functools import cmp_to_key

class Packet:
    def __init__(self, rows: List[str]):
        self.left = eval(rows[0])
        self.right = eval(rows[1])
        self.eval = self._selfEvaluate(eval(rows[0]), eval(rows[1]))

    def __repr__(self):
        return f"<left: {self.left}, right: {self.right}, eval: {self.eval} >"
    
    def _selfEvaluate(self, p1, p2) -> bool:
        if isinstance(p1, int) and isinstance(p2, int):
            if p1 < p2:
                return -1
            if p1 == p2:
                return 0
            return 1

        if isinstance(p1, int):
            p1 = [p1]
        if isinstance(p2, int):
            p2 = [p2]

        for x1, x2 in zip(p1, p2):
            res = self._selfEvaluate(x1, x2)
            if res == 0:
                continue
            return res
        if len(p1) < len(p2):
            return -1
        if len(p2) < len(p1):
            return 1
        return 0
    
def compare(p1,p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        if p1 == p2:
            return 0
        return 1

    if isinstance(p1, int):
        p1 = [p1]
    if isinstance(p2, int):
        p2 = [p2]

    for x1, x2 in zip(p1, p2):
        res = compare(x1, x2)
        if res == 0:
            continue
        return res
    if len(p1) < len(p2):
        return -1
    if len(p2) < len(p1):
        return 1
    return 0


with open(sys.argv[1], "r") as f:
    rows = f.read().split('\n\n')
rows = [p.split('\n') for p in rows]
packets = []

for p in rows:
    packets.append(Packet(p))
cnt = 0
for i, p in enumerate(packets):
    if p.eval == -1:
        cnt += i+1
print(f"Part 1: {cnt}")

packets = [eval(c) for r in rows for c in r if c]
divs = [[[2]],[[6]]]
for div in divs:
    packets.append(div)

part2 = 1
for i, p in enumerate(sorted(packets, key=cmp_to_key(compare))):
    if p in divs:
        part2 *= i+1
print(f"Part2: {part2}")