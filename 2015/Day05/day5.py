#!/usr/bin/env python3
import sys

G = open(sys.argv[1]).read().splitlines()

nice = 0
for string in G:
    SEEN = {}
    double = False
    prev = None
    for ch in string:
        
        s = SEEN.setdefault(ch, 0)
        
        if prev and prev == ch:
            double = True
        
        SEEN[ch] += 1
        prev = ch
    
    vowels = sum([value for key, value in SEEN.items() if key in ['a', 'e', 'i', 'o', 'u']]) >= 3
    substr = not any(ss in string for ss in ['ab', 'cd', 'pq', 'xy'])
    
    nice += double and vowels and substr

print(f'Part 1: {nice}')

p2 = 0
for string in G:
    trip, double = False, False
    l = 3
    for j in range(len(string) - (l - 1)):
        ss = string[j:j+l]
        if ss == ss[::-1]:
            trip = True
    
    pairs = {}
    for i, ch in enumerate(string):
        for j in range(i, len(string) + 1):
            if i + 2 == j:
                tmp = string[i:j]
                if tmp in pairs and abs(pairs[tmp] - i) > 1:
                    double = True
                
                pairs[tmp] = i
                
                
    p2 += trip and double

print(f'Part 2: {p2}')