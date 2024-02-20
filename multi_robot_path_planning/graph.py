class Graph():
    def __init__(self) -> None:
        self.vertices = {}

    def load(self, data: dict):
        self.vertices = {}
        for vertex, edges in data.items():
            self.add_vertex(vertex, edges)

    def add_vertex(self, name, edges):
        self.vertices[name] = edges
