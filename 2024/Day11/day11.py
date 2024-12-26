#!/usr/bin/env python3
import sys
from collections import deque
from functools import cache
# sys.setrecursionlimit(10**6)

# p1 = 25
# p2 = 75

# def sol(blinks):
#     stones = deque(open(sys.argv[1], 'r').read().strip().split(' '))
#     t = time.time()
#     for blink in range(blinks):
#         # print(f'Blink {blink+1}, time between blinks: {time.time() - t}')
#         t = time.time()
#         new_stones = []
#         while stones:
#             stone = stones.popleft()
#             l = len(stone)

#             if int(stone) == 0:
#                 new_stones.append('1')
            
#             elif l % 2 == 0:
#                 m = int(l / 2)
#                 new_stones.append(str(int(stone[:m])))
#                 new_stones.append(str(int(stone[m:])))

#             else:
#                 new_stones.append(str(2024 * int(stone)))
        
#         stones = deque(new_stones)
    
#     return len(stones)

# print(f"Part 1: {sol(p1)}")


@cache
def sol2(x, d=75):
    if d == 0:
        return 1
    d = d - 1
    if x == 0:
        return sol2(1 , d)
    xstr = str(x)
    l = len(xstr)
    if l % 2 == 0:
        return sol2(int(xstr[: l // 2]), d) + sol2(int(xstr[l // 2 :]), d)
    else:
        return sol2(x * 2024, d)

stones = list(map(int,open(sys.argv[1], 'r').read().strip().split(' ')))
print(f'Part 1: {sum([sol2(rock, 25) for rock in stones])}')
print(f'Part 2: {sum([sol2(rock, 75) for rock in stones])}')