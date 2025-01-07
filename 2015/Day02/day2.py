#!/usr/bin/env python3
import sys
from itertools import combinations
from math import prod

G = list(map(lambda x: sorted(list(map(int, x.split('x')))), open(sys.argv[1]).read().splitlines()))

print(f'Part 1: {sum([prod(x[:2]) + 2 * sum(prod(y) for y in combinations(x, 2)) for x in G])}')
 
print(f'Part 2: {sum(prod(x) + 2 * sum(x[:2]) for x in G)}')
 
 
#       __
#     /  /|
#    /  / |
#   /  /__|
#  /__//  /
#  |  |  /
#  |  | /
#  |__|/
