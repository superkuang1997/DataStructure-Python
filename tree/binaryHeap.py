"""
二叉堆在逻辑上通过树实现，实际上是通过列表实现
实现二叉堆的列表符合堆次序，但并不是有序表
通过下沉操作，每次出队的值时都可以实现有序
"""


class BinaryHeap:

    def __init__(self):
        self.headList = [0]  # 二叉堆列表中下标为0的项仅作占位
        self.currentSize = 0

    def insert(self, item):
        self.headList.append(item)
        self.currentSize += 1
        self.perUp(self.currentSize)

    def perUp(self, i):
        while i // 2 > 0:  # i为1时结束循环
            if self.headList[i] < self.headList[i // 2]:
                temp = self.headList[i // 2]
                self.headList[i // 2] = self.headList[i]
                self.headList[i] = temp
            i = i // 2

    def delMin(self):
        Min = self.headList[1]
        self.headList[1] = self.headList[self.currentSize]  # 用队尾节点替换队首节点
        self.currentSize -= 1
        self.headList.pop()
        self.perDown(1)  # 下沉操作
        return Min

    def perDown(self, i):
        while (i * 2) <= self.currentSize:  # 如果至少有一个子节点，即不是叶节点
            mc = self.minChild(i)  # 子节点中较小的一个
            if self.headList[i] > self.headList[mc]:
                temp = self.headList[i]
                self.headList[i] = self.headList[mc]
                self.headList[mc] = temp
            i = mc

    def minChild(self, i):
        """
        :param i: 当前节点序号
        :return: 子节点中较小节点的序号
        """
        if i * 2 + 1 > self.currentSize:  # 只有唯一的左子节点
            return i * 2
        else:  # 有两个子节点则为较小的一个
            if self.headList[i * 2] < self.headList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        """ 根据无序表生成堆
        """
        i = len(alist) // 2  # 最后一个节点的父节点
        self.currentSize = len(alist)
        self.headList = [0] + alist
        while i > 0:
            self.perDown(i)
            i -= 1

    def isEmpty(self):
        return self.currentSize == 0


if __name__ == "__main__":
    bh = BinaryHeap()
    bh.buildHeap([5, 8, 1, 4, 8, 9, 18, 27])
    print(bh.headList, bh.currentSize)
    bh.insert(6)
    print(bh.headList, bh.currentSize)

    # 顺序出队
    size = bh.currentSize
    for i in range(size):
        if i != size - 1:
            print(bh.delMin(), end=" -> ")
        else:
            print(bh.delMin(), end="")
