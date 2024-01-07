#!/usr/bin/env python3
import sys

"""
Original: https://www.youtube.com/watch?v=2Rk2-NxmgR4
Shoelace Theorem: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0p6WHFjOFBabTMtVVpLYjE5MmdLMW5VSVVFZ3xBQ3Jtc0ttY0taVUJtMUoyVlZzYkhKbE4ycXdmdWZHdUtSOTRBUGtfQjNGZGx5eEs3OHpvX3ZDd0pRQkN5RkJpYTVJRzM0YXJBcTJfdGpuVzk4dzE0eFFoTXRzMmV1cEgtQmJDWlp2SnFDaGxhMW1oaHlTQzF3MA&q=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FShoelace_formula&v=2Rk2-NxmgR4
Pick's Thm: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0RPQkg5amZOT3pESUNDcEpQNkFmeWU1LVZwZ3xBQ3Jtc0tubFY5MkhJQ0lzV2xOaExGYm5LYmlhSThadGtKZmdwZWN3Q3ZGUkYtVUY0dUxyMEJuQlBIdzN5VTNQaVJHTWhYRGxjZ2FLd19sVnFkN0tDQjBiV0xYZ3ZlZVJ0aEdYNldhNW5nODdMakV2QXEzWk5RSQ&q=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FPick%2527s_theorem&v=2Rk2-NxmgR4
"""
class Decoder:
    def part1(self, rows):
        rows = [row.split() for row in rows]
        perimeter_length = sum([int(row[1]) for row in rows])
        # points_visited = self.to_points(rows=rows, full_perimeter=True)
        # grid = self.create_grid(points_visited=points_visited)
        # total = self.ray_cast(grid=grid)
        points_visited = self.to_points(rows=rows)
        internal_area = self.shoelace(points=points_visited)
        """
        Pick's Theorem: 
        A = i + b/2 - 1
        i = A - b/2 + 1
        i + b = solution = A + b/2 + 1

        """
        solution = internal_area + perimeter_length// 2 + 1
        return solution

    def part2(self, rows):
        rows = [row.split() for row in rows]
        rows = self.convert_hex(rows=rows)
        perimeter_length = sum([int(row[1]) for row in rows])
        points_visited = self.to_points(rows=rows)
        internal_area = self.shoelace(points=points_visited)
        solution = internal_area + perimeter_length // 2 + 1
        return solution

        return 0
    
    def convert_hex(self, rows):
        new_rows = []
        reverse_dir_dict = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
        for row in rows:
            n, dir = row[2][2:7], row[2][7]
            new_row = reverse_dir_dict[dir], str(int(n, 16)) 
            new_rows.append(new_row)
        return new_rows
    
    def shoelace(self, points: list[tuple]):
        total = 0 
        for (r1, c1), (r2, c2) in zip(points, points[1:] + [points[0]]):
            total += (r1 + r2) * (c1 - c2)
        return total // 2

    def to_points(self, rows: list[str], full_perimeter = False):
        # convert instructions to grid (perimeter)
        direction_mapping = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        x, y = 0, 0
        points_visited = [(0, 0)]

        for row in rows:
            direction, steps = row[:2]
            steps = int(steps)
            dx, dy = direction_mapping[direction]

            if full_perimeter:
                for _ in range(steps):
                    x += dx
                    y += dy
                    points_visited.append((x, y))
            else:
                x += dx * steps
                y += dy * steps
                points_visited.append((x,y))

        return points_visited

    def create_grid(self, points_visited):
        """
        requires full_perimeter=True
        """
        # Extract x and y coordinates from points_visited
        x_coords, y_coords = zip(*points_visited)

        # Set up the grid
        max_x, min_x = max(x_coords), min(x_coords)
        max_y, min_y = max(y_coords), min(y_coords)

        # Initialize the grid with '#' characters
        grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

        # Mark visited points with '.'
        for x, y in points_visited:
            grid[y - min_y][x - min_x] = '#'

        return grid
    
    def ray_cast(self, grid: list[str]):
        """
        Invlaid Method: requires full_perimeter=True
        """
        # for row in grid:
        # for ch in row:
        # ray cast: while number of hashtags is odd, sum += instances of '.'
        total = 0
        for row in grid:
            print(row)
            outside = True
            other = 0
            for ch in row:
                match ch:
                    case '.':
                        if not outside:
                            other += 1
                    case '#':
                        other += 1
                        outside = not outside
            print(other)
            total += other
        return total

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