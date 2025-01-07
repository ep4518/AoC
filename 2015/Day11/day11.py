#!/usr/bin/env python3
import sys

G = open(sys.argv[1]).read().splitlines()
x = list(G[0])

"""
ord('a'), ord('z') == 97, 122
"""

def find_next(x):
    
    def is_valid_password(x):
    
        trip, iol, doub = False, False, False
        
        for i in range(l-2):
            ords = [ord(ch) for ch in x[i:i+3]]
            diffs = [b - a for a, b in zip(ords, ords[1:])]
            if set(diffs) == {1}:
                trip = True
        
        for i in range(l-1):
            for j in range(i+2, l-1):
                if len(set([c for c in x[i:i+2]])) == 1 and len(set([c for c in x[j:j+2]])) == 1 and x[i] != x[j]:
                    doub = True
                    
        iol = not any(ch in x for ch in ['i', 'o', 'l'])
        
        return trip and iol and doub
    
    l = len(x)
    found = False
    while not found:
        k = 1
        while ord(x[-k]) == 122 and k < l:
            x[-k] = chr(97)
            k += 1 
                
        x[-k] = chr(ord(x[-k]) + 1)
        
        if ''.join(x) == 'abcdffaa':
            print('hit')
            
        if is_valid_password(x):
            found = not found
            
    return x

p1 = find_next(x)
print(f'Part 1: {''.join(p1)}')
print(f'Part 2: {''.join(find_next(p1))}')