class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # we add a new element at the beginning of the data
    # structure, unlike in the stack
    def enqueue(self, item):
        self.items.append(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)