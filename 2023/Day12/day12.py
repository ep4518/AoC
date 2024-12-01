#!/usr/bin/env python3
import sys
from itertools import combinations

class springsDecoder:
    def decode(self, rows):
        total = 0
        for row in rows:
            springs, nums = row.split()
            nums = [int(n) for n in nums.split(',')]
            total += self.get_combinations(springs, nums)
        
        return total
    
    def get_combinations(self, springs, nums):
        """ 
        Recursive function for getting the number of combinations.
        Authored by: https://www.youtube.com/watch?v=0kvDfjjJPog

        """
        total = 0

        if len(springs) == 0:
            if len(nums) == 0:
                return 1 
            return 0

        if len(nums) == 0:
            if "#" in springs:
                return 0
            return 1

        if len(springs) < sum(nums) + len(nums) - 1:
            return 0

        if springs[0] in ".?":
            total += self.get_combinations(springs[1:], nums)

        n = nums[0]
        if (springs[0] in "#?" and 
            "." not in springs[:n] and
            (len(springs) == n or springs[n] in ".?")):
            total += self.get_combinations(springs[n+1:], nums[1:])

        return total

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day11.py [.txt]")
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
