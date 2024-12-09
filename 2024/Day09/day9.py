#!/usr/bin/env python3
import sys

G = list(open(sys.argv[1], 'r').read().strip()[::-1])

FILES, SPACES, new = [], [], []
i, j, o, none_count = 0, 0, 0, 0

while G:
    
    n = int(G.pop())
    if i % 2 == 0:
        new += n * [str(j)]
        FILES.append((o, n, j))
        j += 1
    
    else:
        new += n * [None]
        none_count += n
        SPACES.append((o, n))
    
    o += n
    i += 1

new2 = new.copy()
i = 0
while none_count:
    block_id = new.pop()

    if block_id is not None:
        while new[i] is not None:
            i += 1
        
        new[i] = block_id
    
    none_count -= 1

for i, l, file_id in reversed(FILES):
    for space_i, (i_s, l_s) in enumerate(SPACES):
        if i_s < i and l <= l_s:
            new2[i_s:i_s+l], new2[i:i+l] = new2[i:i+l], new2[i_s:i_s+l]
            SPACES[space_i] = (i_s+l, l_s - l)
            break

print(f'Part 1: {sum([i * int(num) for i, num in enumerate(new)])}')
print(f'Part 2: {sum([i * int(num) for i, num in enumerate(new2) if num])}')