def ordered_sequence_search(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    return found


ordered_sequence_search([1, 3, 5, 8, 12, 18], 6)