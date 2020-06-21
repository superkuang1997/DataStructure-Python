from node import Node


class UnorderList():
    def __init__(self):
        self.head = None   # head表示表头，表示对第一个节点的引用信息

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:  # 计算复杂度为O(n)
            current = current.getNext()
            count += 1
        return count

    def append(self, item):
        current = self.head
        if current == None:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp
        else:
            after = self.head.getNext()
            while after != None:
                current = current.getNext()
                after = current.getNext()
            temp = Node(item)
            current.setNext(temp)
            temp.setNext(None)

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count += 1
        if current == None:
            raise IndexError("{0} is not in list".format(item))
        return count

    def insert(self, pos, item):
        current = self.head
        if pos != 0:
            for i in range(pos-1):
                current = current.getNext()
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)

        elif pos == 0:
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp

    def pop(self, pos=-1):
        current = self.head
        if pos < 0:  # 负向索引转正向索引
            pos = self.size() + pos
        if pos > self.size() - 1:  # 判断是否超出索引范围
            raise IndexError("list index out of range")
        if pos != 0:
            for i in range(pos):
                previous = current
                current = current.getNext()
            previous.setNext(current.getNext())
            return current.getData()
        else:
            self.head = current.getNext()
            return current.getData()

    def display(self):
        val = []
        current = self.head
        while current != None:
            val.append(current.getData())
            current = current.getNext()
        return val