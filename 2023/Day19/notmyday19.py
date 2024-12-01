#!/usr/bin/env python3
import math
import sys


ops = {"<": int.__lt__, ">": int.__gt__}


def apply_workflows(part, workflow):
    if workflow in "AR":
        return workflow

    for category, op, num, target in workflows[workflow]:
        if category == "default" or ops[op](part[category], num):
            return apply_workflows(part, workflow=target)

    assert False


with open(sys.argv[1], "r") as f:
    raw_workflows, raw_parts = f.read().split("\n\n")

# parse workflows
workflows = {}
for line in raw_workflows.splitlines():
    # px{a<2006:qkq,m>2090:A,rfg}
    name, raw_rules = line.rstrip("}").split("{")
    rules = []
    for rule in raw_rules.split(","):
        if ":" not in rule:
            rules.append(("default", None, None, rule))
            continue
        condition, target = rule.split(":")
        category = condition[0]
        op = condition[1]
        assert op in "<>"
        num = int(condition[2:])
        assert num >= 0
        rules.append((category, op, num, target))
    workflows[name] = rules

# loop over parts, if accept add to total
part1 = 0
for line in raw_parts.splitlines():
    # {x=787,m=2655,a=1222,s=2876}
    values = line.strip("{}").split(",")
    part = {}
    for value in values:
        vtype, v = value.split("=")
        part[vtype] = int(v)
    if apply_workflows(part, workflow="in") == "A":
        part1 += sum(part.values())

print(f"Part 1: {part1}")


def apply_workflows_ranges(ranges, workflow):
    if workflow == "R":
        return 0
    if workflow == "A":
        return math.prod(stop - start for start, stop in ranges.values())

    total = 0
    for category, op, num, target in workflows[workflow]:
        if category == "default":
            total += apply_workflows_ranges(ranges, workflow=target)
            continue
        start, stop = ranges[category]
        if op == "<":
            match_range = (start, min(num, stop))
            miss_range = (max(num, start), stop)
        else:
            match_range = (max(num + 1, start), stop)
            miss_range = (start, min(num + 1, stop))
        if match_range[0] < match_range[1]:
            next_ranges = dict(ranges)
            next_ranges[category] = match_range
            total += apply_workflows_ranges(next_ranges, workflow=target)
        if miss_range[0] < miss_range[1]:
            ranges = dict(ranges)
            ranges[category] = miss_range
        else:
            break

    return total


part2 = apply_workflows_ranges({k: (1, 4001) for k in "xmas"}, workflow="in")
print(f"Part 2: {part2}")
