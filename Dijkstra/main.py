from algorithm import dijkstra_algorithm
from graph import *


def main():
    graph1, adj_matrix1 = create_random_graph(8, 15, add_weights=True)
    plot_graph(graph1)

    print(dijkstra_algorithm(adj_matrix1))

    plot_graph(min_distance_graph(graph1))

    return 0


if __name__ == '__main__':
    main()
