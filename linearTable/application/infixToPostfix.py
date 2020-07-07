from linearTable.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTWVUXYZ" or token in "1234567890":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            top_token = opStack.pop()
            while top_token != '(':
                postfixList.append(top_token)
                top_token = opStack.pop()
        else:
            while (not opStack.isEmpty) and (prec[opStack.peek() >= prec[token]]):
                tokenList.append(opStack.pop())  # 如果栈顶有操作符优先级高，弹出并加入postfixList
            opStack.push(token)
    return "".join(postfixList)
infixToPostfix("( ( A  +  ( B * C ) ) + D )")