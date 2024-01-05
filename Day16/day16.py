#!/usr/bin/env python3
import sys
from collections import deque

class Decoder:
    def decode1(self, rows):
        grid = [row.strip() for row in rows]
        total = self.bfs(grid=grid, start=(0, -1, 0, 1))

        return total
    
    def decode2(self, rows):
        total = 0
        grid = [row.strip() for row in rows]
        height = len(grid)
        width = len(grid[0])
        for r in range(height): 
            total = max(total, self.bfs(grid=grid, start=(r, -1, 0, 1))) 
            total = max(total, self.bfs(grid=grid, start=(r, width, 0 , -1)))
        for c in range(width):
            total = max(total, self.bfs(grid=grid, start=(-1, c, 1, 0)))
            total = max(total, self.bfs(grid=grid, start=(height, c, -1, 0)))
        return total
            
    def bfs(self, grid, start: (int, int, int, int)):
        seen = set()
        queue = deque([start])
        height = len(grid)
        width = len(grid[0])
  
        while queue:
            r, c, dr, dc = queue.popleft()

            # Move
            r += dr
            c += dc

            if not (0 <= r < height and 0 <= c < width):
                continue
            
            # turn
            next_dirs = []
            match grid[r][c]:
                case "/":
                    # 0, 1 <-> -1, 0
                    # 1, 0 <-> 0, -1
                    next_dirs.append((-dc, -dr))
                case "\\":
                    # 0, 1 <-> 1, 0
                    next_dirs.append((dc, dr))
                case "|":
                    if dc == 0:
                        next_dirs.append((dr, dc))
                    else:
                        next_dirs.extend([(-1, 0), (1, 0)])
                case "-":
                    if dr == 0:
                        next_dirs.append((dr, dc))
                    else:
                        next_dirs.extend([(0, 1), (0, -1)])
                case ".":
                    next_dirs.append((dr, dc))

            for dr,dc in next_dirs:
                if (r, c, dr, dc) not in seen:
                    seen.add((r,c,dr,dc))
                    queue.append((r, c, dr, dc))

        visited = set([(r, c) for (r, c, _, _) in seen])
        
        return len(visited)



def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.decode1(rows= rows)
            Part2 = decoder_instance.decode2(rows= rows)
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
