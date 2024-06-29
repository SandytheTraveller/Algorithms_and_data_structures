# Check if a given list of numbers represents a max-heap or not
#


# Returns true if the array is a max-heap
def _isMaxHeap(arr):
    n = len(arr)
    arr.insert(0, 0) # add zero at the beginning to simplify the index computation

    # check all nodes
    for i in range(1, n):
        # if left child is greater return false
        if 2 * i <= n and arr[2 * i] > arr[i]:
            return False
        # if right child is greater return false
        if 2 * i + 1 <= n and arr[2 * i + 1] > arr[i]:
            return False
    return True

# optimized version with less iteratios and no addition of an initial zero
def isMax_optimized(arr):
    n = len(arr)
    # check all the nodes
    # we can stop the loop in the middle of the list
    # since after that point the nodes are all leaves
    for i in range(1, n//2):
        # if left child is greater, return false
        if arr[2 * i + 1] > arr[i]:
            return False
        # if right child is greater, return false
        if arr[2 * i + 2] > arr[i]:
            return False
    return True


def isMaxHeap(arr):
    if isMax_optimized(arr):
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