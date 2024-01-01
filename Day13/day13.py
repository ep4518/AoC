#!/usr/bin/env python3
import sys

class springsDecoder:
    def decode(self, rows):
        total = 0
        grids = self.parse(rows)
        for i, grid in enumerate(grids):
            transposed_grid = [''.join(row) for row in zip(*grid)]
            # print(f" ============ This is Grid {i + 1}. =========== ")
            # for row in grid:
            #     print(row)
            reflection_in_x_axis = self.find_mirror(grid = grid)
            reflection_in_y_axis = self.find_mirror(grid = transposed_grid)
            total += 100 * reflection_in_x_axis + reflection_in_y_axis
            
        return total
    
    def find_mirror(self, grid: list[str]) -> int:
        for i in range(1, len(grid)):
            flag = True
            above = grid[:i][::-1]
            below = grid[i:]
            for above_row, below_row in zip(above, below):
                if above_row != below_row:
                    flag = False
            if flag:            
                return i
        return 0 
    
    def parse(self, rows):
        grid, grids  = [], []
        for row in rows:
            row = row.replace("\n", "")
            if row:
                grid.append(row)
            else:
                grids.append(grid)
                grid = []
        grids.append(grid)
        return grids
            
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day13.py [.txt]")
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
