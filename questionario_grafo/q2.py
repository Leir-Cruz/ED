#exemplo de grafo direcionado
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighboors = {}
    
    def addNeighboor(self, key, weight):
        self.neighboors[key] = weight   

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
            for v in self.vertList.values():
                v.neighboors.pop(key) if key in v.neighboors else None

    def myEdges(self):
        edges, totalWeight = 0, 0
        for v in self.vertList.values():
            for w in v.neighboors:
                edges += 1
                totalWeight += v.neighboors[w]
        return edges, totalWeight

    
myGraph = Graph()
for i in range(int(input())):
    myInput = input().split()
    if myInput[0] == 'IV':
        myGraph.addVertex(myInput[1])
    elif myInput[0] == 'IA':
        if myGraph.existence(myInput[1]) and myGraph.existence(myInput[2]):
            keyOne, keyTwo = myGraph.getVertex(myInput[1]), myGraph.getVertex(myInput[2])
            keyOne.addNeighboor(keyTwo.key, float(myInput[3]))
    elif myInput[0] == 'RV':
        if myGraph.existence(myInput[1]):
            myGraph.removeVertex(myInput[1])
    else:
        if myGraph.existence(myInput[1]) and myInput[2] in myGraph.getVertex(myInput[1]).neighboors:
            myGraph.getVertex(myInput[1]).neighboors.pop(myInput[2])

edges, weight = myGraph.myEdges()
print(f"{len(myGraph.vertList)} vertice(s), {edges} aresta(s) e peso total {weight:.2f}.")

for i in myGraph.vertList.values():
    print(f'{i.key} vizinhos: {i.neighboors}')