#!/usr/bin/env python3
import sys
from typing import List

directions = {
    "U": (-1,0),
    "D": (1,0),
    "L": (0,-1),
    "R": (0,1)
}

def part1(rows: List[int]) -> int:
    cnt = 4 * len(rows) - 4
    for i in range(1, len(rows) - 1):
        for j in range(1, len(rows[i])-1):
            row = rows[i]
            ch = row[j]
            for d in directions:
                r, c = i, j
                flag = True
                dr, dc = directions[d]
                while 0 < r < len(rows) - 1 and 0 < c < len(rows[i]) - 1:
                    r, c = r + dr, c + dc
                    if ch > rows[r][c]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt += 1
                    break

    return cnt

def part2(rows: List[int]) -> int:
    res = 0
    for i in range(1, len(rows) - 1):
            for j in range(1, len(rows[i])-1):
                row = rows[i]
                ch = row[j]
                ss = 1
                for d in directions:
                    r, c = i, j
                    dr, dc = directions[d]
                    k, x = 0, 0
                    while 0 < r < len(rows) - 1 and 0 < c < len(rows[i]) - 1:
                        k += 1
                        r, c = r + dr, c + dc
                        if ch > rows[r][c]:
                            continue
                        else:
                            x = k
                            break
                    ss *= max(x,k)
                res = max(ss, res)

    return res

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day8.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [list(r.rstrip()) for r in rows]     
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