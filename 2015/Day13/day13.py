#!/usr/bin/env python3
import sys
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem as tsp
from networkx.algorithms.approximation import christofides, greedy_tsp, simulated_annealing_tsp, threshold_accepting_tsp, asadpour_atsp

E = list(map(lambda x: [el for i, el in enumerate(x.split()) if i in [0, 2, 3, 10]], open(sys.argv[1]).read().splitlines()))

dG = nx.DiGraph()
with open('inputD.dot', 'w') as f:
    f.write("strict digraph day13 { \n")
    for e in E:
        abs_weight = int(e[2])
        weight = abs_weight if e[1] == 'gain' else -abs_weight
        dG.add_edge(e[0][0], e[-1][0], weight=weight)
        # dot -Tpng inputD.dot > graphD.png; open graphD.png 
        f.write(f"\t{e[0][0]} -> {e[-1][0]} [ label =\"{weight}\"];\n")
    f.write("}")
    
G = nx.Graph()
with open('input.dot', 'w') as f:
    f.write("strict graph day13 { \n")
    for u, d, w, v in E:
        u, v = u[0], v[0]
        w = int(w) if d == 'gain' else -int(w)
        if G.has_edge(u, v):
            w += G.get_edge_data(u, v)['weight']
            G.remove_edge(u, v)
            f.write(f"\t{u} -- {v} [ label =\"{w}\"];\n")

        # print(u, v, w)
        G.add_edge(u, v, weight=w)
        # dot -Tpng input.dot > graph.png; open graph.png 
        
    f.write("}")

G2 = G.copy()   
smallest = max(G.edges[a, b]['weight'] for a, b in G.edges)
for a, b in G.edges():
    G2.edges[a, b]['weight'] = -G.edges[a, b]['weight'] + smallest

res = tsp(G2, method=christofides, cycle=True, nodes=G2.nodes)
cost = sum([G.get_edge_data(*edge)['weight'] for edge in zip(res, res[1:])])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, 
        edge_color="gray", 
        node_size=1000, 
        font_weight="bold",
)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.show()
print(f'Part 1: {cost}')
print("NOT VALID METHOD -> COMBINATORICS")