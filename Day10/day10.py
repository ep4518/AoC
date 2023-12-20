#!/usr/bin/env python3
import sys

class MazeDecoder:
    def decode(self, rows: list[str]) -> list[tuple]:
        grid = self.parse(rows)
        start = self.find_start(grid)
        locations = []
        locations.append(start)
        locations.append((start[0]-1,start[1]))
        break_outer = False
        for i, row in enumerate(grid):
            for j in range(len(row)):
                # Move from current location to next location in pipe
                next_location = self.take_step(grid, locations[-1], locations[-2])
                if next_location != start:
                    locations.append(next_location)
                else:
                    break_outer = True
                    break

            if break_outer:
                break
        
        return round(len(locations)/2)

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

        print(f"{grid[y][x], x, y}")
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

        # for direction in eight_directions:
        #     coordinate = eight_directions[direction]
        #     i, j = coordinate[1], coordinate[0]
        #     if i >= 0 and j >= 0 and i < bottom_bound and j < right_bound:
        #         tmp = grid[i][j]
        #         if (i,j) != previous_location:
        #             if direction == "up":
        #                 print(f"Direction: {direction} => Item: {tmp}")
        #                 if tmp == '|':
        #                     if grid[y-2][x] in ['7', 'F', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check up for connection
        #                 elif tmp == 'F':
        #                     if grid[y-1][x+1] in ['7', 'J', '-']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check up-right for connection
        #                 elif tmp == '7':
        #                     if grid[y-1][x-1] in ['L', 'F', '-']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j) 
        #                     # check up-left for connection
        #                 else:
        #                     continue
        #             elif direction == "down":
        #                 # print(f"Direction: {direction} => Item: {tmp}")
        #                 if tmp == '|':
        #                     if grid[y+2][x] in ['J', 'L', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check down for connection
        #                 elif tmp == 'L':
        #                     if grid[y+1][x+1] in ['J', '7', '-']:
        #                         print('test')
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j) 
        #                     # check down-right for connection
        #                 elif tmp == 'J':
        #                     if grid[y+1][x-1] in ['F', 'L', '-']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check down-left for connection
        #                 else:
        #                     pass
        #             elif direction == "right":
        #                 # print(f"Direction: {direction} => Item: {tmp}")
        #                 if tmp == '-':
        #                     if grid[y][x+2] in ['7', 'J', '-']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check right for connection
        #                 elif tmp == '7':
        #                     if grid[y+1][x+1] in ['J', 'L', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # move right one
        #                     # check down for connection
        #                 elif tmp == 'J':
        #                    if grid[y-1][x+1] in ['F', '7', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j) 
        #                     # move right one
        #                     # check up-right for connection
        #                 else:
        #                     pass
        #             elif direction == "left":
        #                 # print(f"Direction: {direction} => Item: {tmp}")
        #                 if tmp == '-':
        #                     if grid[y][x-2] in ['F', 'L', '-']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check left for connection
        #                 elif tmp == 'L':
        #                     if grid[y-1][x-1] in ['F', '7', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check up-left for connection
        #                 elif tmp == 'F':
        #                     if grid[y+1][x-1] in ['J', 'L', '|']:
        #                         print(f"Result: Direction is {direction}. Item is {tmp}.")
        #                         return (i,j)
        #                     # check down-left for connection
        #                 else:
        #                     pass

    # def is_connection(self, direction: str, location: tuple, grid: list[list[str]]) -> tuple:
    #     # check up for connection. Connection if up == 7, F, |
    #     # check down for connection. Connection if down == J, L, |
    #     # check left for connection. Connection if left == F, L, -
    #     # check right for connection. Connection if right == J, 7, -
    #     i, j = location[1], location[0]
    #     if direction == "up":
    #         if grid[i][j] in ['7', 'F', '|']:
    #             print(f"Connection found in direction: {direction}, Coordinate: ({i}, {j}), Item: {grid[i][j]}")
    #             return 1
    #     elif direction == "down":
    #         if grid[i][j] in ['J', 'L', '|']:
    #             print(f"Connection found in direction: {direction}, Coordinate: ({i}, {j}), Item: {grid[i][j]}")
    #             return 1
    #     elif direction == "left":
    #         if grid[i][j] in ['F', 'L', '-']:
    #             print(f"Connection found in direction: {direction}, Coordinate: ({i}, {j}), Item: {grid[i][j]}")
    #             return 1
    #     elif direction == "right":
    #         if grid[i][j] in ['J', '7', '-']:
    #             print(f"Connection found in direction: {direction}, Coordinate: ({i}, {j}), Item: {grid[i][j]}")
    #             return 1
            
    
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day9.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            score = 0
            rows = file.readlines()
            print(MazeDecoder().decode(rows))

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0
 
if __name__ == "__main__":
    main()
