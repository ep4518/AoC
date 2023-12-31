#!/usr/bin/env python3
import sys
from itertools import combinations

class universeDecoder:
    def decode(self, rows):
        total_sum = 0
        grid = self.parse(rows)
        galaxies = self.find_galaxies(grid)
        empties = self.find_empty(grid)
        # print(empties)
        galaxyPairs = combinations(galaxies.keys(), 2)

        # [print(key, value) for key, value in galaxies.items()]
        i = 0

        for pair in list(galaxyPairs):
            distance = self.calculate_distance(galaxies[pair[0]], galaxies[pair[1]], 1000000, empties)
            total_sum += distance

        return total_sum
    
    def calculate_distance(self, galaxy1: tuple[int, int], galaxy2: tuple[int, int], expansion: int, empties: list[list[int]]) -> int:
        y1, x1 = galaxy1
        y2, x2 = galaxy2
        empty_rows = empties[0]
        empty_columns = empties[1]
        total = 0

        for i in range(min(y1, y2), max(y1, y2)):
            if empty_rows[i] != 0:
                total += expansion 
            else:
                total += 1

        for i in range(min(x1, x2), max(x1, x2)):
            if empty_columns[i] != 0:
                total += expansion 
            else:
                total += 1
        return total
    
    def find_galaxies(self, grid: list[list[str]]) -> dict:
        galaxies = {}
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    cnt += 1
                    galaxies[f"galaxy{cnt}"] = (i, j)
        
        return galaxies

    def find_empty(self, grid: list[list[str]]) -> list[list[int]]:
        empties = [[0] * len(grid),[0] * len(grid [0])]
        for i, row in enumerate(grid):
            # print(i, row)
            if not any(ch == '#' for ch in row):
                empties[0][i] = 1 
        
        transpose = [list(row) for row in zip(*grid)]

        for i, row in enumerate(transpose):
            if not any(ch == '#' for ch in row):
                empties[1][i] = 1 
 
        return empties
    
    def parse(self, rows: list[str]) -> list[list[str]]:
        new = []
        for row in rows:
            row = row.replace('\n', '')
            new_row = []
            [new_row.append(element) for element in row]
            new.append(new_row)

        return new

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day11.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            universe = universeDecoder()
            Part2 = universe.decode(rows=rows)
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
