class BinHeap:
    def __init__(self):
        # Binary Heap initialized with the first element set at 0
        self.heapList = [0]
        self.currentSize = 0

    def buildHeap(self, alist):
        # heapify the input list
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]

        while i > 0:
            # self.heapify(i)
            self.percDown(i)
            i -= 1

    # iterative heapify down
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    # auxiliary method to find the index of the min child
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1


    # This method heapify up
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]

                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        # self.heapify(1)
        self.percDown(1)
        return retval

