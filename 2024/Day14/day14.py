#!/usr/bin/env python3
import sys
from math import prod

rows = open(sys.argv[1]).read().strip().split('\n')

if sys.argv[1] == 'input.txt':
    R, C = 103, 101
elif sys.argv[1] == 'test.txt':
    R, C = 7, 11

robots = []
for row in rows:
    a, b = row.split(' ')
    a = a.split('=')[1]
    j, i = map(int,a.split(','))
    b = b.split('=')[1]
    dj, di = map(int, b.split(','))
    robots.append(([i, j], (di, dj)))

t = 100
final_robots = []
for robot in robots:
    ((i, j), (di, dj)) = robot
    i = (i + di * t) % R
    j = (j + dj * t) % C
    final_robots.append((i, j))
    
quads = ((R // 2 - 1, C // 2 - 1), (R - R //2, C // 2 - 1), (R // 2  - 1, C - C // 2), (R - R // 2, C - C // 2))

robot_quad = [[],[],[],[]]
for robot in final_robots:
    (i, j)= robot
    if i <= quads[0][0] and j <= quads[0][1]:
        robot_quad[0].append(robot)
    elif i >= quads[1][0] and j <= quads[1][1]:
        robot_quad[2].append(robot)
    elif i <= quads[2][0] and j >= quads[2][1]:
        robot_quad[1].append(robot)
    elif i >= quads[3][0] and j >= quads[3][1]:
        robot_quad[3].append(robot)


def find(t=0):
    while True:
        t+=1
        final_robots = set()
        for robot in robots:
            ((i, j), (di, dj)) = robot
            i = (i + di * t) % R
            j = (j + dj * t) % C
            final_robots.add((i, j))

        seen = set()
        components = 0
        for (i, j) in final_robots:
            if all(((i + di) % R, (j + dj) % C) not in seen for (di, dj) in [(0,1), (1,0), (-1,0), (0, -1)]):
                components += 1

            seen.add((i,j))

        if components < 250:
            for i in range(R):
                for j in range(C):
                    if (i, j) in final_robots:
                        print('#',end='')
                    else:
                        print('.',end='')
                print('')
            print('\n\n')
            break

    return t

t = find(-1)
print(f'Part 1: {prod([len(quad) for quad in robot_quad])}')
print(f'Part 2: {t}')