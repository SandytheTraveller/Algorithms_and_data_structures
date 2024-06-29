# Check if a given list of numbers represents a max-heap or not
#


# Returns true if the array is a max-heap
def _isMaxHeap(arr):

    # TODO

    pass


def isMaxHeap(arr):
    if _isMaxHeap(arr):
        print("Yes")
    else:
        print("No")


# Driver Code
if __name__ == '__main__':
    arr1 = [90, 36, 18, 8, 25, 7, 1]   # expected answer: YES
    isMaxHeap(arr1)

    arr2 = [90, 36, 18, 98, 25, 7, 1]  # expected answer: NO
    isMaxHeap(arr2)

    arr3 = [90, 36, 18, 8, 25, 7, 20]  # expected answer: NO
    isMaxHeap(arr3)
