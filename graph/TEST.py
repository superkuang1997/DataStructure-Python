def kosaraju(self):
    trans_graph = self.transposition()
    self.dfs()
    sequence = sorted([(x.id, x.finish) for x in self], key=lambda x: x[1], reverse=True)

    return sequence


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
    graph = Graph()
    for vertex in after:
        for nbr in after[vertex]:
            graph.addEdge(vertex, nbr)
    return graph