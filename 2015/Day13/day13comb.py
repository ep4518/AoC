import sys
from itertools import permutations
import networkx as nx
import matplotlib.pyplot as plt
import copy

from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem as tsp
from networkx.algorithms.approximation import christofides, greedy_tsp, simulated_annealing_tsp, threshold_accepting_tsp, asadpour_atsp

E = list(map(lambda x: [el for i, el in enumerate(x.split()) if i in [0, 2, 3, 10]], open(sys.argv[1]).read().splitlines()))

G = nx.Graph()
for u, d, w, v in E:
        u, v = u[0], v[0]
        w = int(w) if d == 'gain' else -int(w)
        if G.has_edge(u, v):
            w += G.get_edge_data(u, v)['weight']
            G.remove_edge(u, v)
        
        G.add_edge(u, v, weight=w)


def max_arrangement_score(G):
    
    nodes = list(G.nodes)
    perms = list(permutations(nodes[:-1], len(nodes[:-1])))

    for perm in perms: 
        mirror = perm[::-1]
        if mirror in perms:
            perms.remove(mirror)

    perms = [list(perm) + nodes[-1:] for perm in perms]

    cost = [sum([G.get_edge_data(*edge)['weight'] for edge in zip(p, p[1:] + p[0:])]) for p in perms]
    
    return max(cost)

print(f'Part 1: {max_arrangement_score(G)}')

nodes = copy.deepcopy(G.nodes)
for n in nodes:
    G.add_edge(n, 'X', weight=0)
    
print(f'Part 2: {max_arrangement_score(G)}')