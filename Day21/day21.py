#!/usr/bin/env python3
import sys
from typing import List
from collections import deque

class Decoder:
    directions = {
        "North":    (-1, 0),
        "South":    (1, 0),
        "East":     (0, 1),
        "West":     (0, -1)
    }

    def part1(self, rows):
        cnt = 0
        tmp = []
        startr, startc = self.get_start(rows)
        dq = deque([(startc, startr)])
        seen = set()
        while dq:
            i, j = dq.popleft()
            if (i,j) in seen:
                continue
            res = self.get_directions(i, j, rows)
            tmp.extend(r for r in res)
            if not dq:
                cnt += 1
                dq.extend(r for r in set(tmp))
                tmp = []
                seen.update(r for r in set(tmp))
            if cnt == 10:
                return len(dq)
    
    def get_directions(self, i: int, j: int, rows):
        res = []
        for direction in self.directions:
            ddr, ddc = i + self.directions[direction][0], j + self.directions[direction][1]
            g = rows[ddr][ddc]
            if g != '#' and 0 <= ddr < len(rows) - 1 and 0 <= ddc < len(rows[0]) - 1:
                res.append((ddr, ddc))
        return [r for r in res]

    def get_start(self, grid: List[List[str]]):
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch in ['S']:
                    return (i, j)

    def part2(self, rows):
        return 0

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day21.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.part1(rows=rows)
            Part2 = decoder_instance.part2(rows=rows)
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