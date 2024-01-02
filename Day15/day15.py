#!/usr/bin/env python3
import sys

class Decoder:
    def decode1(self, rows):
        total = 0
        sequence = self.parse(rows)
        for str in sequence:
            total += self.hash_algorithm(str)
        return total    
    
    def decode2(self, rows):
        sequence = self.parse(rows)
        boxes = self.hashmap(sequence= sequence)
            
        return 0
    
    def hashmap(self, sequence):
        boxes = self.generate_boxes()
        for str in sequence:
            label = ''
            instruction = ''
            for ch in str:
                if ch.isalpha():
                    label += ch
                else:
                    instruction += ch

            # label = ''.join(ch for ch in str if ch.isalpha())
            box_num = self.hash_algorithm(label)

            # print(label, instruction, box_num)

            if instruction[0] == '=':
                boxes = self.add(int(instruction[1]), boxes, label)
            else:
                boxes = self.subtract(boxes, label)

        return boxes
    
    def add(self, lens_num: int, boxes: list[list[str]], label: str) -> list[list[str]]:
        # box_num = self.hash_algorithm(label)
        # box = boxes[box_num]
        # if any(box[lens][0] == label for lens in box):
        #     boxes[box_num][lens_num - 1] = (label, lens_num)
        # elif any(box[lens][0] != label for lens in box):
        pass
        
        

        return boxes
    
    def subtract(self, boxes: list[list[str]], label: str) -> list[list[str]]:
        box_num = self.hash_algorithm(label)
        for lens in boxes[box_num]:
            if lens == label:
                lens = ''
        
        return boxes
    
    def generate_boxes(self):
        return [['' for i in range(9)] for _ in range(256)]

    def hash_algorithm(self, str: str):
        value = 0
        for ch in str:
            value += ord(ch)
            value *= 17
            value = value % 256
        return value

    def parse(self, rows):
        input = []
        for row in rows:
            input.extend(row.strip().split(','))
        return input
        # return [row.strip().split(',') for row in rows]
            
def main():
    if len(sys.argv) != 2:
        print("Improper Usage: python day14.py [.txt]")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r') as file:
            rows = file.readlines()
            decoder_instance = Decoder()
            Part1 = decoder_instance.decode1(rows= rows)
            Part2 = decoder_instance.decode2(rows= rows)
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
