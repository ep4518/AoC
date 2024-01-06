#!/bin/bash

YEAR=2023

# day variable has no leading 0 and must be between 1 and 25
day=${1##+(0)}
if ((day < 1 || day > 25)); then
    echo "Invalid day input: $1. Must be between 1 and 25."
    return
fi
# project vartiable is "dayXX" where XX is the day variable
project=$(printf "Day%02d" $1)

# get session cookie from file if .session exists
if [[ -f ".session" ]]; then
  AOC_SESSION=$(<".session")
fi

# validate session cookie
if [ -z "$AOC_SESSION" ]; then
    echo "AOC_SESSION isn't set. Cannot continue."
    return
fi
VALIDSESSION=$(curl -s "https://adventofcode.com/${YEAR}/day/1/input" --cookie "session=${AOC_SESSION}")
if [[ $VALIDSESSION =~ "Puzzle inputs differ by user." ]] || [[ $VALIDSESSION =~ "500 Internal Server" ]]; then
    echo "Invalid AOC_SESSION. Cannot continue."
    return
fi

# start rust project if second argument is rust
if [ "$2" = "rust" ]; then

    if [[ -d "${project}-rs" ]]; then
        cd ${project}-rs
        return
    fi

    cargo new ${project}-rs

    cd ${project}-rs

    curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

    echo -n 'fn main() {
    let data = include_str!("../input.txt").trim();
    println!(
        "Part 1: {}",
        ""
    );

    println!(
        "Part 2: {}",
        ""
    );
}' > src/main.rs

# python directory structure
else

    mkdir ${project}

    cd ${project}

    curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

    touch test.txt

    echo -n "#!/usr/bin/env python3
import sys

class Decoder:
    def part1(self, rows):
        return 0

    def part2(self, rows):
        return 0

def main():
    if len(sys.argv) != 2:
        print(\"Improper Usage: python day${day}.py [.txt]\")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.part1(rows=rows)
            Part2 = decoder_instance.part2(rows=rows)
            print(f\"Part 1: {Part1}\")
            print(f\"Part 2: {Part2}\")

    except FileNotFoundError:
        print(f\"File '{sys.argv[1]}' not found.\")
    except PermissionError:
        print(f\"Permission denied for '{sys.argv[1]}'.\")
    except Exception as e:
        print(f\"An error occurred: {e}\")

    return 0

if __name__ == \"__main__\":
    main()" > day${day}.py

chmod +x day${day}.py 

code day${day}.py 
fi