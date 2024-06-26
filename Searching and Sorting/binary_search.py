def binarySearch(alist, item, left, right):
    if right < left:
        return None
    else:
        middle = (left + right) // 2

        if alist[middle] == item:
            return middle
        elif alist[middle] > item:
            return binarySearch(alist, item, left, middle - 1)
        else:
            return binarySearch(alist, item, middle + 1, right)


if __name__ == '__main__':
    alist = [5, 7, 10, 20, 35, 40, 55]
    item = 10
    print(binarySearch(alist, item, 0, len(alist) - 1))