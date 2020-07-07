# access the Palindromes(回文词)

from linearTable.deque import Deque


def palchecker(aString):
    stringDeque = Deque()
    for ch in aString:
        stringDeque.addFront(ch)
    balance = True
    while stringDeque.size() > 1 and balance:
        first = stringDeque.removeRear()
        last = stringDeque.removeFront()
        if first != last:
            balance = False
    return balance


palchecker('abadaba')