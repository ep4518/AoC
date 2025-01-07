#!/usr/bin/env python3
import sys
from pprint import pprint
import json

J = json.load(open(sys.argv[1], 'r'))

def sum_numbers(data, part2=False):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_numbers(item, part2=part2) for item in data)
    elif isinstance(data, dict):
        if part2 and "red" in data.values():
                return 0
        return sum(sum_numbers(value, part2=part2) for value in data.values())
    return 0

print(f'Part 1: {sum_numbers(J)}')
print(f'Part 2: {sum_numbers(J, part2=True)}')
