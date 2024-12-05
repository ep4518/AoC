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

mul_pattern = re.compile(r"mul\((-?\d+),\s*(-?\d+)\)|do\(\)|don't\(\)")

do_flag = True

xx = ('').join(rows)

tot = 0
it = re.finditer(mul_pattern, xx)
while (m := next(it, None)) is not None:
    group, groups = m.group(), m.groups()
    if group == "do()": do_flag = True
    elif group == "don't()": do_flag = False
    elif groups != (None, None):
        tot +=  int(groups[0]) * int(groups[1]) if do_flag else 0
        
print(f'Part 2: {tot}')