#!/usr/bin/env python3
import sys

class Decoder:
    def decode(self, rows):
        n = 500
        for i in range(1, n + 1):
            grid = self.parse(rows)
            grid = self.tilt_cycle(grid= grid, num= i)
            score = self.calculate(grid= grid)
            print(f"i = {i}, score = {score}")
           
        return score
    
    def tilt_cycle(self, grid: list[list[str]], num: int):
        for i in range(num):    
            grid = self.tilt(grid= grid, direction= 'up')
            # transpose = [list(row) for row in zip(*grid)]
            # for row in transpose:
            #     print(row)
            # print("==================================================")
            grid = self.tilt(grid=  grid, direction= 'up')
            # for row in grid:
            #     print(row)
            # print("==================================================")
            grid = self.tilt(grid=  grid, direction= 'down')
            # transpose = [list(row) for row in zip(*grid)]
            # for row in transpose:
            #     print(row)
            # print("==================================================")
            grid = self.tilt(grid=  grid, direction= 'down')
            # for row in grid:
            #     print(row)
            # print("==================================================")
        
        return grid

    def tilt(self, grid: list[list[str]], direction:str):

        transpose = [list(row) for row in zip(*grid)]

        score = 0

        new = []

        if direction == 'up':
            for i, row in enumerate(transpose):
                self.move_O_to_left(row)
            new = transpose

        elif direction == 'down':
            for i, row in enumerate(transpose):
                new.append(self.move_O_to_left(row[::-1])[::-1])
            
        
        return new

    def calculate(self, grid):
        score = 0
        for i, row in enumerate(grid):
            for ch in row:
                if ch == 'O':
                    score += len(grid) - i
        return score
    
    def move_O_to_left(self, lst):
        left_index = 0

        for i in range(len(lst)):
            if lst[i] == 'O':
                lst[i], lst[left_index] = lst[left_index], lst[i]
                left_index += 1
            elif lst[i] == '#':
                left_index = i + 1

        return lst
    
    
    def parse(self, rows):
        grid = [list(row.strip()) for row in rows]
        return grid

            
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            springs = Decoder()
            Part1 = springs.decode(rows=rows)
            print(f"Part 1: {Part1}")


    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()
