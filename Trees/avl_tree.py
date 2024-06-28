class AVLNode:
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 # bottom starts at height of 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __setitem__(self, key, value):
        self.root = self._put(self.root, key, value)

    def __delitem__(self, key):
        self.root = self._delete(self.root, key)

    def __getitem__(self, key):
        node = self._find_node(self.root, key)
        return node.value if node else None

    def __contains__(self, key):
        return self[key] is not None

    def _height(self, node):
        return node.height if node else 0

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right)


    def _put(self, node, key, value):
        if not node:  # place found, return new node
            self.size += 1
            return AVLNode(key, value)
        elif key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:  # equal
            node.value = value
            return node
        return self._adjust_node(node)

    def _delete(self, node, key):
        if not node:
            return node  # not found

        # find node with key
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:  # equal, it is found
            if node.left is None:  # case of only right child
                return node.right  # replace node with child
            elif node.right is None:  # case of only left child
                return node.left  # replace node with child
            # case of two children
            succ = self._get_min_node(node.right)  # successor of node
            node.key = succ.key  # copy
            node.value = succ.value
            node.right = self._delete(node.right, succ.key)  # delete succ succ key
        return self._adjust_node(node)

    def _adjust_node(self, node):
        # update the height of the current node before
        # checking the balance factor
        node.height = 1 + max(self._height(node.right), self._height(node.left))
        balance = self._balance(node)
        # check for imbalance and rotate to correct
        if balance > 1:  # left heavy
            if self._balance(node.left) < 0:
                node.left = self._leftRotate(node.left)  # Left Right
            return self._rightRotate(node)
        elif balance < -1:
            if self._balance(node.right) > 0:
                node.right = self._rightRotate(node.right)  # Right Left
            return self._leftRotate(node)
        return node

    def _leftRotate(self, a):
        b = a.right
        x = b.left
        b.left = a
        a.right = x
        # the height of the nodes involved in the rotation are updated
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        b.height = 1 + max(self._height(b.left), self._height(b.right))
        return b

    def _rightRotate(self, a):
        b = a.left
        x = b.right
        b.right = a
        a.left = x
        # the height of the nodes involved in the rotation are updated
        a.height = 1 + max(self._height(a.left), self._height(a.right))
        b.height = 1 + max(self._height(b.left), self._height(b.right))
        return b