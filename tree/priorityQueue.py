"""
优先队列
"""


class PriorityQueue:

    def __init__(self):
        self.headArray = [(0, 0)]  # 占位
        self.currentSize = 0

    def insert(self, item):
        self.headArray.append(item)
        self.currentSize += 1
        self.perUp(self.currentSize)

    def perUp(self, i):
        while i // 2 > 0:  # i为1时结束循环
            if self.headArray[i][0] < self.headArray[i // 2][0]:
                temp = self.headArray[i // 2]
                self.headArray[i // 2] = self.headArray[i]
                self.headArray[i] = temp
            i = i // 2

    def delMin(self):
        Min = self.headArray[1]
        self.headArray[1] = self.headArray[self.currentSize]  # 用队尾节点替换队首节点
        self.currentSize -= 1
        self.headArray.pop()
        self.perDown(1)  # 下沉操作
        return Min

    def perDown(self, i):
        while (i * 2) <= self.currentSize:  # 如果至少有一个子节点(左)，即不是叶节点
            mc = self.minChild(i)  # 子节点中较小的一个
            if self.headArray[i][0] > self.headArray[mc][0]:
                temp = self.headArray[i]
                self.headArray[i] = self.headArray[mc]
                self.headArray[mc] = temp
            i = mc

    def minChild(self, i):
        """
        :param i: 当前节点序号
        :return: 子节点中较小节点的序号
        """
        if i * 2 + 1 > self.currentSize:  # 只有唯一的左子节点
            return i * 2
        else:  # 有两个子节点则为较小的一个
            if self.headArray[i * 2][0] < self.headArray[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        """ 根据无序表生成堆
        """
        i = len(alist) // 2  # 最后一个节点的父节点
        self.currentSize = len(alist)
        self.headArray = [(0, 0)] + alist
        while i > 0:
            self.perDown(i)
            i -= 1

    def isEmpty(self):
        return self.currentSize == 0

    def rearrange(self, key, val):
        done = False
        find = 0
        i = 1
        while not done and i <= self.currentSize:
            if self.headArray[i][1] == key:
                done = True
                find = i
            else:
                i += 1
        if find:
            self.headArray[find] = (val, key)
            self.perUp(find)

    def search(self, key):
        for item in self.headArray:
            if key == item[1]:
                return True
        return False

    def __contains__(self, item):
        return self.search(item)


if __name__ == "__main__":
    bh = PriorityQueue()
    bh.buildHeap([(1, "a"), (3, "c"), (2, "b"), (-5, "d")])
    bh.rearrange("b",-10)

    while not bh.isEmpty():
        print(bh.delMin())
