# Third Exercise
#
# Reversing the content of Stack using recursion
# You can use only one Stack, no other data structures are needed
# You cannot use any iterative loop
#
# HINT: you need TWO recursive functions one to empty the stack one to fill in

import sys
sys.path.append("..")
from stack import Stack

def insertBack(st, item):
    if st.isEmpty():
        st.push(item)
    else:
        tmp = st.pop()
        insertBack(st, item)
        st.push(tmp)


def reverseStack(st):
    if st.isEmpty():
        return

    el = st.pop()
    reverseStack(st)
    insertBack(st, el)


if __name__ == "__main__":
    st = Stack()

    for i in range(1, 10):
        st.push(i)

    print(st.elements)
    reverseStack(st)
    print(st.elements)
