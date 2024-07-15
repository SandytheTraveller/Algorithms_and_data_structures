# method implementing level order traversal
from queue import Queue
def levelOrder(root):
    if root is None:
        return True

    q = Queue()
    q.enqueue(root)

    while q.size() > 0:
        current = q.dequeue()
        print(current.key)

        if current.leftChild is not None:
            q.enqueue(current.leftChild)
        if current.rightChild is not None:
            q.enqueue(current.rightChild)