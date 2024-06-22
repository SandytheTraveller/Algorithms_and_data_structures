def sum_of_numbers(items):
    if len(items) == 0:
        return 0
    else:
        return items[0] + sum_of_numbers(items[1:])

items = [1, 3, 5, 7, 9]
print(sum_of_numbers(items))


def listsum(numList):
    theSum = 0
    for num in numList:
        theSum += num
    return theSum


print(listsum([1,3,5,7,9]))