# Given a BST and a number k find the node with the  k'th largest key and return its content (key, value)
# E.g. With the following tree if k=1 the node is 22, since it is the largest key
#                              if k=2 the node is 12, since it is the second largest key
#      10
#     /  \
#    8 	  12
#   / \     \
#  3   9    22
#

from BST import BST


def get_kthLargest(root, k):
    #
    # TODO
    #
    pass


if __name__ == "__main__":

    myTree = BST()
    myTree[10] = "A"
    myTree[8] = "B"
    myTree[12] = "C"
    myTree[3] = "D"
    myTree[9] = "E"
    myTree[22] = "F"

    k = 1  # expected result 22, F
    print(get_kthLargest(myTree.root, k))

    k = 2  # expected result 12, C
    print(get_kthLargest(myTree.root, k))
