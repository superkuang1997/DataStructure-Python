""" 单链表实现二叉树 """


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild  # 先插入的数据置于底层
            self.rightChild = temp  # 后插入的数据置于顶层

    def getRootVal(self):
        return self.root

    def setRootVal(self, val):
        self.root = val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def preorder(self, tree):
        """ go through the tree from root vertex to left leaf vertex,
            then to right leaf vertex.
        """
        if tree:
            print(tree.getRootVal())
            self.preorder(tree.getLeftChild())
            self.preorder(tree.getRightChild())

    def inorder(self, tree):
        """ go through the tree from left leaf vertex to root
            then to right leaf vertex.
        """
        if tree:
            self.inorder(tree.getLeftChild())
            print(tree.getRootVal())
            self.inorder(tree.getRightChild())

    def postorder(self, tree):
        """ go through the tree from left leaf vertex to right leaf vertex
            then to root.
        """
        if tree:
            self.postorder(tree.getLeftChild())
            self.postorder(tree.getRightChild())
            print(tree.getRootVal())
