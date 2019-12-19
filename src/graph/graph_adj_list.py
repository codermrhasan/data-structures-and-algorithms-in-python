class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor]=weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]
    
    def __repr__(self):
        return f"{self.id}"
    
    def __str__(self):
        return f"{self.id} connectedTo: {[x.id for x in self.connectedTo]}"

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        self.numVertices += 1
        return newVertex
    
    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None
    
    def addEdge(self, f, t, weight=0):
        if f not in self.vertexList:
            self.addVertex(f)
        if t not in self.vertexList:
            self.addVertex(t)
        self.vertexList[f].addNeighbor(self.vertexList[t], weight)
    
    def getVertices(self):
        return self.vertexList.keys()
    
    def __contains__(self, key):
        return key in self.vertexList
    
    def __iter__(self):
        return iter(self.vertexList.values())
        