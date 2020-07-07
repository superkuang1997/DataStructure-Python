# 拓扑排序的对象必须是有向无圈图（DAG）
from DFS import DFSGraph


def topologicalSort(graph, startVert):
    for vertex in graph:
        vertex.setColor("white")
        vertex.setPred(None)
    graph.dfsVisit(graph.getVertex(startVert))
    for vertex in graph:
        if vertex.getColor() == "white":
            graph.dfsVisit(vertex)


if __name__ == "__main__":

    g = DFSGraph()
    g.addEdge("a", "d")
    g.addEdge("b", "d")
    g.addEdge("c", "d")
    g.addEdge("d", "e")
    g.addEdge("d", "h")
    g.addEdge("e", "f")
    g.addEdge("f", "g")
    g.addEdge("h", "g")
    g.addEdge("i", "e")
    topologicalSort(g, "d")

    for vertex in [g.getVertex(key) for key in g.getVertices()]:
        print(str(vertex).ljust(25, " "),
            "discovery:", vertex.discovery, "finish:", vertex.finish)
