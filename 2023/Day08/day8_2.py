#!/usr/bin/env python3
import sys
import time

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            leftRight, rows, count = parse(rows)
            start_nodes = find_start_nodes(rows)
            rows = sorted(rows, key=lambda x: x[0])
            score = compute(leftRight, rows, start_nodes)
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


def compute(instructions, map, start_nodes):
    direction = []
    node = []
    for i, n in enumerate(start_nodes):
        node.append(find_node(n[0], map))
        direction.append(node[i][1][instructions[0] == 'R'])
    for j in range(1, len(instructions)**4):
        flag = True
        for i, n in enumerate(start_nodes):
            node[i] = find_node(direction[i], map)
            direction[i] = node[i][1][instructions[j % len(instructions)] == 'R']
            print(i, node[i][0], node[i][1], instructions[j % len(instructions)], direction[i])

            if not is_end_node(direction[i]):
                # print(f"For ghost {i} Node: {direction[i]} is not an end node. Current: {instructions[j % len(instructions)]}")
                flag = False
            # else: 
                # print(f"For ghost {i} Node: {direction[i]} is an end node. Current: {instructions[j % len(instructions)]}")
        
        # print(node)
        if flag == True:
            print(f"True {j+1}")
            return j + 1

    return "Error not found"


def find_node(direction, map):
    low, high = 0, len(map) - 1

    while low <= high:
        mid = (low + high) // 2
        current_direction = map[mid][0]

        if current_direction == direction:
            return map[mid]
        elif current_direction < direction:
            low = mid + 1
        else:
            high = mid - 1

    return None
        
def find_start_nodes(map):
    start_nodes = [] 
    for i in range(len(map)):
        if map[i][0][-1] == 'A':
            start_nodes.append(map[i])
    return start_nodes

def is_end_node(node):
    return node[-1] == 'Z'



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Part 2 took {(end - start) * 1000:.2f}ms")
