import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


def create_random_graph(number_of_vertices: int, number_of_edges: int, add_weights: bool):
    # Генерация случайного графа
    g = nx.gnm_random_graph(number_of_vertices, number_of_edges)

    # Добавление весов
    if add_weights:
        for (u, v) in g.edges():
            g[u][v]['weight'] = random.randint(1, 30)

    # Генерация матрицы смежности графа
    adj_matrix = nx.adjacency_matrix(g).toarray()

    return g, adj_matrix


def plot_graph(graph):
    layout = nx.shell_layout(graph)
    nx.draw(graph, layout, with_labels=True)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.show()


def prims_algorithm(adjacency_matrix: np.array):
    mst_matrix = np.zeros((len(adjacency_matrix), len(adjacency_matrix)))
    to_visit = [i for i in range(1, len(adjacency_matrix))]  # города кроме начального(0)
    visited = [0]

    for _ in to_visit:
        current_min = np.inf

        start = 0
        end = 0
        for ind in visited:
            for index, elem in enumerate(adjacency_matrix[ind]):
                if 0 < elem < current_min and index not in visited:
                    current_min = elem  # веса путей
                    start, end = ind, index

        if current_min == np.inf:
            mst_matrix[start][end] = 0
        else:
            mst_matrix[end][start] = mst_matrix[start][end] = current_min

        visited.append(end)  # содержит карту пути

    mst_graph = nx.from_numpy_matrix(mst_matrix)

    return mst_graph, mst_matrix

# my_graph, my_graph_matrix = create_random_graph(10, 20, add_weights=True)
# plot_graph(my_graph)
#
# my_mst_graph, my_mst_graph_matrix = prim(my_graph_matrix)
# plot_graph(my_mst_graph)
