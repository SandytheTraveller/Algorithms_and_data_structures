# function to recursively divide the array
def merge_sort(alist):
    if len(alist) > 1:
        middle = len(alist) // 2
        left = alist[:middle]
        right = alist[middle:]

        merge_sort(left)
        merge_sort(right)
        merge(alist, left, right)


# function to merge the array
def merge(alist, left, right):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            alist[k] = left[i]
            i += 1
        else:
            alist[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        alist[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        alist[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    alist = [26, 54, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(alist)
    print(alist)