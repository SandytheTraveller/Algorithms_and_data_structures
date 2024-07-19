from stack import Stack
from binary_tree import Node

def inorder(root):
    if root is None:
        return -1

    s = Stack()
    current = root

    while current or s.size() > 0:
        if current:
            s.push(current)
            current = current.leftChild
        else:
            s.pop()
            print(current.key)
            current = current.rightChild


if __name__ == "__main__":
    root = Node("A")
    root.leftChild = Node("B")
    root.leftChild.leftChild = Node("D")
    root.leftChild.rightChild = Node("E")
    root.rightChild = Node("C")
    root.rightChild.leftChild = Node("F")

    inorder(root)