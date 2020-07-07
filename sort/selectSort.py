def selectionSort(alist):
    passnum = len(alist) - 1  # 替换位置
    while passnum > 0:
        exchange = False
        positionOfMax = 0
        for i in range(1, passnum+1):
            if alist[i] > alist[positionOfMax]:
                positionOfMax = i
        alist[positionOfMax], alist[passnum] = alist[passnum], alist[positionOfMax]
        passnum -= 1