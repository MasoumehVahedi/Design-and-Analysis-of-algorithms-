# Problem Description
We are give a grid of integers where each integer represents the elevation at that point. Imagine this grid as a topographic map.

### Objective:

We need to find the path from the top-left corner (0, 0) to the bottom-right corner (n-1, n-1) such that the maximum number on our path is minimized. This is like swimming across the grid where the water level is rising, and we want to keep the highest point we need to swim over as low as possible.

### Constrains:

We can move in four directions- up, down, left, right, but not diagonally.

## How Dijkstra's Algorithm Applies:

Dijkstra's Algorithm is a famous algorithm for finding the shortest path in a graph. In this case, it can be adapted to solve the "Swim in Rising Water" problem.

#### 1- Graph Representation: Each cell in the grid can be considered a node in the graph, and the edges connect adjacent cells. The weight of an edge can be considered as the elevation of the cell it leads to.

#### 2- Priority Queue: Dijkstra's Algorithm uses a priority queue to keep track of the next node to visit. In this problem, the priority queue will prioritize the path with the lowest maximum elevation.

#### 3- Algorithm Process:

- Start from the top-left cell.\\
- At each step, choose the next cell to move to based on the one with the lowest maximum elevation along the path so far.\\
- Continue this process until you reach the bottom-right cell.\\
