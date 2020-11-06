'''
Function that takes in a Binary Tree's root and returns the sum of node depths
and the sum all of subtree node depths.

Depth is the distance between a node in a Binary Tree and the tree's root.
Therefore, the root's depth is 0, and each step away from that root is 1 greater
in depth. For this function, depths for each subtree will be added, with depths
for each subtree relative to the subtree root.

Binary tree has properties of left, right, and value.  Left and right are 
pointers to the next node level or (None / null) and value is an integer.
'''
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# Solution 3 - Class based to track depths and counts
# O(n) time | O(h) space where n is the number of nodes in the BT
# and h is the height of the BT
class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths


def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

    numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodes

# Solution 2 - Iterative Implementation, using a list for stack
# Complexity O(N log (N)) time | O(h) Space
# Where N is the number of nodes in the binary tree and h is the height of the tree
def allKindsOfNodeDepths(root):
    sumOfAllDepths = 0
    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node is None:
            continue
        sumOfAllDepths += nodeDepths(node)
        stack.append(node.left)
        stack.append(node.right)
    return sumOfAllDepths


def nodeDepths(node, depth=0):
    if node is None:
        return 0
    return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)

# Solution 1 - Recursive Implementation, calculating nodeDepths for each subtree and adding together
# Complexity O(N log (N)) time | O(h) Space
# Where N is the number of nodes in the binary tree and h is the height of the tree
# def allKindsOfNodeDepths(root):
#     if root is None:
#         return 0
#     return sumOfNodeDepths(root, 0) + allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right)


# def sumOfNodeDepths(node, depth):
#     if node is None:
#         return 0
#     return depth + sumOfNodeDepths(node.left, depth + 1) + sumOfNodeDepths(node.right, depth + 1)
