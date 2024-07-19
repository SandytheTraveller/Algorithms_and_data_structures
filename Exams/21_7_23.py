# SURNAME:             NAME:            STUDENT ID NUMBER:             PC NUMBER:

# Given a BST and a number K, return the path from the root to the node K as a list of numbers.
# Return instead NONE if the node is not present in the BST
#
# NOTE: You can use a Stack or a Queue but it is not mandatory
#
# E.g.
#               50                      K = 55 -> [50, 60, 55]
# 	        /       \                   k = 20 -> [50, 18, 25, 20]
# 	      18 	     60                 K = 50 -> [50]
#  	    /   \      /    \               K = 75 -> NONE
#      11    25   55     80
#     /     /       \
#    3     20        57
#


import sys
sys.path.append("..")


#
# DO NOT MODIFY THE FOLLOWING LINES!
#
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._addNode(self.root, key)

    def _addNode(self, node, key):
        if key < node.key:
            if node.leftChild is None:
                node.leftChild = Node(key)
            else:
                self._addNode(node.leftChild, key)

        if key > node.key:
            if node.rightChild is None:
                node.rightChild = Node(key)
            else:
                self._addNode(node.rightChild, key)
#
# DO NOT MODIFY THE PREVIOUS LINES!
#


# YOU CAN MODIFY THE FOLLOWING FUNCTION IN ANY WAY
# YOU CAN ADD ADDITIONAL FUNCTIONS IF NEEDED
def getPath(root, k):
    if root is None:
        return None

    path = []
    current = root

    while current is not None:
        path.append(current.key)

        if current.key == k:
            return path
        elif current.key < k:
            current = current.rightChild
        else:
            current = current.leftChild

    return None


# Test code
if __name__ == '__main__':
    bst1 = BST()
    bst1.add(50)
    bst1.add(18)
    bst1.add(11)
    bst1.add(3)
    bst1.add(25)
    bst1.add(20)
    bst1.add(60)
    bst1.add(55)
    bst1.add(57)
    bst1.add(80)

    k = 55  # Expected result [50, 60, 55]
    print(getPath(bst1.root, k))

    k = 20  # Expected result [50, 18, 25, 20]
    print(getPath(bst1.root, k))

    k = 50  # Expected result [50]
    print(getPath(bst1.root, k))

    k = 75  # Expected result NONE
    print(getPath(bst1.root, k))
