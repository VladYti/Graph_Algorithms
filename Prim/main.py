from prim_alghoritm import plot_graph, create_random_graph, prims_algorithm


def main():

    my_graph, my_graph_matrix = create_random_graph(10, 20, add_weights=True)
    plot_graph(my_graph)

    my_mst_graph, my_mst_graph_matrix = prims_algorithm(my_graph_matrix)
    plot_graph(my_mst_graph)

    return 1


if __name__ == '__main__':
    main()
