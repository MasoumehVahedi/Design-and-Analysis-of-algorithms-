

class EdgeWeightedGraph:
    def __init__(self, V):
        """ In this graph, we need to create an array of bags to store Edges and Nodes (vertices) """
        self.V = V
        self.adj = self.bagEdges()


    def bagEdges(self):
        """ We have a bag that stores edges or a list of edges (a nested list) """
        adj = [[] for _ in range(self.V)]
        return adj

    def addEdge(self, e):
        """
         This function adds edges to two neighbor lists (v and w)
         e: is an Edge.
         e store twice because one edge is connected with two nodes v and w
        """
        v = e.either_node()
        w = e.other_node(v)
        # Now, we add edges in our empty bag (adj)
        self.adj[v].append(e)
        self.adj[w].append(e)

    def adjacent(self, v):
        return self.adj[v]

