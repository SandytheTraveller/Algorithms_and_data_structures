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
from stack import Stack

# iteration
def deleteMidElem(st):
    aux_st = Stack()

    if st.size() % 2 == 1:
        for i in range(st.size() // 2):
            aux_st.push(st.pop())
        st.pop()
        while not aux_st.isEmpty():
            st.push(aux_st.pop())
    else:
        for i in range(st.size() // 2 - 1):
            aux_st.push(st.pop())
        st.pop()
        st.pop()
        while not aux_st.isEmpty():
            st.push(aux_st.pop())
    return st

def deleteMidElem_rec(st, mid_point, pos):
    if st.isEmpty():
        return

    # Remove current item
    item = st.pop()

    # Recursive call
    deleteMidElem_rec(st, mid_point, pos + 1)

    # Put all items back except middle
    if pos != mid_point:
        st.push(item)


# Test Code
if __name__ == "__main__":
    st = Stack()

    for i in range(1, 12):
        st.push(i) # [1,2,3,4,5,6,7,8,9]

    print(st.elements)
    deleteMidElem(st)
    print(st.elements)
