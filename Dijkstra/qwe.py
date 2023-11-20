import numpy as np
import networkx as nx
from graph import create_random_graph, plot_graph


def dijkstra_algorithm(adjacency_matrix: np.array):
    min_dist = np.zeros((len(adjacency_matrix), len(adjacency_matrix)))
    to_visit = [i for i in range(1, len(adjacency_matrix))]
    visited = [0]
    current_step_line = [np.inf] * len(adjacency_matrix)
    current_step_line[0] = 0

    for _ in to_visit:
        start = 0
        end = 0

        for i in visited:
            for j, weight in enumerate(adjacency_matrix[i]):
                if 0 < weight < current_step_line[j]:
                    current_step_line[j] = weight
                    start = i
                    end = j

        if current_step_line[end] == np.inf:
            min_dist[start][end] = 0
        else:
            min_dist[end][start] = min_dist[start][end] = current_step_line[end]

    min_graph = nx.from_numpy_matrix(min_dist)
    return min_graph, min_dist


g, m = create_random_graph(5, 8, add_weights=True)
plot_graph(g)
print(m)

g1, m1 = dijkstra_algorithm(m)
plot_graph(g1)
print(m1)


