

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either_node(self):
        """One of the vertex or node will return """
        return self.v

    def other_node(self, vertex):
        """ The other node will return """
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def comapre_to_edges(self, edge_weight):
        """ We compare two edges based on their weights """
        if self.weight < edge_weight:
            return -1
        elif self.weight > edge_weight:
            return 1
        else:
            return 0



