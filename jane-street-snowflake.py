import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.animation as animation

#     5         15
#      \   10  /
#       \ / \ /
#    2 - 7 - 12- 17
#     \ / \ / \ /
#  0 - 4 - 9 - 14 - 18
#     / \ / \ / \
#    1 - 6 - 11- 16
#       / \ / \ 
#      /   8   \
#     3         13

# Starting with any one peg missing, can we find the game with the maximum moves
# A move (as in checkers) is one peg jumping over another into an empty slot.

edges = [(0, 4),(1, 4),(1, 6),(2, 4),(2, 7),(3, 6),(4, 6),(4, 7),
         (4, 9),(5, 7),(6, 8),(6, 9),(6, 11),(7, 9),(7, 10),(7, 12),
         (8, 11),(9, 11),(9, 12),(9, 14),(10, 12),(11, 13),(11, 16),(11, 14),
         (12, 14),(12, 15),(12, 17),(14, 16),(14, 17),(14, 18)]

lines = [(0, 4, 9, 14, 18), (3, 6, 9, 12, 15), (5, 7, 9, 11, 13),
        (2, 4, 6, 8), (8, 11, 14, 17), (2, 7, 12, 17), 
        (1, 4, 7, 10), (10, 12, 14, 16), (1, 6, 11, 16)]

def moves(state, final_states=None, visited_states=None, depth=0, debug=False):
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
                            if debug:
                                print(f"{'  ' * depth}Move: {line[i+2]} -> {line[i]} (depth {depth + 1})")
                            moves(new_state, final_states, visited_states, depth + 1, debug)

                    if i - 2 >= 0:
                        if state[line[i - 1]] and state[line[i - 2]]:
                            move_made = True
                            new_state = state.copy()
                            new_state[line[i]], new_state[line[i - 1]], new_state[line[i - 2]] = True, False, False
                            if debug:
                                print(f"{'  ' * depth}Move: {line[i-2]} -> {line[i]} (depth {depth + 1})")
                            moves(new_state, final_states, visited_states, depth + 1, debug)

    if not move_made:  
        final_states.append(state)
    return final_states

data = {}
results = {}
debug = False

for i in [0, 4, 9, 2]:                              # Rotational Symmetries
    state = {j: True for j in range(19)}
    state[i] = False
    if debug:
        print(f"\nStarting with hole at {i}:")
    data[i] = moves(state, debug=debug)
    results[i] = min([sum(map(lambda value: value, state.values())) for state in data[i]])

print(125 * "=")
print(results)
print(125 * "=")

iS = 0

initial_state = {i: True for i in range(19)}
initial_state[iS] = False

state_sequence = [initial_state] + moves(initial_state)

G = nx.from_edgelist(edges)
# pos = nx.spring_layout(G)
pos = {0: np.array([-1.00890925,  0.00118087]), 4: np.array([-0.50076007,  0.00146988]), 1: np.array([-0.62719227, -0.36305452]), 
       6: np.array([-0.24510666, -0.42829153]), 2: np.array([-0.64072334,  0.36605158]), 7: np.array([-0.25673849,  0.43266779]), 
       3: np.array([-0.49416979, -0.86811295]), 9: np.array([-0.00141309,  0.00068652]), 5: np.array([-0.51525057,  0.86849481]), 
       8: np.array([ 0.00998786, -0.72763896]), 11: np.array([ 0.2585045 , -0.43309267]), 10: np.array([-0.01019943,  0.72652729]), 
       12: np.array([0.24537004, 0.42674486]), 14: np.array([ 5.02087602e-01, -3.46427034e-04]), 13: np.array([ 0.51521084, -0.87148466]), 
       16: np.array([ 0.64126126, -0.36671701]), 15: np.array([0.49165244, 0.86970524]), 17: np.array([0.6285788 , 0.36402901]), 
       18: np.array([1.00780958, 0.00118087])}

fig, ax = plt.subplots(figsize=(6, 6))

def update(num):
    ax.clear()
    state = state_sequence[num]

    node_colors = ["yellow" if state[node] else "skyblue" for node in G.nodes]
    nx.draw(
        G, pos=pos, with_labels=True, 
        node_color=node_colors, 
        edge_color="gray", 
        node_size=1000, 
        font_weight="bold", ax=ax
    )

    ax.set_title(f"Initial State {iS}\nFinal State {num + 1}")

ani = animation.FuncAnimation(fig, update, frames=len(state_sequence), interval=1000, repeat=True)
plt.show()