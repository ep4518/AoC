#!/usr/bin/env python3
import sys

G = open(sys.argv[1]).read()

print(f'Part 1: {sum([1 if c == '(' else -1 for c in G])}')

floor = 0  
for i, c in enumerate(G):
    floor += 1 if c == '(' else -1
    
    if floor == -1:
        break
        
print(f'Part 2: {i+1}')