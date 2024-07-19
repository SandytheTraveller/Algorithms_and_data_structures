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

import sys
from stack import Stack

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
# Solution 1, binary search using preorder traversal
def getClosestValue(root, val):
    if root.key == val:
        return val

    # the first element keeps track of the current min difference,
    # the second is the closest value in the tree
    res = [sys.maxsize, None]

    return _getClosestValue_preorder(root, val, res)


# Recursive auxiliary method for Solution 1
def _getClosestValue_preorder(root, val, res):

    if root is None:
        return res[1]

    if root.key == val:
        return root.key

    diff = abs(root.key - val)

    if diff < res[0]:
        res[0] = diff
        res[1] = root.key

    # Traverse the tree exploiting the properties of a BST
    if val < root.key:
        return _getClosestValue_preorder(root.left, val, res)
    else:
        return _getClosestValue_preorder(root.right, val, res)

# Solution 2, iterative implementation of Solution 1, using a Stack
def getClosestValue_iterative(root, val):
    if root is None:
        return

    if root.key == val:
        return val

    st = Stack()
    st.push(root)

    min_diff = sys.maxsize
    closest_val = None

    while not st.isEmpty():
        current = st.pop()
        current_val = current.key

        if current_val == val:
            return val

        diff = abs(current_val - val)

        if diff < min_diff:
            min_diff = diff
            closest_val = current_val

        # Traverse the tree exploiting the properties of a BST
        if val < current_val and current.left:
            st.push(current.left)
        elif val > current_val and current.right:
            st.push(current.right)

    return closest_val

# Solution 3, using a modified in-order traversal exploiting the property of a BST
def getClosestValue_inorder(root, val):
    if root.key == val:
        return val

    # the first list keeps track of the current min difference,
    # the second is the closest value in the tree
    min_diff = [sys.maxsize]
    closest_val = [None]
    return _getClosestValue_inorder(root, val, min_diff, closest_val)


def _getClosestValue_inorder(root, val, min_diff, closest_val):
    if root is None:
        return

    left = _getClosestValue_inorder(root.left, val, min_diff, closest_val)

    if root.key == val:
        return val

    diff = abs(root.key - val)

    if diff < min_diff[0]:
        min_diff[0] = diff
        closest_val[0] = root.key
    else:
        return closest_val[0]

    right = _getClosestValue_inorder(root.right, val, min_diff, closest_val)

    return left or right


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
    print(getClosestValue_inorder(bst1.root, k))

    k = 14  # expected result 15
    print(getClosestValue_inorder(bst1.root, k))

    k = 20  # expected result 20
    print(getClosestValue_inorder(bst1.root, k))

    N = 13  # expected result 12
    print(getClosestValue_inorder(bst1.root, N))

    N = 18  # expected result 20
    print(getClosestValue_inorder(bst1.root, N))
