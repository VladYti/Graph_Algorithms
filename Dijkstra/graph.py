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


def min_distance_graph(graph):
    adj_matrix = nx.adjacency_matrix(graph).toarray()
    p1 = nx.shortest_path(graph, source=0, weight='weight')
    min_dist_adj_matrix = np.zeros((len(adj_matrix), len(adj_matrix)))

    for item in p1.items():
        if item[0] != 0:
            min_dist_adj_matrix[item[0]][item[1][-2]] = 1

    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if min_dist_adj_matrix[i][j] == 0:
                min_dist_adj_matrix[i][j] = min_dist_adj_matrix[j][i]
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix)):
            if min_dist_adj_matrix[i][j] != 0:
                min_dist_adj_matrix[i][j] = adj_matrix[i][j]

    graph1 = nx.from_numpy_matrix(min_dist_adj_matrix)

    return graph1
