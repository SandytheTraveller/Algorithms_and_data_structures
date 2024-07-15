class Stack:
    def __init__(self):
        self.elements = []

    # check if the stack is empty
    def isEmpty(self):
        return True if self.elements == [] else False

    # insert an element
    def push(self, item):
        self.elements.append(item)

    # remove and return the last element
    def pop(self):
        return self.elements.pop()

    # return the last element, but do not remove it
    def peak(self):
        if len(self.items) > 0:
            return self.items[-1]

    # return the size of the stack
    def size(self):
        return len(self.elements)
