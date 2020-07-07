from linearTable.stack import Stack


def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():   # 如果此时栈为空，说明右括号多了
                balance = False
            else:
                s.pop()  # 弹出栈中的左括号
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False