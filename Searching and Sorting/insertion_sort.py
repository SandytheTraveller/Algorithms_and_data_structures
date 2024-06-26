# Python style implementation
def swapPython(A, x, y):
    A[x], A[y] = A[y], A[x]

def insertion_sort(alist):
    # execution starts at index 1 since we assume that the first element
    # is already in order
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        # shift of the elements in the sorted sub-list until the
        # correct position for the new elements is found
        while position > 0 and alist[position - 1] > current_value:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = current_value

if __name__ == '__main__':
    alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(alist)
    print(alist)