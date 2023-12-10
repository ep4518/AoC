#!/usr/bin/env python3
import sys
from typing import List, Dict
import numpy as np
import cProfile

def profile_code():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            almanac = parse(rows)
            print(almanac)
            # lowest_location = lowest(almanac)
            # print(f"Lowest location: {lowest_location}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0

def map_location(input_val: int, mapping: List[List[int]]) -> int:
    for elem in mapping:
        if elem[0] <= input_val < elem[0] + elem[2]:
            return input_val - elem[0] + elem[1] 
    return input_val

def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]

        if mid_value == target:
            return True 
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False 

def lowest(almanac):
    print(almanac["seeds"])
    locations = []
    seed_not_found = True

    seed_to_soil = np.array(almanac["seed-to-soil"])
    soil_to_fertilizer = np.array(almanac["soil-to-fertilizer"])
    fertilizer_to_water = np.array(almanac["fertilizer-to-water"])
    water_to_light = np.array(almanac["water-to-light"])
    light_to_temperature = np.array(almanac["light-to-temperature"])
    temperature_to_humidity = np.array(almanac["temperature-to-humidity"])
    humidity_to_location = np.array(almanac["humidity-to-location"])

    i = 0
    while (seed_not_found):
        i += 1
        seed = map_location(i, humidity_to_location)
        seed = map_location(seed, temperature_to_humidity)
        seed = map_location(seed, light_to_temperature)
        seed = map_location(seed, water_to_light)
        seed = map_location(seed, fertilizer_to_water)
        seed = map_location(seed, soil_to_fertilizer)
        seed = map_location(seed, seed_to_soil)
        
        if binary_search(almanac["seeds"], seed):
            min_location = i
            seed_not_found = False
    
    return min_location

# Custom sorting key function
def custom_sort_key(element):
    if element % 2 == 1:  # Odd number
        return (1, -element)  # Sort odd numbers in descending order
    else:  # Even number
        return (0, element)  # Sort even numbers normally

def seed_convert(almanac):
    data = almanac["seeds"]
    data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
    data = sorted(data, key=lambda x: x[0])
    data = [item for pair in data for item in pair]
    new_list = [item for start, end in zip(data[::2], data[1::2]) for item in range(start, start + end + 1)]
    almanac["seeds"] = new_list
    return almanac

def parse(rows):
    almanac = {
        "seeds": [],
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": []
    }
    for row in rows:
        words = row.split()
        if words:
            if words[0][0].isalpha():
                title = words[0]
                skip_row = True  # Set the flag to True when a title is encountered
            else:
                skip_row = False  # Reset the flag when a non-title row is encountered

            if title == "seeds:":
                almanac["seeds"] = [int(word) for word in words[1:]]
            if not skip_row:
                words = [int(word) for word in words]
                if(title == "seed-to-soil"):
                    almanac["seed-to-soil"].append(words)
                elif(title == "soil-to-fertilizer"):
                    almanac["soil-to-fertilizer"].append(words)
                elif(title == "fertilizer-to-water"):
                    almanac["fertilizer-to-water"].append(words)
                elif(title == "water-to-light"):
                    almanac["water-to-light"].append(words)
                elif(title == "light-to-temperature"):
                    almanac["light-to-temperature"].append(words)
                elif(title == "temperature-to-humidity"):
                    almanac["temperature-to-humidity"].append(words)
                elif(title == "humidity-to-location"):
                    almanac["humidity-to-location"].append(words)
    
    almanac = seed_convert(almanac)
    return almanac


if __name__ == "__main__":
    cProfile.run("profile_code()", sort='cumulative')
