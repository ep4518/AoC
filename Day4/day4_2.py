#!/usr/bin/env python3
import sys
from typing import List, Tuple

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day4.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            total_sum = 0 
            rows = file.readlines()
            my_dict = {}
            for i in range(len(rows)):
                my_dict[f"Game {i+1}"] = 0   
            for i, row in enumerate(rows):
                my_dict[f"Game {i+1}"] += 1
                ticket = parse(row)
                score, game = get_score(ticket)
                for k in range(my_dict[f"Game {i+1}"]):
                    for j in range(score):
                        if i + j + 1 < len(rows):
                            my_dict[f"Game {i + j + 2}"] += 1
        print(my_dict)
        total_sum = sum(my_dict.values())
        print(total_sum)
        
        


    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0

def get_score(ticket: Tuple[int, List[str], List[str]]):
    game = ticket[0]
    win_numbs = ticket[1]
    my_numbs = ticket[2]
    score = 0

    for number in my_numbs:
        if number in win_numbs:
            if score == 0:
                score = 1
            else:
                score += 1

    return score, game



def parse(row: str) -> Tuple[int, List[str], List[str]]:
    numbers = []
    current_number = ''
    for char in row:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''
        if char in "|:":
            current_number = char
            numbers.append(current_number)
            current_number = ''
    
    # Check for the last number if the line ends with a digit
    if current_number:
        numbers.append(int(current_number))

    # Find the index of the colon
    colon_index = numbers.index(':')

    # Extract the integer, first list, and second list
    integer_part = int("".join(map(str, numbers[:colon_index])))
    list1 = numbers[colon_index + 1:numbers.index('|')]
    list2 = numbers[numbers.index('|') + 1:]

    # Create a tuple
    result_tuple = (integer_part, list(map(int, list1)), list(map(int, list2)))

    return result_tuple

if __name__ == "__main__":
    main()
