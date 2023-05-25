from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_safe(self, v, color, colors):
        for i in range(self.vertices):
            if self.adj_matrix[v][i] and colors[i] == color:
                return False
        return True

    def graph_coloring(self):
        result = [-1] * self.vertices
        result[0] = 0
        min_color = 0

        priority_queue = PriorityQueue()
        priority_queue.put((1, 0, result))

        while not priority_queue.empty():
            level, node, colors = priority_queue.get()

            if node == self.vertices:
                return colors

            for color in range(min_color, self.vertices):
                if self.is_safe(node, color, colors):
                    new_colors = colors[:]
                    new_colors[node] = color

                    # Compute the number of conflicts in the new coloring
                    conflicts = sum([self.is_safe(node, c, new_colors) for c in range(self.vertices)])

                    priority_queue.put((conflicts, node + 1, new_colors))

                    if color >= min_color:
                        min_color = color + 1

        return None


# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

colors = g.graph_coloring()
if colors is None:
    print("No solution exists.")
else:
    print("Graph coloring solution:")
    for i in range(len(colors)):
        print("Vertex", i, ":", colors[i])
