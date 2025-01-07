#!/usr/bin/env python3
import sys
import hashlib

G = open(sys.argv[1]).read().strip()

def run(z: int = 5):
    def has_leading_zeros(hash_str, num_zeros):
        return hash_str[:num_zeros] == '0' * num_zeros

    i = 0
    while True:
        i += 1
        s = G + str(i)
        result = hashlib.md5(s.encode())
        a = result.hexdigest()
        if has_leading_zeros(a, z):
            break
    
    return i

print(f'Part 1: {run(5)}')
print(f'Part 2: {run(6)}')