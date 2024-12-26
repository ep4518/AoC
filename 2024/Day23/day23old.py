#!/usr/bin/env python3
import sys
import numpy as np
from typing import List

class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.nodes = list({node for edge in self.edges for node in edge}) 
        self.adjacency_matrix = np.zeros((0, 0))
        self.update_adjaceny_matrix()
        self.largest_cycle = []

    def add_edge(self, edge):
        self.edges.append(edge)
        self.update_adjaceny_matrix()
    
    def update_adjaceny_matrix(self):
        self.nodes = list({node for edge in self.edges for node in edge})
        n = len(self.nodes)
        self.adjacency_matrix = np.zeros((n, n))
        node_to_index = {node: i for i, node in enumerate(self.nodes)}
        for u, v in self.edges:
            self.adjacency_matrix[node_to_index[u], node_to_index[v]] = 1
            self.adjacency_matrix[node_to_index[v], node_to_index[u]] = 1 

    def is_in_graph(self, node):
        return any(node in edge for edge in self.edges)
    
    def find_triples(self):
        n = self.adjacency_matrix.shape[0]
        triples = set()
        for i in range(n):
            for j in range(n):
                if self.adjacency_matrix[i][j] == 1:
                    for k in range(n):
                        if self.adjacency_matrix[j][k] == 1 and self.adjacency_matrix[k][i] == 1:
                            triples.add(tuple(sorted([self.nodes[i], self.nodes[j], self.nodes[k]])))
        self.triples = triples

    
    def __repr__(self):
        return f"Graph(edges={self.edges})"
    
    @property
    def length(self):
        return len(self.edges)
        

edges = list(map(lambda x: tuple(x.split('-')), open(sys.argv[1]).read().strip().split('\n')))

graphs = [Graph([edges[0]])]
for i, edge in enumerate(edges[1:]):
    if i % 100 == 0:
        print(i)
    flag = True
    for graph in graphs:
        if any(graph.is_in_graph(node) for node in edge):
            flag = False
            graph.add_edge(edge)
    
    if flag:
        graphs.append(Graph([edge]))

triples = set()
for graph in graphs:
    graph.find_triples()
    triples = triples | graph.triples

final = {triple for triple in triples if any(x[0] == 't' for x in triple)}

print(f'Part 1: {len(final)}')