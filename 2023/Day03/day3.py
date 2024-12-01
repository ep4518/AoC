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
            numbers, line_count = findnumbers(file)
            # print(numbers)
            for number_info in numbers:
                number_sum += check_surroundings(file, number_info, line_count)
            print(number_sum)

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0

def is_symbol(char):
    # Exclude '.' from string.punctuation
    symbols_without_dot = string.punctuation.replace('.', '')
    return char in symbols_without_dot

def findnumbers(file):
    numbers = []
    line_count = 0
    for line_number, line in enumerate(file, start=1):
        line_count += 1
        char_number = 0
        while char_number < len(line):
            if line[char_number].isnumeric():
                i = 1
                while char_number + i < len(line) and line[char_number + i].isnumeric():
                    i += 1
                number = int(line[char_number:char_number + i])
                numbers.append({"number": number, "line": line_number, "char": char_number, "length": i})
                char_number += i
            else:
                char_number += 1
    return numbers, line_count

def check_surroundings(file, number_info, line_count):
    line_number = number_info["line"]
    char_number = number_info["char"]
    number_length = number_info["length"]
    number = number_info["number"]

    start_line = max(1, line_number - 1)
    end_line = min(line_number + 1, line_count)

    surroundings = []
    file.seek(0)        # Reset file pointer to the beginning
    for current_line_number, current_line in enumerate(file, start=1):
        if start_line <= current_line_number <= end_line:
            surroundings.append(current_line)

    symbol_found = False
    for line_num, line in enumerate(surroundings, start=start_line):
        for char_num, char in enumerate(line):
            if (
                line_num == line_number and
                char_num >= char_number and
                char_num < char_number + number_length
            ):
                continue  # Skip the characters within the number

            if (
                char_num >= char_number - 1 and
                char_num <= char_number + number_length 
            ):
                if is_symbol(char):
                    symbol_found = True
                    break

    if symbol_found:
        return number
    else: 
        return 0

if __name__ == "__main__":
    main()


