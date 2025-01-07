#!/usr/bin/env python3
import sys
import re
from collections import deque

pattern = re.compile(r'(?:(?P<in1>[a-z]+|\d+)|NOT (?P<not_in>[a-z]+)|(?P<in2>[a-z]+|\d+) (?P<op>[A-Z]+) (?P<in3>[a-z]+|\d+)) -> (?P<out>[a-z]+)')
G = open(sys.argv[1]).read().splitlines()

combinations = [
    ['in2', 'op', 'in3', 'out'],
    ['in1', 'out'],
    ['not_in', 'out'],
]

operations = {
    'AND':      lambda x, y: x & y,
    'OR':       lambda x, y: x | y,
    'LSHIFT':   lambda x, y: x << y,
    'RSHIFT':   lambda x, y: x >> y,
}
def search(vars):
    already = vars.keys()
    Q = deque(G)
    while Q:
        line = Q.popleft()
        try:
            m = pattern.match(line).groupdict()
            m = {key: item for key, item in m.items() if item!=None}
            if m['out'] in already:
                continue
            keys = list(m.keys())
            if keys == combinations[0]:
                vars[m['out']] = operations[m['op']](vars.get(m['in2'], m['in2'] if m['in2'].isalpha() else int(m['in2'])), 
                                                    vars.get(m['in3'], m['in3'] if m['in3'].isalpha() else int(m['in3'])))
            elif keys == combinations[1]:
                vars[m['out']] = vars[m['in1']] if m['in1'].isalpha() else int(m['in1'])
            elif keys == combinations[2]:
                vars[m['out']] = ~vars[m['not_in']] % 2 ** 16

        except:
            Q.append(line)
    
    return vars['a']

p1 = search({})
print(f'Part 1: {p1}')
print(f'Part 2: {search({'b': p1})}')