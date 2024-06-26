class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

class UnOrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        size = 0
        current = self.head
        while current != None:
            size += 1
            current = current.getNext()

        return size

    def add(self, elem):
        newElement = Node(elem)
        newElement.setNext(self.head)
        self.head = newElement

    def search(self, item):
        current = self.head
        found = False
        while current != None:
            if current.getData() != item:
                current = current.getNext()
            else:
                found = True
        return found