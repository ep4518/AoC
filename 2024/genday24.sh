#!/bin/bash

YEAR=2024

# day variable has no leading 0 and must be between 1 and 25
day=${1##+(0)}
if ((day < 1 || day > 25)); then
    echo "Invalid day input: $1. Must be between 1 and 25."
    return
fi
# project vartiable is "dayXX" where XX is the day variable
project=$(printf "Day%02d" $1)

# get session cookie from file if .session exists
if [[ -f "../.session" ]]; then
  AOC_SESSION=$(<"../.session")
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

mkdir ${project}

cd ${project}

curl -s "https://adventofcode.com/${YEAR}/day/${day}/input" --cookie "session=${AOC_SESSION}" -o input.txt

touch test.txt

echo -n "#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as file:
    rows = [r.strip() for r in file.readlines()]

for row in rows:
    print(row)


" > day${day}.py

chmod +x day${day}.py 

code day${day}.py input.txt test.txt

open -a "Microsoft Edge" "https://adventofcode.com/${YEAR}/day/${day}"