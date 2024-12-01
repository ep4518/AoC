#!/usr/bin/env python3
import sys
import heapq
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Grid:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def heuristic(self, current, goal):
        # Simple Manhattan distance heuristic
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def is_straight(self, current, neighbor, prev_node):
        if prev_node is None:
            return False

        dx1 = current[0] - prev_node[0]
        dy1 = current[1] - prev_node[1]
        dx2 = neighbor[0] - current[0]
        dy2 = neighbor[1] - current[1]

        return (dx1 == dx2 and dy1 == dy2) or (dx1 == -dx2 and dy1 == -dy2)

    def neighbors(self, current, prev_node=None):
        row, col = current
        possible_neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        
        valid_neighbors = [
            (r, c) for r, c in possible_neighbors
            if 0 <= r < self.rows and 0 <= c < self.cols
            and (r, c) != prev_node
            and not self.is_straight(current, (r, c), prev_node)
        ]

        return valid_neighbors

    def get_cost(self, current, neighbor):
        return self.data[neighbor[0]][neighbor[1]]

def astar_search(grid, start, goal):
    open_list = [(0, start)]
    closed_set = set()
    g_scores = {start: 0}
    parent = {start: None}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = reconstruct_path(parent, goal)
            return path, g_scores[goal]

        closed_set.add(current_node)

        for neighbor in grid.neighbors(current_node, parent[current_node]):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_scores[current_node] + grid.get_cost(current_node, neighbor)

            if neighbor not in [item[1] for item in open_list] or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + grid.heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parent[neighbor] = current_node

    return None, None

def reconstruct_path(parent, goal):
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    return path[::-1]

class Decoder:
    def decode1(self, rows):
        grid = self.parse(rows=rows)
        for row in grid:
            print(row)

        grid = Grid(grid)
        start_node = (0, 0)
        goal_node = (grid.rows - 1, grid.cols - 1)
        path, score = astar_search(grid, start_node, goal_node)

        if path:
            print("Path:", path, "Score:", score)
            self.plot_path(grid, path)
        else:
            print("No path found.")

        return score

    def decode2(self, rows):
        # Implementation for Part 2
        return 0

    def parse(self, rows):
        lst = [row.strip() for row in rows]
        return [[int(digit) for digit in item] for item in lst]

    def plot_path(self, grid, path):
        fig, ax = plt.subplots()
        ax.imshow(grid.data, cmap='gray_r')

        for node in path:
            rect = patches.Rectangle(
                (node[1], node[0]), 1, 1, linewidth=1, edgecolor='r', facecolor='none'
            )
            ax.add_patch(rect)

        plt.show()

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.decode1(rows=rows)
            Part2 = decoder_instance.decode2(rows=rows)
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
