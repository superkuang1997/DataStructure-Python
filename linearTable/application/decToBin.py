from linearTable.stack import Stack


def divideBy2(decNumber):
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber //= 2
    binString = ''
    while remStack.size()!= 0:
        binString += str(remStack.pop())
    return binString


print(divideBy2(241))