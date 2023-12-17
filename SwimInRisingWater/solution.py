""" This modified Dijkstra's algorithm accounts for the rising water levels by ensuring that
    we always move to a cell with the lowest possible elevation.
    It guarantees that you reach the target cell in the minimum possible time.

    Note: heappush function is to maintain a priority queue (min-heap) where the smallest of these maximum values
    is always at the top of the heap. This allows our algorithm to always choose the path with the currently
    smallest maximum value, which is a common approach in problems where we need to minimize the maximum value
    encountered along a path."""


import heapq


class Solution:
    def __init__(self):
        # grid[i][j], where i is the row index and j is the column index.
        # self.grid = [[0 for _ in range(N)] for _ in range(N)]
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 4 Direction
        self.visit = set()

    def move(self, grid):
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]]    # Initialize (time/maxHeight or weight, row, column)
        while minHeap:
            # Using heappop to remove and return the smallest element
            t, row, col = heapq.heappop(minHeap)
            # (N -1, N -1): The bottom-right corner is our destination means the deepest and largest grid
            if row == N - 1 and col == N -1:
                return t
            for dr, dc in self.directions:
                neighbor_row, neighbor_col = row + dr, col + dc
                if (neighbor_row < 0 or neighbor_col < 0 or
                    neighbor_row == N or neighbor_col == N or
                    (neighbor_row, neighbor_col) in self.visit):
                    continue
                self.currentPos(neighbor_row, neighbor_col)
                heapq.heappush(minHeap, [max(t, grid[neighbor_row][neighbor_col]), neighbor_row, neighbor_col])

    def currentPos(self, row, col):
        return self.visit.add((row, col))











