# Kruskal's algorithm implementation

class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))
    edges.sort()

    minimum_spanning_tree = []
    union_find = UnionFind(graph.keys())

    for weight, v1, v2 in edges:
        if union_find.find(v1) != union_find.find(v2):
            union_find.union(v1, v2)
            minimum_spanning_tree.append((v1, v2, weight))
            

    return minimum_spanning_tree

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 3)],
    'C': [('A', 4), ('B', 2), ('D', 5)],
    'D': [('B', 3), ('C', 5)]
}

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(edge)
    
minimumCost = 0
for v1, v2, weight in minimum_spanning_tree:
    minimumCost += weight
print("Minimum Spanning Tree:", minimumCost)
