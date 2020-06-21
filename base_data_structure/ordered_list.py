from node import Node

class OrderedList():
    def __init__(self):
        self.head = None   # head表示表头，表示对第一个节点的引用信息

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True  # found
            else:
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        current = self.head
        previous = None
        stop = False  # 找到大于item的值
        found = False  # 找到等于item的值
        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        stop = False
        found = False
        while current != None and not stop and not found:
            if current.getData() == item:
                found = True
                if previous == None:  # 如果移除的是第一个
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())

            else:
                if current.getData() > item:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()

    def size(self):
        current = self.head
        count = 0
        while current != None:
            current = current.getNext()
            count += 1
        return count

    def isEmpty(self):
        return self.head == None

    def index(self, item):
        current = self.head
        found = False
        stop = False
        count = 0
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item or current.getNext() == None:
                    stop = True
                else:
                    current = current.getNext()
                    count += 1
        if stop:
            raise IndexError("{0} is not in list".format(item))
        return count

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


# In[93]:


o = OrderedList()


# In[97]:


o.add(2)
o.add(4)
o.add(7)


# In[95]:


o.size()


# In[100]:


o.display()


# In[99]:


o.pop(0)


# In[82]:


o.pop(-1)


# In[28]:


o.pop()

