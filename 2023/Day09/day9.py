#!/usr/bin/env python3
import sys
import numpy as np

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day9.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            score = 0
            rows = file.readlines()
            rows, count = parse(rows)
            for row in rows:
                # print(compute(row))
                score += compute(row)
                
            
            print(score)
    
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0
    
def parse(rows):
    count = 0
    new = []
    for i, row in enumerate(rows):
        count += 1
        row = row.replace('\n', '')
        row = row.split()
        row = [int(element) for element in row]
        new.append(row)

    return new, count


def compute(row):
    tmp = np.array(row)
    result_matrix = tmp.reshape(1, -1)  # Reshape to a row vector
    while not np.all(tmp == 0):
        tmp = np.diff(tmp)
        tmp_padded = np.pad(tmp, (0, result_matrix.shape[1] - len(tmp)), mode='constant')
        result_matrix = np.vstack([result_matrix, tmp_padded])

    for i in range(result_matrix.shape[1] - len(tmp) - 1):
        k = i + 1
        result_matrix[-k-1, len(tmp) + k] = result_matrix[-k, len(tmp) + k - 1] + result_matrix[-k - 1, len(tmp) + k - 1]

    return result_matrix[0, result_matrix.shape[1] - 1] + result_matrix[1, result_matrix.shape[1] - 1]

if __name__ == "__main__":
    main()
