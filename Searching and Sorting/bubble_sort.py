# standard way to swap items
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

# Python style implementation
def swapPython(A, x, y):
    A[x], A[y] = A[y], A[x]


def bubbleSort(alist):
    for i in range(0, len(alist)):
        for j in range(0, len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                swapPython(alist, j, j + 1)


# it can be modified to stop early if the array is already sorted
# best case complexity: O(n)
def shortBubbleSort(alist):
    exchanges = True

    for i in range(len(alist) - 1):
        if not exchanges:
            return
        exchanges = False

        for j in range(len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                swap(alist, j, j + 1)
                exchanges = True

if __name__ == '__main__':
    alist = [5, 12, 45, 36, 1, 5, 7]
    bubbleSort(alist)
    print(alist)