# node class
from stack import Stack
from queue import Queue


class Node:
    def __init__(self, key):
        # each node has a key and tw references to its (eventual)
        # left and right children
        self.key = key
        self.leftChild = None
        self.rightChild = None

    # when a new is inserted, it can be added as a leaf node
    # or it can go to a position already occupied, pushing down the entire subtree
    def insertLeft(self, key):
        if self.leftChild is None:
            self.leftChild = Node(key)
        else:
            t = Node(key)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, key):
        if self.leftChild is None:
            self.rightChild = Node(key)
        else:
            t = Node(key)
            t.rightChild = self.rightChild
            self.rightChild = t

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.rightChild), height(root.leftChild))

def isBalanced(root):
    if root is None:
        return True
    left_height = height(root.leftChild)
    right_height = height(root.rightChild)
    if abs(left_height - right_height) <= 1 and isBalanced(root.leftChild) and isBalanced(root.rightChild):
        return True
    return False


def postorder(root):
    if root:
        postorder(root.leftChild)
        postorder(root.rightChild)
        print(root.key)


def postorderIterative(root):
    if root is None:
        return

    st = Stack()
    current = root

    while not st.isEmpty() or current is not None:
        while current:
            if current.rightChild is not None:
                st.push(current.rightChild)
            st.push(current)
            current = current.leftChild
        current = st.pop()

        if current.rightChild is not None and st.peek() == current.rightChild:
            st.pop()
            st.push(current)
            current = current.rightChild
        else:
            print(current.key)
            current = None


def copyTree(root):
    if root is None:
        return None

    rootCopy = Node(root.key)
    rootCopy.leftChild = copyTree(root.leftChild)
    rootCopy.rightChild = copyTree(root.rightChild)

    return rootCopy

def _deleteTree(root):
    if root:
        root.leftChild = _deleteTree(root.leftChild)
        root.rightChild = _deleteTree(root.rightChild)
        del root
        return None

def deleteTree(root):
    _deleteTree(root)
    root = None
    return root

# Tree example
if __name__ == "__main__":
    root = Node("A")
    root.leftChild = Node("B")
    root.leftChild.leftChild = Node("D")
    root.leftChild.rightChild = Node("E")
    root.rightChild = Node("C")
    root.rightChild.leftChild = Node("F")