# Breadth First Search 广度优先搜索

from wordsBucket import createBucket
from linearTable.queue_ import Queue


def bfs(start):

    start.setDistance(0)  # set the initial distance to zero
    start.setPred(None)  # set the initial predecessor to None
    verticesQueue = Queue()
    verticesQueue.enqueue(start)  # enqueue the start node

    while verticesQueue.size() > 0:
        currentVert = verticesQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("gray")
                nbr.setDistance(currentVert.getDistance() + 1)  # set neighbor vertices distance
                nbr.setPred(currentVert)
                verticesQueue.enqueue(nbr)
        currentVert.setColor("black")


def traverse(graph, target):
    trace = graph.getVertex(target)
    while trace.getPred():
        print(trace.getID())
        trace = trace.getPred()
    print(trace.getID())


if __name__ == "__main__":
    g = createBucket("fourletterwords.txt")
    start = g.getVertex("FUCK")
    bfs(start)
    traverse(g, "PUMP")
