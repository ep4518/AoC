#!/usr/bin/env python3
import sys
from typing import List, Dict

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day5.py [.txt]")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            almanac = parse(rows)
            print(almanac)
            lowest_location = lowest(almanac)
            print(f"Lowest location: {lowest_location}")


    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return 0

def map_location(input: int, mapping: List[int]) -> int:
    for elem in mapping:
        if elem[1] <= input and elem[1] + elem[2] > input:
            return elem[0] - elem[1] + input
    return input

def lowest(almanac: Dict[int, List[List[int]]]) -> int:
    locations = []
    seed_to_soil = almanac["seed-to-soil"]
    soil_to_fertilizer = almanac["soil-to-fertilizer"]
    fertilizer_to_water = almanac["fertilizer-to-water"]
    water_to_light = almanac["water-to-light"]
    light_to_temperature = almanac["light-to-temperature"]
    temperature_to_humidity = almanac["temperature-to-humidity"]
    humidity_to_location = almanac["humidity-to-location"]

    # print(almanac)
    for seed in almanac["seeds"]:
        output = map_location(seed, seed_to_soil)
        output = map_location(output, soil_to_fertilizer)
        output = map_location(output, fertilizer_to_water)
        output = map_location(output, water_to_light)
        output = map_location(output, light_to_temperature)
        output = map_location(output, temperature_to_humidity)
        output = map_location(output, humidity_to_location)
        locations.append(output)

    return min(locations)

def seed_convert(almanac: Dict[int, List[List[int]]]) -> List[int]:
    data = almanac["seeds"]
    new_list = []

    for i in range(0, len(data), 2):
        start_point = data[i]
        end_point = data[i + 1]
        new_list.extend(range(start_point, start_point + end_point + 1))

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
    main()
    
'''
Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

'''