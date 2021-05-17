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

    def removeVertex(self, key):
        if self.existence(key):
            removed = self.vertList.pop(key)
            for item in removed.neighboors:
                v = self.getVertex(item)
                v.neighboors.pop(key) if key in v.neighboors else None

    def myMin(self):
        graus = [len(item.neighboors.keys()) for item in self.vertList.values()]
        graus.sort()
        return graus[0] if len(graus) > 0 else 0


myGraph = Graph()
for i in range(int(input())):
    myInput = input().split()
    if myInput[0] == 'IV':
        myGraph.addVertex(myInput[1])
    elif myInput[0] == 'IA':
        if myGraph.existence(myInput[1]) and myGraph.existence(myInput[2]):
            keyOne, keyTwo = myGraph.getVertex(myInput[1]), myGraph.getVertex(myInput[2])
            keyOne.addNeighboor(keyTwo)
            keyTwo.addNeighboor(keyOne)
    elif myInput[0] == 'RV':
        if myGraph.existence(myInput[1]):
            myGraph.removeVertex(myInput[1])
    else:
        if myGraph.existence(myInput[1]) and myGraph.existence(myInput[2]):
            myGraph.getVertex(myInput[1]).neighboors.pop(myInput[2])
            myGraph.getVertex(myInput[2]).neighboors.pop(myInput[1])

value = myGraph.myMin()
print(value)

