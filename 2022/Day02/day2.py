#!/usr/bin/env python3
import sys
from typing import List

score = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
        }

def part1(rows: List[int]) -> int:
    rps = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'rock',
        'Y': 'paper',
        'Z': 'scissors'
       }
    s = 0
    for row in rows:
        o, u = row.rstrip().split(' ')
        s += score[rps[u]]
        if rps[u] == 'rock' and rps[o] == 'scissors' or rps[u] == 'scissors' and rps[o] == 'paper' or rps[u] == 'paper' and rps[o] == 'rock':
            s += 6
        elif rps[u] == rps[o]:
            s += 3

    return s

def part2(rows: List[int]) -> int:
    rps = {
        'A': 'rock',
        'B': 'paper',
        'C': 'scissors',
        'X': 'lose',
        'Y': 'draw',
        'Z': 'win'
        }
    win = {'rock': 'paper',
           'scissors': 'rock',
           'paper': 'scissors'}
    lose = {value: key for key, value in win.items()}
    s = 0
    for row in rows:
        o, res = row.rstrip().split(' ')
        r = rps[res]
        if r == 'win':
            s += score[win[rps[o]]]
            s += 6
        elif r == 'draw':
            s += score[rps[o]]
            s += 3
        else:
            s += score[lose[rps[o]]]
    return s

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day2.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
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