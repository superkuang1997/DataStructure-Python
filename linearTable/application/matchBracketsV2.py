from linearTable.stack import Stack


def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol in '{([':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balance = False
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False


def match(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


parChecker('{[{}[]]}')