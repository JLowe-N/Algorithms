'''
Given a Binary Search Tree - validate that the BST property is satisified for all
nodes and return a boolean.
'''
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Complexity - Time O(N) where N is the number of nodes
# Space O(d) where d is the depth of the longest branch - this is due
# to recursion filling up the call stack
def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftTreeIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftTreeIsValid and validateBstHelper(tree.right, tree.value, maxValue)
