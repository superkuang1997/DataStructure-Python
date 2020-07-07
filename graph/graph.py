from vertex import Vertex


class Graph:

    def __init__(self):
        self.vertexList = {}  # 存储顶点
        self.numVertex = 0

    def addVertex(self, key):
        """ add vertex
        """
        newVertex = Vertex(key)  # 生成顶点
        self.vertexList[key] = newVertex  # 向图中添加顶点
        self.numVertex += 1
        return newVertex

    def addEdge(self, v1, v2, weight=0):
        """ add an edge between two vertices
        """
        # add vertex if not exists
        if v1 not in self.vertexList:
            nv = self.addVertex(v1)
        if v2 not in self.vertexList:
            nv = self.addVertex(v2)
        self.vertexList[v1].addNeighbor(self.vertexList[v2], weight)

    def getVertex(self, n):
        """ return vertex if exists
        """
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def getVertices(self):
        """ get all vertices
        """
        return self.vertexList.keys()

    def __contains__(self, n):
        return n in self.vertexList

    def __iter__(self):
        return iter(self.vertexList.values())


if __name__ == "__main__":
    g = Graph()
    # 添加顶点
    for i in range(6):
        g.addVertex((i))
    # 添加边
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(9, 10, 5)
    g.addEdge(9, 1, 5)

    print(g.vertexList)
    print(g.getVertex(0))

    print("-" * 25)
    for vertex in g:
        for nbrv in vertex.getConnections():
            print("({0}, {1})".format(vertex.getID(), nbrv.getID()))