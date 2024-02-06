#!/usr/bin/env python3
from sys import argv
from collections import deque 

# Not my day 22.
class Brick:

    # 1,0,1~1,2,1
    def __init__(self, line) -> None:
        points = [list(map(int, p.split(','))) for p in line.strip().split('~')]
        p1, p2 = sorted(points, key=lambda p: p[2])
        self.x1, self.y1, self.z1 = p1
        self.x2, self.y2, self.z2 = p2
        assert self.z1 <= self.z2
        self.supported_by = set()
        self.supports = set()

    def __repr__(self):
        return f"<brick ({self.x1, self.y1, self.z1}, {self.x2, self.y2, self.z2})>"

    def overlaps(self, other) -> bool:
        return (
            max(self.x1, other.x1) <= min(self.x2, other.x2) and
            max(self.y1, other.y1) <= min(self.y2, other.y2)
        )

with open(argv[1], 'r') as f:
    rows = f.readlines()

bricks = sorted([Brick(line) for line in rows], key=lambda b: b.z1)

# Bricks fall
for i, brick in enumerate(bricks):
    floor = 1
    for other in bricks[:i]:
        if brick.overlaps(other):
            floor = max(floor, other.z2 + 1)
    fall_distance = brick.z1 - floor
    brick.z1 -= fall_distance
    brick.z2 -= fall_distance

bricks.sort(key=lambda b : b.z2)

for i, brick in enumerate(bricks):
    for other in bricks[:i]:
        if brick.overlaps(other) and other.z2 == brick.z1 - 1:
            brick.supported_by.add(other)
            other.supports.add(brick)

part1 = 0
for brick in bricks:
    if all(len(other.supported_by) > 1 for other in brick.supports):
        part1 += 1
print(f"Part 1: {part1}")

part2 = 0
for brick in bricks:
    dq  = deque([brick])
    falling = set()
    while dq:
        b = dq.popleft()
        if b in falling:
            continue
        falling.add(b)
        for sb in b.supports:
            if sb.supported_by.issubset(falling):
                dq.append(sb)
    part2 += len(falling) - 1

print(f"Part 2: {part2}")
