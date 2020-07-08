import sys
from graph import Graph
from tree.priorityQueue import PriorityQueue


def dijkstra(graph, start):
    pq = PriorityQueue()
    for v in graph:
        v.setDistance(sys.maxsize)
    start = graph.getVertex(start)
    start.setDistance(0)
    pq.buildHeap([[v.getDistance(), v] for v in graph])
    while not pq.isEmpty():
        currentVert = pq.delMin()[1]
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.rearrange(nextVert, newDist)


def traceback(graph, target):
    traceRoute = []
    trace = graph.getVertex(target)
    traceRoute.append(trace.id)
    minDist = trace.distance
    while trace.getPred():
        trace = trace.getPred()
        traceRoute.append(trace.id)
    traceRoute.reverse()
    print("The minimum of distance:", minDist)
    print("traceRoute:", traceRoute)


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
    dijkstra(g, "v1")
    traceback(g, "v6")






