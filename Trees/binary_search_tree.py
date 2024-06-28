# binary search tree implementation

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        # this time a node has noth a key and a value
        self.key = key
        self.value = val
        # the node keeps track of its left and right children and
        # of its parent nor
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        """recursive method to insert a new element in a correct position"""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)


    def get(self, key):
        if self.root is None:
            return None
        node = self._get(self.root, key)
        if node:
            return node.value
        return None

    def _get(self, currentNode, key):
        """recursive method to visit the tree and fin the correct node"""
        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode
        if key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def findSuccessor(self, node):
        # If the right child of the node to be removed has
        # no left child, the right child is the successor
        # If the right child of the node to be removed has a
        # left child, the successor is always the left most node
        succ = node.rightChild
        while succ.hasLeftChild():
            succ = succ.leftChild
        return succ

    def spliceOut(self, node):
        if node.isLeaf():
            # the splice is different if the successor is a leaf
            # or has a right child
            if node.isLeftChild():
                node.parent.leftChild = None

            else:
                node.parent.rightChild = None
        elif node.hasRightChild():
            if node.isLeftChild():
                node.parent.leftChild = node.rightChild
            else:
                node.parent.rightChild = node.rightChild
            node.rightChild.parent = node.parent

    def remove(self, currentNode):
        # case 1: delete a leaf node
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            succ = self.findSuccessor(currentNode)
            self.spliceOut(succ)
            currentNode.key = succ.key
            currentNode.payload = succ.value

        else: # case 2: this node has one child
            if currentNode.isLeftChild():
                if currentNode.hasLeftChild():  # has a left child
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                else:  # has a right child
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                if currentNode.hasLeftChild():  # has a left child
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:  # has a right child
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
            else:  # current node is the root
                if currentNode.hasLeftChild():  # has a left child
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                            currentNode.leftChild.value,
                                            currentNode.leftChild.leftChild,
                                            currentNode.leftChild.rightChild)
                else:  # has a right child
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                            currentNode.rightChild.value,
                                            currentNode.rightChild.leftChild,
                                            currentNode.rightChild.rightChild)


# Deleting a node
# a simpler impplementation with recursion
def delete(self, key):
    self.root = self._delete(self.root, key)

# Auxiliary method to find the successor
def _findSuccessor(self, node):
    successor = node.rightChild
    while successor.leftChild is not None:
        successor = successor.leftChild
    return successor

def _delete(self, node, key):
    if not node:
        return node # not found

    # find node with key
    if key < node.key:
        node.leftChild = self._delete(node.leftChild, key)
    elif key > node.key:
        node.rightChild = self._delete(node.rightChild, key)
    else: # equal, it is found
        if node.leftChild is None:
            if node.rightChild is None: # case of leaf node
                return None
            else: # case of only rightChild child
                return node.rightChild # replace node with child
        elif node.rightChild is None: # case of only leftChild child
            return node.leftChild # replace node with child

        # case of two children
        succ = self._findSuccessor(node) # get the successor of the node
        node.key = succ.key # copy
        node.rightChild = self._delete(node.rightChild, succ.key) # delete succ succ key
    return node