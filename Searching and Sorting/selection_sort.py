# Python style implementation
def swapPython(A, x, y):
    A[x], A[y] = A[y], A[x]


def selection_sort(alist):
    for i in range(len(alist) - 1):
        positionOfMax = 0

        # search for the right position for the current
        # element before the swap
        for j in range(len(alist) - i):
            if alist[j] > alist[positionOfMax]:
                positionOfMax = j

        # at most one swap at each pass
        swapPython(alist, j, positionOfMax)

if __name__ == '__main__':
    alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(alist)
    print(alist)