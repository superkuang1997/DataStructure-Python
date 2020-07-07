def shellSort(alist):
    sublist_num = len(alist) // 2
    while sublist_num > 0:
        for start_position in range(sublistcount):
            gapInsertionSort(alist, start_position, sublist_num)
        sublistcount //= 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[index]
        position = index
        while position >= gap and alist[position-gap] > current_value:
            alist[position] = alist[position - gap]
            position -= gap
        alist[position] = current_value