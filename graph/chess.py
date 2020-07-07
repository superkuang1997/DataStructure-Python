from graph import Graph


def legalMove(x, y, borderSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, borderSize) and legalCoord(newY, borderSize):
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(pos, borderSize):
    if 0 <= pos < borderSize:
        return True
    else:
        return False


def knightGraph(borderSize):
    ktGraph = Graph()
    for row in range(borderSize):
        for col in range(borderSize):
            nodeID = posToNodeID(row, col, borderSize)
            newPosition = legalMove(row, col, borderSize)
            for edge in newPosition:
                nid = posToNodeID(edge[0], edge[1], borderSize)
                ktGraph.addEdge(nodeID, nid)
    return ktGraph


def posToNodeID(row, col, borderSize):
    return row * borderSize + col


if __name__ == "__main__":
    kg = knightGraph(5)
    print(kg.getVertices())
    for vertex in kg:
        print(vertex)