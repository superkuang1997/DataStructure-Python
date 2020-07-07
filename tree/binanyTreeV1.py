""" 顺序表实现二叉树 """


class BinaryTree:

    def __init__(self, r):
        self.root = [r, [], []]

    def insertLeft(self, newBranch):
        t = self.root.pop(1)
        if len(t) > 1:  # root存在子树
            self.root.insert(1, [newBranch, t, []])
        else:
            self.root.insert(1, [newBranch, [], []])

    def insertRight(self, newBranch):
        t = self.root.pop(2)
        if len(t) > 1:  # root存在子树
            self.root.insert(2, [newBranch, [], t])
        else:
            self.root.insert(2, [newBranch, [], []])

    def getRootVal(self):
        return self.root[0]

    def setRootVal(self, val):
        self.root[0] = val

    def getLeftChild(self):
        return self.root[1]

    def getRightChild(self):
        return self.root[2]
