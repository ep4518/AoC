#!/usr/bin/env python3
import sys
import re

comap = {'turn on': '1', 'turn off': '0', 'toggle': '-1'}
pattern = re.compile(r'(?P<com>turn on|turn off|toggle) (?P<n1>\d{1,3}),(?P<n2>\d{1,3}) through (?P<n3>\d{1,3}),(?P<n4>\d{1,3})')
input = [{key: int(value) for key, value in item.items()} for item in list(map(lambda x: {**x, 'com': comap[x['com']]}, (map(lambda x: x.groupdict(), (map(pattern.match, open(sys.argv[1]).read().splitlines()))))))]

G = [[0 for _ in range(1000)] for _ in range(1000)]
G2 = [[0 for _ in range(1000)] for _ in range(1000)]
k2map = {0: -1, 1: 1, -1: 2}

for a in input: 
    k = a['com'] 
    k2 = k2map[k]  
    for i in range(a['n1'], a['n3']+1):
        for j in range(a['n2'], a['n4']+1):
            if k == -1:
                G[i][j] ^= 1
            else:
                G[i][j] = k
            G2[i][j] = max(0, G2[i][j] + k2)
                
print(f'Part 1: {sum(c for x in G for c in x)}')
print(f'Part 1: {sum(c for x in G2 for c in x)}')

# print('\n'.join(('').join(str(c) for c in line) for line in G))