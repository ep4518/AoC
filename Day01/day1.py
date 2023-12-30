#!/usr/bin/env python3
import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 2:
        print(f"Improper Usage: python day1.py [.csv]")
        return 1
    
    result = 0
    count = 0

    try:
        with open(sys.argv[1], 'r') as file1: 
            fieldnames = ['RawValue']
            reader1 = csv.DictReader(file1, fieldnames=fieldnames)

            for row in reader1:
                cypher = row['RawValue']
                cypherNumbers = [int(char) for char in cypher if char.isdigit()]

                if cypherNumbers:
                    number = int(str(cypherNumbers[0]) + str(cypherNumbers[-1]))
                    count += 1
                    result += number
    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    print(result, count)
    return result


if __name__ == "__main__":
    main()
