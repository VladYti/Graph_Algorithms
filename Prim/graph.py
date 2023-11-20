# import networkx as nx
# import matplotlib.pyplot as plt
# import random
# import numpy as np
#
#
#
#
# Matrix = np.random.randint(0, 2, (7, 7))
# for i in range(len(Matrix)):
#     for j in range(len(Matrix)):
#         if i == j:
#             Matrix[i, j] = 0
# print(type(Matrix))
#
#
# G = nx.from_numpy_matrix(Matrix)
#
# for (u, v) in G.edges():
#     G[u][v]['weight'] = random.randint(5, 15)
#
#
# layout = nx.spring_layout(G)
# nx.draw(G, layout, with_labels=True)
# labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
# plt.show()
