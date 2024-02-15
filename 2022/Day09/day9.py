#!/usr/bin/env python3
import sys
from typing import List

directions = {
    "U": (0,1),
    "D": (0,-1),
    "L": (-1,0),
    "R": (1,0)
}

tail_move = {
    (2,0): (1,0),
    (0,2): (0,1),
    (-2,0): (-1,0),
    (0,-2): (0,-1),
    (2,1): (1,1),
    (1,2): (1,1),
    (-2,1): (-1,1),
    (2,-1): (1,-1),
    (1,-2): (1,-1),
    (-1, 2): (-1,1),
    (-1,-2): (-1,-1),
    (-2,-1): (-1,-1),
    (2,2): (1,1),           #""" The Final 4 Directions Required for the multi knot snake (k > 2)"""
    (-2,-2):(-1,-1),
    (2,-2): (1, -1),
    (-2,2): (-1,1) 
}


def prn_grid(points):
    # Determine the size of the grid
    max_x = max(point[0] for point in points) + 1
    max_y = max(point[1] for point in points) + 1

    # Initialize the grid with empty spaces
    grid = [["." for _ in range(max_y)] for _ in range(max_x)]

    # Fill in the points
    for x, y in points:
        grid[x][y] = "X"

    # Print the grid
    for row in reversed(grid):
        print(" ".join(row))

def part1(rows: List[int]) -> int:
    origin = (0,0)
    x, y = origin
    tx, ty = origin
    h_visited = {origin}
    t_visited = {origin}
    for row in rows:
        dx, dy = directions[row[0]]
        for _ in range(int(row[1])):
            x, y = x + dx, y + dy
            h_visited.add((x,y))
            rel_x, rel_y = x - tx, y - ty
            if (rel_x,rel_y) in tail_move:
                dtx, dty = tail_move[rel_x, rel_y]
                tx, ty = tx + dtx, ty + dty
                t_visited.add((tx,ty))

    # prn_grid(sorted(list(h_visited), key = lambda x : x[0]))
    # print("=============================")
    # prn_grid(sorted(list(t_visited), key = lambda x : x[0]))

    return len(t_visited)

class Rope:
    def __init__(self, k: int):
        self.knot_num = k
        self.size = 0
        self.tail = None
        self.head = None
        for i in range(self.knot_num):
            self.append(i)
    
    def __repr__(self):
        """Represent the BackwardLinkedList from tail to head."""
        knots = []
        current = self.tail
        while current:
            knots.append(f"{current.name}: {current.location}")
            current = current.prev
        return " -> ".join(knots) + " (head)"

    def append(self, value):
        new_knot = Knot(value)
        if self.head is None:
            # If the list is empty, make the new node both the head and the tail
            self.head = new_knot
            self.tail = new_knot
        else:
            # If the list is not empty, adjust pointers accordingly
            self.tail.next = new_knot
            new_knot.prev = self.tail
            self.tail = new_knot
        self.size += 1

    def move(self, d: tuple, n: int):
        dx, dy = d
        for i in range(n):
            ptr = self.head
            x, y = ptr.location
            x, y = x + dx, y + dy
            ptr.location = (x,y)
            ptr.visited.add((x,y))
            while ptr.next is not None:
                x, y = ptr.location
                ptr = ptr.next
                tx, ty = ptr.location
                rel_x, rel_y = x - tx, y - ty
                if (rel_x, rel_y) in tail_move:
                    dtx, dty = tail_move[rel_x, rel_y]
                    tx, ty = tx + dtx, ty + dty
                    ptr.location = (tx, ty)
                    ptr.visited.add((tx,ty))

    def get_solution(self):
        return len(self.tail.visited)
    
    def prn_snake(self):
        points = []
        ptr = self.head
        while ptr.next is not None:
            points.append(ptr.location)
            ptr = ptr.next
        print(points)

class Knot:
    def __init__(self, number: int):
        self.origin = (0,0)
        self.location = self.origin
        self.visited = {self.origin}
        self.name = number
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f"<name: {self.name}, location: {self.location}>"

def part2(rows: List[int]) -> int:
    r = Rope(10)
    for row in rows:
        r.move(directions[row[0]], int(row[1]))
    # r.prn_snake()
    return r.get_solution()

def t(rows):
    r = Rope(2)
    for row in rows:
        r.move(directions[row[0]], int(row[1]))
    # r.prn_snake()
    return r.get_solution()

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day9.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [r.rstrip().split() for r in rows]
            Part1 = part1(rows)
            Part2 = part2(rows)
            test = t(rows)
            print(f"Part 1: {Part1}")
            print(f"Part 2: {Part2}")
            print(f"Part 1 w OOP: {test}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()