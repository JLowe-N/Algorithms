"""
Takes in a Binary Tree and returns a list of its branch sums ordered from
leftmost branch sum to rightmost branch sum

A branch sum is the sum of all values in a Binary Tree branch.  A Binary Tree
branch is a path of nodes in a tree that starts at the root node and ends at
any leaf node.
"""
def branchSums(tree):
    sumsList = []
    calculateBranchSums(tree,  sumsList, runningSum = 0)
    return sumsList

def calculateBranchSums(tree, sumsList, runningSum):
    runningSum += tree.value
    if tree.left is None and tree.right is None:
        sumsList.append(runningSum)
        return
    if tree.left:
        calculateBranchSums(tree.left, sumsList, runningSum)
    if tree.right:
        calculateBranchSums(tree.right, sumsList, runningSum)