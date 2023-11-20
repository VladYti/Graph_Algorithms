import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(graph):


    layout = nx.shell_layout(graph)
    nx.draw(graph, layout, with_labels=True)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos=layout, edge_labels=labels)
    plt.show()


def primsAlgorithm(adjacency_matrix: np.array):
    number_of_vertices = len(adjacency_matrix)
    # Creating another adjacency Matrix for the Minimum Spanning Tree:
    mst_matrix = np.zeros((number_of_vertices, number_of_vertices))

    # Once the Adjacency Matrix is filled, we can start looking for the MST:
    # Defining a really big number:

    # This is a list showing which number_of_vertices are already selected so we don't pick the same vertex twice and we can actually know when stop looking
    selected_vertices: list[bool] = [False for _ in range(number_of_vertices)]

    # While there are number_of_vertices that are not included in the MST, keep looking:
    while False in selected_vertices:
        # We use the big number we created before as the possible minimum weight
        minimum = np.inf

        # The starting vertex
        start = 0

        # The ending vertex
        end = 0

        for i in range(number_of_vertices):
            # If the vertex is part of the MST, look its relationships
            if selected_vertices[i]:
                # Again, we use the Symmetric Matrix as an advantage:
                for j in range(i, number_of_vertices):
                    # If the vertex analyzed have a path to the ending vertex AND its not included in the MST (to avoid cycles)
                    if not selected_vertices[j] and adjacency_matrix[i][j] > 0:
                        # If the weight path analyzed is less than the minimum of the MST
                        if adjacency_matrix[i][j] < minimum:
                            # print(adjacency_matrix[i][j])
                            # Defines the new minimum weight, the starting vertex and the ending vertex
                            minimum = adjacency_matrix[i][j]
                            start, end = i, j

        # Since we added the ending vertex to the MST, it's already selected:
        selected_vertices[end] = True

        # Filling the MST Adjacency Matrix fields:

        if minimum == np.inf:
            mst_matrix[start][end] = 0
        else:
            mst_matrix[end][start] = mst_matrix[start][end] = minimum

        print(minimum)

    # Show off:
    mst_graph = nx.from_numpy_matrix(mst_matrix)
    return mst_graph, mst_matrix


def create_adj_matrix(number_of_vertices: int, add_weights: bool):
    matrix = np.random.randint(0, 2, (number_of_vertices, number_of_vertices))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                matrix[i, j] = 0
            matrix[j, i] = matrix[i, j]
            if add_weights:
                if matrix[i, j] == 1:
                    matrix[i, j] = matrix[j, i] = random.randint(5, 15)

    return matrix
