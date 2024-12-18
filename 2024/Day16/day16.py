#!/usr/bin/env python3
import sys
import heapq

G = [list(row) for row in open(sys.argv[1]).read().strip().split('\n')]
R = len(G)
C = len(G[0])

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = (R - 2, 1)

Q = [(0, *start, 0, [start])]
SEEN = {(*start, 0)}
seats = set()
part1 = None
best = float('inf')

while Q:
    score, x, y, d, path = heapq.heappop(Q)
    SEEN.add((x, y, d))

    if G[x][y] == 'E':
        if not part1:
            # print("\n".join("".join("O" if (y, x) in path else "." for x in range(C)) for y in range(R)))
            # print("=" * C)
            part1 = score
        if score <= best:
            best = score
            for point in path:
                seats.add(point)
        else:
            break

    dx, dy = dirs[d]
    xx, yy = x + dx, y + dy
    if 0 <= xx < R and 0 <= yy < C and G[xx][yy] != '#' and (xx, yy, d) not in SEEN:
            heapq.heappush(Q, (score + 1, xx, yy, d, path + [(xx, yy)]))

    for new_d in [(d + 1) % 4, (d - 1) % 4]:
        ndx, ndy = dirs[new_d]
        if (x, y, new_d) not in SEEN and G[x+ndx][y+ndy] != '#':
            heapq.heappush(Q, (score + 1000, x, y, new_d, path))

print(f"Part 1: {part1}")
part2 = len(seats)
print(f"Part 2: {part2}")