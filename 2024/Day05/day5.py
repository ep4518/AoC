#!/usr/bin/env python3
import sys
from collections import defaultdict

rules = []
pages = []
with open(sys.argv[1], 'r') as file:
    flag = True
    for line in file:

        if line == '\n':
            flag = not flag
            continue

        if flag:
            rules.append(line.rstrip())
        else:
            pages.append(line.rstrip())

new_rules = defaultdict(list)
_ = [new_rules[int(k)].append(int(i)) for rule in rules for k, i in [rule.split('|')]]
pages = [tuple(map(int,page.split(','))) for page in pages]

def reorder_page_list(x: (int)):
    x = list(x)
    for i, page in enumerate(x):
        for j, p in enumerate(x[:i]):
            if p in new_rules[page]:
                x[i], x[j] = x[j], x[i]
    
    return tuple(x)

cnt1, cnt2 = 0, 0
for page_list in pages:
    flag = True
    for i, page in enumerate(page_list):
        if any(p in new_rules[page] for p in page_list[:i]):
            flag = False
            page_list = reorder_page_list(page_list)
            break

    if flag:
        cnt1 += page_list[int(len(page_list)/2)] 

    if not flag:
        cnt2 += page_list[int(len(page_list)/2)] 

print(f'Part 1: {cnt1}')
print(f'Part 2: {cnt2}')