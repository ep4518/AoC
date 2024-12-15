#!/usr/bin/env python3
import sys
from collections import deque

G, I = open(sys.argv[1]).read().strip().split('\n\n')
G = G.split('\n')
G = [list(row) for row in G]
I = deque(('').join(I.split('\n')))
G2, I2 = G, I
R = len(G)
C = len(G[0])

def GPSscore(G, part2=False):
    def GPS(i,j):
        return 100 * i + j
    
    cnt = 0
    box = '[' if part2 else 'O'
    for i, row in enumerate(G):
        for j, ch in enumerate(row):
            if ch == box:
                cnt += GPS(i, j)
    return cnt

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch == '@':
            start = i, j

dmap = { '<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

i, j = start
while I:
    move = I.popleft()
    di, dj = dmap[move]
    ii, jj = i + di, j + dj
    while 0 <= ii < R and 0 <= jj < C:
        if G[ii][jj] == '.':
            for k in range(max(abs(ii-i), abs(jj-j)), 0, -1):
                G[i + k * di][j + k * dj] = G[i + (k - 1) * di][j + (k - 1) * dj] 
            G[i][j] = '.'
            i += di
            j += dj
            break
        
        if G[ii][jj] == '#':
            break

        ii += di
        jj += dj
    
print(f'Part 1: {GPSscore(G)}')

G, I = open(sys.argv[1]).read().strip().split('\n\n')
G = G.split('\n')
G = [list(row) for row in G]
I = deque(('').join(I.split('\n')))

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        if ch == '#':
            row[j] = '##'
        elif ch == 'O':
            row[j] = '[]'
        elif ch == '.':
            row[j] = '..'
        elif ch == '@':
            row[j] = '@.'

    G[i] = list(('').join(row))

for i, row in enumerate(G):
    for j, ch in enumerate(row):
        # print(ch,end='')
        if ch == '@':
            start = i, j
#     print('')
# print('')

R = len(G)
C = len(G[0])

i, j = start
while I:
    move = I.popleft()
    di, dj = dmap[move]
    if move in ['<','>']:
        ii, jj = i + di, j + dj
        while 0 <= ii < R and 0 <= jj < C:
            if G[ii][jj] == '.':
                for k in range(max(abs(ii-i), abs(jj-j)), 0, -1):
                    G[i + k * di][j + k * dj] = G[i + (k - 1) * di][j + (k - 1) * dj] 
                G[i][j] = '.'
                i += di
                j += dj
                break
            
            if G[ii][jj] == '#':
                break

            ii += di
            jj += dj 
    
    else:
        coords = [(i,j)]
        seen = set()
        flag = True
        while coords:
            y, x = coords.pop()
            seen.add((y, x))
            ii, jj = y + di, x + dj
            if 0 <= ii < R and 0 <= jj < C:
                if G[ii][jj] == '[':
                    coords.append((ii, jj))
                    coords.append((ii, jj + 1))
                elif G[ii][jj] == ']':
                    coords.append((ii, jj))
                    coords.append((ii, jj - 1))
                elif G[ii][jj] == '#':
                    flag = False
                    break
        
        if flag:
            reverse = True if di == 1 else False
            for y, x in sorted(seen, key=lambda x: x[0], reverse=reverse):
                G[y+di][x] = G[y][x]
                G[y][x] = '.'
            
            G[i][j] = '.'

            i += di
            j += dj
    
    # for row in G:
    #     print(('').join(row))

                    
G = [('').join(row) for row in G]
print(f'Part 2: {GPSscore(G, part2=True)}')