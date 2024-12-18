#!/usr/bin/env python3
import sys

rows = open(sys.argv[1]).read().strip().split('\n')

for row in rows:
    if row == '':
        continue

    name, value = row.split(':')

    match name:

        case 'Register A':
            A = int(value)
        case 'Register B':
            B = int(value)
        case 'Register C':
            C = int(value)
        case 'Program':
            program = list(map(int, value.split(',')))

def find(A, B=B, C=C, program=program):

    combo = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C}
    out = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]

        match opcode:

            case 0:
                combo[4] = int(combo[4] / 2 ** combo[operand])
            case 1:
                combo[5] = combo[5] ^ operand
            case 2:
                combo[5] = combo[operand] % 8
            case 3:
                if combo[4] == 0:
                    pass
                else:
                    i = operand
                    continue
            case 4:
                combo[5] = combo[5] ^ combo[6]
            case 5:
                out.append(combo[operand] % 8)
            case 6:
                combo[5] = int(combo[4] / 2 ** combo[operand]) 
            case 7:
                combo[6] = int(combo[4] / 2 ** combo[operand])

        i +=  2

    return out

print(f'Part 1: {','.join(list(map(str, find(A))))}')

candidates = [0]
for l in range(len(program)):
    new_candidates = []
    for c in candidates:
        for i in range(8):
            target = (c << 3) + i
            if find(target) == program[-l-1:]:
                new_candidates.append(target)
    
    candidates = new_candidates
    # print(candidates)

print(f'Part 2: {min(candidates)}')