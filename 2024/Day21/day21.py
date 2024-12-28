#!/usr/bin/env python3
import sys
from collections import deque

rows = open(sys.argv[1]).read().strip().split("\n")

codes = [deque([ch for ch in row]) for row in rows]
end = [int(row.replace('A', '')) for row in rows]

# for x in range(0,10):
#     j = (x - 1) % 3
#     i = 2 - (x - 1) // 3
#     print(x, i, j)


def manhattan(X, Y):
    return abs(X[0] - Y[0]) + abs(X[1] - Y[1])

def inbounds9(Z: list[int]):
    return 0 <= Z[0] < 4 and 0 <= Z[1] < 3 and Z != [3, 0]

def gen_paths(X, Y, path=None, inbounds=inbounds9):
    
    if path is None:
        path = []

    if X == Y:
        return [path + ["A"]]

    paths = []
    if X[0] - Y[0] > 0:
        if inbounds([Y[0] + 1, Y[1]]):
            paths += gen_paths(X, [Y[0] + 1, Y[1]], path + ["v"])
    if X[0] - Y[0] < 0:
        if inbounds([Y[0] - 1, Y[1]]):
            paths += gen_paths(X, [Y[0] - 1, Y[1]], path + ["^"])
    if X[1] - Y[1] > 0:
        if inbounds([Y[0], Y[1] + 1]):
            paths += gen_paths(X, [Y[0], Y[1] + 1], path + [">"])
    if X[1] - Y[1] < 0:
        if inbounds([Y[0], Y[1] - 1]):
            paths += gen_paths(X, [Y[0], Y[1] - 1], path + ["<"])

    return paths

def second_robot(code):
    print(code) 
    
    keypad = {'A': [0, 2], '<': [1, 0], 'v': [1, 1], '>': [1, 2], '^': [0, 1]}
    def inboundsD(Z):
        return Z in keypad.values()
    
    loc = keypad['A']
    code = deque(code)
    paths = [[]]
    while code:
        target = keypad[code.popleft()]
        
        new_paths = []
        for path in paths:
            for p in gen_paths(target, loc, path, inbounds=inboundsD):
                new_paths.append(p)
                
        paths = new_paths
        loc = target
        
    return paths
        

result = 0
A = (3, 2)
loc = A
moves = 0
for e, code in enumerate(codes):
    paths = [[]]
    while code:
        n = code.popleft()
        if n == "A":
            target = A
        else:
            n = int(n)
            if n == 0:
                target = (3, 1)
            else:
                target = (2 - (n - 1) // 3, (n - 1) % 3)

        moves += manhattan(target, loc) + 1

        new_paths = []
        for path in paths:
            for p in gen_paths(list(target), list(loc), path):
                new_paths.append(p)

        paths = new_paths
        loc = target
        
    second_paths = [second_robot(p) for p in paths]
    third_paths = [[second_robot(p) for p in x] for x in second_paths]

    minimum_len = 99999 
    for i in range(len(third_paths)):
        for j in range(len(third_paths[i])):
                for k in range(len(third_paths[i][j])):
                    minimum_len = min(minimum_len, len(third_paths[i][j][k]))
    print(minimum_len, end[e])
    result += minimum_len * end[e]

print(f'Part 1: {result}')