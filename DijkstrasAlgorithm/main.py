from GreedyAlgorithms.EdgeWeightedGraph.edgeWeightedGraph import EdgeWeightedGraph
from GreedyAlgorithms.EdgeWeightedGraph.edg import Edge
from DijkstrasAlgorithm import Dijkstra

if __name__ == "__main__":
    n = 4        # Number of vertices in the graph
    src = 0      # Starting (or source) vertex
    graph = EdgeWeightedGraph(n)
    graph.addEdge(Edge(0, 1, 10))
    graph.addEdge(Edge(0, 2, 6))
    graph.addEdge(Edge(0, 3, 5))
    graph.addEdge(Edge(1, 3, 15))
    graph.addEdge(Edge(2, 3, 4))

    dijkstra = Dijkstra(graph, src=0)

    for dist, node in dijkstra.shortestPath().items():
        print(f"{node} at weight {dist}")


