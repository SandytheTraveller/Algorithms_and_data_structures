from stack import Stack

class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rigthChild = None

def buildParseTree(fpexp):
    fplist = fpexp.split()

    # we use stack to keep track of the previous positions in the tree
    pStack = Stack()
    eTree = Node('')  # initialize the tree with an empty node
    pStack.push(eTree)
    currentTree = eTree

    for el in fplist:
        if el == '(':
            # rule 1
            currentTree.leftChild = Node('')
            pStack.push(currentTree)
            currentTree = currentTree.leftChild
        # rule 2
        elif el in ['+', '-', '*', '/']:
            currentTree.key = el
            currentTree.rightChild = Node('')
            pStack.push(currentTree)
            currentTree = currentTree.rightChild
        # rule 4
        elif el == ')':
            currentTree = pStack.pop()
        else:
            try:
                # rule 3
                currentTree.key = int(el)
                parent = pStack.pop()
                currentTree = parent
            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(el))
    return eTree

def postorderEvaluation(node):
    opers = {'+': operator.add,'-': operator.sub,'*': operator.mul, '/': operator.truediv}

    if node:
        res1 = postorderEvaluation(node.leftChild)
    res2 = postorderEvaluation(node.rightChild)
    if res1 and res2:
        return opers[node.key](res1, res2)
    else:
        return node.key

def inorderPrintexp(node):
    sVal = ""
    if node:
        sVal = '(' + inorderPrintexp(node.leftChild)
        sVal = sVal + str(node.key)
        sVal = sVal + inorderPrintexp(node.rightChild) + ')'
    return sVal