# Reverse the content of a Queue using Recursion
# You can use only one Queue, no other data structures are needed
# You cannot use any iterative loop
import sys
sys.path.append("..")
from queue import Queue

def reverseQueue(q):
    if q.isEmpty():
        return
    else:
        el = q.dequeue()
        reverseQueue(q)
        q.enqueue(el)


if __name__ == "__main__":
    q = Queue()

    for i in range(1, 10):
        q.enqueue(i) # [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(q.items)
    reverseQueue(q)
    print(q.items)