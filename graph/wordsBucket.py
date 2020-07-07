from graph import Graph


def createBucket(file):
    d = {}
    graph = Graph()
    with open(file, "r", encoding="utf-8") as f:
        words = f.readlines()
        words = [x.rstrip("\n") for x in words]  # 去除换行符\n
        for word in words:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    #  建立边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)
    return graph


if __name__ == "__main__":
    g = createBucket("fourletterwords.txt")
    print(g.getVertices())
    for vertex in g:
        for nbrv in vertex.getConnections():
            print("({0}, {1})".format(vertex.getID(), nbrv.getID()))
