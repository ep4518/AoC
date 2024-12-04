#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]


directions = {
    'u' : (-1, 0),
    'ur': (-1, 1),
    'r' : (0, 1),
    'dr': (1, 1),
    'd' : (1, 0),
    'dl': (1, -1),
    'l' : (0, -1),
    'ul': (-1, -1)
}

h, w = len(rows), len(rows[0])
chars1 = ['M','A','S']
directions2 = {k: directions[k] for k in ['ur', 'dr', 'dl', 'ul']}
matches2 = [['M', 'M', 'S', 'S'],
            ['S', 'M', 'M', 'S'],
            ['S', 'S', 'M', 'M'],
            ['M', 'S', 'S', 'M']]
cnt1 = 0
cnt2 = 0

for i, row in enumerate(rows):
    for j, ch in enumerate(row):
        if ch == 'X':

            for (direction, (di, dj)) in directions.items():
                flag = True
                ii, jj = i + di, j + dj
                for a, char in enumerate(chars1):
                    if  (0 <= ii < h) and (0 <= jj < w) and rows[ii][jj] == char:
                        ii += di
                        jj += dj
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt1 += 1

        if ch == 'A':

            tmp = []
            for (direction, (di, dj)) in directions2.items():
                ii, jj = i + di, j + dj
                if  (0 <= ii < h) and (0 <= jj < w):
                    tmp.append(rows[ii][jj])
            
            if tmp in matches2:
                cnt2 += 1

print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')