#!/usr/bin/env python3
import sys
import re
from itertools import permutations
import networkx as nx

pattern = re.compile(r'(?P<loc1>[a-zA-Z]+) to (?P<loc2>[a-zA-Z]+) = (?P<dist>\d+)') 
data = list(map(lambda x: list(x.groupdict().values()) , list(map(pattern.match, open(sys.argv[1]).read().splitlines()))))

G = nx.Graph()

for a, b, dist in data:
    G.add_edge(a, b, weight=int(dist))
    
solve = lambda func: (
    func(sum(relations[trip]['weight'] for trip in zip(route, route[1:]))
         for route in permutations(locations)))

locations = G.nodes()
relations = G.edges()

print(solve(min))
print(solve(max))