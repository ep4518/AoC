#!/usr/bin/env python3
import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 2:
        print(f"Improper Usage: python day1.py [.csv]")
        return 1
    
    i = 0
    result = 0

    try:
        with open(sys.argv[1], 'r') as file1: 
            fieldnames = ['RawValue']
            reader1 = csv.DictReader(file1, fieldnames=fieldnames)

            for row in reader1:
                cypher = row['RawValue']
                digit_positions = []  # List to store digit positions
                digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
                
                for digit in digits:
                    count = 0
                    start_index = 0  # Start searching from the beginning of the 'RawValue' field
                    while digit in cypher.lower()[start_index:]:
                        index = cypher.lower()[start_index:].index(digit)
                        count += 1
                        digit_positions.append((digits[digit], start_index + index))  # Store digit and its position
                        start_index += index + len(digit)
            
                count2 = 0
                updated_cypher = cypher  # Initialize a new variable for each iteration
                for digit in digit_positions:
                    index = digit[1] + count2  # Adjust the index calculation
                    updated_cypher = updated_cypher[:index] + digit[0] + updated_cypher[index+len(digit[0]):]
                    count2 += len(digit[0]) - 1  # Adjust the count2 to account for the replaced characters

                cypherNumbers = [int(char) for char in updated_cypher if char.isdigit()]

                if cypherNumbers:
                    number = int(str(cypherNumbers[0]) + str(cypherNumbers[-1]))
                    i += 1
                    result += number
                    print(i, cypherNumbers, number)
    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(result)
    return result


if __name__ == "__main__":
    main()
