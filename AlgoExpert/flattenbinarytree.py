'''
Given a binary tree, flatten it, and return its leftmost node in a 
structure similar to a linked list (except with left and right pointers instead
of prev and next), nodes follow the original tree's left-to-right-order.

If tree is a BST, the flattened nodes will be sorted.
'''


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Solution 2 - Use variables to store pointers where changes need to made
# Complexity O(n) Time | O(d) space where n is number of nodes and d is depth
# of the deepest branch in the tree (call stack memory usage)
def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]

def connectNodes(left, right):
    left.right = right
    right.left = left
    


# Solution 1 - Create array of nodes through inorder recursive traversal
# Complexity O(n) Time | O(n) space where n is # of nodes
# def flattenBinaryTree(root):
#     inOrderNodes = flattenTree(root, [])
#     for i in range(len(inOrderNodes) - 1):
#         leftNode = inOrderNodes[i]
#         rightNode = inOrderNodes[i + 1]
#         leftNode.right = rightNode
#         rightNode.left = leftNode
#     return inOrderNodes[0]


# def flattenTree(tree, array):
#     if tree is not None:
#         flattenTree(tree.left, array)
#         array.append(tree)
#         flattenTree(tree.right, array)

#     return array
