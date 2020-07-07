# Depth First Search for knight tourist 深度优先搜索解决骑士周游问题

from chess import knightGraph


def knightTour(borderSize, start):
    """
    knight tour question
    :param borderSize:the size of chessborder
    :param start:the start of a tour
    :return:a valid route
    """
    kg = knightGraph(borderSize)
    start = kg.getVertex(start)
    return knightTourHelper(0, [], start, borderSize ** 2 - 1)


def orderByAvail(vertex):
    """按照连接边进行排序，调整算法搜索方向加速收敛"""
    resList = []
    for nbr in vertex.getConnections():
        if nbr.getColor() == "white":
            count = 0
            for nnbr in nbr.getConnections():
                if nnbr.getColor() == "white":
                    count += 1
            resList.append((count, nbr))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


def knightTourHelper(n, path, start, limit):
    start.setColor("gray")
    path.append(start)
    if n < limit:
        nbrList = orderByAvail(start)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTourHelper(n + 1, path, nbrList[i], limit)
            i += 1
        if not done:
            path.pop()
            start.setColor("white")
    else:  # 递归结束条件：达到周游所有点的目标
        done = True

    return [x.id for x in path] if done else False


if __name__ == "__main__":
    print(knightTour(5, 0))
