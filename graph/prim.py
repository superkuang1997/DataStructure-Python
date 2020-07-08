# minimum weight of spanning tree algorithm: prim

import sys
from graph import Graph
from tree.priorityQueue import PriorityQueue


def prim(graph, start):
    pq = PriorityQueue()
    for v in graph:
        v.setDistance(sys.maxsize)
    start = graph.getVertex(start)
    start.setDistance(0)
    pq.buildHeap([[v.getDistance(), v] for v in graph])
    minSpaningTree = Graph()
    pos = 1
    while not pq.isEmpty():
        enqueue = pq.delMin()
        currentDist,currentVert = enqueue[0], enqueue[1]
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getWeight(nextVert)
            if nextVert in pq and newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.rearrange(nextVert, newDist)
        if pos > 1:  # 起始点出队时不添加边
            minSpaningTree.addEdge(currentVert.pred.id, currentVert.id, currentDist)
        pos += 1
    return minSpaningTree


def traceback(Tree):
    sumWeight = 0
    for v in Tree:
        for nbr in v.getConnections():
            sumWeight += v.getWeight(nbr)
    print("The sum of weight:", sumWeight)


if __name__ == "__main__":
    g = Graph()
    g.addEdge("v1", "v2", 3)
    g.addEdge("v1", "v3", 4)
    g.addEdge("v2", "v4", 2)
    g.addEdge("v2", "v5", 4)
    g.addEdge("v3", "v2", 1)
    g.addEdge("v3", "v5", 3)
    g.addEdge("v4", "v5", 1)
    g.addEdge("v4", "v6", 4)
    g.addEdge("v5", "v6", 1)
    minSpaningTree = prim(g, "v1")
    for v in minSpaningTree:
        print(v)
    traceback(minSpaningTree)






