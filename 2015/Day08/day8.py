#!/usr/bin/env python3
import sys
import re

G = open(sys.argv[1]).read().splitlines()

p1 = 0
p2 = 0
for s in G:
    a = len(s)
    s2 = s[::]
    s = s.removeprefix("\"").removesuffix("\"")
    s = re.sub(r'\\\\', r'\\', s)  # Replace \\ with \
    s = re.sub(r'\\"', r'"', s)    # Replace \" with "
    s = re.sub(r'\\x[0-9a-fA-F]{2}', r'_', s)  # Replace \xYY with a single character (_)

    p1 += len(s2) - len(s)
    
    encoded = '"' + s2.replace('\\', '\\\\').replace('"', '\\"') + '"' 
    p2 += len(encoded) - a

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')