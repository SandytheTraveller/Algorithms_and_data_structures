# Check if a binary tree is complete or not
#
# E.g.:
#               A              TRUE
#            /     \
#          B        C
#        /   \     /  \
#       D    E    F    G
#     /  \
#    H    I
#
#               A              FALSE
#            /     \
#          B        C
#        /   \       \
#       D    E        G
#
#
#               A              FALSE
#            /     \
#          B        C
#        /   \
#       D    E
#     /  \
#    H    I
#
#               A              FALSE
#            /     \
#          B        C
#        /   \
#       D    E
#          /
#         I
#
#               A              TRUE
#            /     \
#          B        C
#        /   \     /
#       D    E    F
#

from queue import Queue

class Node:
    # WARNING: DO NOT MODIFY THIS INITIALIZATION METHOD!
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


# recursive solution
def verifyComplete(root):
    return __verifyComplete_recursive(root, 0, countNodes(root))

# auxiliary function to count the number of nodes in the tree
def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.leftChild) + countNodes(root.rightChild)

# auxiliary method using indexes as in binary heap
def __verifyComplete_recursive(root, i, numNodes):
    if root is None: # if tree is empty
        return True

    if i >= numNodes:
        return False

    return(__verifyComplete_recursive(root.leftChild, 2 * i + 1, numNodes) and
           __verifyComplete_recursive(root.rightChild, 2 * i + 2, numNodes))

# Solution using level order traversal
def verifyComplete_levorder(root):
    if root is None:
        return True

    q = Queue()
    q.enqueue(root)

    # this flag become true if a non-full node is encountered
    # we defined a non-full node as a node with 0 or 1 child
    nonFullNode = False

    while not q.isEmpty():
        current = q.dequeue()

        if current.leftChild:
            if nonFullNode:
                return False
            q.enqueue(current.leftChild)
        else:
            nonFullNode = True

        if current.rightChild:
            if nonFullNode:
                return False
            q.enqueue(current.rightChild)
        else:
            nonFullNode = True

    return True


# alternative shorter solution with level order traversal
def verifyComplete_levorder_alt(root):
    if root is None:
        return True

    q = Queue()
    q.enqueue(root)

    # this flag become true when a NULL node is encountered
    nullNode = False

    while not q.isEmpty():
        current = q.dequeue()

        if current is None:
            nullNode = True
        else:
            if nullNode:
                return False
            q.enqueue(current.leftChild)
            q.enqueue(current.rightChild)

    return True



# Test code
if __name__ == '__main__':

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root1 = Node("A")
    root1.leftChild = Node("B")
    root1.leftChild.leftChild = Node("D")
    root1.leftChild.leftChild.leftChild = Node("H")
    root1.leftChild.leftChild.rightChild = Node("I")
    root1.leftChild.rightChild = Node("E")
    root1.rightChild = Node("C")
    root1.rightChild.leftChild = Node("F")
    root1.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root2 = Node("A")
    root2.leftChild = Node("B")
    root2.leftChild.leftChild = Node("D")
    root2.leftChild.rightChild = Node("E")
    root2.rightChild = Node("C")
    root2.rightChild.rightChild = Node("G")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root3 = Node("A")
    root3.leftChild = Node("B")
    root3.leftChild.leftChild = Node("D")
    root3.leftChild.leftChild.leftChild = Node("H")
    root3.leftChild.leftChild.rightChild = Node("I")
    root3.leftChild.rightChild = Node("E")
    root3.rightChild = Node("C")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root4 = Node("A")
    root4.leftChild = Node("B")
    root4.leftChild.leftChild = Node("D")
    root4.leftChild.rightChild = Node("E")
    root4.leftChild.rightChild.leftChild = Node("I")
    root4.rightChild = Node("C")

    # WARNING: DO NOT MODIFY THE TREE STRUCTURE!
    root5 = Node("A")
    root5.leftChild = Node("B")
    root5.leftChild.leftChild = Node("D")
    root5.leftChild.rightChild = Node("E")
    root5.rightChild = Node("C")
    root5.rightChild.leftChild = Node("F")


    # Expected result TRUE
    print(verifyComplete(root1))

    # Expected result FALSE
    print(verifyComplete(root2))

    # Expected result FALSE
    print(verifyComplete(root3))

    # Expected result FALSE
    print(verifyComplete(root4))

    # Expected result TRUE
    print(verifyComplete(root5))

