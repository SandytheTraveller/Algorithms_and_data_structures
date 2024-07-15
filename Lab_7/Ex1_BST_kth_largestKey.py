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
from stack import Stack

# iterative solution
def get_kthLargest(root, k):
    if root is None:
        return

    current = root
    st = Stack()

    index = 0

    while not st.isEmpty() or current is not None:
        if current is not None:
            st.push(current)
            current = current.rightChild

        elif not st.isEmpty():
            current = st.pop()
            index += 1

            if index == k:
                return current.key, current.value
            current = current.leftChild


# recursive solution using an inverted inorder traversal
def __kthLargest(root, k, c):
    if root is None or c[0] >= k:
        return
    right = __kthLargest(root.rightChild, k, c)

    c[0] += 1
    if c[0] == k:
        return root.key, root.value

    left = __kthLargest(root.leftChild, k, c)

    return left or right

def get__kthLargest(root, k):
    # we use a list of one element as a counter instead of a variable
    # to avoid unwanted wrong increments during recursion
    c = [0]
    return __kthLargest(root, k, c)

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
