# NAME:                 SURNAME:
#
# Given a binary Tree and the two nodes A and B determine whether A and B are siblings or not
#
# E.g.
#              35                     A=2 and B=12 are siblings
# 	        /      \                  A=40 and B=7 are siblings
# 	      18 	   10                 A=7 and B=21 are NOT siblings
#  	    /   \     /   \               A=18 and B=1 are NOT siblings
#      3     5   7    40
#    /  \            /   \
#   2   12         21     1
#

import sys
sys.path.append("..")


class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None


def areSiblings(root, nodeA, nodeB):
    if root is None or nodeA is None or nodeB is None:
        return False

    left_key = 0
    right_key = 0

    if root.leftChild:
        left_key = root.leftChild.key
    if root.rightChild:
        right_key = root.rightChild.key

    return (left_key == nodeA and right_key == nodeB) or (left_key == nodeB and right_key == nodeA) or areSiblings(root.leftChild, nodeA, nodeB) or areSiblings(root.rightChild, nodeA, nodeB)


# Test code
if __name__ == '__main__':
    root1 = Node(35)
    root1.leftChild = Node(18)
    root1.leftChild.leftChild = Node(3)
    root1.leftChild.leftChild.leftChild = Node(2)
    root1.leftChild.leftChild.rightChild = Node(12)
    root1.leftChild.rightChild = Node(5)
    root1.rightChild = Node(10)
    root1.rightChild.leftChild = Node(7)
    root1.rightChild.rightChild = Node(40)
    root1.rightChild.rightChild.leftChild = Node(21)
    root1.rightChild.rightChild.rightChild = Node(1)

    print(areSiblings(root1, 2, 12))  # Expected result: TRUE
    print(areSiblings(root1, 40, 7))  # Expected result: TRUE
    print(areSiblings(root1, 7, 21))  # Expected result: FALSE
    print(areSiblings(root1, 18, 1))  # Expected result: FALSE