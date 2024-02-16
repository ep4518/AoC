#!/usr/bin/env python3
import sys
from typing import List
from math import prod

class Monkey:
    def __init__(self, text: str) -> None:
        """
        Monkey 0:
            Starting items: 79, 98
            Operation: new = old * 19
            Test: divisible by 23
                If true: throw to monkey 2
                If false: throw to monkey 3
        """
        lines = text.split('\n')
        self.number = int(lines[0].split(' ')[1][0])
        self.items = list(map(int, lines[1].split(':')[1].split(',')))
        self.op =  eval(f"lambda old : {lines[2].split('=')[1]}")
        self.test = int(lines[3].split()[-1])
        self.t = int(lines[4].split()[-1])
        self.f = int(lines[5].split()[-1])
        self.n = 0

    def __repr__(self):
        return f"< Monkey {self.number}: number is {self.n} >"

class World:
    def __init__(self, monkey_texts: str, part2=False) -> None:
        self.monkeys = []
        for mt in monkey_texts:
            self.monkeys.append(Monkey(mt))
        self.part2 =  part2
        self.mod_factor = prod(m.test for m in self.monkeys)

    
    def round(self):
        for m in self.monkeys:
            for item in m.items:
                m.n += 1
                val = m.op(item)
                if self.part2:
                    val = val % self.mod_factor
                else:
                    val = val // 3
                if val % m.test == 0:
                    self.monkeys[m.t].items.append(val)
                else:
                    self.monkeys[m.f].items.append(val)
                m.items = []
    
    def get_score(self):
        sorted_monkeys = sorted(self.monkeys, key=lambda m : m.n, reverse=True)
        return sorted_monkeys[0].n * sorted_monkeys[1].n


with open(sys.argv[1], 'r') as f:
    monkey_texts = f.read().split('\n\n')

world = World(monkey_texts)
for i in range(20):
    world.round()
for m in world.monkeys:
    print(m)
print(f"Part 1: {world.get_score()}")

world2 = World(monkey_texts, part2=True)
for i in range(10000):
    world2.round()

print(f"Part 2: {world2.get_score()}")

