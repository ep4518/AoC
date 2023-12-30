#!/usr/bin/env python3
import sys
from typing import List, Dict

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = parse(rows)
            score = compute(rows)
            print(score)

    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0
    
def parse(rows):
    for i, row in enumerate(rows):
        words = row.split()
        for j in range(1, len(words)):
            words[j] = int(words[j])
        rows[i] = words
    
    return rows

def compute(rows):
    score = 0
    for i in range(1, len(rows[0])):
        time = rows[0][i]
        distance = rows[1][i]
        cnt = 0
        for j in range(time):
            tmp = j * (time - j)
            if tmp > distance:
                cnt += 1
        if score == 0:
            score += cnt
        else:
            score *= cnt

    return score


if __name__ == "__main__":
    main()