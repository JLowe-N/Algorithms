"""
A function that takes in a Binary Tree and returns its max path sum, where a path
is a collection of connected nodes in a tree, where no node is connected to more than two nodes.
The path sum is the sum of the values of nodes in a particular path.
"""

# Complexity - O(N) time - touches all nodes, but only elementary constant time operations
# O(log N) average space as we only have log N nodes on the call stack at any given time
# Space could be O(N) worst case if we have a single branch, completely unbalanced tree.
def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    # This could be negative
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, maxPathSum)
