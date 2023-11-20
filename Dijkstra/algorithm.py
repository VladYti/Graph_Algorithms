import numpy as np


def arg_min(current_step_line: list, viewed_graph_vertices: set):
    min_value_id = -1
    min_value = np.inf  # максимальное значение
    for i, value in enumerate(current_step_line):
        if value < min_value and i not in viewed_graph_vertices:
            min_value = value
            min_value_id = i

    return min_value_id


def get_linked_v(current_vertex: int, adjacency_matrix: np.array):
    for i, weight in enumerate(adjacency_matrix[current_vertex]):
        if weight > 0:
            yield i


def dijkstra_algorithm(adjacency_matrix: np.array):

    # min_dist_adj_matrix = np.zeros((len(adjacency_matrix), len(adjacency_matrix)))
    current_step_line = [np.inf] * len(adjacency_matrix)  # определяем строку веов на текущем шаге
    start_vertex = 0
    current_vertex = 0
    viewed_vertices = {start_vertex}
    current_step_line[start_vertex] = 0  # задеём вес для стартовой вершины равный 0

    while current_vertex != -1:
        for j in get_linked_v(current_vertex, adjacency_matrix):
            if j not in viewed_vertices:
                weight = current_step_line[current_vertex] + adjacency_matrix[current_vertex][j]
                if weight < current_step_line[j]:
                    current_step_line[j] = weight

        current_vertex = arg_min(current_step_line, viewed_vertices)
        if current_vertex > 0:
            viewed_vertices.add(current_vertex)

    return current_step_line
