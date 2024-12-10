import numpy as np
import matplotlib.pyplot as plt

#     3         13
#      \   8   /
#       \ / \ /
#    1 - 6 - 11- 16
#     \ / \ / \ /
#  0 - 4 - 9 - 14 - 18
#     / \ / \ / \
#    2 - 7 - 12- 17
#       / \ / \ 
#      /   10  \
#     5         15

# Starting with any one peg missing, can we find the game with the maximum moves
# A move (as in checkers) is one peg jumping over another into an empty slot.

edges = [(0, 4),(1, 4),(1, 6),(2, 4),(2, 7),(3, 6),(4, 6),(4, 7),
         (4, 9),(5, 7),(6, 8),(6, 9),(6, 11),(7, 9),(7, 10),(7, 12),
         (8, 11),(9, 11),(9, 12),(9, 14),(10, 12),(11, 13),(11, 16),(11, 14),
         (12, 14),(12, 15),(12, 17),(14, 16),(14, 17),(14, 18)]

lines = [(0, 4, 9, 14, 18), (3, 6, 9, 12, 15), (5, 7, 9, 11, 13),
        (2, 4, 6, 8), (8, 11, 14, 17), (2, 7, 12, 17), 
        (1, 4, 7, 10), (10, 12, 14, 16), (1, 6, 11, 16)]

class AdjMatrix:
    def __init__(self, n):
        self._adj_matrix = np.zeros((n,n), dtype=int)

    def add_edge(self, i, j):
        self._validate_indices(i,j)
        self._adj_matrix[i][j] = 1
        self._adj_matrix[j][i] = 1

    def rm_edge(self, i, j):
        self._validate_indices(i,j)
        self._adj_matrix[i][j] = 0
        self._adj_matrix[j][i] = 0

    def look_up(self, i, j):
        self._validate_indices(i, j)
        return self._adj_matrix[i][j] == 1

    def get_adjacent_nodes(self, node):
        self._validate_indices(node, node)
        return [i for i in range(self._adj_matrix.shape[0]) if self._adj_matrix[node][i] == 1]
    
    def _validate_indices(self, i, j):
        n = self._adj_matrix.shape[0]
        if i < 0 or i >= n or j < 0 or j >= n:
            raise IndexError("Index out of bounds for the adjacency matrix.")
        

    def __iter__(self):
        return iter(self._adj_matrix)
    
    def __repr__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self._adj_matrix])

    def get_matrix(self):
        return self._adj_matrix

def moves(state, final_states=None, visited_states=None, depth=0):
    if final_states is None:
        final_states = []
    if visited_states is None:
        visited_states = set()

    serialized_state = tuple(sorted(state.items()))
    
    if serialized_state in visited_states:
        return final_states
    visited_states.add(serialized_state)

    move_made = False
    for current, peg in state.items():
        if not peg:
            for line in lines:
                if current in line:
                    i = line.index(current)
                    l = len(line)

                    if i + 2 < l:
                        if state[line[i + 1]] and state[line[i + 2]]:
                            move_made = True
                            new_state = state.copy()
                            new_state[line[i]], new_state[line[i + 1]], new_state[line[i + 2]] = True, False, False
                            # print(f"{'  ' * depth}Move: {line[i+2]} -> {line[i]} (depth {depth + 1})")
                            moves(new_state, final_states, visited_states, depth + 1)

                    if i - 2 >= 0:
                        if state[line[i - 1]] and state[line[i - 2]]:
                            move_made = True
                            new_state = state.copy()
                            new_state[line[i]], new_state[line[i - 1]], new_state[line[i - 2]] = True, False, False
                            # print(f"{'  ' * depth}Move: {line[i-2]} -> {line[i]} (depth {depth + 1})")
                            moves(new_state, final_states, visited_states, depth + 1)

    if not move_made:  
        final_states.append(state)
    return final_states

# adjMatrix = AdjMatrix(19)

# for (i,j) in edges:
#     adjMatrix.add_edge(i,j)

# plt.imshow(adjMatrix._adj_matrix, cmap='hot', interpolation='nearest')
# plt.show()

data = {}
results = {}

for i in range(19):
    state = {j: True for j in range(19)}
    state[i] = False
    # print(f"\nStarting with hole at {i}:")
    data[i] = moves(state)
    results[i] = min([sum(map(lambda value: value, state.values())) for state in data[i]])

print(results)