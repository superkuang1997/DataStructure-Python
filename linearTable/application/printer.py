import random
from linearTable.queue_ import Queue


class Printer():
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = (newTask.getPages() * 60) / self.pagerate


class Task():
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():  # 如果产生了新的打印需求
            task = Task(currentSecond)  # 传入当前时间
            printQueue.enqueue(task)  # 加入队列

        if (not labprinter.busy()) and (
                not printQueue.isEmpty()):  # 打印机空闲且打印队列不为空
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print(waitingtimes)
    print(averageWait, printQueue.size())


simulation(3600, 5)
