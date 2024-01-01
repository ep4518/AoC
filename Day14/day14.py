#!/usr/bin/env python3
import sys

class springsDecoder:
    def decode(self, rows):
        grid = self.parse(rows)
        score = self.tilt(grid = grid, direction = "north")
           
        return score
    

    def tilt(self, grid: list[str], direction: str = "north"):
        if direction not in ["north", "south", "east", "west"]:
            raise Exception("Invalid direction")

        """
        Tilt North for starters
        """
        transpose = [list(row) for row in zip(*grid)]

        score = 0
        for i, row in enumerate(transpose):
            row = self.move_O_to_left(row)
            score += sum(self.calculate(row))

        return score

    def calculate(self, row):
        for i, ch in enumerate(row):
            if ch == 'O':
                yield len(row) - i
    
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
        grid = []
        for row in rows:
            row = row.replace("\n", "")
            grid.append(row) 
        return grid
            
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            springs = springsDecoder()
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
