# 二叉查找树是一种数据存储结构，一般情况下查找效率高于链表
from BSTtreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None  # 根节点
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:  # 小于当前节点的值，向左分支插入节点
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():  # 大于当前节点的值，向右分支插入节点
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:  # 根节点存在，则调用递归函数
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:  # 向左分支查找
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:  # 向右分支查找
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """ the first step of deletion is to get the node of key, then to delete it.
        :param key: the value of node
        :return: None
        """
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():  # 如果待删除节点右两个子节点
            succ = currentNode.findSuccessor()  # 寻找仅次于被删节点的后继节点
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.val = succ.val

        else:  # 如果待删除节点仅有一个子节点
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():  # 左左
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():  # 右左
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.leftChild.key,
                        currentNode.leftChild.val,
                        currentNode.leftChild.leftChild,
                        currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():  # 左右
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():  # 右右
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(
                        currentNode.rightChild.key,
                        currentNode.rightChild.val,
                        currentNode.rightChild.leftChild,
                        currentNode.rightChild.rightChild)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put('a', 1)
    bst.put('b', 3)
    bst.put('c', 2)
    bst.put('d', 7)
    bst.put('e', 8)

    print(bst['d'])
    del bst['d']
    print(bst['d'])




