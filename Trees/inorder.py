from stack import Stack

# method that implements inorder traversal
def inorder(root):
    if root is None:
        return

    st = Stack()
    current = root

    while current is not None or st.size() > 0:
        if current is not None:
            st.push(current)
            current = current.leftChild
        elif st.size() > 0:
            current = st.pop()
            print(current.key)
            current = current.rightChild

# recursive implementation of inorder traversal
def inorder_recursive(root):
    if root is None:
        return
    inorder_recursive(root.leftChild)
    print(root.key)
    inorder_recursive(root.rightChild)
