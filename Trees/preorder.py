from stack import Stack

# method which realizes preorder traversal
def preorder(root):
    if root is None:
        return

    st = Stack()
    st.push(root)

    while st.size() > 0:
        current = st.pop()
        print(current.key)

        if current.rightChild is not None:
            st.push(current.rightChild)
        if current.leftChild is not None:
            st.push(current.leftChild)


# recursive implementation of the preorder traversal
def preorder_recursive(root):
    if root is None:
        return
    print(root.key)
    preorder_recursive(root.leftChild)
    preorder_recursive(root.rightChild)