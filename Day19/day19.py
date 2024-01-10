#!/usr/bin/env python3
import sys
from typing import Dict

class Decoder:
    def part1(self, rows):
        total = 0
        assignments = []
        workflows, parts = self.parse(rows=rows)
        for part in parts: 
            assignments.append(self.assign(part=part, workflow=workflows["in"], workflows=workflows))
        
        for assignment in zip(assignments, parts):
            if assignment[0]:
                total += sum(value for value in assignment[1].values())
        return total

    def part2(self, rows):
        total = 0
        workflows, _ = self.parse(rows=rows)
        print(workflows)
        return 0
    
    def assign(self, part, workflow, workflows):
        condition_met = False  # Flag to track if a condition has been met

        for elem in workflow[:-1]:
            colon = elem.find(':')
            part_val, sign, val = part[elem[0]], elem[1], int(elem[2:colon])

            if (sign == '>' and part_val > val) or (sign == '<' and part_val < val):
                end = elem[(colon + 1):]
                if end == 'A':
                    condition_met = True  # Set the flag to True
                    return 1
                elif end == 'R':
                    return 0
                else: 
                    result = self.assign(part, workflow=workflows[f"{end}"], workflows=workflows)
                    condition_met = True  # Set the flag to True
                    if result == 1:
                        return 1  # Return immediately if a condition has been met
                    else:
                        break  # Break out of the loop if a recursive call did not meet the condition

        if condition_met or workflow[-1] == 'R':
            return 0

        if workflow[-1] == 'A':
            return 1
        else:
            result = self.assign(part, workflow=workflows[f"{workflow[-1]}"], workflows=workflows)
            return result


    def parse(self, rows):
        workflows =[]
        parts = []
        flag = True
        for row in rows:
            row = row.replace('\n','')
            skip = False
            if row == '':
                flag = False
                skip = True
            if flag:
                workflows.append(row)
            else:
                if not skip:
                    parts.append(row)

        workflows2 = {}
        for workflow in workflows:
            workflow = workflow.replace('}', '').split('{')
            rhs = workflow[1].split(',')
            workflows2[workflow[0]] = rhs
        
        parts2 = []
        for part in parts:
            part = part.replace('{', '').replace('}', '')
            part = part.split(',')
            part_dict = {}
            for elem in part:
                part_dict[elem[0]]= int(elem[2:])
            parts2.append(part_dict)

        return workflows2, parts2
        
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day19.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            # Part1 = decoder_instance.part1(rows=rows)
            Part2 = decoder_instance.part2(rows=rows)
            # print(f"Part 1: {Part1}")
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