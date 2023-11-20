def BFS(a, s, t, parent):
    # Mark all the vertices as not visited
    visited = [False] * len(a)

    # Create a queue for BFS
    queue = [s]

    # Mark the source node as visited and enqueue it
    visited[s] = True

    # Standard BFS Loop
    while queue:

        # Dequeue a vertex from queue and print it
        u = queue.pop(0)

        # Get all adjacent vertices of the dequeued vertex u
        # If a adjacent has not been visited, then mark it
        # visited and enqueue it
        for ind, val in enumerate(a[u]):
            if visited[ind] is False and val > 0:
                # If we find a connection to the sink node,
                # then there is no point in BFS anymore
                # We just have to set its parent and can return true
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
                if ind == t:
                    return True

    # We didn't reach sink in BFS starting
    # from source, so return false
    return False


def FordFulkerson(a, source, sink):
    # This array is filled by BFS and to store path
    parent = [-1] * len(a)

    max_flow = 0  # There is no flow initially

    # Augment the flow while there is path from source to sink
    while BFS(a, source, sink, parent):

        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, a[parent[s]][s])
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges
        # along the path
        v = sink
        while v != source:
            u = parent[v]
            a[u][v] -= path_flow
            a[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    graph_1 = [[0, 20, 30, 10, 0],
               [0, 0, 40, 0, 30],
               [0, 0, 0, 10, 20],
               [0, 0, 0, 0, 20],
               [0, 0, 0, 0, 0]]

    source = 0
    sink = 4

    print("The maximum possible flow is %d " % FordFulkerson(graph_1, source, sink))


main()
