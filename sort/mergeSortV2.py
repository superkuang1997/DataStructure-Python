def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        alist.clear()
        while lefthalf and righthalf:
            if lefthalf[0] < righthalf[0]:
                alist.append(lefthalf.pop(0))
            else:
                alist.append(righthalf.pop(0))
        alist.extend(righthalf if righthalf else lefthalf)