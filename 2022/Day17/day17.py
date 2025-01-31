#!/usr/bin/env python3
import sys
from typing import List
from tqdm import tqdm

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
        
    def prn_top(self):
        for row in range(self.grid_height, self.grid_height-5, -1):  # Iterate over rows in reverse
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
        
        def my_func(dx, dy, symbol='@'): 
            for x, y in location:
                self.grid[(x, y)] = '.'               
            for x, y in location:
                if symbol == '#':
                    self.block_height = max(y, self.block_height)
                self.grid[(x + dx, y + dy)] = symbol
                new.add((x + dx, y + dy))

        if any(self.grid[(x + dx, y)] in ['#', '|'] for x, y in location):
            if not any(self.grid[(x, y - 1)] in ['#', '-'] for x, y in location):
                my_func(0, -1)  # move directly down
                return new, False
            else: 
                my_func(0, 0, '#') # landed
                return new, True
        elif any(self.grid[(x + dx, y - 1)] in ['#', '-'] for x, y in location): 
            my_func(dx, 0, '#') # landed
            return new, True
        else:
            my_func(dx, -1) # continue
            return new, False
     

    def move_shape(self, s='hline'): 
        current = self.add_shape(self.shapes[s])
        while True:
            w = self.q.pop()
            current, flag = self.descend(current, w)
            # self.prn_grid()
            # print(w)
            if flag: 
                # self.prn_grid()
                break
            if self.q == []:
                self.q = [[ch for ch in row[::-1]] for row in self.rows][0] 


def part1(rows: List[int]) -> int:
    game = Game(rows)
    for _ in range(2022//5):
        game.round()
    game.move_shape('hline')
    game.move_shape('cross')
    game.prn_top()
    return game.block_height

def part2(rows: List[int]) -> int:
    game = Game(rows)
    x, r = divmod(1000000000000,len(rows[0]))
    for _ in tqdm(range(len(rows[0]))):
        game.round()
    
    ans = game.block_height * x
    a,b = divmod(r, 5)
    new = Game(rows)
    for _ in range(a):
        new.round()
    print(b)
    # new.move_shape('hline')
    # new.move_shape('cross')
    # new.move_shape('el')
    # new.move_shape('vline')  
    ans += new.block_height

    return ans


with open(sys.argv[1], "r") as f:
    rows = f.read().split('\n')
# print(f"Part 1: {part1(rows)}")
print(f"Part 2: {part2(rows)}")