#!/usr/bin/env python3
import sys

class MazeDecoder:
    def decode(self, rows: list[str]) -> int:
        grid = self.parse(rows)
        start = self.find_start(grid)
        locations = []
        visited = set()
        locations.append(start)
        locations.append((start[0]+1,start[1]))
        visited.add(start)

        break_outer = False
        for i, row in enumerate(grid):
            for j in range(len(row)):
                next_location = self.take_step(grid, locations[-1], locations[-2])
                if next_location != start:
                    locations.append(next_location)
                    visited.add(next_location)
                else:
                    break_outer = True
                    break

            if break_outer:
                break

        return locations, visited


    def parse(self, rows: list[str]) -> list[list[str]]:
        new = []
        for row in rows:
            row = row.replace('\n','')
            new_row = []
            [new_row.append(element) for element in row]
            new.append(new_row)

        return new
    
    def find_start(self, grid: list[list[str]]) -> tuple:
        for i, row in enumerate(grid):
            for j in range(len(row)):
                if grid[i][j] == 'S':
                    start = (i,j)
        return start
    
    def create_maze_plot(self, grid_size: tuple, locations: list[tuple]) -> None:
        maze = [[' ' for _ in range(grid_size[1])] for _ in range(grid_size[0])]

        for y, x in locations:
            maze[y][x] = '*'

        for row in maze:
            print(''.join(row))
    
    def take_step(self, grid: list[list[str]], location: tuple, previous_location: tuple) -> tuple:
        x, y = location[1], location[0]
        prev_x, prev_y = previous_location[1], previous_location[0]
        right_bound, bottom_bound = len(grid[1]), len(grid)
        eight_directions = {
            "up": (x,y-1),
            "down": (x,y+1),
            "right": (x+1,y),
            "left": (x-1,y),
            "left_up": (x-1,y-1),
            "left_down": (x-1,y+1),
            "right_up": (x+1,y-1),
            "right_down": (x+1,y+1),
        }

        # print(f"{grid[y][x], x, y}")
        X = grid[y][x] 

        if X == '|':
            y = 2 * y - prev_y
            return (y,x)
        if X == '-':
            x = 2 * x - prev_x
            return (y,x)
        if X == 'F':
            if x == prev_x:
                x = x + 1
                return (y,x)
            elif y == prev_y:
                y = y + 1
                return (y,x)
        if X == 'J':
            if x == prev_x:
                x = x - 1
                return (y,x)
            elif y == prev_y:
                y = y - 1
                return (y,x)
        if X == 'L':
            if x == prev_x:
                x = x + 1
                return (y,x)
            elif y == prev_y:
                y = y - 1
                return (y,x)
        if X == '7':
            if x == prev_x:
                x = x - 1
                return (y,x)
            elif y == prev_y:
                y = y + 1
                return (y,x)

    def count_interior_points(self, rows: list[str]) -> int:
        part2 = 0
        for line in rows:
            line = line.replace('\n', '')
            print(line)
            outside = True
            startF = None
            for ch in line:
                if ch == 'S':
                    ch = 'F'
                    match ch:
                        case ".":
                            if not outside:
                                part2 += 1
                        case "|":
                            outside = not outside
                        case "F":
                            startF = True
                        case "L":
                            startF = False
                        case "-":
                            assert not startF is None
                        case "7":
                            assert not startF is None
                            if not startF:
                                outside = not outside
                            startF = None
                        case "J":
                            assert not startF is None
                            if startF:
                                outside = not outside
                            startF = None
                        case _:
                            print(f"Unexpected character: {ch}")

        return part2



    
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day9.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            maze_decoder = MazeDecoder()
            locations, _ = maze_decoder.decode(rows)
            maze_decoder.create_maze_plot((len(rows), len(rows[0].strip())), locations)

            part2 = maze_decoder.count_interior_points(rows)
            print(f"Interior points: {part2}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

 
if __name__ == "__main__":
    main()

