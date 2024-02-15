#!/usr/bin/env python3
import sys
from typing import List
from collections import deque
from tqdm import tqdm

class Monkey:
    def __init__(self, number, items, t, pos, neg):
        self.items = deque(items)
        self.number = number
        self.div = t
        self.pos = pos
        self.neg = neg
        self.cnt = 0
    
    def __repr__(self):
        return f"< Monkey {self.number}: items {list(self.items)} | Inspections {self.cnt} >"
    
    
    def monkey_go(self, lst: List['Monkey']):
        while self.items:
            self.cnt += 1
            item = self.items.popleft()
            next, item = self.test(item)
            lst[next].items.append(item)


def t0(self, worry):
    x = worry % self.div
    worry *= 19
    if x % 19 == 0:
        return self.pos, worry
    return self.neg, worry

def t1(self, worry):
    x = worry % self.div
    worry += 6
    if x % 19 == 0:
        return self.pos, worry
    return self.neg, worry

def t2(self, worry):
    x = worry % self.div
    worry *= worry
    if x % 19 == 0:
        return self.pos, worry
    return self.neg, worry

def t3(self, worry):
    x = worry % self.div
    worry += 3
    if x % 19 == 0:
        return self.pos, worry
    return self.neg, worry


    
def round(ms: List['Monkey']):
    for _, m in enumerate(ms):
        m.monkey_go(ms)

def part1(rows: List[int]) -> int:
    m0 = Monkey(0, [79, 98], 23, 2, 3)
    m1 = Monkey(1,[54,65,75,74], 19, 2, 0)
    m2 = Monkey(2, [79, 60,97], 13, 1, 3)
    m3 = Monkey(3, [74], 17, 0, 1) 
    m0.test = t0.__get__(m0, Monkey)
    m1.test = t1.__get__(m1, Monkey)
    m2.test = t2.__get__(m2, Monkey)
    m3.test = t3.__get__(m3, Monkey)
    monkeys = [m0, m1, m2, m3]

    for _ in tqdm(range(1)):
        round(monkeys)

    for m in monkeys:
        print(m)

    res = sorted(monkeys, key=lambda x : x.cnt, reverse=True)[0:2]
    return res[0].cnt * res[1].cnt

def part2(rows: List[int]) -> int:
    return 0

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day11.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [r.rstrip().split() for r in rows]
            Part1 = part1(rows)
            Part2 = part2(rows)
            print(f"Part 1: {Part1}")
            print(f"Part 2: {Part2}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()