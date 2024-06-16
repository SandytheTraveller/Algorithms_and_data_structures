# Second Exercise: Delete the middle element of Stack
#
# Write a program that removes the middle element of a Stack
# E.g.: input [1, 2, 3, 4, 5]
#       output [1, 2, 4, 5]
#
# Try to solve it in two ways, using recursion and using iteration
#
# NOTE: you can use an auxiliary stack
import sys
sys.path.append("..")
from LinearStructures import Stack


def deleteMidElem(st):

     # TODO
     pass


# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st)
    deleteMidElem(st)
    print(st)
