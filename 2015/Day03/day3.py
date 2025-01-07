#!/usr/bin/env python3
import sys

G = open(sys.argv[1]).read()

i, j, i1, j1, i2, j2 = 0, 0, 0, 0, 0, 0
houses, santa, robo = [set([(i, j)]) for _ in range(3)]

for k, c in enumerate(G):
    
    match c:
        case '^':
            j -= 1
            if k % 2 == 0:
                j2 -= 1
            else:
                j1 -= 1
        case '>':
            i += 1
            if k % 2 == 0:
                i2 += 1
            else:
                i1 += 1 
        case '<':
            i -= 1
            if k % 2 == 0:
                i2 -= 1
            else:
                i1 -= 1
        case 'v':
            j += 1
            if k % 2 == 0:
                j2 += 1
            else:
                j1 += 1
    
    houses.add((i, j))
    santa.add((i1, j1))
    robo.add((i2, j2))
    
print(f'Part 1: {len(houses)}')
print(f'Part 1: {len(santa | robo)}')

