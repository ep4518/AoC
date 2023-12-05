#!/usr/bin/env python3
import sys
import string

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day2.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            number_sum = 0
            numbers, gears, line_count = findnumbers(file)

            for gear_info in gears:
                number_sum += check_surroundings(file, gear_info, line_count, numbers)
            print(f"Sum of numbers with symbols in surroundings: {number_sum}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0

def is_symbol(char):
    symbols_without_dot = string.punctuation.replace('.', '')
    return char in symbols_without_dot

def is_integer(s):
    try:
        s = int(s)
        return s
    except ValueError:
        return s

def findnumbers(file):
    numbers = []
    gears = []
    line_count = 0
    gear_count = 0
    for line_number, line in enumerate(file, start=1):
        line_count += 1
        char_number = 0
        while char_number < len(line):
            if line[char_number] == '*':
                gear_count += 1
                gears.append({"line": line_number, "char": char_number, "gear": gear_count})
            if line[char_number].isnumeric():
                i = 1
                while char_number + i < len(line) and line[char_number + i].isnumeric():
                    i += 1
                number = int(line[char_number:char_number + i])
                numbers.append({"number": number, "line": line_number, "char": char_number, "length": i})
                char_number += i
            else:
                char_number += 1
    return numbers, gears, line_count

def get_numbers_around_position(numbers, line_number, char_number):
    neighboring_numbers = []

    for number_info in numbers:
        # print(f"Processing number_info: {number_info}")
        if (
            line_number - 1 <= number_info["line"] <= line_number + 1 and
            char_number - 1 <= number_info["char"] + number_info["length"] - 1 and 
            number_info["char"] <= char_number + 1
        ):
            if number_info.get("number") is not None:
                neighboring_numbers.append(number_info["number"])

    return neighboring_numbers

def get_surroundings(file, line_number, line_count):
    start_line = max(1, line_number - 1)
    end_line = min(line_number + 1, line_count)

    surroundings = []
    file.seek(0)  # Reset file pointer to the beginning
    for current_line_number, current_line in enumerate(file, start=1):
        if start_line <= current_line_number <= end_line:
            surroundings.append(current_line)

    return surroundings

def create_matrix(surroundings, line_number, char_number):
    matrix = [['' for _ in range(3)] for _ in range(3)]

    for line_num, line in enumerate(surroundings, start=line_number - 1):
        for char_index, char in enumerate(line[char_number - 1:char_number + 2]):
            matrix[line_num - line_number + 1][char_index] = is_integer(char) if char.isdigit() else char

    return matrix

def transpose_matrix(matrix):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        raise ValueError("Input matrix should be a 3x3 matrix.")

    transposed_matrix = [[matrix[j][i] for j in range(3)] for i in range(3)]

    return transposed_matrix


def analyze_and_check(matrix, gear_info, numbers):
    line_number = gear_info["line"]
    char_number = gear_info["char"]
    transpose = transpose_matrix(matrix=matrix)

    rows = any(isinstance(column[0], int) for column in transpose) + any(isinstance(column[1], int) for column in transpose) + any(isinstance(column[2], int) for column in transpose) 
    leftrightnotmiddlecolumns = any(isinstance(column[0], int) for column in matrix) and not any(isinstance(column[1], int) for column in matrix) and any(isinstance(column[2], int) for column in matrix)
    # nottopbottom = (not any(isinstance(column[0], int) for column in transpose)) and (not any(isinstance(column[2], int) for column in transpose))

    if rows ==3:
        return False
    if rows == 2:
        gear_info["bool"] = True
        print(f"Found gear on line {line_number} character index {char_number}")
        neighboring_numbers = get_numbers_around_position(numbers, line_number, char_number)
    elif rows == 1 and leftrightnotmiddlecolumns:
        gear_info["bool"] = True
        print(f"Found gear on line {line_number} character index {char_number}")
        neighboring_numbers = get_numbers_around_position(numbers, line_number, char_number)
    else:
        gear_info["bool"] = False
        neighboring_numbers = []
        print(f"Found something on line {line_number} character index {char_number}")


    return neighboring_numbers


def calculate_power(neighboring_numbers):
    if len(neighboring_numbers) == 2:
        power = neighboring_numbers[0] * neighboring_numbers[1]
        return power
    else:
        return 0

def check_surroundings(file, gear_info, line_count, numbers):
    line_number = gear_info["line"]
    char_number = gear_info["char"]

    surroundings = get_surroundings(file, line_number, line_count)
    matrix = create_matrix(surroundings, line_number, char_number)

    neighboring_numbers = analyze_and_check(matrix, gear_info, numbers)

    if len(neighboring_numbers) == 2:
        print(neighboring_numbers)
        return calculate_power(neighboring_numbers)
    return 0


if __name__ == "__main__":
    main()
