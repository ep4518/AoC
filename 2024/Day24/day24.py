#!/usr/bin/env python3
import sys
from collections import deque
from dataclasses import dataclass
from typing import List
import re

start, gates = list(map(lambda g: g.split('\n'), open(sys.argv[1]).read().strip().split('\n\n')))

@dataclass
class Connection:
    ins: List[str]
    out: str
    op: str
    
    def __str__(self) -> str:
        return f"{self.out} = {self.ins[0]} {self.op} {self.ins[1]}"
    
    def __eq__(self, other) -> bool:
        return self.ins == other.ins and self.op == other.op
    
operations = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y
}

out_map = {}
for s in start:
    a, b = s.split(':')
    out_map[a] = int(b.strip())

wire_map = {}
final_keys = []
pattern = re.compile(r'(\w{3})\s([A-Z]{2,3})\s(\w{3})\s->\s(\w{3})')
for g in gates:
    i1, op, i2, out = pattern.match(g).groups()
    wire_map[out] = Connection([i1, i2], out, op)
    if out[0] == 'z':
        final_keys.append(out)

Q = deque(wire_map.values())
while Q:
    try:
        conn = Q.popleft()
        out_map[conn.out] = operations[conn.op](out_map[conn.ins[0]], out_map[conn.ins[1]])

    except:
        Q.append(conn)

out_map = {key: out_map[key] for key in sorted(out_map)} 

print(f'Part 1: {int(''.join([str(value) for key, value in out_map.items() if key in final_keys])[::-1], 2)}')

x = int(''.join([str(value) for key, value in out_map.items() if key[0] == 'x'])[::-1], 2)
y = int(''.join([str(value) for key, value in out_map.items() if key[0] == 'y'])[::-1], 2)
z = int(''.join([str(value) for key, value in out_map.items() if key[0] == 'z'])[::-1], 2)
# print(format(z^(x+y), '046b')[::-1])
znums = [f'z{i:02d}' for i, n in enumerate(format(z^(x+y), '046b')[::-1]) if int(n) == 1]
# format(x+y, '046b')[::-1]
# format(z, '046b')[::-1]

tmp = {key: value for key, value in out_map.items() if key[0] == 'z'}
tmp1 = {key: value for (key, value), x in zip(tmp.items(), list(format(z^(x+y), '046b')[::-1])) if x == '1'}

print(znums)

def f(n, val='z'):
    return val + str(n).zfill(2)

def contributing_gates(w: str):
    res = set([w])
    conn = wire_map[w]
    for i in range(2):
        if conn.ins[i] in wire_map:
            res |= contributing_gates(conn.ins[i])
    
    return res

def uniquely_contributing_gates(n):
    
    gates = contributing_gates(f(n)) - contributing_gates(f(n - 1))
    print('\n'.join(str(wire_map[gate]) for gate in gates))

def a():
    print(f'0\n')
    print('\n'.join(str(wire_map[gate]) for gate in contributing_gates(f(0)))) 
    for i in range(1, 45):
        print(f'\n{i}\n')
        uniquely_contributing_gates(i)
        
def find_wire(op: str | None = None, in1: str | None = None, in2: str | None = None):
    for wire in wire_map.values():
        if op and op != wire.op:
            continue
        if in1 and in1 not in wire.ins:
            continue
        if in2 and in2 not in wire.ins:
            continue
        return wire
            

def fix_bit(i, find_i=False):
    
    def swap(w1: str, w2: str) -> None:
        wire_map[w1], wire_map[w2] = wire_map[w2], wire_map[w1]

    """
    prevxor | a_{i-1} = x_{i-1} XOR y_{i-1}
    
    c_i = a_{i-1} AND b_{i-1} | something else from prev
    b_i = x_{i-1} AND y_{i-1}
    d_i = c_i OR b_i
    a_i = x_i XOR y_i
    z_i = d_i XOR a_i
    
    """
    x_i_1, y_i_1 = f(i - 1, 'x'), f(i - 1, 'y')
    
    a_i_1 = find_wire(op='XOR', in1=x_i_1, in2=y_i_1)
    b_i = find_wire (op='AND', in1=x_i_1, in2=y_i_1)
    c_i = find_wire(op='AND', in1=a_i_1.out)
    d_i = find_wire(op='OR', in1=c_i.out, in2=b_i.out)
    a_i = find_wire(op='XOR', in1=f(i, 'x'), in2=f(i, 'y'))
    z_i = find_wire(op='XOR', in1=d_i.out, in2= a_i.out)
        
    if z_i is None:
        z_i = wire_map[f(i)]
        to_swap = list(set(z_i.ins) ^ set([a_i.out, d_i.out]))
    if z_i.out != f(i):
        to_swap = [f(i), z_i.out]
            
    swap(*to_swap)
    return to_swap

part2 = []
for i in [7, 11, 18, 35]:
    part2.extend(fix_bit(i))
    
print(f'Part 2: {','.join(sorted(part2))}')


# # """
# # dot -Tpng input.dot > graph.png; open graph.png
# with open('input.dot', 'w') as f:
#     f.write("strict digraph day24 { \n") 
#     for conn in wire_map.values():
#         f.write(f"\t{conn.ins[0]} -> {conn.out} [ label =\"{conn.op}\"];\n")
#         f.write(f"\t{conn.ins[1]} -> {conn.out} [ label =\"{conn.op}\"];\n")
#     f.write("}")
# # """