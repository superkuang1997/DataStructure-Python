from linearTable.stack import Stack


def postfixEval(postfixExpr):
    opStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            opStack.push(int(token))
        else:
            operand2 = opStack.pop()
            operand1 = opStack.pop()
            result = doMath(token, operand1, operand2)
            opStack.push(result)
    return opStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


postfixEval("4 2 3 + *")