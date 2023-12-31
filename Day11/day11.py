#!/usr/bin/env python3
import sys
from itertools import combinations

class universeDecoder:
    def decode(self, rows):
        total = 0
        grid = self.parse(rows)
        grid = self.expand(grid, 1)
        galaxies = self.find_galaxies(grid)
        galaxyPairs = combinations(galaxies.keys(), 2)

        # self.prn_grid(grid)

        for pair in list(galaxyPairs):
            distance = self.calculate_distance(galaxies[pair[0]], galaxies[pair[1]])
            total += distance
            #int(pair[0], galaxies[pair[0]], pair[1], galaxies[pair[1]], distance)

        return total
    
    def prn_grid(self, grid: list[list[str]]) -> None:
        for row in grid:
            print(row)
    
    def calculate_distance(self, galaxy1: tuple[int, int], galaxy2: tuple[int, int]) -> int:
        x1, y1 = galaxy1
        x2, y2 = galaxy2
        
        # print( abs(x1 - x2) + abs(y1 - y2))

        return abs(x1 - x2) + abs(y1 - y2)
    
    def find_galaxies(self, grid: list[list[str]]) -> dict:
        galaxies = {}
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '#':
                    cnt += 1
                    galaxies[f"galaxy{cnt}"] = (i, j)
        
        return galaxies

    def expand(self, grid: list[list[str]], n: int) -> list[list[str]]:
        grid = self.add_rows(grid, n)

        transpose = [list(row) for row in zip(*grid)]

        transpose = self.add_rows(transpose, n)

        grid  = [list(row) for row in zip(*transpose)]
                
        return grid
    
    def add_rows(self, grid: list[list[str]], n: int) -> list[list[str]]:
        new = []
        for row in grid:
            if not any(ch == '#' for ch in row):
                for i in range(n):
                    new.append(row)
            new.append(row)
        
        return new

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
            Part1 = universe.decode(rows=rows)
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
