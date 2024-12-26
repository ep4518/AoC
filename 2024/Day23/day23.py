#!/usr/bin/env python3
import sys
import numpy as np
from typing import List
from collections import defaultdict

edges = list(map(lambda x: tuple(x.split('-')), open(sys.argv[1]).read().strip().split('\n')))

E = defaultdict(set)
for a, b in edges:
    E[a].add(b)
    E[b].add(a)

nodes = sorted(E.keys())
triples = set()
for i, a in enumerate(nodes):
    for j in range(i+1,len(nodes)):
        for k in range(j+1,len(nodes)):
            b, c = nodes[j], nodes[k]
            if a in E[b] and a in E[c] and b in E[c]:
                if any(x.startswith('t') for x in [a, b, c]):
                    triples.add((a, b, c))

print(f'Part 1: {len(triples)}')

sets = set()
def search(node, req):
    key = tuple(sorted(req))
    if key in sets: return
    sets.add(key)
    for neighbour in E[node]:
        if neighbour in req: continue
        if not all (neighbour in E[query] for query in req): continue
        # if not (req <= E[neighbour]): continue
        search(neighbour, {*req, neighbour})

for x in E:
    search(x, {x})

print('Part 2:',','.join(sorted(max(sets, key=len))))