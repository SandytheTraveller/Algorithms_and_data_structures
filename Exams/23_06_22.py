# Insert here your NAME, SURNAME and STUDENT ID
#
# Remember to rename the file adding your name and surname at the end
#
#
#
# Given a Binary Tree, compute and print the sum of all the nodes present in a level for each level of the tree
#
#  E.g.
#
#          20             Sum of level 0 = 20
#        /    \
#      15      40         Sum of level 1 = 55
#    /    \      \
#  10      30     50      Sum of level 2 = 90
#    \           /
#     22        3         Sum of level 3 = 25
#
#
# NOTE: You can use a stack or a queue if you want, but it is not mandatory
#
# HINT: Common ways to solve this problem involves a pre-order or a level-order traversal of the tree
#

from Queue import Queue

import sys
sys.path.append("..")

#
# DO NOT MODIFY THE FOLLOWING LINES!
#
class Node:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

#
# DO NOT MODIFY THE PREVIOUS LINES!
#


# YOU CAN MODIFY THE FOLLOWING FUNCTION IN ANY WAY
# YOU CAN ADD ADDITIONAL FUNCTIONS IF NEEDED

# solution with level order traversal of the tree
def level_sum(root):
    if root is None:
        print('Sum of level 0: ', 0)
        return

    q = Queue()
    q.enqueue(root)

    level = -1

    while not q.isEmpty():
        size = q.size() # amount of nodes on this level
        sum = 0

        level += 1 # we moved to the next level
        while size:
            currentNode = q.dequeue()
            sum += currentNode.key

            # add left or right child to the queue
            if currentNode.leftChild is not None:
                q.enqueue(currentNode.leftChild)
            if currentNode.rightChild is not None:
                q.enqueue(currentNode.rightChild)
            size -= 1 # we removed the child, so the size is decreased by 1
        print(f'Sum of level {level} = {sum}')

# solution using DFS traversal
def sum_DFS(root):
    if root is None:
        return
    totals = []
    _compute_sum(root, 0, totals)

    for idx, num in enumerate(totals):
        print('Sum of level', idx, '=', num)


# auxiliary method that performs a pre-order traversal
def _compute_sum(root, level, totals):
    if root is not None:
        if level >= len(totals):
            totals.append(0)
        totals[level] += root.key
        _compute_sum(root.leftChild, level + 1, totals)
        _compute_sum(root.rightChild, level + 1, totals)




# Test Code
if __name__ == '__main__':
    root1 = Node(20)
    root1.leftChild = Node(15)
    root1.leftChild.leftChild = Node(10)
    root1.leftChild.leftChild.rightChild = Node(22)
    root1.leftChild.rightChild = Node(30)
    root1.rightChild = Node(40)
    root1.rightChild.rightChild = Node(50)
    root1.rightChild.rightChild.leftChild = Node(3)


    # Expected outcome for the given example:
    #
    #  Sum of level 0 is 20
    #  Sum of level 1 is 55
    #  Sum of level 2 is 90
    #  Sum of level 3 is 25
    #
    level_sum(root1)
