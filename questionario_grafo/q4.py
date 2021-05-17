class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighboors = {}
    
    def addNeighboor(self, vertex):
        self.neighboors[vertex.key] = Vertex(vertex)
    

class Graph:
    def __init__(self):
        self.vertList = {}

    def addVertex(self, key):
        newVextex = Vertex(key)
        self.vertList[key] = newVextex

    def existence(self, key):
        return True if key in self.vertList else False

    def getVertex(self,n):
        return self.vertList[n] if n in self.vertList else None

myGraph = Graph()
for i in range(int(input())):
    myInput = input().split()
    myGraph.addVertex(myInput[0])
    for item in myInput[2:]:
        myGraph.addVertex(item) 
        myGraph.getVertex(myInput[0]).addNeighboor(myGraph.getVertex(item))
        myGraph.getVertex(item).addNeighboor(myGraph.getVertex(myInput[0]))

