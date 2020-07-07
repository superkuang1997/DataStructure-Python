# Kosaraju: Strongly Connected Components 强连通分支算法
# There are paths back and forth between any two vertices V and W in C,
# that is (V, W) (W, V) are paths of C, and C is the largest subset with such properties

from graph import Graph


class SCCGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def kosaraju(self):
        self.dfs()
        sequence = sorted([(x.id, x.finish) for x in self], key=lambda x:x[1], reverse=True)
        transGraph = self.transposition()
        self.trans_dfs(transGraph, orderList=sequence)
        return transGraph


    def transposition(self):
        before = {}
        after = {}
        for vertex in self.getVertices():
            before[vertex] = [x.id for x in self.getVertex(vertex).getConnections()]
        for vertex in before:
            for nbr in before[vertex]:
                if nbr not in after:
                    after[nbr] = []
                after[nbr].append(vertex)
        graph = SCCGraph()
        for vertex in after:
            for nbr in after[vertex]:
                graph.addEdge(vertex, nbr)
        return graph


    def dfs(self):
        self.time = 0
        for vertex in self:
            vertex.setColor("white")
            vertex.setPred(None)
        for vertex in self:
            if vertex.getColor() == "white":
                self.dfsVisit(vertex)

    def trans_dfs(self, graph, orderList):
        self.time = 0
        for tup in orderList:
            vertex = graph.getVertex(tup[0])
            vertex.setColor("white")
            vertex.setPred(None)
        for tup in orderList:
            vertex = graph.getVertex(tup[0])
            if vertex.getColor() == "white":
                graph.dfsVisit(vertex)

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

    def searchSCC(self, graph):
        res = {}
        for vertex in graph:
            trace = vertex
            while trace.getPred():
                trace = trace.getPred()
            trace = trace.getID()
            if trace not in res:
                res[trace] = list(vertex.getID())
            else:
                res[trace].append(vertex.getID())
        return res


if __name__ == "__main__":
    g = SCCGraph()
    g.addEdge("a", "b")
    g.addEdge("b", "c")
    g.addEdge("b", "e")
    g.addEdge("c", "c")
    g.addEdge("c", "f")
    g.addEdge("d", "b")
    g.addEdge("d", "g")
    g.addEdge("e", "a")
    g.addEdge("e", "d")
    g.addEdge("f", "h")
    g.addEdge("g", "e")
    g.addEdge("h", "i")
    g.addEdge("i", "f")

    G = g.kosaraju()
    res = G.searchSCC(G)
    print(res)