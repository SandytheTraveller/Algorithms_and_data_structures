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


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    # adding a new element at the beginning of the list
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head

        while current is not None:
            if current.getData() == item:
                return True
            else:
                if current.getData() > item:
                    return False
                else:
                    current = current.getNext()
        return False

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count
