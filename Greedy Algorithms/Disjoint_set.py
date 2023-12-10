

class UnionFind:
    def __init__(self, size):
        # Create Vertices or Nodes subsets with single elements
        self.parent = [node for node in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, p):
        """ Traverse up the tree to find set of an element p using path compression"""
        if self.parent[p] != p:      # if p is not the root
            self.parent[p] = self.find(self.parent[p])      # Path compression
        return self.parent[p]

    def union(self, x, y):
        """ Join two subsets x and y into a single subset by rank. """
        # 1- Find roots
        rootX = self.find(x)
        rootY = self.find(y)
        # 2- Check if already united: If rootX and rootY are the same, it means x and y are already in the same subset,
        # and no further action is needed.
        if rootX == rootY:
            return False
        # 3- Union by rank: If rootX and rootY are different, the subsets are not yet united, and the method will merge the two trees.
        # The tree with the smaller rank is attached to the root of the tree with the larger rank. Merge smaller tree into larger one:
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX

        # If ranks are same, then make one as root and increment its rank by one
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True

    def connected(self, x, y):
        """ This function checks if two elements x and y are the same (in the same subset) which means they are connected. """
        return self.find(x) == self.find(y)









