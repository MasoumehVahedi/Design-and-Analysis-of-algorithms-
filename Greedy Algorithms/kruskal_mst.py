"""
  We implement Kruskal's greedy algorithm for Minimum Spanning Tree (MST).
  Here is the steps to find MST using Kruskal's algorithm:
  1- Sort all the edges in non-decreasing order of their weights
  2- Select the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed,
     include this edge. Else, discard it.
  3- Repeat step#2 until there are (V-1) edges in the spanning tree.

  Note: v, w, weight = self.graph
"""

import heapq
from collections import deque
from Disjoint_set import UnionFind



class KruskalMST:
    def __init__(self, graph):
        self.graph = graph
        self.mst = deque()    # Queue to store MST edges
        self.uf = UnionFind(self.graph.V)    # V = number of vertices in the graph

        # Create a priority queue of edges sorted by weights
        self.xy = []
        for v in range(self.graph.V):
            for e in self.graph.adjacent(v):
                if v < e.other_node(v):        # Avoid adding duplicate edges
                    self.xy.append((e.weight, e))
        heapq.heapify(self.xy)   # using heapify to convert list into heap

        ####### Kruskal's algorithm ########
        while len(self.mst) < self.graph.V - 1:           # Number of edges to be taken is less than to V-1
            weight, edge = heapq.heappop(self.xy)    # using heappop() to pop smallest element
            v = edge.either_node()
            w = edge.other_node(v)
            if not self.uf.connected(v, w):
                self.uf.union(v, w)
                self.mst.append(edge)     # enqueue to mst


    def edges(self):
        return list(self.mst)


    def total_weight(self):
        return sum(edge.weight for edge in self.mst)










