#!/usr/bin/env python3
import sys
from typing import List

def part1(rows: List[int]) -> int:
    X = 1
    cycle = 0
    res = 0
    for row in rows:
        if row[0] == "noop":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += X * cycle
                print(X)
        else:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += X * cycle
                print(X)
            
            cycle += 1
            if (cycle - 20) % 40 == 0:
                res += X * cycle
                print(X)
            X += int(row[1])
        if cycle > 221:
            return res
    return res

def part2(rows: List[int]) -> int:
    X = 1
    output, curr_line = [], []
    cycle = 0
    for row in rows:
        # print(row, cycle, X, curr_line)
        if cycle % 40 == 0 and cycle != 0:
            output.append(curr_line)
            curr_line = []
        if row[0] == "noop":
            cycle, curr_line = progress(X, cycle, curr_line)
        else:
            print(f"Start cycle {cycle + 1}: begin executing {row[0]+row[1]}")
            cycle, curr_line = progress(X, cycle, curr_line)
            if cycle % 40 == 0 and cycle != 0:
                output.append(curr_line)
                curr_line = [] 
            cycle, curr_line = progress(X, cycle, curr_line)
            X += int(row[1])
            print(f"End of cycle  {cycle}: finish executing {row[1]} (Register X is now {X})")
        print("\n")
        if cycle > 240:
            break
    output.append(curr_line) 
    for row in output:
        print(('').join(row))
    return 0

def check(X, cycle):
        return cycle % 40 in [X-1, X, X + 1]

def progress(X, cycle, curr_line): 
    if check(X, cycle):
        curr_line.append('#')
        word = "pixel"
    else: 
        curr_line.append('.')
        word = "dot"
    print(f"During cycle {cycle}: CRT draws {word} in posistion {cycle%40}")
    print(f"Current CRT row: {('').join(curr_line)}")
    cycle += 1
    return cycle, curr_line

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day10.py [.txt]")
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