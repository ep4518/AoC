#!/usr/bin/env python3
import sys
from typing import List

class Directory():
    def __init__(self, rows):
        self.rows = rows
        self.directory = self.constructor(self.rows)
    
    def constructor(self, rows):
        parents = []
        directory = {'/': {}}
        p1 = directory
        for row in self.rows:
            if row[1] == "cd":
                if row[2] != "..":
                    parents.append(p1)
                    p1 = p1[row[2]]
                else:
                    p1 = parents.pop()
                    continue
            elif row[1] == "ls":
                continue
            elif row[0] == 'dir':
                p1[row[1]] = {}
            else:
                try:
                    p1[row[1]] = int(row[0]) 
                except ValueError:
                    print(f"Value {row[0]} is not an integer.")
        return directory
    
    def list_directory(self, directory=None, indent=0):
            # If directory is None, we're at the root
            if directory is None:
                directory = self.directory
            
            for key, value in directory.items():
                print('  ' * indent + key)
                if isinstance(value, dict):  # If the value is a dictionary, it's a subdirectory
                    # Recurse into subdirectory
                    self.list_directory(value, indent + 1)

    def calculate_size(self, directory=None, path="/"):
        """
        Calculate sizes of all directories and return a dictionary where
        each key is a directory path and its value is the total size of files in that directory.
        """
        if directory is None:
            directory = self.directory

        sizes = {}  # Initialize the sizes dictionary to hold directory paths and their sizes

        total_size = 0  # Initialize total size for the current directory

        for key, value in directory.items():
            if isinstance(value, dict):  # If the value is a dictionary, it's a subdirectory
                subdirectory_path = f"{path}{key}" if path.endswith('/') else f"{path}/{key}"
                sub_sizes, sub_total_size = self.calculate_size(value, subdirectory_path)
                sizes[subdirectory_path] = sub_total_size  # Store the total size of the subdirectory
                total_size += sub_total_size  # Add the subdirectory's total size to the current directory's total size
                sizes.update(sub_sizes)  # Merge the sizes from the subdirectory into the main sizes dictionary
            else:
                # It's a file, add its size directly to the current directory's total size
                total_size += value

        # For the root directory, update its total size after processing all items
        if path == "/":
            sizes[path] = total_size

        return sizes, total_size

def part1(rows: List[int]) -> int:
    cnt = 0
    dir = Directory(rows)
    res = dir.calculate_size()[0]
    for _, value in res.items():
        if value <= 100000:
            cnt += value
    return cnt

def part2(rows: List[int]) -> int:
    TotalDiskSpace = 70000000
    required = TotalDiskSpace - 30000000
    dir = Directory(rows)
    res, total = dir.calculate_size()
    poss = []
    for key, value in res.items():
        if value >= (total - required):
            poss.append((key, value))

    return sorted(poss, key=lambda x: x[1])[0][1]

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day7.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            rows = [r.rstrip().split() for r in rows]
            Part1 = part1(rows)
            Part2 = part2(rows)
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