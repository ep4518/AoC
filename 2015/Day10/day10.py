#!/usr/bin/env python3
import sys

G = open(sys.argv[1]).read().splitlines()

def look_and_say(x: str):

    new = ''
    l = len(x)
    i, j, k = 0, 0, 0
    while i < l:
        while x[i] == x[j]:
            k += 1
            j += 1
            if j >= l:
                break

        new += str(k) + x[i]
        i = j
        k = 0

    return new

x = G[0]

for i in range(40):
    x = look_and_say(x)

print(f'Part 1: {len(x)}')
for i in range(10):
    x = look_and_say(x)
    
print(f'Part 2 {len(x)}')