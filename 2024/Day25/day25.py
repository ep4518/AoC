#!/usr/bin/env python3
import sys
import numpy

def tranpsose(matrix):
    """ Returns list of lists """
    return [list(row) for row in zip(*matrix)]

schematics = list(map(lambda x: list(map(list, x.split('\n'))), open(sys.argv[1]).read().strip().split('\n\n')))
schematics_t = [list(zip(*x)) for x in schematics]

keys, locks = [], []
for i, schematic in enumerate(schematics_t):
    heights = []
    for pin in schematic:
            heights.append(pin.count('#') - 1)
    if all(element == '#' for element in schematics[i][0]):
        keys.append(heights)
    else:
        locks.append(heights)

p1 = 0
for key in keys:
    for lock in locks:
        p1 += all(k + l <= 5 for k, l in zip(key, lock))

print(f'Part 1: {p1}')



