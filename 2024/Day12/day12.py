#!/usr/bin/env python3
import sys
from collections import deque

G = list(map(list, open(sys.argv[1]).read().strip().split("\n")))
R = len(G)
C = len(G[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def inbounds(i, j):
    return 0 <= i < R and 0 <= j < C


def perimeter(region):

    return sum(
        [
            sum(
                [
                    1
                    for di, dj in directions
                    if not inbounds(i + di, j + dj)
                    or inbounds(i + di, j + dj)
                    and (i + di, j + dj) not in region
                ]
            )
            for i, j in region
        ]
    )


def sides(region: tuple[tuple[int]]) -> int:
    up, down, left, right = (set() for _ in range(4))
    for r, c in region:
        if (r - 1, c) not in region:
            up.add((r, c))
        if (r + 1, c) not in region:
            down.add((r, c))
        if (r, c - 1) not in region:
            left.add((r, c))
        if (r, c + 1) not in region:
            right.add((r, c))

    count = 0
    for r, c in up:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r - 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r - 1, c + 1) in left and (r, c) not in right:
            count += 1

    for r, c in down:
        if (r, c) in left:
            count += 1
        if (r, c) in right:
            count += 1
        if (r + 1, c - 1) in right and (r, c) not in left:
            count += 1
        if (r + 1, c + 1) in left and (r, c) not in right:
            count += 1

    return count


regions = []
SEEN = set()
for i in range(R):
    for j in range(C):
        if (i, j) in SEEN:
            continue
        new_region = set()
        Q = deque([(i, j)])
        while Q:
            i, j = Q.popleft()
            new_region.add((i, j))
            for di, dj in directions:
                ii, jj = i + di, j + dj
                if inbounds(ii, jj) and G[ii][jj] == G[i][j] and not (ii, jj) in SEEN:
                    Q.append((ii, jj))
                    SEEN.add((ii, jj))

        regions.append(tuple(new_region))

regions = []
seen = set()
for r in range(R):
    for c in range(C):
        if (r, c) in seen:
            continue
        region = set()
        queue = deque([(r, c)])
        while queue:
            rr, cc = queue.popleft()
            region.add((rr, cc))
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = rr + dr, cc + dc
                if (
                    (nr, nc) not in seen
                    and 0 <= nr < R
                    and 0 <= nc < C
                    and G[nr][nc] == G[rr][cc]
                ):
                    queue.append((nr, nc))
                    seen.add((nr, nc))
        regions.append(region)


# for region in regions:
#     print("\n".join("".join(G[i][j] if (i, j) in region else "." for j in range(C)) for i in range(R)))

print(f"Part 1: {sum(len(r) * perimeter(r) for r in regions)}")
print(f"Part 2: {sum(len(r) * sides(r) for r in regions)}")
