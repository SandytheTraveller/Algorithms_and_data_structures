# Given a BST and a number K, return the node in the BST that is closest to K,
# i.e. the node with the minimum absolute difference with K.
#
# E.g.
# Given the following BST and k=7 the closest node is 5, since |7-5| = 2 is the minimum difference
#
#           15
#         /    \
#       10     20
#      /  \      \
#    5    12      25
#


#
# WARNING: DO NOT MODIFY THE FOLLOWING LINES!
#
# BST Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Basic BST implementation
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
            if node.left is None:
                node.left = Node(key)
            else:
                self._addNode(node.left, key)

        if key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._addNode(node.right, key)

#
# DO NOT MODIFY THE PREVIOUS LINES!
#


# YOU CAN MODIFY THE FOLLOWING FUNCTION IN ANY WAY
# YOU CAN ADD ADDITIONAL FUNCTIONS IF NEEDED
def getClosestValue(bst, val):
    if bst is None:
        return 0

    if bst.root.key == val:
        return val


# Test Code
if __name__ == '__main__':

    # Sample BST
    bst1 = BST()
    bst1.add(15)
    bst1.add(10)
    bst1.add(20)
    bst1.add(5)
    bst1.add(12)
    bst1.add(25)

    # VALUES TO TEST
    k = 7  # expected result 5
    print(getClosestValue(bst1, k))

    k = 14  # expected result 15
    print(getClosestValue(bst1, k))

    k = 20  # expected result 20
    print(getClosestValue(bst1, k))

    N = 13  # expected result 12
    print(getClosestValue(bst1.root, N))

    N = 18  # expected result 19
    print(getClosestValue(bst1.root, N))
