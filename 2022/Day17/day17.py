#!/usr/bin/env python3
import sys
from typing import List

class Game():
    def __init__(self, rows):
        self.rows = rows
        self.q = [[ch for ch in row[::-1]] for row in self.rows][0]
        self.shapes = {
            "cross": [(3,1), (4,1), (5,1), (4,2), (4,0)],
            "hline": [(3,0), (4,0), (5,0), (6,0)],
            "el": [(3,0), (4,0), (5,0), (5,1), (5,2)],
            "vline": [(3,0), (3,1), (3,2), (3,3)],
            "square": [(3,0), (3,1), (4,0), (4,1)]
        }
        self.wind = {
            ">" : 1,
            "<": -1
        }
        self.grid = {
            (0,0) : "+",
            (8,0) : "+",  
        }
        for i in range(1,8): self.grid[(i,0)] = '-'
        for i in range(1,5): 
            self.grid[(0,i)] = '|'
            self.grid[(8,i)] = '|'
            for j in range(1,8): self.grid[(j,i)] = '.'

        self.block_height = 0
        self.grid_height = 4

    def round(self):
        self.move_shape('hline')
        self.move_shape('cross')
        self.move_shape('el')
        self.move_shape('vline')
        self.move_shape('square')
        return 0
    def add_new_row(self):
        self.grid_height += 1
        self.grid[(0,self.grid_height)] = '|'
        self.grid[(8,self.grid_height)] = '|'
        for i in range(1,8): self.grid[(i,self.grid_height)] = '.'
    
    def remove_top_row(self):
        for i in range(0,9): self.grid[(i, self.grid_height)] = ''
        self.grid_height -= 1

    def prn_grid(self):
        for row in range(self.grid_height, -1, -1):  # Iterate over rows in reverse
            for col in range(0, 9):  # Assuming 9 is the width including borders
                print(self.grid.get((col, row), ' '), end='')  # Print each cell
            print()  # Newline after each row
    
    def add_shape(self, shape):
        s = sorted(shape, key=lambda x: x[1])
        location = set()
        shape_height = s[-1][1] - s[0][1] + 1  # +1 to include both top and bottom rows
        lowest_point = s[0][1]

        # Calculate the necessary gap (3 rows in this case)
        gap = 3

        # Determine how many rows to add based on the shape's height and the desired gap
        required_height = self.block_height + gap + shape_height
        rows_to_add = required_height - self.grid_height

        if rows_to_add > 0:
            for _ in range(max(0, rows_to_add)):  # Only add rows if needed
                self.add_new_row()
        else:
            for _ in range(max(0, -rows_to_add)):
                self.remove_top_row()

        # Adjust origin based on the updated grid height
        origin = self.grid_height - shape_height + 1 - lowest_point

        for x, y in shape:
            self.grid[(x, y + origin)] = '@'
            location.add((x, y + origin))

        return location
    
    def descend(self, location, wind):
        dx = self.wind[wind]
        new = set()

        def clear_current_positions():
            for x, y in location:
                self.grid[(x, y)] = '.'

        def check_and_update_landing():
            # Check if movement would result in landing on a block or floor after moving sideways)
            if any(self.grid[(x + dx, y - 1)] in ['#', '-'] for x, y in location):
                # Update positions without moving down, object lands
                for x, y in location:
                    self.block_height = max(y, self.block_height)
                    self.grid[(x + dx, y)] = '#'
                    new.add((x + dx, y))
                return True
            return False

        # Check for immediate obstacle beneath
        if any(self.grid[(x, y - 1)] in ['#', '-'] for x, y in location):
            clear_current_positions()
            # Move sideways if possible, then check for landing due to obstacle below new position
            if not check_and_update_landing():
                for x, y in location:
                    # If no obstacle below after moving sideways, move down
                    self.block_height = max(y, self.block_height)
                    self.grid[(x + dx, y - 1)] = '#'
                    new.add((x + dx, y - 1))
            return new, True
                

        # If moving sideways into a vertical obstacle, move down directly
        if any(self.grid[(x + dx, y - 1)] in ['|'] for x, y in location):
            clear_current_positions()
            for x, y in location:
                self.grid[(x, y - 1)] = '@'
                new.add((x, y - 1))
            return new, False
        elif any(self.grid[(x + dx, y)] in ['#'] for x, y in location) and not any(self.grid[(x, y - 1)] in ['#'] for x, y in location):
            clear_current_positions()
            for x, y in location:
                self.grid[(x, y - 1)] = '@'
                new.add((x, y - 1))
            return new, False
        else:
            clear_current_positions()
            # Check for landing due to obstacle below new position after moving sideways
            if not check_and_update_landing():
                for x, y in location:
                    # If no immediate obstacle, proceed with moving down and sideways
                    self.grid[(x + dx, y - 1)] = '@'
                    new.add((x + dx, y - 1))
            else:
                return new, True

        return new, False
     

    def move_shape(self, s='hline'): 
        current = self.add_shape(self.shapes[s])
        while True:
            w = self.q.pop()
            current, flag = self.descend(current, w)
            self.prn_grid()
            print(self.q)
            if flag: 
                self.prn_grid()
                break
            if self.q == []:
                self.q = [[ch for ch in row[::-1]] for row in self.rows][0] 


def part1(rows: List[int]) -> int:
    game = Game(rows)
    game.round()
    game.round()
    # for _ in range(2022//5):
    #     game.round()
    # game.move_shape('hline')
    # game.move_shape('cross')
    return game.block_height

def part2(rows: List[int]) -> int:
    return 0

with open(sys.argv[1], "r") as f:
    rows = f.read().split('\n')
print(f"Part 1: {part1(rows)}")