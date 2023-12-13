""" Dijkstra's Algorithm:
    Dijkstra's Algorithm is a Breadth First Search (BFS) algorithm but instead of doing regular
    queue where we are going to use a priority queue aka MinHeap.
    
    In shortestPath method:
    Initialize MinHeap to [0, src] which means from the source node what is the total distance it
    is going to reach the source node that is zero, and src is the node at that like distance. """

import heapq

class Dijkstra:
    def __init__(self, graph, src):
        self.graph = graph      # src, dist, weight = self.graph
        self.src = src

    def shortestPath(self):
        shortest = {}    # Map vertex to distance of the shortest path
        minHeap = [[0, self.src]]     # first value is weight (here is our distance), and second is node.
        ### BFS ###
        while minHeap:      # when minHeap is not empty
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            # Iterate over all edges connected to the node n1
            for edge in self.graph.adjacent(n1):
                n2 = edge.other_node(n1)       # Get the other node connected by the edge
                w2 = edge.weight               # Get the weight of the edge
                if n2 not in shortest:
                    heapq.heappush(minHeap, [w1 + w2, n2])    # it means, the total weight takes to reach to n2

        ### What if in BFS there are certain nodes that we just did not visit. If so, we assign those nodes a distance -1. ###
        for i in range(self.graph.V):    # V = number of vertices in the graph
            if i not in shortest:
                shortest[i] = -1

        return shortest


