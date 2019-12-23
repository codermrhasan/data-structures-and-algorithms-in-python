from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.visited = False

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1, vertex2, weight=0):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            vertex1.neighbours.append(Edge(vertex2, weight))

    def get_neighbours(self, vertex):
        return vertex.neighbours
    
    def get_vertices(self):
        return self.vertices or None
    
    def breadth_first(self, root, operate):
        q = deque()
        q.appendleft(root) # for behave like a queue
        to_reset = set()
        while q:
            current = q.pop()
            current.visited = True
            to_reset.add(current)
            
            operate(current) # getting the nodes which are visited
            
            for edge in current.neighbours:
                if not edge.vertex.visited:
                    q.appendleft(edge.vertex)
        
        for vertex in to_reset:
            vertex.visited = False

    def __len__(self):
        return len(self.vertices)

        
