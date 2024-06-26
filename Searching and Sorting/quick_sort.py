def quick_sort(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)
        quick_sort(alist, first, split_point - 1)
        quick_sort(alist, split_point + 1, last)


def partition(alist, first, last):
    pivotValue = alist[first] # choice of the pivot value
    left = first + 1
    right = last

    done = False
    while not done:
        while left <= right and alist[left] <= pivotValue:
            left += 1

        while alist[right] >= pivotValue and right >= left:
            right -= 1

        # loop until right mark reaches the split point
        if right < left:
            done = True
        else:
            alist[left], alist[right] = alist[right], alist[left]

    # move the current pivot value in the split point
    alist[first], alist[right] = alist[right], alist[first]

    return right


if __name__ == '__main__':
    alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist) - 1)
    print(alist)
