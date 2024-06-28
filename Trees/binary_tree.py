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

def preorder(root):
    if root:
        print(root.key)
        preorder(root.leftChild)
        preorder(root.rightChild)


def inorder(root):
    if root:
        inorder(root.leftChild)
        print(root.key)
        inorder(root.rightChild)

def postorder(root):
    if root:
        postorder(root.leftChild)
        postorder(root.rightChild)
        print(root.key)

def iterativePreorder(root):
    if root is None:
        return

    st = Stack()
    st.push(root)

    while not st.isEmpty():
        current = st.pop()
        print(current.key)
        if current.rightChild is not None:
            st.push(current.rightChild)
        if current.leftCHild is not None:
            st.push(current.leftChild)

def iterativeInorder(root):
    if root is None:
        return

    st = Stack()
    current = root

    while not st.isEmpty() or current is not None:
        if current is not None:
            st.push(current)
            current = current.leftChild
        elif not st.isEmpty():
            current = st.pop()
            print(current.key)
            current = current.rightChild


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

def levelOrder(root):
    if root is None:
        return

    q = Queue()
    q.enqueue(root)

    while q.size() > 0:
        # at each iteration, dequeue the current
        # node and enqueue its children, if present
        currentNode = q.dequeue()
        print(currentNode.key)

        if currentNode.leftChild is not None:
            q.enqueue(currentNode.leftChild)
        if currentNode.rightChild is not None:
            q.enqueue(currentNode.rightChild)

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