from stack import Stack

def postorder(root):
    if root is None:
        return

    st = Stack()
    current = root

    while not st.isEmpty() or current is not None:
        while current:
            if current.rightChild is not None:
                st.push(current.rightChild)
            st.push(current)
            current = current.leftChild

        current = st.pop()

        if current.rightChild is not None and st.peek() == current.rightChild:
            st.pop()
            st.push(current)
            current = current.rightChild
        else:
            print(current.key)
            current = None
