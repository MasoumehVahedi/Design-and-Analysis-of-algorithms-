"""
   Node 1: node1
   Node 2: node2
   Weight: weight
   Info_node = [node1, node2, weight]
"""


class Graph:
    def __init__(self, V):
        self.V = V    # Number of nodes
        self.bag_nodes = []

    def addEdge(self, v1, v2, weight):
        self.bag_nodes.append([v1, v2, weight])


    # Print a graph representation
    def print_graph_nodes(self):
        num_edges = len(self.bag_nodes)
        for i in range(num_edges):
            print(f"edge{ i+1 }: {self.bag_nodes[i]}")


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(0, 0, 25)
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 2, 3)
    graph.addEdge(1, 3, 1)
    graph.addEdge(1, 4, 15)
    graph.addEdge(4, 2, 7)
    graph.addEdge(4, 3, 11)

    graph.print_graph_nodes()










