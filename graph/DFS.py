from graph import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.setColor("white")
            vertex.setPred(None)
        for vertex in self:
            if vertex.getColor() == "white":
                self.dfsVisit(vertex)

    def dfsVisit(self, startVert):
        startVert.setColor("gray")
        self.time += 1
        startVert.setDiscovery(self.time)
        for nextVert in startVert.getConnections():
            if nextVert.getColor() == "white":
                nextVert.pred = startVert
                self.dfsVisit(nextVert)
        self.time += 1
        startVert.setFinish(self.time)
        startVert.setColor("black")


if __name__ == "__main__":

    g = DFSGraph()
    g.addEdge("a", "b")
    g.addEdge("a", "d")
    g.addEdge("b", "c")
    g.addEdge("b", "d")
    g.addEdge("d", "e")
    g.addEdge("e", "f")
    g.addEdge("e", "b")
    g.addEdge("f", "c")
    g.dfs()

    for vertex in [g.getVertex(key) for key in g.getVertices()]:
        print(str(vertex).ljust(25, " "), "discovery:", vertex.discovery, "finish:", vertex.finish)

