#!/usr/bin/env python3
import sys
from collections import defaultdict

rows = list(map(int, open(sys.argv[1]).read().strip().split('\n')))

def evolve(secret):
    def mix(value, secret):
        return value ^ secret

    def prune(secret):
        return secret % 16777216
    
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(int(secret / 32), secret))
    secret = prune(mix(secret * 2048, secret))

    return secret

p1 = 0
seq_map = defaultdict(int)
for secret in rows: 
    seen = set()
    secrets = [(secret := evolve(secret)) % 10 for _ in range(2000)]
    diffs = [y - x for x, y in zip(secrets, secrets[1:])]
    p1 += secret

    for n, *seq in zip(secrets[4:], diffs, diffs[1:], diffs[2:], diffs[3:]):
        seq = tuple(seq)
        if seq in seen: continue
        seen.add(seq)
        seq_map[seq] += n

print(f'Part 1: {p1}')
print(f'Part 2: {seq_map[max(seq_map, key=seq_map.get)]}')