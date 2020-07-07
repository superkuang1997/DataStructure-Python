class Vertex:

    def __init__(self, _id):
        self.id = _id
        self.connectTo = {}
        self.color = "white"
        self.distance = 0
        self.pred = None
        self.discovery = 0
        self.finish = 0

    def addNeighbor(self, nbr, weight=0):
        """ add neighbor vertex
        :param nbr: Vertex, the another neighbor vertex.
        :param weight: int, the weight of the edge about two vertices
        :return:
        """
        self.connectTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connect to ' + str([x.id for x in self.connectTo])

    def getConnections(self):
        """获取已连接的所有顶点"""
        return self.connectTo.keys()

    def getID(self):
        """获取自顶点标号"""
        return self.id

    def getWeight(self, nbr):
        """获取相邻顶点权值"""
        return self.connectTo[nbr]

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.pred

    def getDiscovery(self):
        return self.discovery

    def getFinish(self):
        return self.finish

    def setDistance(self, distance):
        self.distance = distance

    def setPred(self, pred):
        self.pred = pred

    def setColor(self, color):
        self.color = color

    def setDiscovery(self, time):
        self.discovery = time

    def setFinish(self, time):
        self.finish = time


if __name__ == "__main__":
    v = Vertex("a")
    v.addNeighbor(Vertex("b"))
    v.addNeighbor(Vertex("c"))
    print(v.connectTo)

