#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            leftRight, rows, count = parse(rows)
            # print(leftRight, rows, count)
            score = compute(leftRight, rows)
            print(score)
    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0
    
def parse(rows):
    new = []
    count = 0
    leftRight = rows[0][:-1]
    for i, row in enumerate(rows[2:]):
        count += 1
        row = row.split()
        row = [row[0], (row[2][1:-1], row[3][:-1])]
        new.append(row)

    return leftRight, new, count

def compute(instructions, map):
    node = find_node('AAA', map)
    direction = node[1][instructions[0] == 'R'] 
    for i in range(1, len(instructions) ** 2):
        node = find_node(direction, map)
        direction = node[1][instructions[i % len(instructions)] == 'R']
        # print(i, node[0], node[1], instructions[i % len(instructions)], direction)
        if direction == 'ZZZ':
            return i + 1
    return "Not Found"

def find_node(direction, map):
    for i in range(len(map)):
        if map[i][0] == direction:
            return map[i]
    return "Not Found"



if __name__ == "__main__":
    main()
