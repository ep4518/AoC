#!/usr/bin/env python3
import sys
from typing import List
from collections import deque

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
    
    def test(self, worry):
            
        if worry % self.div == 0:
            return self.pos
        return self.neg
    
    def monkey_go(self, lst: List['Monkey']):
        while self.items:
            self.cnt += 1
            item = self.items.popleft()
            item = self.operation(item)
            next = self.test(item)
            lst[next].items.append(item)



def t0(self, worry):
    return (worry * 7) // 3

def t1(self, worry: int) -> int:
    return (worry + 3) // 3

def t2(self, worry: int):
    return (worry + 4) // 3

def t3(self, worry: int):
    return (worry + 5) // 3

def t4(self, worry):
    return (worry * 5) // 3

def t5(self, worry: int) -> int:
    return (worry * worry) // 3

def t6(self, worry: int):
    return (worry + 8) // 3

def t7(self, worry: int):
    return (worry + 1) // 3
    
def round(ms: List['Monkey']):
    for _, m in enumerate(ms):
        m.monkey_go(ms)

def part1(rows: List[int]) -> int:
    m0 = Monkey(0, [62, 92, 50, 63, 62, 93, 73, 50], 2, 7, 1)
    m1 = Monkey(1, [51, 97, 74, 84, 99], 7, 2, 4)
    m2 = Monkey(2, [98, 86, 62, 76, 51, 81, 95], 13, 5, 4)
    m3 = Monkey(3, [53, 95, 50, 85, 83, 72], 19, 6, 0) 
    m4 = Monkey(4, [59, 60, 63, 71], 11, 5, 3)
    m5 = Monkey(5, [92, 65], 5, 6, 3)
    m6 = Monkey(6, [78], 3, 0, 7) 
    m7 = Monkey(7, [84, 93, 54], 17, 2, 1) 
    
    m0.operation = t0.__get__(m0, Monkey)
    m1.operation = t1.__get__(m1, Monkey)
    m2.operation = t2.__get__(m2, Monkey)
    m3.operation = t3.__get__(m3, Monkey)
    m4.operation = t4.__get__(m4, Monkey)
    m5.operation = t5.__get__(m5, Monkey)
    m6.operation = t6.__get__(m6, Monkey)
    m7.operation = t7.__get__(m7, Monkey)
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]

    for _ in range(20):
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