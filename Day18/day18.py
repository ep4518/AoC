#!/usr/bin/env python3
import sys

class Decoder:
    def part1(self, rows):
        rows = [row.split() for row in rows]
        total = sum([int(row[1]) for row in rows])
        grid = self.to_grid(rows=rows)
        total += self.ray_cast(grid=grid)
        return total

    def part2(self, rows):
        return 0
    
    def to_grid(self, rows: list[str]):
        # convert instructions to grid (perimeter)
        pass
    
    def ray_cast(self, grid: list[str]):
        # for row in grid:
        # for ch in row:
        # ray cast: while number of hashtags is odd, sum += instances of '.'
        return 0

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day18.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.part1(rows=rows)
            Part2 = decoder_instance.part2(rows=rows)
            print(f"Part 1: {Part1}")
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