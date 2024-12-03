#!/usr/bin/env python3
import sys
import re
from math import prod

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]

mul_pattern = re.compile(r"mul\((-?\d+),\s*(-?\d+)\)")

# Explanation of the regex:
# mul             - matches the literal string "mul"
# \(              - matches the literal opening parenthesis '('
# -?              - matches an optional '-' for negative numbers
# \d+             - matches one or more digits (the integer part)
# ,\s*            - matches a comma followed by any amount of whitespace
# -?\d+           - matches another optional negative sign and digits for the second integer
# \)              - matches the literal closing parenthesis ')'

print(f'Part 1: {sum([sum([int(x)*int(y) for (x,y) in mul_pattern.findall(row)]) for row in rows])}') 

do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

do_flag = True

xx = ('').join(rows)

mul = [(m.start(0), m.end(0), tuple(map(int, m.groups()))) for m in re.finditer(mul_pattern, xx)][::-1]
do = [(m.start(0), m.end(0)) for m in re.finditer(do_pattern, xx)][::-1]
dont = [(m.start(0), m.end(0)) for m in re.finditer(dont_pattern, xx)][::-1]

i = 0
tot = 0
start, _, x = mul.pop()
x = prod(x)
do_i, _ = do.pop()
dont_i, _ = dont.pop()
while mul:

    if i == start:
        if do_flag:
            tot += x
        
        start, _, x = mul.pop()
        x = prod(x)

    if i == do_i:
        do_flag = True
        try:
            do_i, _ = do.pop()
        except:
            do_i = float('inf')


    if i == dont_i:
        do_flag = False 
        try:
            dont_i, _ = dont.pop()
        except:
            dont_i = float('inf')

    i+=1

        
print(f'Part 2: {tot+x}')