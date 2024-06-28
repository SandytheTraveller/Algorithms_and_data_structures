def heapify(aList, size, i):
    # Find largest among root and children
    largest = i
    l = 2 * i
    r = 2 * i + 1
    if l <= size and aList[i] < aList[l]:
        largest = l
    if r <= size and aList[largest] < aList[r]:
        largest = r
    # If root is not largest, swap with largest and continue heapify
    if largest != i:
        aList[i], aList[largest] = aList[largest], aList[i]
        heapify(aList, size, largest)

def heapSort(aList):
    size = len(aList)
    # insert a zero at the beginning to simplify the index computation
    aList.insert(0, 0)
    i = size // 2
    # Step 1: Create the max heap
    while i > 0:
        heapify(aList, size, i)
        i = i - 1
    while size > 1:
        # Step 2: place in position the current max element
        aList[1], aList[size] = aList[size], aList[1]
        size = size - 1
        # Step 3, heapify, the remaining elements
        heapify(aList, size, 1)
    # remove the initial zero
    aList.pop(0)