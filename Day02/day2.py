#!/usr/bin/env python3
import sys

def main():
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    sum = 0

    if len(sys.argv) != 2:
        print("Improper Usage: python day2.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            for line in file:
                flag = True
                line = line.strip()
                game, decoded_list = decoder(line)

                for instance in decoded_list:
                                counts = instance['Counts']
                                for color, value in counts.items():
                                    if value > cubes[color]:
                                         flag = False
                                        # print(f"Warning: {color} count in instance {instance['Instance']} exceeds cube limit!")
                if flag == True:
                     sum += int(game)
            print(f"Sum of IDs is {sum}.")
        
    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def extract_counts(game_str):
    counts = {'red': 0, 'green': 0, 'blue': 0}
    for item in game_str.split(','):
        parts = item.strip().split()
        if len(parts) == 2 and parts[1] in counts:
            counts[parts[1]] += int(parts[0])
    return counts

def decoder(row: str):
    separators = [';', ':']

    for sep in separators:
        row = row.replace(sep, ';') 

    games = row.split(';')
    decoded_list = [game.strip() for game in games]
    game = decoded_list[0].strip().split()[1]
    decoded_list = [{'Instance': i, 'Counts': extract_counts(instance)} for i, instance in enumerate(decoded_list)][1:]
    
    return game, decoded_list


if __name__ == "__main__":
    main()
