class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # the Stack is initialised as an empty linked list,
        # so head is equal to None
        self.head = None

    # to check if the Stack is empty,
    # we can simply check if the head of the linked list is None
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # to get the size of the Stack we need
    # to traverse all the linked list and count the nodes
    def size(self):
        count = 0
        if not self.isEmpty():
            currentNode = self.head
            while currentNode is not None:
                count += 1
                currentNode = currentNode.next
        return count

    # push is equivalent to adding an
    # item at the head of the Linked list
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # pop is equivalent to removing the current head of the linked list
    # and set the next node as new head
    def pop(self):
        if self.isEmpty():
            return None
        else:
            head_node = self.head
            self.head = self.head.next
            head_node.next = None
            return head_node.data

    # peek is equivalent to reading the
    # head of the Linked list
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data