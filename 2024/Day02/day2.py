#!/usr/bin/env python3
import sys
from typing import List
from itertools import combinations

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]


def parse_row(row: str):
    prev_num = None
    prev_diff = 0
    flag = True
    for num in row.split(' '):
        num = int(num)
        if prev_num is None:
            prev_num = num
            continue
        else:
            diff = num - prev_num
            if abs(diff) > 3 or abs(diff) < 1 or (prev_diff * diff < 0):
                flag = False
                break
        prev_diff = diff
        prev_num = num

    if flag:
        return 1

    return 0


cnt = 0
for row in rows:
    cnt += parse_row(row)

print(f"Part 1: {cnt}")

cnt2 = 0
for row in rows:
    if parse_row(row) == 1:
        cnt2 += 1
    else:
        for new_row in [(' ').join(n) for n in list(combinations(row.split(' '), len(row.split(' ')) - 1))]:
            if parse_row(new_row) == 1:
                cnt2 += 1
                break

print(f"Part 2: {cnt2}")
