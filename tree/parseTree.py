import operator
from linearTable.stack import Stack
from tree.binaryTreeV2 import BinaryTree


def buildParseTree(expr):
    exprlist = expr.split()
    stack = Stack()
    tree = BinaryTree('')
    stack.push(tree)
    currentTree = tree
    for i in exprlist:
        if i == '(':
            currentTree.insertLeft('')
            stack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = stack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            stack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = stack.pop()
        else:
            raise ValueError
    return tree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub,
             '*': operator.mul, '/': operator.truediv}
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()
    if left and right:
        fn = opers.get(parseTree.getRootVal())
        return fn(evaluate(left), evaluate(right))
    else:
        return parseTree.getRootVal()


def printExep(tree):
    sVal = ''
    if tree:
        if tree.getLeftChild() and tree.getRightChild():
            sVal = '(' + printExep(tree.getLeftChild())
        else:
            sVal = printExep(tree.getLeftChild())

        sVal = sVal + str(tree.getRootVal())

        if tree.getLeftChild() and tree.getRightChild():
            sVal = sVal + printExep(tree.getRightChild()) + ')'
        else:
            sVal = sVal + printExep(tree.getRightChild())

    return sVal


expr = "( ( 3 + 2 ) * ( 1 + 6 ) )"
parseTree = buildParseTree(expr)
print(evaluate(parseTree))
print(printExep(parseTree))
parseTree.postorder(parseTree)
