#!/usr/bin/env python3
import sys
import heapq

"""
https://gitlab.com/0xdf/aoc2023/-/blob/main/day17/day17.py?ref_type=heads
"""

class Decoder:
    def decode1(self, rows):
        dict_grid = self.dict_parse(rows=rows)
        height = len(rows)
        width = len(rows[0].strip())

        queue = [(0, 0, 0 ,0 ,0 ,0)]
        seen = set()

        while queue:

            heat, r, c, dr, dc, s = heapq.heappop(queue)
            
            if (r, c, dr, dc, s) in seen:
                continue

            if r == height - 1 and c == width - 1:
                total = heat
                break

            seen.add((r, c, dr, dc, s))

            for next_dr, next_dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_r = r + next_dr
                next_c = c + next_dc
                if next_r < 0 or next_r >= height or next_c < 0 or next_c >= width:
                    continue  # off the grid, not valid
                if next_dr == -dr and next_dc == -dc:
                    continue  # can't go backwards
                if next_dr == dr and next_dc == dc:
                    if s < 3:
                        heapq.heappush(
                            queue,
                            (
                                heat + dict_grid[(next_r, next_c)],
                                next_r,
                                next_c,
                                next_dr,
                                next_dc,
                                s + 1,
                            ),
                        )
                    else:
                        continue
                else:
                    heapq.heappush(
                        queue,
                        (heat + dict_grid[(next_r, next_c)], next_r, next_c, next_dr, next_dc, 1),
                    )

        return total


    def decode2(self, rows):
        dict_grid = self.dict_parse(rows=rows)
        height = len(rows)
        width = len(rows[0].strip())
        queue2 = [(0, 0, 0, 0, 0, 0)]
        seen2 = set()

        while queue2:
            heat, r, c, dr, dc, s = heapq.heappop(queue2)

            if (r, c, dr, dc, s) in seen2:
                continue

            if r == height - 1 and c == width - 1:
                total = heat
                break

            seen2.add((r, c, dr, dc, s))

            for next_dr, next_dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_r = r + next_dr
                next_c = c + next_dc
                if next_r < 0 or next_r >= height or next_c < 0 or next_c >= width:
                    continue  # off the grid, not valid
                if next_dr == -dr and next_dc == -dc:
                    continue  # can't go backwards
                if next_dr == dr and next_dc == dc:
                    if s < 10:
                        heapq.heappush(
                            queue2,
                            (
                                heat + dict_grid[(next_r, next_c)],
                                next_r,
                                next_c,
                                next_dr,
                                next_dc,
                                s + 1,
                            ),
                        )
                    else:
                        continue
                elif s >= 4 or (dr == 0 and dc == 0):
                    heapq.heappush(
                        queue2,
                        (heat + dict_grid[(next_r, next_c)], next_r, next_c, next_dr, next_dc, 1),
                    )


        return total

    def dict_parse(self, rows):
        return {(r, c): int(v) for r, line in enumerate(rows) for c, v  in enumerate(line.strip())}
    
    def parse(self, rows):
        lst = [row.strip() for row in rows]
        return [[int(digit) for digit in item] for item in lst]

def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.decode1(rows=rows)
            Part2 = decoder_instance.decode2(rows=rows)
            print(f"Part 1: {Part1}")
            print(f"Part 2: {Part2}")

    except FileNotFoundError:
        print(f"File '{sys.argv[1]}' not found.")
    except PermissionError:
        print(f"Permission denied for '{sys.argv[1]}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return 0

if __name__ == "__main__":
    main()
