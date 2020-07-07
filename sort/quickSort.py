def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        split_value = alist[first]
        leftmark = first + 1
        rightmark = last
        while True:
            while leftmark <= rightmark and alist[leftmark] <= split_value:
                leftmark += 1

            while leftmark <= rightmark and alist[rightmark] >= split_value:
                rightmark -= 1

            if leftmark > rightmark:
                alist[first], alist[rightmark] = alist[rightmark], alist[first]
                break
            else:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        quickSortHelper(alist, first, rightmark-1)
        quickSortHelper(alist, rightmark+1, last)
