import sys
from functools import cache


@cache
def count_combinations(target: str) -> int:
    if target == "":
        return 1
    count = 0
    for option in options:
        if target.startswith(option):
            count += count_combinations(target[len(option) :])
    return count


with open(sys.argv[1], "r") as f:
    options = f.readline().strip().split(", ")
    f.readline()
    targets = f.read().strip().split("\n")


combinations = [count_combinations(t) for t in targets]
part1 = len([c for c in combinations if c != 0])
print(f"Part 1: {part1}")

part2 = sum(combinations)
print(f"Part 2: {part2}")