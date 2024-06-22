def printMovement(n, source, destination):
    print("Move disk", n, "from rod", source, "to rod", destination)

def towers_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        printMovement(1, source, destination)
        return
    else:
        towers_of_hanoi(n - 1, source, auxiliary, destination)
        printMovement(n, source, destination)
        towers_of_hanoi(n - 1, auxiliary, destination, source)


n = 5
towers_of_hanoi(n, 'A', 'C', 'B')