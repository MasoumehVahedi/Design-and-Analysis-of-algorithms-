from GreedyAlgorithms.EdgeWeightedGraph.edgeWeightedGraph import EdgeWeightedGraph
from GreedyAlgorithms.EdgeWeightedGraph.edg import Edge
from kruskal_mst import KruskalMST

if __name__ == "__main__":
    V = 4
    graph = EdgeWeightedGraph(V)
    graph.addEdge(Edge(0, 1, 10))
    graph.addEdge(Edge(0, 2, 6))
    graph.addEdge(Edge(0, 3, 5))
    graph.addEdge(Edge(1, 3, 15))
    graph.addEdge(Edge(2, 3, 4))

    mst = KruskalMST(graph)
    for edge in mst.edges():
        print(f"{edge.v} - {edge.w} at weight {edge.weight}")

    print(f"Total weight of MST: {mst.total_weight()}")
